from Models import *
import os
import datetime

db = SqliteDatabase("data.db")

def createBD():
    data = False
    if os.path.isfile("data.db"):
        os.remove("data.db")
    with db:
        db.create_tables([Client, Order])
        data = True
    return data

def fillBD():
    data = False
    if (os.path.isfile("data.db")):
        with db:
            clients = [
                {'Name':'David','City':'Al Mithnab','Address':'46 Kyle Valley'},
                {'Name':'William','City':'Fredrikstad','Address':'Flat 28g Liam Brooks'},
                {'Name':'Anthony','City':'Naga','Address':'09 Wilson Harbours'},
                {'Name':'Christopher','City':'Abepura','Address':'08 Jordan Pine'},
                {'Name':'Richard','City':'Zografou','Address':'Flat 48 Yasmine'},
                {'Name':'Kevin','City':'Oosterhout','Address':'3 Colin Avenue Paulaport'},
                {'Name':'Jeremy','City':'Adelaide','Address':'948 Matilda Common'},
                {'Name':'Jack','City':'Astana','Address':'Studio 15y Lilly Lock'},
                {'Name':'Joseph','City':'Bandung','Address':'14 Saunders Hollow'},
                {'Name':'Kevin','City':'Berlin','Address':'693 Lee Circles'}
            ]
            Client.insert_many(clients).execute()
            unit = Client.select()
            orders = [
                {'Client_id':unit[0],'Date':datetime.date(2023,1,12),'Amount':10,'Description':'Car'},
                {'Client_id':unit[1],'Date':datetime.date(2023,1,1),'Amount':40,'Description':'Snake'},
                {'Client_id':unit[2],'Date':datetime.date(2023,1,22),'Amount':50,'Description':'Crown'},
                {'Client_id':unit[3],'Date':datetime.date(2023,1,25),'Amount':200,'Description':'Cat'},
                {'Client_id':unit[4],'Date':datetime.date(2023,1,9),'Amount':140,'Description':'Boat'},
                {'Client_id':unit[5],'Date':datetime.date(2023,1,13),'Amount':150,'Description':'Chane'},
                {'Client_id':unit[6],'Date':datetime.date(2023,1,10),'Amount':30,'Description':'Chips'},
                {'Client_id':unit[7],'Date':datetime.date(2023,1,5),'Amount':90,'Description':'Lamp'},
                {'Client_id':unit[8],'Date':datetime.date(2023,1,11),'Amount':13,'Description':'Sins'},
                {'Client_id':unit[9],'Date':datetime.date(2023,1,14),'Amount':20,'Description':'Bottles'}
            ]
            Order.insert_many(orders).execute()
    else:
        print("DB IS NOT EXIST")

def showClientsBD():
    data = False
    if (os.path.isfile("data.db")):
        print(f"{'id' : <10}{'Name' : <15}{'City' : <15}{'Address' : <10}")
        for i in Client.select():
            print(f"{i.id : <10}{i.Name : <15}{i.City : <15}{i.Address : <10}")
    else:
        print("DB IS NOT EXIST")
    return Client.select().count()

def showOrdersBD():
    data = False
    if (os.path.isfile("data.db")):
        print(f"{'id' : <10}{'Client_id' : <14}{'Date' : <16}{'Amount' : <10}{'Description' : <10}")
        for i in Order.select():
            print(f"{i.id : <10}{i.Client_id}\t\t{i.Date}\t{i.Amount : <10}{i.Description : <10}")
    else:
        print("DB IS NOT EXIST")
    return Order.select().count()
        

if __name__ == "__main__":
    while True:
        print("---MENU---")
        print("init\nfill\nshow [CLIENTS/ORDERS]\nexit")
        x = input()
        if (x == 'init'):
            createBD()
             
        elif (x == 'fill'):
            fillBD()
            
        elif (x == 'show CLIENTS'):
            showClientsBD()

        elif (x == 'show ORDERS'):
            showOrdersBD()

        elif (x == 'exit'):
            break

        else:
            print("INCORRECT INPUT")

