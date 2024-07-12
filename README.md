
# HealthHub - Your Complete Wellness Companion 🏥💪

Welcome to **HealthHub**, your comprehensive wellness companion designed to help you maintain a healthier lifestyle. This platform integrates cutting-edge AI technology, including **MindsDB**, to offer a variety of tools like a **Diagnosis Predictor**, **Health Chatbot**, **Weekly Health Planner**, and **Health Checklist**.

[![Quira Vote](https://img.shields.io/badge/Quira-View%20Repo-blue)](https://quira.sh/repo/sneha-4-22-Health_assistant-824874405?utm_source=copy&utm_share_context=quests_repos)
<!--
[![GitHub Stars](https://img.shields.io/github/stars/sneha-4-22/HealthHub?style=social)](https://github.com/sneha-4-22/Health_assistant/stargazers)
-->
## Table of Contents 📑

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Diagnosis Predictor](#diagnosis-predictor)
  - [Health Chatbot](#health-chatbot)
  - [Weekly Health Planner](#weekly-health-planner)
  - [Health Checklist](#health-checklist)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features 🌟

### Diagnosis Predictor 🩺

Powered by MindsDB, the Diagnosis Predictor analyzes your symptoms and provides accurate health predictions.

1. Navigate to the Diagnosis Predictor section.
2. Fill in your age, gender, and symptoms.
3. Click on the "Predict Diagnosis" button.
4. View the predicted diagnosis along with an explanation and confidence level.

[Demo Video](https://example.com/demo-diagnosis-predictor)

### Health Chatbot 🤖

The chatbot answers your health queries instantly, providing reliable advice and information. It use MindsDB (gpt 3.5 turbo) mind.

1. Navigate to the Health Chatbot section.
2. Type your health-related question in the input box.
3. Click the "Send" button to get an instant response from the chatbot.

[Demo Video](https://example.com/demo-health-chatbot)

### Weekly Health Planner 🗓️

Plan your weekly health activities effortlessly with our interactive planner. Based on the user interaction with the chatbot it will automatically generate for them.

1. Navigate to the Weekly Health Planner section.
2. Select the start and end dates for your plan.
3. Click on the "Generate Plan" button to receive a detailed weekly health plan.



[Demo Video](https://example.com/demo-weekly-health-planner)

### Health Checklist ✅

Keep track of your daily health goals with our customizable checklist.

1. Navigate to the Health Checklist section.
2. Add new items to your checklist using the input box and "Add" button.
3. Check off completed items to keep track of your progress.



[Demo Video](https://example.com/demo-health-checklist)


## YouTube Demonstration



[![Watch the video](https://img.youtube.com/vi/oDEMWkdwTWs/0.jpg)](https://www.youtube.com/watch?v=oDEMWkdwTWs)


## Requirements
- Python 3.7 or higher
- MindsDB SDK
- SQLite3
  
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Health_assistant.git
    cd Health_assistant
    ```

2. **Install required packages**:
    ```bash
    pip install mindsdb_sdk sqlite3
    ```

3. **Set up MindsDB**:
    - Follow the [MindsDB installation guide](https://docs.mindsdb.com/install) to install and run MindsDB locally.
    - Note the server address and port (default is `http://127.0.0.1:47334`).

4. **Create and populate the SQLite database**:
    ```bash
    python data.py
    ```

## Usage
(CLI)
1. **Run the assistant**:
    ```bash
    python diagnosis_assistant.py
    ```

2. **Follow the on-screen prompts** to input patient details and get a diagnosis:
    - Enter patient's age
    - Enter patient's gender (M/F)
    - Enter three symptoms

3. **View the predicted diagnosis and explanation**.

4. 
(WEB)
```bash
    python app.py
```


##  Data
The SQLite database (`health_data.db`) is pre-populated with the following sample data:

| ID | Age | Gender | Symptom1      | Symptom2             | Symptom3      | Diagnosis       |
|----|-----|--------|---------------|----------------------|---------------|-----------------|
| 1  | 35  | M      | fever         | cough                | fatigue       | flu             |
| 2  | 50  | F      | chest pain    | shortness of breath  | dizziness     | heart disease   |
| 3  | 29  | M      | nausea        | headache             | fatigue       | migraine        |
| 4  | 67  | F      | cough         | shortness of breath  | fatigue       | bronchitis      |
| 5  | 45  | M      | dizziness     | nausea               | headache      | hypertension    |
| ...| ... | ...    | ...           | ...                  | ...           | ...             |


## Support 💬

If you like this project, please support it by upvoting on Quira and starring the GitHub repository!

[![Quira Repo](https://img.shields.io/badge/Quira-View%20Repo-blue)](https://quira.sh/repo/sneha-4-22-Health_assistant-824874405?utm_source=copy&utm_share_context=quests_repos)
<!--
[![GitHub Stars](https://img.shields.io/github/stars/sneha-4-22/HealthHub?style=social)](https://github.com/sneha-4-22/Health_assistant)
-->
Thank you for your support!

