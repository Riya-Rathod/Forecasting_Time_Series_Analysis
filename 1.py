
import streamlit as st
import pickle
from datetime import date
import datetime
import pandas as pd
st.set_page_config(page_title='Forecasting',layout='wide')
st.set_option('deprecation.showPyplotGlobalUse',False)
st.title("Stock Prediction")


START="1986-03-13"
TODAY=date.today().strftime("%Y-%m-%d")

msft=pd.read_csv('Stock_Price.csv')
df1=pd.read_csv("Cleaned_Data.csv")
#
st.header("Stock Market Price Forecasting")
filename='trained_model.sav'

loaded_model=pickle.load(open(filename, 'rb'))

def predicting(n_days):
    #gap_day=(datetime.date.today()+datetime.timedelta(days=n_days))
    #future_days=(datetime.date.today()-gap_day).days
    date1 = date(2023, 11, 17)
    previous_days=(datetime.date.today()-date1).days
    total=(n_days+previous_days)
    ypred_future=loaded_model.predict(start=9498,end=9498+total-1)
    futuredate_arima=pd.DataFrame({'Close':ypred_future})
    
    l=[]
    
    
    start_date = datetime.datetime(2023,11,17,0,0,0)
    #start_date = datetime.datetime.today()
    for i in range(total): 
        start_date += datetime.timedelta(days=1)
        l.append(start_date)

    futuredate_arima['Date']=l
    
    
    future_data_Arima=pd.concat([df1,futuredate_arima])
    future_data_Arima=future_data_Arima.set_index('Date')
    futuredate_arima.set_index('Date',inplace=True)
    col1,col2=st.columns([1,2])
    col2.line_chart(future_data_Arima)
    col2.line_chart(futuredate_arima['Close'])
    with col1:
        st.write("Prediction of next ",n_days,"days")
        st.dataframe(futuredate_arima.iloc[-n_days:])


column1, column2 = st.columns([1,2])




    
company=column1.selectbox("Pick Company", ["Microsoft"],
                         index=None,
placeholder="Select company...",)
    
    
#with column2:
   
if company=='Microsoft':
        
    with column1:
            
            plots=st.radio(
                "Plots 👉",
       
                options=["Upto next 14 days of prediction","Select Date until when to predict",
                         "Cleaned Original data",'2 years forecasted data','1 year forecasted data',
                         '6 months forecasted data'])
            if plots=='Cleaned Original data':
                
                column2.write('Microsoft stock data from 1986-03-13 to 2023-11-16 ')
                #col1,col2=column2.columns([1,2])
                
                
                column2.dataframe(msft)
                column2.line_chart(df1['Close'])
            
            if plots=='Upto next 14 days of prediction':
                with column2:
                    n_days=st.slider("Select number of days:",7,14)
                    if n_days==7:
                        predicting(n_days)
                    elif n_days==8:
                        predicting(n_days)
                    elif n_days==9:
                        predicting(n_days)
                    elif n_days==10:
                        predicting(n_days)
                    elif n_days==11:
                        predicting(n_days)
                    elif n_days==12:
                        predicting(n_days)
                    elif n_days==13:
                        predicting(n_days)
                    elif n_days==14:
                        predicting(n_days)
                        
            if plots=='Select Date until when to predict':
                 with column2:
                     d = st.date_input("Select the date till when to predict :",
                                       datetime.date.today()+datetime.timedelta(days=1),
                                       min_value=datetime.date.today()+datetime.timedelta(days=1))
                     st.write('Predicting till :', d)
                     def numOfDays(date1, date2):
                      #check which date is greater to avoid days output in -ve number
                        if date2 > date1:   
                            return (date2-date1).days
                        else:
                            return (st.error('Error: End date must fall after start date.'))
                     
                     
                     # Driver program
                     date1 = date(2023, 11, 17)
                     #date2 = d
                     no_of_days=numOfDays(date1, d)#no of days between last date we have data till and selected date
                     #st.write("a",no_of_days)
                     
                     gap_days=datetime.date.today()-date1#no of days between last date we have data till and current date
                     #st.write(gap_days)
                     if no_of_days > gap_days.days:   
                         total=no_of_days-gap_days.days
                     else:
                         st.error("Please selet future dates")
                  
                     
                     #st.write(total)
                     #no_of_days=d-date(2025, 11, 17)
                     ypred_future=loaded_model.predict(start=9498,end=9498+no_of_days)#521 days or 2 years
                     futuredate_arima=pd.DataFrame({'Close':ypred_future})
                     futuredate_arima=pd.DataFrame({'Close':ypred_future})
                     futuredate_arima['Date']=pd.date_range(start='2023-11-17',end=d)
                     future_data_Arima=pd.concat([df1,futuredate_arima])
                     future_data_Arima=future_data_Arima.set_index('Date')
                     futuredate_arima.set_index('Date',inplace=True)
                     col1,col2=st.columns([1,2])
                     col1.dataframe(futuredate_arima.iloc[-1])
                     col2.line_chart(future_data_Arima)
                     col2.line_chart(futuredate_arima['Close'])
                     col1.dataframe(futuredate_arima.iloc[-total:])
                     
                        
    if plots=='2 years forecasted data':
                
                column2.write('Microsoft stock data from 1986-03-13 to 2025-11-16 ')
                with column2:
                    predicting(730)
               


                
    if plots=='1 year forecasted data':
              column2.write('Microsoft stock data from 1986-03-13 to 2024-11-16 ')
              with column2:
                  predicting(365)#261 days or 1 year
               
    if plots=='6 months forecasted data':
               column2.write('Microsoft stock data from 1986-03-13 to 2024-05-16 ')
               with column2:
                   predicting(180)#129 days or 6 months
                  
                
       
    