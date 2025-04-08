📘 SIEM-TOOL: Log Analysis & Threat Detection Using Machine Learning
A Security Information and Event Management (SIEM) solution that enables log data analysis and threat detection using machine learning techniques. The system provides a user-friendly interface built with Streamlit, allowing users to register, log in, upload logs, and get instant predictions of anomalies or threats in network logs.

🚀 Features
🔐 User Registration & Login (Streamlit-based UI)

📊 Log Upload and Analysis

🤖 ML Models for Threat Detection (Random Forest, Logistic Regression)

📈 Visual Reports and Accuracy Graphs

📁 SQLite Database for User Management

🧠 Trained models saved and reused (model.pickle, finalpred.pickle)

🎨 Background-themed UI with HTML styling

💻 How to Run
1. Install Requirements
       pip install streamlit scikit-learn pandas matplotlib seaborn
2. Run the Registration Page
       streamlit run LogAnalysis.py
3. Run the App Dashboard (after login)
       streamlit run app.py

📈 Model Training
To train the model on a fresh dataset:
       python MainFile.py

This script:
      Reads Log Data.csv

🛡️ Security Note
Passwords are stored as plaintext in the current version. For production use, always hash and salt passwords using bcrypt or similar.

👨‍💻 Author
Developed by [Your Name]

📜 License
This project is licensed under the MIT License.
