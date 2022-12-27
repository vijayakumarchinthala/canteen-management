n=int(input("Press 1 to go to the ordering window\nPress 2 to view a specific receipt\nPress 3 to delete a record using phone number"))
import mysql.connector as mc
if n==1:
    from tkinter import *
    import random
    import datetime
    import time
    import mysql.connector as mc


    root=Tk()
    root.geometry("3840x2160")
    root.title("Canteen management System")


    tops=Frame(root, width=1600,relief=SUNKEN)
    tops.pack(side=TOP)

    f1=Frame(root,width=800,height=700,relief=SUNKEN, bd=20)
    f1.pack(side=LEFT)

    f2=Frame(root,width=800,height=700,relief=SUNKEN,bg='white',bd=10)
    f2.pack(side=RIGHT)

    localtime=time.asctime()

    lblInfo=Label(tops, font=('helvetica',50),text="GVK Chinmaya Vidyalaya ",fg="Black",bd=10)
    lblInfo.grid(row=0,column=0)

    lblInfo=Label(tops,font=('arial',20,'bold'),text=localtime,fg="red",bd=10)
    lblInfo.grid(row=1,column=0)


    def Ref():
        
        phn=rand.get()
            
        if (Patties.get()==""):
            CoPatties=0
        else:
            CoPatties=int(Patties.get())
        
        if (Noodles.get()==""):
            CoNoodles=0
        else:
            CoNoodles=int(Noodles.get())

        if (Samosa.get()==""):
            CoSamosa=0
        else:
            CoSamosa=int(Samosa.get())

        if (Cocacola.get()==""):
            CoD=0
        else:
            CoD=int(Cocacola.get())
            
        if (Burger.get()==""):
            CoBurger=0
        else:
            CoBurger=float(Burger.get())

            
        if (Sandwich.get()==""):
            CoSandwich=0
        else:
            CoSandwich=float(Sandwich.get())

                       
        CostofPatties =CoPatties * 20
        CostofCocacola=CoD * 25
        CostofNoodles = CoNoodles* 30
        CostofSamosa = CoSamosa * 7
        CostBurger = CoBurger* 40
        CostSandwich=CoSandwich * 30
        

        TotalCost=(CostofPatties+CostofCocacola+CostofNoodles+CostofSamosa+CostBurger+CostSandwich)
     
        FinalCost ="Rs"+str (TotalCost)


        Total.set(FinalCost)


    rand = StringVar()
    Patties=StringVar()
    Noodles=StringVar()
    Samosa=StringVar()
    Total=StringVar()
    Cocacola=StringVar()
    Burger=StringVar()
    Sandwich=StringVar()

    lblnote= Label(tops, font=('arial', 16,'bold'),text="NOTE: Please add a zero against the food item not ordered by the customer")
    lblnote.grid(row=2, column=0)

    lblReference= Label(f1, font=('arial', 16,'bold'),text="Phone number",bd=40)
    lblReference.grid(row=0, column=0)
    txtReference=Entry(f1, font=('arial',16),textvariable=rand,bg="white",bd=10, justify='right')
    txtReference.grid(row=0,column=1)

    lblPatties= Label(f1, font=('arial', 16,'bold'),text="Patties (Rs.20)",bd=40)
    lblPatties.grid(row=1, column=0)
    txtPatties=Entry(f1, font=('arial',16),textvariable=Patties,bg="white",justify='right',bd=10)
    txtPatties.grid(row=1,column=1)


    lblNoodles= Label(f1, font=('arial', 16,'bold'),text="Noodles (Rs.30)",bd=40)
    lblNoodles.grid(row=2, column=0)
    txtNoodles=Entry(f1, font=('arial',16),textvariable=Noodles,bg="white",justify='right',bd=10)
    txtNoodles.grid(row=2,column=1)


    lblSamosa= Label(f1, font=('arial', 16,'bold'),text="Samosa (Rs.7)",bd=40)
    lblSamosa.grid(row=3, column=0)
    txtSamosa=Entry(f1, font=('arial',16),textvariable=Samosa,bg="white",justify='right',bd=10)
    txtSamosa.grid(row=3,column=1)


    lblCocacola= Label(f1, font=('arial', 16,'bold'),text="Coca-cola (Rs.25)",bd=40)
    lblCocacola.grid(row=0, column=2)
    txtCocacola=Entry(f1, font=('arial',16),textvariable=Cocacola,bg="white",justify='right',bd=10)
    txtCocacola.grid(row=0,column=3)

    lblBurger= Label(f1, font=('arial', 16,'bold'),text="Burger (Rs.40)",bd=40)
    lblBurger.grid(row=1, column=2)
    txtBurger=Entry(f1, font=('arial',16),textvariable=Burger,bg="white",justify='right',bd=10)
    txtBurger.grid(row=1,column=3)


    lblSandwich= Label(f1, font=('arial', 16,'bold'),text="Sandwich (Rs.30)",bd=40)
    lblSandwich.grid(row=2, column=2)
    txtSandwich=Entry(f1, font=('arial',16),textvariable=Sandwich,bg="white",justify='right',bd=10)
    txtSandwich.grid(row=2,column=3)


    lblTotalCost= Label(f1, font=('arial', 16,'bold'),text="Total Cost",bd=40)
    lblTotalCost.grid(row=3, column=2)
    txtTotalCost=Entry(f1, font=('arial',16),textvariable=Total,bg="powder blue",bd=10, justify='right')
    txtTotalCost.grid(row=3,column=3)

    #RECEIPT#########################################################################################
    lblReference= Label(f2, font=('arial', 16),text="Reference:", bg='white')
    lblReference.grid(row=0, column=0)
    txtReference=Label(f2, font=('arial',16),textvariable=rand,bg="white",width=20)
    txtReference.grid(row=0,column=1)

    lblPatties= Label(f2, font=('arial', 16),text="Patties:", bg='white')
    lblPatties.grid(row=1, column=0)
    txtPatties=Label(f2, font=('arial',16),textvariable=Patties,bg="white",width=20)
    txtPatties.grid(row=1,column=1)

    lblNoodles= Label(f2, font=('arial', 16),text="Noodles:", bg='white')
    lblNoodles.grid(row=2, column=0)
    txtNoodles=Label(f2, font=('arial',16),textvariable=Noodles,bg="white",width=20)
    txtNoodles.grid(row=2,column=1)

    lblSamosa= Label(f2, font=('arial', 16),text="Samosa:", bg='white')
    lblSamosa.grid(row=3, column=0)
    txtSamosa=Label(f2, font=('arial',16),textvariable=Samosa,bg="white",width=20)
    txtSamosa.grid(row=3,column=1)

    lblCocacola= Label(f2, font=('arial', 16),text="Coca-cola:", bg='white')
    lblCocacola.grid(row=4, column=0)
    txtCocacola=Label(f2, font=('arial',16),textvariable=Cocacola,bg="white",width=20)
    txtCocacola.grid(row=4,column=1)

    lblBurger= Label(f2, font=('arial', 16),text="Burger:", bg='white')
    lblBurger.grid(row=5, column=0)
    txtBurger=Label(f2, font=('arial',16),textvariable=Burger,bg="white",width=20)
    txtBurger.grid(row=5,column=1)

    lblSandwich= Label(f2, font=('arial', 16),text="Sandwich:", bg='white')
    lblSandwich.grid(row=6, column=0)
    txtSandwich=Label(f2, font=('arial',16),textvariable=Sandwich,bg="white",width=20)
    txtSandwich.grid(row=6,column=1)

    lblTotalCost= Label(f2, font=('arial', 16),text="Total Cost:", bg='white')
    lblTotalCost.grid(row=7, column=0)
    txtTotalCost=Label(f2, font=('arial',16),textvariable=Total,bg="white", width=20)
    txtTotalCost.grid(row=7,column=1)

    lblsalutation=Label(f2, font=('arial',16), text="Do visit again :)", bg='white')
    lblsalutation.grid(row=8, column=1)


    def qexit():
        root.destroy()

    btntotal=Button(f1,padx=16,pady=8,fg="black",font=('arial',16),width=10,text="Total",bg="red",command=Ref)
    btntotal.grid(row=6,column=1)
    btnexit=Button(f1,padx=16,pady=8,fg="black",font=('arial',16),width=10,text="Exit",bg="red",command=qexit)
    btnexit.grid(row=6,column=2)

    def reset():
        Patties.set("")
        Noodles.set("")
        Samosa.set("")
        Cocacola.set("")
        Total.set("")
        rand.set("")
        Burger.set("")
        Sandwich.set("")


    btnreset=Button(f1,padx=16,pady=8,fg="black",font=('arial',16),width=10,text="Reset",bg="red",command=reset)
    btnreset.grid(row=6,column=3)

    def save():
        mycon=mc.connect(host="localhost", user="root", password='tiger',database="gvkcv")
        cursor=mycon.cursor()
        r=rand.get()
        p=Patties.get()
        n=Noodles.get()
        sa=Samosa.get()
        co=Cocacola.get()
        b=Burger.get()
        sand=Sandwich.get()
        total=Total.get()
        s='INSERT INTO invoices values(%s,%s,%s,%s,%s,%s,%s,%s)'
        t=[r,p,n,sa,co,b,sand,total]
        cursor.execute(s,t)
        mycon.commit()
        print("value inserted")
        mycon.close()

    btnsave=Button(f1,padx=16,pady=8,fg="black",font=('arial',16),width=10,text="save",bg="red",command=save)
    btnsave.grid(row=7,column=3)
elif n==2:
    mycon=mc.connect(host="localhost", user="root", password='tiger',database="gvkcv")
    cursor=mycon.cursor()
    phnno=int(input("enter the phone no"))
    print("total cost:")
    s="select total from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    print("No of sandwiches:")
    s="select sandwich from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    print("No of patties:")
    s="select patties from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    print("No of noodles:")
    s="select noodles from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    print("No of samosa:")
    s="select samosa from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    print("No of coca cola:")
    s="select cocacola from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    print("No of burgers:")
    s="select burger from invoices where Phonenumber=%s;"
    t=[phnno]
    cursor.execute(s,t)
    data=cursor.fetchall()
    print(data)
    mycon.commit()
    mycon.close()
elif n==3:
    mycon=mc.connect(host="localhost", user="root", password='tiger',database="gvkcv")
    cursor=mycon.cursor()
    phnno=int(input("enter phn no whose record you wanna delete"))
    s="delete from invoices where Phonenumber=%s"
    t=[phnno]
    cursor.execute(s,t)
    mycon.commit()
    mycon.close()
    print("Record deleted")
    



