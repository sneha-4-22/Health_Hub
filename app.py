import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import mindsdb_sdk
import time

app = Flask(__name__)

MINDSDB_HOST = 'https://cloud.mindsdb.com'
MINDSDB_API_KEY = os.environ.get('MINDSDB_API_KEY')

client = OpenAI(
    api_key=MINDSDB_API_KEY,
    base_url="https://llm.mdb.ai/"
)

def connect_to_mindsdb():
    try:
        print("Attempting to connect to MindsDB...")
        server = mindsdb_sdk.connect(MINDSDB_HOST, api_key=MINDSDB_API_KEY)
        print("Connected successfully to MindsDB!")
        return server
    except Exception as error:
        print(f"Failed to connect to MindsDB. Error: {error}")
        return None

server = connect_to_mindsdb()
if server is None:
    print("Failed to connect to MindsDB. Please check your API key and connection settings.")
    exit(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    age = data['age']
    gender = data['gender']
    symptom1 = data['symptom1']
    symptom2 = data['symptom2']
    symptom3 = data['symptom3']
    
    diagnosis, explanation = predict_diagnosis(server, age, gender, symptom1, symptom2, symptom3)
    
    return jsonify({'diagnosis': diagnosis, 'explanation': explanation})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    
    response = get_chatbot_response(user_message)
    
    return jsonify({'response': response})

def predict_diagnosis(server, age, gender, symptom1, symptom2, symptom3):
    try:
        query = f"""
        SELECT diagnosis, diagnosis_explain
        FROM health_diagnosis.diagnosis_predictor
        WHERE age = {age}
        AND gender = '{gender}'
        AND symptom1 = '{symptom1.strip()}'
        AND symptom2 = '{symptom2.strip()}'
        AND symptom3 = '{symptom3.strip()}'
        """
        print(f"Executing query: {query}")  
        result = server.query(query)
        result_list = result.fetch()
        print(f"Query result: {result_list}")  
        if result_list:
            return result_list[0]['diagnosis'], result_list[0].get('diagnosis_explain', 'No explanation provided')
        else:
            return "Unable to predict", "No results returned from the model"
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return "Unable to predict", f"An error occurred during prediction: {str(e)}"

def get_chatbot_response(user_message):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in health, diet, and lifestyle advice. Provide concise and helpful responses."},
                {"role": "user", "content": user_message}
            ],
            stream=False
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error getting chatbot response: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)