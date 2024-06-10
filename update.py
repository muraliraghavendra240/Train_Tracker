import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data
def update():   
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_No' , 'Name' , 'Train_Type' , 'Source' , 'Destination' ,'Availability'])
    with st.expander("Current Trains"):       
        st.dataframe(df)  
    list_of_dealers = [i[0] for i in view_only_dealer_names()]  
    selected_dealer = st.selectbox("Train to Edit", list_of_dealers)  
    selected_result = get_dealer(selected_dealer)
    if selected_result:   
            Train_No = selected_result[0][0]       
            Name = selected_result[0][1]        
            Train_Type = selected_result[0][2]       
            Source = selected_result[0][3]       
            Destination = selected_result[0][4]
            Availability=selected_result[0][5]
            col1, col2 = st.columns(2)
            with col1:           
                new_Train_No = st.text_input("Train_No:",Train_No)    
                new_Train_name = st.text_input("Name:",Name)
            with col2:          
                new_Train_Type = st.text_input("Train_Type:",Train_Type)
                new_Source= st.text_input("Source:",Source)  
                new_Destination = st.text_input("Destination:",Destination)
                new_Availability = st.selectbox(Availability, ["Yes", "No"])
            if st.button("Update Train"):           
                edit_dealer_data(new_Train_No , new_Train_name , new_Train_Type , new_Source , new_Destination ,new_Availability , Train_No , Name , Train_Type , Source , Destination ,Availability) 
                st.success("Successfully updated:: {} to ::{}".format(Train_No, new_Train_No))   
    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Train_No' , 'Name' , 'Train_Type' , 'Source' , 'Destination' ,'Availability'])
    with st.expander("Updated data"):    
         st.dataframe(df2)