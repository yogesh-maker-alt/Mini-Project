import mysql.connector
import streamlit as st

#import emoji

# import library for connection.
mydb = mysql.connector.connect(user='root', password='12345', host='localhost', database='CUST_MANAGEMENT')
mycursor = mydb.cursor()

add = mydb.cursor()
print("Connection Established.")


# col="INSERT INTO CUST_INFO (CUST_NAME, PH_NUMBER, ADDRESS, PINCODE) VALUES (%s,%s,%s,%s)"
# val=(input("Enter you name : "),input("Enter you contact number : "),input("Enter you address : "),int(input("Enter you pincode : ")))
#
#

# Create stremlit app

def main():
    global add
    st.title("ORDER MANAGEMENT SYSTEM ")

    st.expander(":smile:")

    # Display options for CRUD operations
    option = st.sidebar.selectbox("Select an option", ("Customers", "Orders"))
    # Perform selected CRUD Operations
    if option == "Customers":
        st.subheader("Enter Customers Details")
        CUST_NAME = st.text_input("Enter you name : ")
        CUST_CONT = st.number_input("Enter you contact number : ")
        CUST_ADD = st.text_input("Enter you address : ")
        CUST_PINCODE = st.number_input("Enter you pincode : ")
        if st.button("Create"):
            col = "INSERT INTO CUST_INFO (CUST_NAME, PH_NUMBER, ADDRESS, PINCODE) VALUES (%s,%s,%s,%s)"
            val = (CUST_NAME, CUST_CONT, CUST_ADD, CUST_PINCODE)
            add.execute(col, val)
            mydb.commit()
            st.success("Data added successfully!!!")


    else:
        st.subheader("Enter Orders Details")
        PRODUCT = st.text_input("Enter Product Name : ")
        ORDER_DATE = st.date_input("Enter Ordered Date :")
        SHIPPED_DATE = st.date_input("Enter Shipped Date")
        ORD_STATUS = st.text_input("Enter Order Status : ")
        CUST_ID = st.number_input("Enter customer ID: ")
        if st.button("Create"):
            column = "INSERT INTO CUST_ORDERS (PRODUCT,ORDER_DATE,SHIPPED_DATE,ORD_STATUS,CUST_ID) VALUES (%s,%s,%s,%s,%s)"
            value = (PRODUCT, ORDER_DATE, SHIPPED_DATE, ORD_STATUS, CUST_ID)
            add.execute(column, value)
            mydb.commit()
            st.success("Data added successfully!!!")


if __name__ == "__main__":
    main()

# print(add.rowcount,"record inserted.")


# print("Your cust_id",add.lastrowid,"done")

# st.title("Order Management Office")

# # side baar
# sidebar=st.sidebar.selectbox(
#     "Please select!!",
#     ("Customer","Order")
# )

# if sidebar == "Customer" :
#     a=st.dataframe(add)


# else :
#     pass





