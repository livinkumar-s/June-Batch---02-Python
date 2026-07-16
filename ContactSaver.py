import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="junebatch2"
)

cursor=conn.cursor()

# cursor.execute("SELECT * FROm actors")
# print(cursor.fetchmany(3))

# cursor.execute("INSERT INTO contacts (name, phone) VALUE (%s,%s)",["Ken","6383366775"])
# conn.commit()
# print("Contact added...!")

def addConcact():
    try:
       name=input("Enter the Name: ")
       phone=input("Enter the Phone Number: ")
       cursor.execute("INSERT INTO contacts (name, phone) VALUE (%s,%s)",[name,phone])
       conn.commit()
    except Exception:
        print("Give Valid Inputs...!")
        addConcact()
          
def viewAll():
    pass

def SearchContact():
    searchterm=input("Search Contact: ")
    pattern= f"%{searchterm}%"
    cursor.execute("SELECT name, phone from contacts WHERE name LIKE %s OR phone LIKE %s",[pattern,pattern])
    contacts=cursor.fetchall()

    for name,phone in contacts:
        print(f"Name: {name}, Phone: {phone}")

def DeleteContact():
    pass

def UpdateContact():
    searchterm=input("Search Contact: ")
    pattern= f"%{searchterm}%"
    cursor.execute("SELECT * from contacts WHERE name LIKE %s OR phone LIKE %s",[pattern,pattern])
    contacts=cursor.fetchall()

    if len(contacts)==0:
        print("No Matching Results")
        return

    for id,name,phone in contacts:
        print(f"Id: {id}, Name: {name}, Phone: {phone}")

    userId=int(input("Choose an Id: "))
    cursor.execute("SELECT name, phone FROM contacts where id=%s",[userId])
    currentDetails=cursor.fetchone()

    

    name=input(f"Enter The Name({currentDetails[0]}): ")
    phone=input(f"Enter The Phone Number({currentDetails[1]}): ")

    cursor.execute("UPDATE contacts SET name=%s, phone=%s WHERE id=%s",[name if name!="" else currentDetails[0],phone if phone!="" else currentDetails[1],userId])
    conn.commit()
    print("Updated Successfully...!")

# SearchContact --> choose id --> update....

while True:
    inp=int(input("0--> Exit\n1 --> Add Contact\n2 --> View All Contact\n3 --> Search Contact\n4 --> Delete Contact\n5 --> Update Contact\nChoose an Option: "))
    if inp==0:
        break
    elif inp==1:
        addConcact()
    elif inp==2:
        viewAll()
    elif inp==3:
        SearchContact()
    elif inp==4:
        DeleteContact()
    elif inp==5:
        UpdateContact()