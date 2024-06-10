import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="train")
c = mydb.cursor()
def create_table():  
    c.execute('CREATE TABLE IF NOT EXISTS train(Train_No TEXT, Name TEXT, Train_Type TEXT, Source TEXT, Destination TEXT,Availability TEXT)')
def add_data(Train_No , Name , Train_Type , Source , Destination ,Availability ):   
    c.execute('INSERT INTO train(Train_No , Name , Train_Type , Source , Destination ,Availability) VALUES (%s,%s,%s,%s,%s, %s)',(Train_No , Name , Train_Type , Source , Destination ,Availability))  
    mydb.commit()
def view_all_data():    
    c.execute('SELECT * FROM train')    
    data = c.fetchall()
    return data
def view_only_dealer_names():  
    c.execute('SELECT Train_No FROM train')  
    data = c.fetchall()
    return data
def get_dealer(Train_No): 
    c.execute('SELECT * FROM train WHERE Train_No="{}"'.format(Train_No))   
    data = c.fetchall()
    return data
def edit_dealer_data(new_Train_No , new_Name , new_Train_Type , new_Source , new_Destination ,new_Availability , Train_No , Name , Train_Type , Source , Destination ,Availability ):  
    c.execute("UPDATE train SET Train_No=%s, Name=%s,Train_Type=%s, Source=%s, Destination=%s, Availability=%s WHERE Train_No=%s and Name=%s and Train_Type=%s and Source=%s and Destination=%s and Availability=%s", (new_Train_No , new_Name , new_Train_Type , new_Source , new_Destination ,new_Availability , Train_No , Name , Train_Type , Source , Destination ,Availability))   
    mydb.commit()   
    #data = c.fetchall()
    #return data
def delete_data(Train_No):  
    c.execute('DELETE FROM train WHERE Train_No="{}"'.format(Train_No))   
    mydb.commit()