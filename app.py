#import mysql.connector
#mydb = mysql.connector.connect(host="localhost",user="root",password="")
#c = mydb.cursor()
#c.execute("CREATE DATABASE train")
import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
def main():    
    st.title("Train App")    
    menu = ["Add", "View", "Update", "Delete"]   
    choice = st.sidebar.selectbox("Menu", menu)  
    create_table()
    if choice == "Add":        
        st.subheader("Enter Train Details:")       
        create()
    elif choice == "View":       
            st.subheader("View created tasks")       
            read()
    elif choice == "Update":    
        st.subheader("Update created tasks")      
        update()
    elif choice == "Delete":      
        st.subheader("Delete created tasks")       
        delete()
    else:        
        st.subheader("About tasks")
if __name__ == '__main__':   
    main()
