
# HealthHub - Your Complete Wellness Companion 🏥💪

Welcome to **HealthHub**, your comprehensive wellness companion designed to help you maintain a healthier lifestyle. This platform integrates cutting-edge AI technology, with the help of  **MindsDB**, to offer a variety of tools like a **Diagnosis Predictor**, **Health Chatbot**, **Weekly Health Planner**, and **Health Checklist**.


## Table of Contents 📑

- [Features](#features)
  - [Diagnosis Predictor](#diagnosis-predictor)
  - [Health Chatbot](#health-chatbot)
  - [Weekly Health Planner](#weekly-health-planner)
  - [Health Checklist](#health-checklist)
- [YouTube Demonstration](#youtube-demonstration)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Features 🌟

### Diagnosis Predictor 🩺

Powered by MindsDB, the Diagnosis Predictor analyzes your symptoms and provides accurate health predictions.

1. Navigate to the Diagnosis Predictor section.
2. Fill in your age, gender, and symptoms.
3. Click on the "Predict Diagnosis" button.
4. View the predicted diagnosis along with an explanation and confidence level.





[Demo Video](https://github.com/user-attachments/assets/6d500300-9bfe-46b3-9616-e7fdae5a38e0)

### Health Chatbot 🤖

The chatbot answers your health queries instantly, providing reliable advice and information. It use MindsDB (gpt 3.5 turbo) mind.

1. Navigate to the Health Chatbot section.
2. Type your health-related question in the input box.
3. Click the "Send" button to get an instant response from the chatbot.



[Demo Video](https://github.com/user-attachments/assets/eabee797-abdd-4b38-bcca-e91a7239356a)

### Weekly Health Planner 🗓️

Plan your weekly health activities effortlessly with our interactive planner. Based on the user interaction with the chatbot it will automatically generate for them.

1. Navigate to the Weekly Health Planner section.
2. Select the start and end dates for your plan.
3. Click on the "Generate Plan" button to receive a detailed weekly health plan.


[Demo Video](https://github.com/user-attachments/assets/bf48438f-a94c-4596-b79c-06324147883e)

### Health Checklist ✅

Keep track of your daily health goals with our customizable checklist.

1. Navigate to the Health Checklist section.
2. Add new items to your checklist using the input box and "Add" button.
3. Check off completed items to keep track of your progress.


[Demo Video](https://github.com/user-attachments/assets/6adeace5-b0d2-4e78-915f-add9954b8651)


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
    - make .env file add your mindsDB api key 
```bash
    MINDSDB_API_KEY=''
```
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






