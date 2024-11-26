# Import Streamlit
import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "Cameroon": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
     },
    "Nigeria": {
        "Transportation": 0.18,  # kgCO2/km
        "Electricity": 0.50,  # kgCO2/kWh
        "Diet": 1.30,  # kgCO2/meal
        "Waste": 0.12  # kgCO2/kg
    },
    "Rwanda": {
        "Transportation": 0.12,  # kgCO2/km
        "Electricity": 0.45,  # kgCO2/kWh
        "Diet": 1.20,  # kgCO2/meal
        "Waste": 0.08  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Carbon Footprint Calculator App")

# Streamlit app code
st.title("Carbon Footprint Calculator 👣 ")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["Cameroon", "Nigeria", "Rwanda"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")


# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste


# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
 
    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")

   # Note about average CO2 emissions in selected country

        if country == "Cameroon":
            st.warning("The value for CO2 emissions (metric tons per capita) in Cameroon was 0.38 as of 2023. Over the past 28 years, this indicator reached a maximum value of 0.551 in 1994 and a minimum value of 0.202 in 1992.")
        elif country == "Nigeria":
            st.warning("The value for CO2 emissions (metric tons per capita) in Nigeria was 0.54 as of 2020. Over the past years, this indicator peaked at 0.69 in 1990.")
        elif country == "Rwanda":
            st.warning(" The latest value from 2020 is 0.11 metric tons, unchanged from 0.11 metric tons in 2019. In comparison, the world average is 3.84 metric tons, based on data from 185 countries. Historically, the average for Rwanda from 1990 to 2020 is 0.08 metric tons.")

