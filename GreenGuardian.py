import streamlit as st
import pickle

#with open('model.pkl', 'rb') as file:
    #model = pickle.load(file)
with open("Crop_recommender_model.pkl", 'rb') as file:  
    model=pickle.load(file)

st.title("Green Guardian")
st.write("Green Guardian helps you to Select the particular crop type based the soil and whether conditions")
st.write("Input Data")

#Nitogen
st.subheader("Nitrogen Level")
N = st.text_input("Enter the Nitrogen Level in the soil")
st.write("Nitrogen Level :", N)

#Phosphorus
st.subheader("Phosphorus Level")
P = st.text_input("Enter the Phosphorus Level in the soil")
st.write("Phosphorus Level :", P)

#Potassium
st.subheader("Potassium Level")
K = st.text_input("Enter the Potassium Level in the soil")
st.write("Potassium Level :", K)

#Temperature
st.subheader("Temperature - Degree celsius (Enter the value in float)")
temperature = st.text_input("Enter the Temperature value")
st.write("Temperature(Degree Celsius) :", temperature)

#Humidity
st.subheader("Humidity - Percentage (Enter the value in float)")
humidity = st.text_input("Enter the Humidity value")
st.write("Humidity(%) :", humidity)

#ph
st.subheader("ph (Enter the value in float)")
ph = st.text_input("Enter the ph value")
st.write("ph :", ph)

#rainfall
st.subheader("rainfall - mm (Enter the value in float)")
rainfall = st.text_input("Enter the rainfall value")
st.write("Rainfall(mm) :", rainfall)

# Button
#st.subheader("Button Example")
if st.button("Crop"):
    st.write("Predicted Crop is")
    yhat_test = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
    if yhat_test == 0:
        st.write("The crop that gives the best yield is **Apple**")
    elif yhat_test == 1:
        st.write("The crop that gives the best yield is **Banana**")
    elif yhat_test == 2:
        st.write("The crop that gives the best yield is **Black Gram**")
    elif yhat_test == 3:
        st.write("The crop that gives the best yield is **ChickPea**")
    elif yhat_test == 4:
        st.write("The crop that gives the best yield is **Coconut**")
    elif yhat_test == 5:
        st.write("The crop that gives the best yield is **Coffee**")
    elif yhat_test == 6:
        st.write("The crop that gives the best yield is **Cotton**")
    elif yhat_test == 7:
        st.write("The crop that gives the best yield is **Grapes**")
    elif yhat_test == 8:
        st.write("The crop that gives the best yield is **Jute**")
    elif yhat_test == 9:
        st.write("The crop that gives the best yield is **Kidney Beans**")
    elif yhat_test == 10:
        st.write("The crop that gives the best yield is **Lentil**")
    elif yhat_test == 11:
        st.write("The crop that gives the best yield is **Maize**")
    elif yhat_test == 12:
        st.write("The crop that gives the best yield is **Mango**")
    elif yhat_test == 13:
        st.write("The crop that gives the best yield is **Moth Beans**")
    elif yhat_test == 14:
        st.write("The crop that gives the best yield is **Mung Beans**")
    elif yhat_test == 15:
        st.write("The crop that gives the best yield is **Musk-Meloan**")
    elif yhat_test == 16:
        st.write("The crop that gives the best yield is **Orange**")
    elif yhat_test == 17:
        st.write("The crop that gives the best yield is **Papaya**")
    elif yhat_test == 18:
        st.write("The crop that gives the best yield is **Pigeon_Peas**")
    elif yhat_test == 19:
        st.write("The crop that gives the best yield is **Pomegranate**")
    elif yhat_test == 20:
        st.write("The crop that gives the best yield is **Rice**")
    else:
        st.write("The crop that gives the best yield is **Water-Melon**")
# Display Messages
#st.success("Success message")
#st.info("Info message")
#st.warning("Warning message")
#st.error("Error message")