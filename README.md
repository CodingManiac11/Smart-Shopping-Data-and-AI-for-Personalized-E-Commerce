🛒 Smart Shopping: Data & AI for Personalized E-Commerce
An AI-powered full-stack web application that revolutionizes online shopping by offering personalized product recommendations, voice search capabilities, and smart analytics using the power of React, Flask, Machine Learning, and NLP.

🔥 Features
🧠 AI-Powered Recommendations: Tailored suggestions based on user behavior and preferences.

🔍 Voice Search Integration: Shop hands-free using your voice.

📊 Smart Analytics: Insightful visualizations for admin and customers.

⚙️ Full-Stack Integration: React frontend + Flask backend + ML models.

🧩 Tech Stack
Layer	Tech Used
💻 Frontend	React, Axios, React Router
🔙 Backend	Flask, Flask-CORS, REST API
🤖 AI/ML	Python, Scikit-learn, Pandas, NLP
🗄️ Database	CSV / JSON (can be extended to MongoDB/PostgreSQL)
🎙️ Voice	Web Speech API / SpeechRecognition
🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/CodingManiac11/Smart-Shopping-Data-and-AI-for-Personalized-E-Commerce.git
cd Smart-Shopping-Data-and-AI-for-Personalized-E-Commerce
2. Backend Setup (Flask)
bash
Copy
Edit
cd backend
python -m venv venv
.\venv\Scripts\activate      # For Windows
# source venv/bin/activate  # For Linux/Mac

pip install -r requirements.txt
python app.py
🟢 Flask should now be running at: http://localhost:5000

3. Frontend Setup (React)
bash
Copy
Edit
cd ../frontend
npm install
npm start
🟢 React app will run at: http://localhost:3000

Make sure the package.json in frontend/ has the following line:

json
Copy
Edit
"proxy": "http://localhost:5000"
📂 Project Structure
java
Copy
Edit
Smart-Shopping-Data-and-AI-for-Personalized-E-Commerce/
├── backend/
│   ├── app.py
│   ├── model/
│   └── static/
├── frontend/
│   ├── public/
│   ├── src/
│   └── package.json
├── dataset/
└── README.md
