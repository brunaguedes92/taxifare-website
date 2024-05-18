import streamlit as st
import datetime
import requests

'''
# Taxi Fare NY 🚕🍎🗽
'''
'''
## Select the parameters of the ride

'''

with st.form("taxi_fare_form"):

    date = st.date_input("Date", datetime.date(2012, 10, 6))
    time = st.time_input("Time", datetime.time(10, 20))
    pickup_latitude = st.text_input("Pickup Latitude", value=-73.9798156)
    pickup_longitude = st.text_input("Pickup Longitude", value=40.7614327)
    dropoff_longitude = st.text_input("Dropoff Longitude", value=40.6413111)
    dropoff_latitude = st.text_input("Dropoff Latitude", value=-73.7803331)
    passenger_count = st.selectbox("Passenger Count", options=[1, 2, 3, 4, 5, 8])

    submitted = st.form_submit_button("Submit")

    if submitted:
        url = 'https://taxifare.lewagon.ai/predict'

        parameters = {
            "pickup_datetime": f"{date} {time}",
            "pickup_longitude": float(pickup_longitude),
            "pickup_latitude": float(pickup_latitude),
            "dropoff_longitude": float(dropoff_longitude),
            "dropoff_latitude": float(dropoff_latitude),
            "passenger_count": int(passenger_count)
        }

        response = requests.get(url, params=parameters)

        '''
        ## Your predicted price is:
        '''
        st.write(round(response.json()['fare'], 2))
