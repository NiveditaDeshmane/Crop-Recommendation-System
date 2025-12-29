# Crop Recommendation System

###  Overview
The **Crop Recommendation System** uses **Machine Learning** to suggest the most suitable crop to grow based on soil and weather conditions.  
It analyzes parameters like Nitrogen (N), Phosphorous (P), Potassium (K), Temperature, Humidity, pH, and Rainfall — then predicts the best crop using a trained model.

---

##  Features
- Perform **Exploratory Data Analysis (EDA)** to understand crop data.
- **Data preprocessing** including scaling and encoding.
- Train and evaluate ML models like **Random Forest** and **Decision Tree**.
- **Model tuning & evaluation** with accuracy reports.
- **Final prediction & deployment** using Streamlit web app.
- Optional integration with **IoT sensors** or **Weather APIs**.

---

##  Tech Stack
- **Language:** Python  
- **Libraries:** pandas, numpy, scikit-learn, seaborn, matplotlib, joblib  
- **Deployment:** Streamlit  
- **Optional APIs:** OpenWeatherMap for real-time weather data  

---

## Project Structure
```
Crop_Recommendation_System/
│
├──  data/
│   ├── Crop_recommendation.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   ├── 04_Evaluation_and_Tuning.ipynb
│   ├── 05_Final_Prediction_and_Deployment.ipynb
│
├──  models/
│   ├── crop_model.pkl
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│
├──  app/
│   ├── app.py
│
├──  utils/
│   ├── visualization.py
│   ├── weather_api.py
│   ├── iot_simulator.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

##  Installation

### Step 1️: Clone the repository
```bash
git clone https://github.com/your-username/Crop_Recommendation_System.git
cd Crop_Recommendation_System
```

### Step 2️: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3️: Run the Streamlit App
```bash
cd app
streamlit run app.py
```

---

##  Usage
1. Launch the Streamlit app.  
2. Enter soil and weather parameters.  
3. Click on **“Recommend Crop”**.  
4. View your suggested crop instantly!  

---

##  Example Prediction
| N | P | K | Temperature | Humidity | pH | Rainfall | Predicted Crop |
|---|---|---|--------------|-----------|----|-----------|----------------|
| 90 | 42 | 43 | 25.5°C | 80% | 6.5 | 200mm | Rice |

---

##  Future Enhancements
- Integration with **real-time weather APIs**   
- **IoT sensor data** for automated soil reading.  
- Add **fertilizer recommendations** and crop rotation logic.  
- Deploy on **AWS / Streamlit Cloud**.  

---

##  Author
**Ankit Jadhav**  
 Data Science & Machine Learning Enthusiast  
www.linkedin.com/in/ankit-jadhav-5556ankit

---

##  License
This project is open-source under the **MIT License**.
