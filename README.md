# Healthcare Diagnosis Assistant

## Overview
The Healthcare Diagnosis Assistant is a predictive tool that uses machine learning to diagnose health conditions based on patient symptoms. It leverages MindsDB for machine learning and an SQLite database for storing patient data. The assistant provides predictions and explanations for various diagnoses based on patient inputs.

## Features
- Predictive diagnosis based on patient symptoms
- Explanation for the predicted diagnosis
- Integration with MindsDB for machine learning
- Uses SQLite database for patient data storage
- Command-line interface for user interaction

## Requirements
- Python 3.7 or higher
- MindsDB SDK
- SQLite3

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/health-assistant.git
    cd diagnosis_assistant.py
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
    python setup_database.py
    ```

## Usage

1. **Run the assistant**:
    ```bash
    python healthcare_diagnosis_assistant.py
    ```

2. **Follow the on-screen prompts** to input patient details and get a diagnosis:
    - Enter patient's age
    - Enter patient's gender (M/F)
    - Enter three symptoms

3. **View the predicted diagnosis and explanation**.

## Files

- **`setup_database.py`**: Script to create and populate the SQLite database with sample data.
- **`healthcare_diagnosis_assistant.py`**: Main script to run the Healthcare Diagnosis Assistant.
- **`requirements.txt`**: List of required Python packages.

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
