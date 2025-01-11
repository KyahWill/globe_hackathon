import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Path to the service account key JSON file
cred = credentials.Certificate('config.json')

# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Flask route to test connection
@app.route('/test_connection', methods=['GET'])
def test_connection():
    try:
        # Try to get a reference to the Firestore collection
        db.collection('test_connection').document('test_doc').set({'status': 'connected'})
        return jsonify({"message": "Firebase connection is successful!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error connecting to Firebase: {str(e)}"}), 500

# Flask route to send data from a JSON file to Firestore
@app.route('/add_data_from_file', methods=['POST'])
def add_data_from_file():
    # Specify the path to your JSON file
    json_file_path = 'fromScraped.json'
    
    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            for each in data:
        
                # Add data to a Firestore collection
                doc_ref = db.collection('scraped_data').add(each)

        return jsonify({"message": "Data added successfully", "id": doc_ref.id}), 200

    except FileNotFoundError:
        return jsonify({"message": "JSON file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"message": "Error decoding JSON file"}), 400
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
