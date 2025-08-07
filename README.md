# Customer-Churn-Prediction
# 🔄 Customer Churn Prediction Web App

This is a web-based **Customer Churn Prediction System** for SaaS applications. It uses a **Logistic Regression model** trained on customer data to predict the likelihood of churn. The application is built using **Flask** (backend) and a sleek, interactive **HTML/CSS/JS frontend** featuring real-time prediction feedback, charts, dark mode toggle, toast notifications, and more.

---

## 🚀 Features

- 📉 Predicts customer churn using a trained logistic regression model
- 📊 Displays prediction probability in a dynamic bar chart
- 🌗 Dark/light mode toggle for improved user experience
- 🔄 Loading spinner to indicate real-time prediction processing
- 🟢 Toast notifications for successful predictions
- ✅ Clean, responsive UI with modern animations

---

## 🛠️ Tech Stack

### Backend:
- Python 3
- Flask
- scikit-learn
- pandas

### Frontend:
- HTML5 + CSS3
- JavaScript (Vanilla)
- Chart.js (for prediction probability graph)
- Custom components for spinner, dark mode, and toasts

---

## 📁 Project Structure

│
├── static/
│ ├── style.css # All custom styles (dark mode, spinner, chart)
│ └── script.js # JS logic for prediction, chart, toasts, toggles
│
├── templates/
│ └── index.html # Main UI of the application
│
├── model/
│ └── churn_model.pkl # Trained logistic regression model
│
├── main.py # Flask backend logic
├── train_model.py # (Optional) Script to train the model
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation
