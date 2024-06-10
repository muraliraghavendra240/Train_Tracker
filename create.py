import streamlit as st
from database import add_data
def create():   
    col1, col2 = st.columns(2)
    with col1:        
        Train_No = st.text_input("Train_No:")    
        Train_name = st.text_input("Name:")
    with col2:        
        Train_Type = st.text_input("Train_Type")
        Source= st.text_input("Source:")  
        Destination = st.text_input("Destination:")
        Availability = st.selectbox("Availability", ["Yes", "No"])
    if st.button("Add Train"):    
        add_data(Train_No , Train_name , Train_Type , Source , Destination ,Availability) 
        st.success("Successfully added Train: {}".format(Train_No))