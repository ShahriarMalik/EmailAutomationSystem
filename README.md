# Intelligent Email Management System

## Project Overview
This project demonstrates an integration of UiPath with Python to automate the process of managing emails. It categorizes emails and creates tasks in JIRA based on the content and urgency of each email. This system aims to enhance workflow efficiency by automating the email summarization and task creation processes.

## Technologies Used
- **UiPath**: Automates interactions with email systems and manages workflow sequences.
- **Python**: Handles backend logic including email categorization and sentiment analysis.
- **Flask**: Serves as the API layer to receive processed data from UiPath and interact with JIRA.
- **JIRA API**: Used to create and manage tasks based on email content.

## Features
- Email summarization to extract key points.
- Categorization of emails into Urgent, Follow-up, and Informational.
- Automatic JIRA task creation based on email urgency and category.

## Getting Started

### Prerequisites
- Python 3.8+
- UiPath Studio 2021.10
- Access to JIRA Software

### Setup and Installation
1. **Python Environment Setup**:
   - Install required Python packages:
     ```bash
     pip install flask nltk requests
     ```
   - Set up the Flask application:
     ```bash
     export FLASK_APP=app.py
     export FLASK_ENV=development
     flask run
     ```

2. **UiPath Setup**:
   - Open the provided `.xaml` files in UiPath Studio.
   - Configure the project dependencies and ensure the Python activities are correctly set up.

3. **JIRA Configuration**:
   - Configure the JIRA API integration by setting your JIRA instance URL, username, and API token in the Python script.

### Running the Application
- Start the Flask server as outlined above.
- Run the UiPath automation from UiPath Studio or UiPath Assistant.

## How It Works
- UiPath retrieves emails and sends email content to the Flask API.
- The Flask API processes the email content, categorizes it, analyzes sentiment, and based on predefined rules, decides if a task should be created in JIRA.
- If required, a JIRA task is created with details about the email and its categorization.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
