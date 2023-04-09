import pandas as pd
import numpy as np
import joblib
import streamlit as st

classifier = joblib.load('air.pkl')

def predict_survived(Gender,CustomerType, Age,TypeofTravel,Class,
       FlightDistance, Inflightwifiservice,
       DepartureArrivaltimeconvenient,EaseofOnlinebooking,
       Gatelocation,Foodanddrink, Onlineboarding, Seatcomfort,
       Inflightentertainment,Onboardservice,Legroomservice,
       Baggagehandling, Checkinservice, Inflightservice,
       Cleanliness,DepartureDelayinMinutes,
       ArrivalDelayinMinutes):
    
      prediction = classifier.predict(
            pd.DataFrame(
            {
         'Gender':[Gender],
         'CustomerType':[CustomerType],
         'Age':[Age],
         'TypeofTravel':[TypeofTravel],
         'Class':[Class],
         'FlightDistance':[FlightDistance],
         'Inflightwifiservice':[Inflightwifiservice],
         'DepartureArrivaltimeconvenient':[DepartureArrivaltimeconvenient],
         'EaseofOnlinebooking':[EaseofOnlinebooking],
         'Gatelocation':[Gatelocation],
         'Foodanddrink':[Foodanddrink], 'Onlineboarding':[Onlineboarding], 'Seatcomfort':[Seatcomfort],
         'Inflightentertainment':[Inflightentertainment], 'Onboardservice':[Onboardservice], 'Legroomservice':[Legroomservice],
         'Baggagehandling':[Baggagehandling], 'Checkinservice':[Checkinservice], 'Inflightservice':[Inflightservice],
         'Cleanliness':[Cleanliness], 'DepartureDelayinMinutes':[DepartureDelayinMinutes],
         'ArrivalDelayinMinutes':[ArrivalDelayinMinutes]}))
      
      
      
      return prediction[0]

def main():
         st.title('Airplane Satisfiction prediction')
         html_temp="""
                     <div style="background-color:orange">
                     <h2 style="color:white;text-align:center;">this our streamlit </h2>
                     </div>
                  """
         st.markdown(html_temp,unsafe_allow_html=True)

         Gender= st.radio('Your gender',['male', 'female'])
         CustomerType= st.radio('Your type',['disloyal Customer','loyal Customer'])
         Age =st.text_input('Your age','')
         TypeofTravel=st.radio('pick type of travel',['Business travel', 'Personal Travel'])
         Class=st.radio('Your class',['Eco Plus', 'Business', 'Eco'])
         FlightDistance=st.text_input('Flight Distance','')
         Inflightwifiservice=st.radio('From 1 to 5 pick our opinion on Inflight wifi service',[0,1,2,3,4,5])
         DepartureArrivaltimeconvenient=st.radio('From 1 to 5 pick our opinion on Departure/Arrival time convenient',[0,1,2,3,4,5])
         EaseofOnlinebooking=st.radio('From 1 to 5 pick our opinion on Ease of Online booking',[0,1,2,3,4,5])
         Gatelocation=st.radio('From 1 to 5 pick our opinion on Gate location',[0,1,2,3,4,5])
         Foodanddrink=st.radio('From 1 to 5 pick our opinion on Food and drink',[0,1,2,3,4,5]) 
         Onlineboarding=st.radio('From 1 to 5 pick our opinion on  Online boarding', [0,1,2,3,4,5])
         Seatcomfort=st.radio('From 1 to 5 pick our opinion on Seat comfort',[0,1,2,3,4,5] )
         Inflightentertainment=st.radio('From 1 to 5 pick our opinion onInflight entertainment',[0,1,2,3,4,5] )
         Onboardservice=st.radio('From 1 to 5 pick our opinion on On-board service ', [0,1,2,3,4,5])
         Legroomservice=st.radio('From 1 to 5 pick our opinion on Leg room service', [0,1,2,3,4,5])
         Baggagehandling=st.radio('From 1 to 5 pick our opinion on Baggage handling', [0,1,2,3,4,5])
         Checkinservice=st.radio('From 1 to 5 pick our opinion on Checkin service', [0,1,2,3,4,5])
         Inflightservice =st.radio('From 1 to 5 pick our opinion on Inflight service', [0,1,2,3,4,5])
         Cleanliness =st.radio('From 1 to 5 pick our opinion on Cleanliness',[0,1,2,3,4,5])
         DepartureDelayinMinutes=st.text_input('Departure Delay in Minutes','')
         ArrivalDelayinMinutes=st.text_input('Arrival Delay in Minutes','')

         result =""
    
         if st.button('predict'):
               result = predict_survived(Gender,CustomerType,Age,TypeofTravel,Class,
                  FlightDistance,Inflightwifiservice,
                  DepartureArrivaltimeconvenient,EaseofOnlinebooking,
                  Gatelocation,Foodanddrink,Onlineboarding,Seatcomfort,
                  Inflightentertainment,Onboardservice,Legroomservice,
                  Baggagehandling,Checkinservice,Inflightservice,
                  Cleanliness,DepartureDelayinMinutes,
                  ArrivalDelayinMinutes)
               st.success('this person is {}'.format(result))
    
    
if __name__ =='__main__':
    main()

    
