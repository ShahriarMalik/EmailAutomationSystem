# Intelligent Email Management System

## Project Overview
This project demonstrates the integration of UiPath with Python to automate the process of email management. It automates tasks such as email categorization and sentiment analysis and creates corresponding tasks in JIRA based on the urgency and content of the emails. The goal is to streamline internal communications within an organization by efficiently managing email workflows.

## Technologies Used
- **UiPath**: Used for automating interactions with email systems and managing workflows.
- **Python**: Manages backend logic including email categorization and sentiment analysis.
- **Flask**: Serves as the API layer that interfaces between UiPath and the backend logic.
- **JIRA API**: Utilized to create and manage tasks based on processed email data.

## Features
- **Email Summarization**: Extracts key points from emails for quick insights.
- **Email Categorization**: Classifies emails into categories such as Urgent, Follow-up, and Informational.
- **Automated JIRA Task Creation**: Generates tasks in JIRA based on the email content and categorization, tagged with appropriate priorities.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- UiPath Studio 2021.10 or newer
- Access to JIRA and corresponding API keys

## Directory Structure

Below is an outline of the directory structure for the Intelligent Email Management System project, detailing where key components are located:

- **/src**: Source files for the project.
  - **/ui_path**: Contains UiPath workflows (.xaml files).
  - **/python**: Contains Python scripts including the Flask app and a requirements file for setting up the Python environment.
- **README.md**: Project documentation

### Setup and Installation
1. **Python Environment Setup**:
   - Install the required Python packages:
     ```bash
     pip install flask nltk requests
     ```
   - Initialize the Flask application to handle requests:
     ```bash
     export FLASK_APP=app.py
     export FLASK_ENV=development
     flask run
     ```

2. **UiPath Setup**:
   - Open the provided `.xaml` files in UiPath Studio.
   - Ensure all dependencies are correctly configured.

3. **JIRA Configuration**:
   - Set up the JIRA API integration by configuring your JIRA instance URL, username, and API token in the Flask application.

### Running the Application
- Start the Flask server as outlined in the setup instructions.
- Execute the UiPath automation from UiPath Studio or UiPath Assistant to process emails and observe the results in JIRA.

## How It Works
- **Email Retrieval**: UiPath retrieves emails and sends the content to the Flask API.
- **Email Processing**: The Flask API uses Python to analyze the content, categorize emails, and determine their sentiment.
- **Task Creation**: Based on the analysis, tasks are created in JIRA with details such as category, priority, and a summary of the email content.

## Contributing
Contributions are welcome! If you have improvements or corrections, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
