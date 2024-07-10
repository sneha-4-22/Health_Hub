# HealthHub
(in progress...........)
## Overview
HealthHub is a web application that prioritizes personal health management using **MindsDB**. Get instant diagnosis predictions, chat with a health assistant, plan your wellness journey, and track your health goals.


## Features
- Predictive diagnosis based on patient symptoms
- Explanation for the predicted diagnosis
- Integration with MindsDB for machine learning
- Uses SQLite database for patient data storage

## YouTube Demonstration



[![Watch the video](https://img.youtube.com/vi/oDEMWkdwTWs/0.jpg)](https://www.youtube.com/watch?v=oDEMWkdwTWs)




## Screenshots
| ![Health Plan Generation](https://github.com/sneha-4-22/Health_assistant/assets/112711068/80e73a53-a012-4681-82a5-55da7fd1730e) |
|:--:|
| **Health Hub** |
| Landing Page |

| ![Nutrition Tracking](https://github.com/sneha-4-22/Health_assistant/assets/112711068/5f9ea399-fc25-4df4-8541-a09ac8a6afe1) |
|:--:|
| **Features** |
| Health hub app features |

| ![Exercise Routines](https://github.com/sneha-4-22/Health_assistant/assets/112711068/a254b73a-d842-4f05-a8dc-69fe8bee56d3) |
|:--:|
| **AI Chatbot Assistant** |
| Interact with our intelligent chatbot for instant health advice and personalized recommendations. |


| ![Exercise Routines](https://github.com/sneha-4-22/Health_assistant/assets/112711068/03e9b841-fce8-4ea7-8b65-d611337630b0) |
|:--:|
| **Intelligent Response System** |
| Our health assistant generates appropriate plans based on user queries during chatbot assistance session, ensuring personalized guidance for each individual's health journey. |





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


## Sample Data
The SQLite database (`health_data.db`) is pre-populated with the following sample data:

| ID | Age | Gender | Symptom1      | Symptom2             | Symptom3      | Diagnosis       |
|----|-----|--------|---------------|----------------------|---------------|-----------------|
| 1  | 35  | M      | fever         | cough                | fatigue       | flu             |
| 2  | 50  | F      | chest pain    | shortness of breath  | dizziness     | heart disease   |
| 3  | 29  | M      | nausea        | headache             | fatigue       | migraine        |
| 4  | 67  | F      | cough         | shortness of breath  | fatigue       | bronchitis      |
| 5  | 45  | M      | dizziness     | nausea               | headache      | hypertension    |
| ...| ... | ...    | ...           | ...                  | ...           | ...             |

## MindsDB Integration

### Connect to MindsDB
The assistant connects to a local MindsDB server to create and train the prediction model.

### Create the Model
The model is created using data from the `patients` table in the SQLite database. The model predicts the `diagnosis` based on `age`, `gender`, `symptom1`, `symptom2`, and `symptom3`.

### Train the Model
The model is trained on the sample data provided in the `patients` table.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
