from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_db
from ai_model import recommend_products

app = Flask(__name__)
CORS(app)

# Ensure MongoDB connection
db = get_db()

@app.route('/')
def home():
    return "API is working!"

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_preferences = data.get('preferences', [])

        # Save preferences to MongoDB
        db.preferences.insert_one({"preferences": user_preferences})

        # Get AI recommendations
        recommendations = recommend_products(user_preferences)
        return jsonify(recommendations)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
