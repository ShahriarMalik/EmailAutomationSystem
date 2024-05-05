from flask import Flask, request, jsonify
from nltk.corpus import wordnet
from nltk.sentiment import SentimentIntensityAnalyzer
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


def get_synonyms(word):
    synonyms = set()
    synsets = wordnet.synsets(word)
    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return synonyms


def categorize_email(text):
    keywords = {
        'Urgent': get_synonyms('urgent') | {'asap', 'immediately', 'critical'},
        'Follow-up': get_synonyms('follow-up') | {'response needed', 'reply needed'},
        'Informational': get_synonyms('informational') | {'newsletter', 'update', 'news'}
    }
    for category, words in keywords.items():
        if any(word in text.lower() for word in words):
            return category
    return 'General'


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)['compound']


def create_jira_task(summary, description, project_key, issue_type, jira_url, auth):
    url = f"{jira_url}/rest/api/2/issue"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type}
        }
    }
    response = requests.post(
        url, json=payload, headers=headers, auth=HTTPBasicAuth(*auth))
    return response.json()


@app.route('/process_email', methods=['POST'])
def process_email():
    data = request.json
    subject = data.get('subject')
    body = data.get('body')
    address = data.get('address')
    jira_url = data.get('jira_url')
    username = data.get('username')
    api_token = data.get('api_token')
    project_key = data.get('project_key')
    issue_type = data.get('issue_type')

    email_content = f"{subject} {body}"
    category = categorize_email(email_content)
    sentiment_score = analyze_sentiment(email_content)

    if category == 'Urgent' and sentiment_score < -0.05:
        summary = "High Priority: Urgent Email Detected"
        description = f"Urgent email received from {address} with sentiment score of {sentiment_score}. Action required."
        response = create_jira_task(
            summary, description, project_key, issue_type, jira_url, (username, api_token))
        return jsonify({"message": "JIRA Task Created: High Priority", "response": response})
    elif category == 'Urgent':
        summary = "Normal Priority: Urgent Email Detected"
        description = f"Urgent email received from {address}. Consider reviewing soon."
        response = create_jira_task(
            summary, description, project_key, issue_type, jira_url, (username, api_token))
        return jsonify({"message": "JIRA Task Created: Normal Priority", "response": response})
    return jsonify({"message": "No JIRA Task Created", "category": category, "sentiment_score": sentiment_score})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
