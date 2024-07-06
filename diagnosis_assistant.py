import mindsdb_sdk
import sqlite3

# MindsDB server address (running locally)
MINDSDB_HOST = 'http://127.0.0.1'
MINDSDB_PORT = 47334  # Updated port based on your MindsDB output

# Connect to MindsDB server locally
def connect_to_mindsdb():
    try:
        print("Attempting to connect to MindsDB locally...")
        server = mindsdb_sdk.connect(f"{MINDSDB_HOST}:{MINDSDB_PORT}")
        print("Connected successfully to MindsDB!")
        return server
    except Exception as error:
        print(f"Failed to connect to MindsDB. Error: {error}")
        return None

# Connect to SQLite database
def connect_to_sqlite(database_name):
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        print(f"Connected to SQLite database '{database_name}' successfully.")
        return conn, cursor
    except sqlite3.Error as e:
        print(f"SQLite database connection failed. Error: {e}")
        return None, None

# Function to make predictions
def predict_diagnosis(model, age, gender, symptom1, symptom2, symptom3):
    try:
        result = model.predict({
            'age': age,
            'gender': gender,
            'symptom1': symptom1,
            'symptom2': symptom2,
            'symptom3': symptom3
        })
        return result['diagnosis'], result.get('diagnosis_explain', 'No explanation provided')
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Unable to predict", "An error occurred during prediction"

# Simple command-line interface
def get_user_input():
    age = int(input("Enter patient's age: "))
    gender = input("Enter patient's gender (M/F): ")
    symptom1 = input("Enter first symptom: ")
    symptom2 = input("Enter second symptom: ")
    symptom3 = input("Enter third symptom: ")
    return age, gender, symptom1, symptom2, symptom3

# Main function
def main():
    # Connect to MindsDB server
    server = connect_to_mindsdb()
    if server is None:
        print("Failed to connect to MindsDB. Exiting.")
        return

    # Add SQLite database as a data source
    try:
        # Check if the database already exists
        existing_dbs = server.list_databases()
        if 'health_data' not in [db.name for db in existing_dbs]:
            server.databases.create(
                name='health_data',
                engine='sqlite',
                connection_args={
                    'db_file': 'health_data.db'  # Changed from 'database' to 'db_file'
                }
            )
            print("SQLite database added as a data source.")
        else:
            print("SQLite database 'health_data' already exists as a data source.")
    except Exception as e:
        print(f"Error handling SQLite database as a data source: {e}")

    # Connect to SQLite database
    conn, cursor = connect_to_sqlite('health_data.db')
    if conn is None or cursor is None:
        print("Failed to connect to SQLite database. Exiting.")
        return

    try:
        # Check if the 'patients' table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='patients'")
        if cursor.fetchone() is None:
            print("Error: 'patients' table not found in the database.")
            return

        # Check if the table has data
        cursor.execute("SELECT COUNT(*) FROM patients")
        row_count = cursor.fetchone()[0]
        print(f"Number of rows in 'patients' table: {row_count}")
        if row_count == 0:
            print("Warning: 'patients' table is empty.")
            return

        # Create or get the project
        try:
            project = server.get_project('health_diagnosis')
            print("Project 'health_diagnosis' already exists.")
        except Exception:
            print("Creating project...")
            project = server.create_project('health_diagnosis')
            print("Project created successfully.")

        # Create and train the model
        try:
            model = project.models.get('diagnosis_predictor')
            print("Model 'diagnosis_predictor' already exists.")
        except Exception:
            print("Creating and training model...")
            model = project.models.create(
                name='diagnosis_predictor',
                predict='diagnosis',
                using={
                    'integration_name': 'health_data',
                    'query': 'SELECT * FROM patients'
                }
            )
            print("Model creation initiated. Waiting for training to complete...")
            model.train()
            print("Model training complete.")

        # Main loop for predictions
        while True:
            print("\nHealthcare Diagnosis Assistant")
            user_data = get_user_input()
            diagnosis, explanation = predict_diagnosis(model, *user_data)
            print(f"\nPredicted diagnosis: {diagnosis}")
            print(f"Explanation: {explanation}")

            if input("\nDo you want to make another prediction? (y/n): ").lower() != 'y':
                break

        print("Thank you for using the Healthcare Diagnosis Assistant!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()