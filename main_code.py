
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter

import sqlite3
from string import *
from tkinter import messagebox
#import subprocess as call
conn=sqlite3.Connection("example.db")


conn.execute('''CREATE TABLE IF NOT EXISTS TEST3
             ( ORIGIN TEXT NOT NULL,
             DESTINATION TEXT NOT NULL,
             NAME TEXT NOT NULL,
             DAY TEXT,MONTH TEXT,YEAR TEXT,GENDER TEXT,TIMING TEXT,MOBILE TEXT NOT NULL,PAIDTHROUGH TEXT NOT NULL,AMOUNTPAID TEXT NOT NULL);''')
conn.execute('''CREATE TABLE IF NOT EXISTS FEEDBACKT
             ( NAME TEXT NOT NULL,
             GENDER TEXT,MOBILE TEXT NOT NULL,BOOKINGEXPERIENCE TEXT NOT NULL,CUSTOMERSERVICE TEXT NOT NULL,
             CALLSERVICE  TEXT NOT NULL,PAYMENTEXPERIENCE TEXT NOT NULL);''')


def home():
    root=tk.Tk()
    root.geometry('10000x10000')
    root.title("VS Travelling Agency")
    swidth = root.winfo_screenwidth()
    sheight = root.winfo_screenheight()
    fr=tk.Frame(root,bg="white",width=swidth,height=sheight).pack()
    bon=Label(root,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
    come=Label(root,text="   Come Explore your Dreams!!!",font=("lucida calligraphy",25),bg="white").place(x=500,y=20)
    lab_me=tk.Label(root,bg="black").place(x=0,y=80,width=swidth,height=70)
    def about():
        root.destroy()
        rooa=tk.Tk()
        rooa.geometry("10000x10000")

        rooa.configure(bg='white')

        #g=Frame(height=700,width=1100,bg="White",highlightbackground="Black", highlightthickness=2)
        #g.place(x=130,y=20)
        title=Label(rooa, text="About Us...",width=10,height=2,bg="White",font=('Helvetica',40)).place(x=600,y=50)
        k=Label(rooa, text="Wake up to the adventure you've been dreaming about.You're about to embark on a journey. Maybe you're yearing for the peace and sancity of nature ?",width=150,height=2,bg="White",font=('Helvetica',10)).place(x=120,y=250)
        a=Label(rooa, text="Maybe you're on a quest to capture a lots of memory ? Or perhaps you'd rather assimilate the culture and ambience places .",width=150,height=2,bg="White",font=('Helvetica',10)).place(x=120,y=300)
        b=Label(rooa, text="Come on a journey with us and discover the choice of destinations offered to you by VS Travel & Tours.Whether your choice will lie with a superior",width=150,height=2,bg="White",font=('Helvetica',10)).place(x=120,y=350)
        c=Label(rooa, text="world class hotel, an unrivalled resort, our world-class National Parks, or one of our distinctive bush lodges, the experience begins here, with us.",width=150,height=2,bg="White",font=('Helvetica',10)).place(x=120,y=400)
        d=Label(rooa, text="Currently it is only available to the north India ,but soon will cover south India as well.",width=150,height=2,bg="White",font=('Helvetica',10)).place(x=120,y=450)
        e=d=Label(rooa, text="So come up with your dreams, the stage to be fulfilled by us .",width=150,height=2,bg="White",font=('Helvetica',10)).place(x=120,y=500)


       
        def home1():
            rooa.destroy()
            home()
        but=tk.Button(rooa,text="HOME",font=("lora",15),bg='lightblue',command=home1).place(width=350,height=40,x=500,y=600)
        rooa.mainloop()
    ab=tk.Button(root,text="ABOUT",bd=0,fg='white',bg='black',font=("lora",15),command=about)
    ab.place(x=10,y=100,width=150,height=40)
    def service():
        root.destroy()
        rooaa =tk.Tk()
        rooaa.configure(bg='white')
        rooaa.geometry("10000x10000")
     #   g=Frame(height=700,width=1100,bg="White",highlightbackground="black", highlightthickness=5)
        #g.place(x=130,y=20)
        title=Label(rooaa, text="Products and Services",width=20,height=2,bg="White",font=('Helvetica',40)).place(x=380,y=50)
        k=Label(rooaa, text="V S Travels has a wide range of products and services to cater to the varied requirements of",width=110,height=2,bg="White",font=('Helvetica',15)).place(x=80,y=250)
        a=Label(rooaa, text="their customers. The staff at this establishment are courteous and prompt at providing any assistance. They",width=110,height=2,bg="White",font=('Helvetica',15)).place(x=80,y=350)
        b=Label(rooaa, text="readily answer any queries or questions that you may have. Pay for the product or service with ease by using",width=110,height=2,bg="White",font=('Helvetica',15)).place(x=80,y=450)
        c=Label(rooaa, text="any of the available modes of payment, such as cash, paytm ,net banking.",width=110,height=2,bg="White",font=('Helvetica',15)).place(x=80,y=550)
        def homeser():
            rooaa.destroy()
            home()
        but_ser=tk.Button(rooaa,text="HOME",font=("lora",15),bg='grey',command=homeser).place(width=350,height=40,x=500,y=650)
        rooaa.mainloop()
    ser=tk.Button(root,text="SERVICES",bd=0,fg='white',bg='black',font=("lora",15),command=service)
    ser.place(x=150,y=100,width=150,height=40)
    def contact():
        root.destroy()
        r=Tk()
        r.geometry("10000x10000")
       
        global ee1,ee2,ee3,ee4,ee5,aa,bb,cc,dd,ee
        aa=StringVar()
        bb=StringVar()
        cc=StringVar()
        dd=StringVar()
        ee=StringVar()
       
        gg=Frame(r,height=768,width=670,bg="black")
        gg.place(x=2,y=2)
        lbl1=Label(r,text="Address",font=("helvetica",20),fg="white",bg="black").place(x=100,y=200)
        lbl2=Label(r,text="Lovely Professional University, Phagwara, Punjab",font=("helvetica",10),fg="white",bg="black").place(x=100,y=250)
        lbl3=Label(r,text="Lets Talk",font=("helvetica",20),fg="white",bg="black").place(x=100,y=300)
        lbl4=Label(r,text="+1800 123 8879",font=("helvetica",10),fg="green",bg="black").place(x=100,y=350)
        lbl5=Label(r,text="General Support",font=("helvetica",20),fg="white",bg="black").place(x=100,y=400)
        lbl6=Label(r,text="vstravels@gmail.com",font=("helvetica",10),fg="green",bg="black").place(x=100,y=450)
        hh=Frame(r,height=768,width=870,bg="white")
        hh.place(x=670,y=2)
        lab1=Label(r,text="Send Us A Message",font=("helvetica",40),bg="white").place(x=770,y=50)
        lab2=Label(r,text="TELL US YOUR NAME *",font=("helvetica",15),bg="white").place(x=770,y=170)
        

        ee1=Entry(r,textvariable=aa).place(x=770,y=210,width=350,height=13)
        
        lab3=Label(r,text="ENTER YOUR EMAIL *",font=("helvetica",15),bg="white").place(x=770,y=260)
        ee3=Entry(r,textvariable=cc,width="20").place(x=770,y=300,width=350,height=13)
        lab4=Label(r,text="ENTER PHONE NUMBER *",font=("helvetica",15),bg="white").place(x=770,y=350)
        ee4=Entry(r,textvariable=dd).place(x=770,y=390,width=350,height=13)
        lab5=Label(r,text="MESSAGE",font=("helvetica",15),bg="white").place(x=770,y=440)
        ee5=Entry(r,textvariable=ee,font=("helvetica",15)).place(x=770,y=480,width=600,height=80)
        def files():
                                          
            first_name=aa.get()
            
            
            email=cc.get()
            phone_no=dd.get()
            le=len(phone_no)
            message_=ee.get()
            
            if (first_name=="" and email=="" and phone_no=="" and message_==""):
                messagebox.showinfo("Warning","Please fill all entries")
            elif(first_name.isalpha()==False ):
                messagebox.showinfo("warning","Name cannot contain numbers")
            elif (le!=10 or phone_no.isalpha==False):
                messagebox.showinfo("Warning","Invalid number")
            elif (phone_no.startswith("0") or phone_no.startswith("1") or phone_no.startswith("2") or phone_no.startswith("3") or phone_no.startswith("4") or phone_no.startswith("5")):
                messagebox.showerror("Warning ","INVALID NUMBER")  
            elif "@" not in email:
                messagebox.showinfo("Error","Invalid Email")
            elif ".com" not in email:
                messagebox.showinfo("Error","Invalid Email")    
            else:
                f8=open("Travel1.txt","a")
                f8.write(first_name+" ")
                
                f8.write(email+"\n")
                f8.write(phone_no+"\n")
                f8.write(message_+"\n\n")
                f8.close()
                messagebox.showinfo("Congratulations","Message Successfully received !")
                r.destroy()
                home()
                
                
                
                
                
               
                
            
                
        bt=Button(r,text="SEND MESSAGE",font=("helvetica",12),bg="green",command=files).place(x=950,y=600)
        def homm():
            r.destroy()
            home()
           
        Button(r,text="Home",command=homm,font=("helvetica",12),bg="green").place(x=1000,y=680)
        r.mainloop()

       
        
        
    con=tk.Button(root,text="CONTACT",bd=0,fg='white',bg='black',font=("lora",15),command=contact)
    con.place(x=300,y=100,width=150,height=40)
   
    def feed():
        root.destroy()
        roof=tk.Tk()
        roof.title("FEEDBACK FORM")
        frame_feed=tk.Frame(roof,bg="white",width=swidth,height=sheight).pack()
        bon=Label(roof,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
        come=Label(roof,text="   Come Explore your Dreams!!!",font=("lucida calligraphy",25),bg="white").place(x=500,y=20)
        ab_me=tk.Label(roof,bg="black").place(x=0,y=80,width=swidth,height=70)
        ab_=tk.Label(roof,text=". . . FEEDBACK FORM  . . .",font=("lucida calligraphy",25),bg="black",fg="white").place(x=550,y=100)
        frame_entry=tk.Frame(roof,bg="grey",width="1300",height="700").place(x=100,y=200)
        lab_name=tk.Label(roof,text="NAME :",bg="grey",font=("lucida calligraphy",15)).place(x=110,y=300)
        name_of=StringVar()
        mobile_num=StringVar()
        genderf=StringVar()
        b_e=StringVar()
        c_s=StringVar()
        cll_s=StringVar()
        p_exp=StringVar()
        val=['EXCELLENT','VERY GOOD','GOOD','BAD','WORST']
        name_enr=tk.Entry(roof,textvariable=name_of).place(x=110,y=350,width=450,height=40)
        lab_mob=tk.Label(roof,text="MOBILE NUMBER :",bg="grey",font=("lucida calligraphy",15)).place(x=700,y=300)
        mob_enr=tk.Entry(roof,textvariable=mobile_num).place(x=700,y=350,width=450,height=40)
        lab_gender=tk.Label(roof,text="Gender:",bg="grey",font=("lucida calligraphy",15)).place(x=110,y=400)
        sex_enr=ttk.Combobox(roof,textvariable=genderf,values=['Male','Female','Others']).place(x=110,y=450,height=40,width=450)
        lab_b_e=tk.Label(roof,text="BOOKING EXPERIENCE :",bg="grey",font=("lucida calligraphy",15)).place(x=700,y=400)
        b_e_enr=ttk.Combobox(roof,textvariable=b_e,values=val).place(x=700,y=450,height=40,width=450)
        lab_c_s=tk.Label(roof,text="CUSTOMER SERVICE :",bg="grey",font=("lucida calligraphy",15)).place(x=110,y=500)
        c_s_enr=ttk.Combobox(roof,textvariable=c_s,values=val).place(x=110,y=550,height=40,width=450)
        lab_cll_s=tk.Label(roof,text="CALL SERVICE :",bg="grey",font=("lucida calligraphy",15)).place(x=700,y=500)
        cll_s_enr=ttk.Combobox(roof,textvariable=cll_s,values=val).place(x=700,y=550,height=40,width=450)
        lab_p_exp=tk.Label(roof,text="PAYMENT EXPERIENCE :",bg="grey",font=("lucida calligraphy",15)).place(x=110,y=600)
        p_exp_enr=ttk.Combobox(roof,textvariable=p_exp,values=val).place(x=110,y=650,height=40,width=450)
        def feedsql():
            a=name_of.get()
            b=mobile_num.get()
            l=len(b)
            c=genderf.get()
            d=b_e.get()
            e=c_s.get()
            f=cll_s.get()
            g=p_exp.get()
            if a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='':
                messagebox.showerror("WARNING","PLEASE ENTER THE ALL DETAILS")
                feed()
            elif (a.isalpha()==False):
                messagebox.showerror("WARNING","Name can only contain alphabets")
            elif (l!=10 or b.isalpha==False):
                messagebox.showinfo("Warning","Invalid number")
            elif (b.startswith("0") or b.startswith("1") or b.startswith("2") or b.startswith("3") or b.startswith("4") or b.startswith("5")):
                messagebox.showerror("Warning ","INVALID NUMBER") 
            else:
                dfed=(a,c,b,d,e,f,g)
                conn.execute(('''INSERT INTO  FEEDBACKT('NAME','GENDER','MOBILE','BOOKINGEXPERIENCE','CUSTOMERSERVICE','CALLSERVICE','PAYMENTEXPERIENCE')VALUES(?,?,?,?,?,?,?)'''),dfed)
                conn.commit()
                messagebox.showinfo("SUCESS","FEEDBACK SUBMITTED SUCESSFULLY")
                roof.destroy()
                home()
        b_submit=tk.Button(roof,text="SUBMIT",font=("lucida calligraphy",15),bg="Lightblue",command=feedsql).place(x=750,y=650,width=350,height=40)            
        roof.mainloop()
    fed=tk.Button(root,text="FEEDBACK",bd=0,fg='white',bg='black',font=("lora",15),command=feed)
    fed.place(x=450,y=100,width=150,height=40)
    def showbok():
        root.destroy()
        ros=tk.Tk()
        ros.configure(bg='grey')
        ros.geometry("10000x10000")
        #frww=tk.Frame(ros,bg="white",width=swidth,height=sheight).pack()
        cu=conn.cursor()
        cu.execute("""SELECT * FROM TEST3""" )
        Label(ros,text="From")
       
        for i in cu.fetchall():
           
            lab=tk.Label(ros,text=i, bg="grey",font=('lora',20)).pack()
           
           
        def homeb():
            ros.destroy()
            home()
        bu_t=tk.Button(ros,text="home",command=homeb,bg="black",font=("lucida calligraphy",15),fg="white",width=15,height=3).place(x=600,y=600)
       
               
       
    book=tk.Button(root,text="ALL BOOKINGS",bd=0,fg='white',bg='black',font=("lora",15),command=showbok)
    book.place(x=600,y=100,width=150,height=40)

    b=tk.Frame(root,bg="grey",width="1300",height="700").place(x=100,y=200)
    byk=tk.Message(root,text="BOOK ",width="200",bd=0,bg="grey",font=("lora",30)).place(x=600,y=220)
    def cancel():
        root.destroy()
        rooc=tk.Tk()
        #rooc.geometry('1000x1000')
        rooc_fr1=tk.Frame(rooc,bg="white",width=swidth,height=sheight).pack()
        log_1=Label(rooc_fr1,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
        log_2=Label(rooc_fr1,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
        rooc_fr2=tk.Label(rooc,bg="black").place(x=0,y=80,width=swidth,height=70)
        ab_can=tk.Button(rooc,text="ABOUT",bd=0,fg='white',bg='black',font=("lora",15))
        ab_can.place(x=10,y=100,width=150,height=40)
        ser_can=tk.Button(rooc,text="SERVICES",bd=0,fg='white',bg='black',font=("lora",15))
        ser_can.place(x=150,y=100,width=150,height=40)
        con_can=tk.Button(rooc,text="CONTACT",bd=0,fg='white',bg='black',font=("lora",15))
        con_can.place(x=300,y=100,width=150,height=40)
        b=tk.Frame(rooc,bg="grey",width="1300",height="500").place(x=100,y=200)
        mob_can=StringVar()
        mobile_en=tk.Label(rooc,text="ENTER YOUR MOBILE NUMBER :",font=("lora",20),bg="grey").place(x=200,y=350)
        mob_enR=tk.Entry(rooc,textvariable=mob_can).place(x=700,y=350,width=450,height=40)
       
        def dell():
            a=mob_can.get()
            conn.execute('''DELETE FROM TEST3 WHERE MOBILE=?''',(a,))
            conn.commit()
            
            messagebox.showinfo("Congrulations","YOUR TICKET WAS SUCESFULLY CANCELLED")
            rooc.destroy()
            home()
        def home_cancel():
            rooc.destroy()
            home()
            
        home1=tk.Button(rooc,text="CANCEL YOUR TICKET",bd=0,fg='white',bg='black',font=("lora",15),command=dell).place(x=1200,y=100)
        bu_t_home=tk.Button(rooc,text="HOME",font=("lora",18),command=home_cancel,bg="black",fg="white",width=25,height=3).place(x=600,y=550)

        
    can=tk.Button(root,text="CANCEL YOUR TICKET",bd=0,fg='white',bg='black',font=("lora",15),command=cancel).place(x=1200,y=100,width=400,height=40)
   
    fro=StringVar()
    to=StringVar()
    name=StringVar()
    gender=StringVar()
    mob=StringVar()
    year1=StringVar()
    month1=StringVar()
    day1=StringVar()
    btk=tk.Message(root,text="YOUR TICKETS ",width="400",bg="grey",bd=0,font=("lora",30)).place(x=500,y=270)
    lab_from=tk.Label(root,text="From*",font=("lora",15),bg='grey').place(x=120,y=350)
    e1=ttk.Combobox(root,textvariable=fro,values=['HYDERABAD','NEW DELHI','AMRITSAR','MUMBAI','KOLKTATA','VIJAYAWADA']).place(x=120,y=400,height="40",width="450")
    lab_from1=tk.Label(root,text="To*",font=("lora",15),bg='grey').place(x=120,y=450)
    year=list(range(2021,2023))
    month= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day=list(range(1,31))
    tim_ing=StringVar()
    e2=ttk.Combobox(root,values=['HYDERABAD','NEW DELHI','AMRITSAR','MUMBAI','KOLKTATA','VIJAYAWADA'],textvariable=to).place(x=120,y=500,height="40",width="450")
    lab_dat=tk.Label(root,text="YEAR*",font=("lora",10)).place(x=150,y=580,width=50,height=40)
    e3=ttk.Combobox(root,values=year,textvariable=year1).place(x=200,y=580,width=50,height=40)
    lab_dat=tk.Label(root,text="MONTH*",font=("lora",10)).place(x=280,y=580,width=50,height=40)
    e4=ttk.Combobox(root,values=month,textvariable=month1).place(x=330,y=580,width=60,height=40)
    lab_dat=tk.Label(root,text="DAY*",font=("lora",10)).place(x=450,y=580,width=50,height=40)
    e5=ttk.Combobox(root,values=day,textvariable=day1).place(x=500,y=580,width=50,height=40)
    #lab_from=tk.Label(root,text="Date(format:dd/mm/yyyy) *",font=("lora",15),bg='grey').place(x=120,y=550)
    #e3=tk.Entry(root,text="from*",fg="black",textvariable=dat).place(x=120,y=600,height="40",width="450")
    #lab_from=tk.Label(root,text="No of passengers *",font=("lora",15),bg='grey').place(x=120,y=650)
    #e4=tk.Entry(root,text="from*",fg="black",textvariable=nop).place(x=120,y=700,height="40",width="450")
    lab_nameof=tk.Label(root,text="Name of the passenger:",font=("lora",15),bg='grey').place(x=700,y=350)
    e_name=tk.Entry(root,textvariable=name).place(x=700,y=400,width=450,height=40)
    lab_sex=tk.Label(root,text='Gender',bg='grey',font=("lora",15)).place(x=700,y=450)
    e_sex=ttk.Combobox(root,textvariable=gender,values=['Male','Female','Others']).place(x=700,y=500,height=40,width=450)
    lab_mob=tk.Label(root,text="Mobile number : ",font=("lora",15),bg='grey').place(x=700,y=550)
    e_mob=tk.Entry(root,textvariable=mob).place(x=700,y=600,width=450,height=40)
    lab_timing=tk.Label(root,text="Choose your timing *",bg="grey",font=("lora",15)).place(x=120,y=650,)
    timing_a=ttk.Combobox(root,values=['12:00 am','6:00 am','9:00 am','12:00 pm','3:00 pm','6:00 pm','9:00 pm',],textvariable=tim_ing).place(x=120,y=700,height=40,width=450)
    def payment():
       
        roop=tk.Tk()
        roop.title("VS Travelling Agency")
        swidth = roop.winfo_screenwidth()
        sheight = roop.winfo_screenheight()
        fr=tk.Frame(roop,bg="white",width=swidth,height=sheight).pack()
        bon=Label(roop,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
        come=Label(roop,text="   Come Explore your Dreams!!!",font=("lucida calligraphy",25),bg="white").place(x=500,y=20)
        lab_me=tk.Label(roop,bg="black").place(x=0,y=80,width=swidth,height=70)
        but_home=tk.Button(roop,text="HOME",bg="black",bd=0,fg="white",font=("lucida calligraphy",25)).place(x=650,y=80)
        frame_pay=tk.Frame(roop,bg="grey").place(x=300,y=200,width=950,height=600)
        lab_heading=tk.Label(roop,bg='grey',font=("lucida calligraphy",20),text="PAYMENT GATEWAY").place(x=600,y=250)
        bu_paytm=tk.Button(roop,text="PAY WITH THE CASH",font=("lucida calligraphy",20),bg="lightblue").place(x=600,y=400)
        bu_paytm=tk.Button(roop,text="PAY WITH DEBIT/CREDIT/INTERNET BANKING",font=("lucida calligraphy",20),bg="lightblue").place(x=460,y=500)
        roop.mainloop()
    def pay():
        root.destroy()
       
        cur=conn.cursor()
        a=fro.get()
        b=to.get()
        c=name.get()
        d=gender.get()
        e=mob.get()
        le=len(e)
        f=year1.get()
        g=month1.get()
        h=day1.get()
        i=tim_ing.get()
        v1=c.isspace()
        v2=c.isalpha()
        if a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h==''or i=='':
            messagebox.showinfo("Warning!","Please Enter the required Fields !")
            home()
        elif(a==b):
            messagebox.showinfo("Destination and Arrivial cannot same")
            home()
       
        elif(c.isalpha()==False ):
            messagebox.showinfo("Name cannot conatain nubers")
            home()
        elif(le>10 or le<10):
            messagebox.showinfo("Warning ","INVALID NUMBER")
        else:
            if a=="HYDERABAD":
                if b=="NEWDELHI":
                    price=1000
                elif b=="AMRITSAR":
                    price=1200
                elif b=="MUMBAI":
                    price=1300
                elif b=="KOLKATA":
                    price=1400
                else:
                    price=1500
            elif a=="NEW DELHI":
                if b=="HYDERABAD":
                    price=1000
                elif b=="AMRITSAR":
                    price=1200
                elif b=="MUMBAI":
                    price=1300
                elif b=="KOLKATA":
                    price=1400
                else:
                    price=1500
            elif a=="MUMBAI":
                if b=="HYDERABAD":
                    price=1000
                elif b=="AMRITSAR":
                    price=1200
                elif b=="NEW DELHI":
                    price=1300
                elif b=="KOLKATA":
                    price=1400
                else:
                    price=1500  
            elif a=="KOLKATA":
                if b=="HYDERABAD":
                    price=1000
                elif b=="AMRITSAR":
                    price=1200
                elif b=="NEW DELHI":
                    price=1300
                elif b=="MUMBAI":
                    price=1400
                else:
                    price=1500  
            elif a=="AMRITSAR":
                if b=="HYDERABAD":
                    price=1000
                elif b=="AMRITSAR":
                    price=1200
                elif b=="NEW DELHI":
                    price=1300
                elif b=="KOLKATA":
                    price=1400
                else:
                    price=1500
            else:
                if b=="AMRITSAR":
                    price=2000
                elif b=="HYDERABAD":
                    price=1000
                elif b=="AMRITSAR":
                    price=1200
                elif b=="NEW DELHI":
                    price=1300
                else:
                    price=1500
           
            #defining sql
            roop=tk.Tk()
           
            roop.title("VS Travelling Agency")
            swidth = roop.winfo_screenwidth()
            sheight = roop.winfo_screenheight()
            fr=tk.Frame(roop,bg="white",width=swidth,height=sheight).pack()
            bon=Label(roop,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
            come=Label(roop,text="   Come Explore your Dreams!!!",font=("lucida calligraphy",25),bg="white").place(x=500,y=20)
            lab_me=tk.Label(roop,bg="black").place(x=0,y=80,width=swidth,height=70)
            but_home=tk.Button(roop,text="HOME",bg="black",bd=0,fg="white",font=("lucida calligraphy",25)).place(x=650,y=80)
            frame_pay=tk.Frame(roop,bg="grey").place(x=300,y=200,width=950,height=600)
            lab_heading=tk.Label(roop,bg='grey',font=("lucida calligraphy",20),text="PAYMENT GATEWAY").place(x=600,y=250)
            def paywith():
                p="CASH"
                dat=(a,b,c,h,g,f,d,i,e,p,price)
                date=h+'/'+g+'/'+f
                conn.execute('''INSERT INTO TEST3('ORIGIN','DESTINATION','NAME','DAY','MONTH','YEAR','GENDER','TIMING','MOBILE','PAIDTHROUGH','AMOUNTPAID')VALUES(?,?,?,?,?,?,?,?,?,?,?)''',dat)
               
                roott=tk.Tk()
                roop.destroy()
                roott.title("VS Travelling Agency")
                swidth = roott.winfo_screenwidth()
                sheight = roott.winfo_screenheight()
                fr=tk.Frame(roott,bg="white",width=swidth,height=sheight).pack()
                bon=Label(roott,text="V.S TRAVELS.. ",font=("lucida calligraphy",40,"bold"),bg="white",bd=0).place(x=10,y=10)
                come=Label(roott,text="   Come Explore your Dreams!!!",font=("lucida calligraphy",25),bg="white").place(x=500,y=20)
                frr_tk=tk.Frame(roott,bg="lightblue").place(x=150,y=100,width="1200",height="600")
                lab_from=tk.Label(roott,text="BOOKING DETAILS ",font=("lucida calligraphy",30,"bold"),bg="lightblue").place(x=500,y=150)
               
                lab_from=tk.Label(roott,text="FROM :  ",font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=160,y=250)
                lab_from1=tk.Label(roott,text=a,font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=350,y=250)
                lab_to=tk.Label(roott,text="TO : ",font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=900,y=250)
                lab_to1=tk.Label(roott,text=b,font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=1100,y=250)
                lab_tot=tk.Label(roott,text="TRAVELLING DATE  : ",font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=160,y=350)
                lab_tod=tk.Label(roott,text=date,font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=600,y=350)
                lab_to3=tk.Label(roott,text="AMOUNT PAID    :",font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=160,y=450)
                lab_to2=tk.Label(roott,text=price,font=("lucida calligraphy",20,"bold"),bd=0,bg="lightblue").place(x=600,y=450)


               
                #lab_tod=tk.Label(roott,text="To*",font=("lucida calligraphy",20,"bold")).place(x=1000,y=250)
                lab_stb=tk.Label(roott,text="BOOKING STATUS :",font=("lucida calligraphy",20,"bold"),bg='lightblue').place(x=150,y=530)
                lab_s=tk.Label(roott,text="CONFIRMED",font=("lucida calligraphy",20,"bold"),bg='lightblue').place(x=500,y=530)
                def lahome():
                    roott.destroy()
                    home()
                but_return=tk.Button(roott,text="home ",font=("lora",15),bg="Lightblue",command=lahome).place(x=500,y=600,width=350,height=40)
               
                roott.mainloop()
            bau_paytm=tk.Button(roop,text="PAY WITH THE CASH",font=("lucida calligraphy",20),bg="lightblue",command=paywith).place(x=600,y=400)
            new=1
            url="https://p-y.tX/UC-jmiq"
            def callback(url):
                webbrowser.open_new(url)
            link1 = tk.Label(roop, text="PAY WITH DEBIT/CREDIT/INTERNET BANKING", bg="lightblue", cursor="hand2",font=("lucida calligraphy",20))
            link1.place(x=460,y=500)
            link1.bind("<Button-1>", lambda e: callback("https://p-y.tm/UC-jmiq"))
            roop.mainloop()
   
   
    but_sub=tk.Button(root,text="Proceed ",font=("lora",15),bg="Lightblue",command=pay).place(x=700,y=700,width=350,height=40)
    root.mainloop()
   
   
home()
