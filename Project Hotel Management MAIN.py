import csv

hotel_fields = ['ID', 'Name', 'Age','Address','Country', 'Email', 'Phone','Checkin date','Checkout date','Room number',
                'Roomrent','Restaurent bill','Laundry bill','Gaming bill','Total bill']
hotel_database = 'hotelrecord.csv'

def add_Customer():

    print("-------------------------")
    print("Add Customer Information")
    print("-------------------------")
    global hotel_fields
    global hotel_database           

    Customer_data = []
    for i in range(9):
        value = input("Enter " + hotel_fields[i] + ": ")
        Customer_data.append(value)
    print ("\n ***** We Have The Following Rooms For You *****")
    print (" 1. Ultra Royal ------> Rs.10000 ")
    print (" 2. Royal  -----------> Rs.5000 ")
    print (" 3. Elite  -----------> Rs.3500  ")
    print (" 4. Budget -----------> Rs.2500 \n")

    roomchoice=int(input("Please Enter Your Choice --> "))
    noofdays=int(input("For How Many Nights Did You Wish To Stay : "))
    roomno=int(input("Enter Customer Room No. : "))
    Customer_data.append(roomno)

    if roomchoice==1:
        roomrent = noofdays * 10000
        print("\nUltra Royal Room Rent : ",roomrent)
    elif roomchoice==2:
        roomrent = noofdays * 5000
        print("\nRoyal Room Rent : ",roomrent)
    elif roomchoice==3:
        roomrent = noofdays * 3500
        print("\nElite Royal Room Rent : ",roomrent)
    elif roomchoice==4:
        roomrent = noofdays * 2500
        print("\nBudget Room Rent : ",roomrent)
    else:
        print("Sorry, May Be You Are Giving Me The Wrong Input. Please Try Again !!!")
        return

    dt=[0,0,0,roomrent]
    Customer_data.append(roomrent)
    Customer_data=Customer_data+dt

    with open(hotel_database, "a") as f:
        writer = csv.writer(f)
        writer.writerows([Customer_data])
    print("\nData saved successfully")
    input("\nPress any key to continue")
    return

def restaurantbill():
    ID=int(input("Enter your ID : "))

    print("\n******RESTAURANT MENU******\n")

    print("""1. Water -------> Rs.20 \n2. Tea -------> Rs.10 \n3. Breakfast Combo -----> Rs.90 \n4. Lunch -------> Rs.110
5. Dinner -----> Rs.150 \n6. Exit\n """)
    choice=int(input("Enter Your Choice : "))
    quantity=int(input("Enter The Quantity : "))

    if (choice==1):
        rtbill = quantity * 20
    elif (choice==2):
        rtbill = quantity * 10
    elif (choice==3):
        rtbill = quantity * 90
    elif (choice==4):
        rtbill = quantity * 110
    elif (choice==5):
        rtbill = quantity * 150
    elif (choice==6):
        return
    else:
        print("Invalid option")
        return

    print ("Total Food Cost = Rs.",rtbill,"\n")

    with open(hotel_database, "r",) as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    i[11] = eval(i[11]) + rtbill
                    i[14] = eval(i[14]) + rtbill
                    data.append(i)
                else:
                    data.append(i)
    with open(hotel_database, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    input('\nPress Any Key To Continue')
    return

def gamingbill():
    ID=int(input("Enter your ID : "))

    print ("\n******GAME MENU*******\n")

    print("""1. Table Tennis -----> Rs.150/HR \n2. Bowling -----> Rs.100/HR \n3. Snooker -----> Rs.250/HR
4. VR Gaming -----> Rs.400/HR \n5. Console Gaming -----> Rs.300/HR \n6. Swimming Pool Games ----> Rs.350/HR
7. Exit\n """)

    game=int(input("Enter What Game You Want To Play : "))
    hour=int(input("Enter No Of Hours You Want To Play : "))
    print("\n\n*************************************************\n")
    if game==1:
        print("YOU HAVE SELECTED TO PLAY : Table Tennis")
        gamebill = hour * 150
    elif game==2:
        print("YOU HAVE SELECTED TO PLAY : Bowling")
        gamebill = hour * 100
    elif game==3:
        print("YOU HAVE SELECTED TO PLAY : Snooker")
        gamebill = hour * 250
    elif game==4:
        print("YOU HAVE SELECTED TO PLAY : VR Gaming")
        gamebill = hour * 400
    elif game==5:
        print("YOU HAVE SELECTED TO PLAY : Console Gaming")
        gamebill = hour * 300
    elif game ==6:
        print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
    elif game ==7:
        return
    else:
        print('Invalid Input')
        return

    print ("Your Total Gaming Bill = Rs.",gamebill,"\n")

    with open(hotel_database, "r") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    i[13] = eval(i[13]) + gamebill
                    i[14] = eval(i[14]) + gamebill
                    data.append(i)
                else:
                    data.append(i)
    with open(hotel_database, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    input('\nPress Any Key To Continue')
    return

def laundrybill():
    ID = input('Enter Customer ID : ')

    print ("\n******LAUNDRY MENU*******\n")

    print ("""1. Shorts----> Rs.30 \n2. Pants----> Rs.40 \n3. Shirt----> Rs.50 \n4. Saree----> Rs.60 \n5. Chudidhar----> Rs.80
6. Exit\n """)
         
    laundary=int(input("Enter Your Choice : "))
    quantity=int(input("Enter The Quantity : "))

    if laundary==1:
        launbill = quantity * 30
    elif laundary==2:
        launbill = quantity * 40
    elif laundary==3:
        launbill = quantity * 50
    elif laundary==4:
        launbill = quantity * 60
    elif laundary==5:
        launbill = quantity * 80
    elif laundary==6:
        return
    else:
        print ("Invalid Option")
        return
    print ("Your Total Laundry Bill = Rs.",launbill,"\n")

    with open(hotel_database, "r") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    i[12] = eval(i[12]) + launbill
                    i[14] = eval(i[14]) + launbill
                    data.append(i)
                else:
                    data.append(i)
    with open(hotel_database, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    input('\nPress Any Key To Continue')
    return

def search():
    Name = input('Enter Customer Name You Want To Search : ')
    with open(hotel_database, "r") as f:
        reader = csv.reader(f)
        count = 0
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[1].lower() == Name.lower():
                    print(i[0:7])
                    count = count + 1
        if count == 0:
            print('No Customer Data Found!')

    input('\nPress any key to continue')

def totalbill():
    global hotel_database
    global hotel_fields
    ID = input('Enter Customer ID : ')
    print ("\n******HOTEL BILL******")
    with open('hotelrecord.csv', "r") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    for j in range(0,15):
                        print('\nCustomer',hotel_fields[j],':',i[j])

    input('\nPress Any Key To Continue')
    return

while(True):
    print("""
1--->Enter Customer Details
2--->Calculate Restaurent Bill
3--->Calculate Laundry Bill
4--->Calculate Gaming Bill
5--->Search Customer
6--->GENERATE TOTAL BILL AMOUNT
7--->EXIT """)
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        add_Customer()
    elif choice ==2:
        restaurantbill()
    elif choice == 3:
        laundrybill()
    elif choice ==4:
        gamingbill()
    elif choice ==5:
        search()
    elif choice ==6:
        totalbill()
    elif choice ==7:
        print("--------------------------------")
        print(" Thank You For Using Our System ")
        print("--------------------------------")
        break
