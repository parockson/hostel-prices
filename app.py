import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# Configure the Streamlit app
st.set_page_config(page_title="Hostel Rent Predictor APP", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["🏠Home", "🧠Predict Hostel Rent"])

# Load model and features
model_path = os.path.join( "model", "hostel_price_model.pkl")
features_path = os.path.join( "model", "model_features.pkl")

model = joblib.load(model_path)
feature_list = joblib.load(features_path)

# ------------------ HOME PAGE ------------------ #
if page == "🏠Home":
    st.title("🏠 Hostel Rent Prediction App🧠 ")

    st.markdown("""
Welcome to the **Hostel Rent Predictor** designed for students and stakeholders of the **University of Cape Coast (UCC)**.

This app allows:
- 🎓 **Students** to estimate hostel rent based on room features, amenities, and location.
- 🧠 **Researchers** to explore data patterns in student accommodation pricing.
- 🏢 **Administrators and hostel owners** to understand factors that influence rent.

---

### 👨‍💻 Authors

---

#### **Mohammed Kamalidin**  
📧 [mkamalidin9@gmail.com](mailto:mkamalidin9@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-kamalidin/)  
🎓 University of Cape Coast  
📘 MSc Data Management and Analysis  
🏢 Assistant Technical Officer @ National Identification Authority

---

#### **Prince Acquah Rockson**  
📧 [parockson@gmail.com](mailto:parockson@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/prince-acquah-rockson/)  
🎓 Kwame Nkrumah University of Science and Technology  
📘 MSc Health Informatics  
💼 Data Analyst @ Halges Fintech  
💻 Software Engineer @ Proxy Solutions
    """)

# ------------------ PREDICT PAGE ------------------ #
elif page == "🧠Predict Hostel Rent":
    st.title("🏘️ Predict Hostel Rent")

    st.markdown("Please provide the details below:")

    # Categorical input options
    gender_options = ["Male", "Female"]
    age_group_options = ["18-24", "25-30", "31-35", "35-40"]
    level_options = ["Certificate", "Diploma", "HND", "Undergraduate", "Postgraduate"]
    lecture_location_options = ["Science", "New Site", "Old Site", "Nduom"]
    accommodation_type_options = ["Private room(1 in a room)", "2 in a room","3 in a room","4 in a room", "5+ in a room"]
    faculty_options = [
    "Faculty of Social Sciences",
    "School of Business",
    "Faculty of Education",
    "Faculty of Science and Technology",
    "School of Medical Sciences",
    "Faculty of Arts",
    "Law School",
    "School of Physical Sciences",
    "School of Health Sciences",
    "Home Science",
    "School of Biological Sciences",
    "Faculty of Agriculture",
]

    duration_options = ["Less than 6 months", "6 months to 1 year", "Between a year and 2 years", "3 years or more"]
    commute_options = ["Walking", "Personal vehicle", "Shuttle"]
    facility_level_options = ["Low", "Medium", "High"]
    hostel_location_options = ["Apewosika", "Kwaprow", "Amamoma", "Domeabra","Abura", "Ankaful", "Eguafo", "Bantuma", "Nkanfoa" ]

    # Form UI
    gender = st.selectbox("Gender", gender_options)
    age_group = st.selectbox("Age Group", age_group_options)
    level = st.selectbox("Level of Study", level_options)
    lecture_location = st.selectbox("Lecture Location", lecture_location_options)
    accommodation_type = st.selectbox("Accommodation Type", accommodation_type_options)
    faculty = st.selectbox("Faculty", faculty_options)
    duration = st.selectbox("Off-Campus Duration", duration_options)
    commute = st.selectbox("Commute Mode", commute_options)
    facility_level = st.selectbox("Room Facility Level", facility_level_options)
    hostel_location = st.selectbox("Hostel Location", hostel_location_options)

    distance_minutes = st.slider("Distance to Lecture (in minutes)", 1, 60, 20)
    room_size_sqm = st.slider("Room Size (sqm)", 10, 40, 20)

    # Amenities
    st.markdown("### Amenities")
    includes_water = st.checkbox("Includes Water")
    includes_electricity = st.checkbox("Includes Electricity")
    includes_waste = st.checkbox("Waste Disposal")
    has_wifi = st.checkbox("Wi-Fi")
    has_study_area = st.checkbox("Study Area")
    has_generator = st.checkbox("Generator Backup")
    has_security = st.checkbox("Security Services")
    has_access_control = st.checkbox("Access Controls")
    has_janitor = st.checkbox("Janitorial Services")
    has_running_water = st.checkbox("Running Water")
    has_extra_storage = st.checkbox("Extra Storage")
    furnished_bed = st.checkbox("Furnished Bed")
    furnished_table = st.checkbox("Furnished Table")
    furnished_chairs = st.checkbox("Furnished Chairs")

    # Rent-related values
    required_deposit = st.number_input("Required Deposit (GHS)", min_value=0, value=2500)
    recent_rent_increase = st.number_input("Recent Rent Increase (GHS)", min_value=0, value=500)
    avg_rent_nearby = st.number_input("Average Rent Nearby (GHS)", min_value=0, value=4000)

    # Prepare input
    input_data = {
        "required_deposit": required_deposit,
        "recent_rent_increase": recent_rent_increase,
        "avg_rent_nearby": avg_rent_nearby,
        "distance_minutes": distance_minutes,
        "room_size_sqm": room_size_sqm,
        "includes_water": int(includes_water),
        "includes_electricity": int(includes_electricity),
        "includes_waste_disposal": int(includes_waste),
        "has_wifi_internet": int(has_wifi),
        "has_study_area": int(has_study_area),
        "has_generator_backup_power": int(has_generator),
        "has_security_services": int(has_security),
        "has_access_controls": int(has_access_control),
        "has_janitorial_services": int(has_janitor),
        "has_running_water": int(has_running_water),
        "has_extra_storage": int(has_extra_storage),
        "furnished_bed": int(furnished_bed),
        "furnished_table": int(furnished_table),
        "furnished_chairs": int(furnished_chairs)
    }

    # One-hot encode categorical features
    categorical = {
        "gender": gender,
        "age_group": age_group,
        "level_of_study": level,
        "lecture_location": lecture_location,
        "accommodation_type": accommodation_type,
        "faculty": faculty,
        "off_campus_duration": duration,
        "commute_mode": commute,
        "facility_level": facility_level,
        "hostel_location": hostel_location
    }

    for col, val in categorical.items():
        col_name = f"{col}_{val}"
        input_data[col_name] = 1

    # Fill all expected features, missing one-hot encodings get 0
    for col in feature_list:
        if col not in input_data:
            input_data[col] = 0

    input_df = pd.DataFrame([input_data])[feature_list]

    # Prediction button
    if st.button("Predict Rent"):
        predicted_rent = model.predict(input_df)[0]
        st.success(f"💰 Estimated Annual Rent: **GHS {predicted_rent:,.2f}**")
