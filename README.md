
# 🏠 UCC Hostel Rent Prediction App

This Streamlit app predicts the annual rent of hostels around the University of Cape Coast (UCC) campus based on user-specified features such as room size, amenities, location, and more. It is built to assist students, researchers, and housing administrators in making informed decisions about accommodation.

---

## 🚀 Features

- 📊 Interactive UI with sliders, checkboxes, and dropdowns for user input
- 🧠 Predicts hostel rent using a trained Gradient Boosting Regressor model
- 🔍 Supports detailed input including:
  - Room type, size, and distance from campus
  - Amenities like Wi-Fi, generator, security, janitorial services
  - Location and commute mode
- 👨‍💻 Two-page interface:
  - 🏠 Home: Overview of app purpose and contributors
  - 🧠 Predict: Input form for predicting rent

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Streamlit** – Web interface
- **Scikit-learn / Gradient Boosting Regressor** – Model training
- **Joblib** – Model serialization
- **Pandas / NumPy** – Data handling and preprocessing

---

## 📂 Project Structure

```
hostel-prices/
│
├── app.py                  # Streamlit app
├── model/
│   ├── hostel_price_model.pkl     # Trained ML model
│   └── model_features.pkl         # Feature list used by the model
├── venv/                   # Virtual environment (optional)
└── README.md
```

---

## 🧪 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ucc-hostel-rent-app.git
cd ucc-hostel-rent-app
```

### 2. Set Up Environment

Create a virtual environment (recommended):

```bash
python -m venv venv
.env\Scriptsctivate      # Windows
```

Install required packages:

```bash
pip install streamlit pandas scikit-learn numpy joblib
```

### 3. Run the App

```bash
streamlit run app.py
```

Then visit: `http://localhost:8501` in your browser.

---

## 📈 Model Info

- **Model Used:** Gradient Boosting Regressor
- **Evaluation Results:**
  - RMSE: 627.91
  - MAE: 285.69
  - R² Score: 0.84
- **Training Features:** 50+ one-hot and numerical features related to room amenities, student profile, and location

---

## 👨‍💻 Authors

### **Mohammed Kamalidin**
📧 [mkamalidin9@gmail.com](mailto:mkamalidin9@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-kamalidin/)  
🎓 University of Cape Coast  
📘 MSc Data Management and Analysis  
🏢 Assistant Technical Officer @ National Identification Authority

---

### **Prince Acquah Rockson**
📧 [parockson@gmail.com](mailto:parockson@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/prince-acquah-rockson/)  
🎓 KNUST – MSc Health Informatics  
💼 Data Analyst @ Halges Fintech  
💻 Software Engineer @ Proxy Solutions

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).
