from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):  # calls constractor
        self.root = root
        self.root.title("Hotel management System")
        self.root.geometry("1295x550+230+220")
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_total = StringVar()
    


        #####title
        lbl_title = Label(self.root, text="Room Booking", font=(
            "times new roman", 18, "bold"), bg="purple", fg="Yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # LOGO
        img2 = Image.open(r"C:\Users\HP\Desktop\Hotel_management\logo.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=3, y=0, width=100, height=50)

        ########### label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", padx=2, font=(
            "times new roman", 12, "bold"))
        labelframeleft .place(x=5, y=50, width=425, height=490)



################entry fiel
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:",
                             font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=(
            "arial", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)
        
########Fetch Data 
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="purple",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)


 ########cust name
        check_in_date = Label(labelframeleft, font=("arial",12,"bold"),text="Check_in Date: ", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date=ttk.Entry(
        labelframeleft,textvariable=self.var_checkin, font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        lbl_Check_out=Label(labelframeleft, font=("arial",12,"bold"),text="Check_Out Date: ", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout, font=("arial",13,"bold"), width=29)
        txt_Check_out.grid(row=2, column=1) 

        label_RoomType = Label(labelframeleft, font=("arial",12,"bold"),text="Room Type: ", padx=2, pady=6)
        label_RoomType. grid(row=3, column=0, sticky=W)
        combo_RoomType=ttk.Combobox(labelframeleft, textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"]=("Single", "Double", "Premium")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        lblRoomAvailable=Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft, textvariable=self.var_roomavailable,font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        
        lblMeal=Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        lblNoOfDays= Label(labelframeleft, font=(
            "arial", 12, "bold"), text="No.of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft, textvariable=self.var_noofdays,font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        lblNoOfDays = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)

        lblNoOfDays = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft,textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=8, column=1)

        lbltotal= Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Total Costs:", padx=2, pady=6)
        lbltotal.grid(row=9, column=0, sticky=W)
        txttotal = ttk.Entry(
            labelframeleft,textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txttotal.grid(row=9, column=1)

 ##############Btn
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update,font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command= self.mDelete,font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #########Bill button
        btnbill = Button(labelframeleft, command=self.total,text="Bill", font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnbill.grid(row=10,
         column=0, padx=1,sticky=W)

 ###########table frame and search system
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE,
                                 text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=200, width=860, height=300)
        lblsearchby = Label(table_frame, text="Search by :",
                            font=("arial", 12,   "bold"), bg="red", fg="white")
        lblsearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.serch_var, font=(
            "“arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("contact","roomavailable")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame,textvariable=self.txt_search,font=(
            "arial", 13, "bold"), width=24)
        txtsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(table_frame, command=self.search ,text="Search",font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(table_frame, command=self.fetch_data,text="Show All", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnshowall.grid(row=0, column=4, padx=1)

##############right side image
        img3 = Image.open(r"C:\Users\HP\Desktop\Hotel_management\bedroom.jpg")
        img3=img3.resize((450,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=860,y=55,width=450,height=150)

        img4 = Image.open(r"C:\Users\HP\Desktop\Hotel_management\bedroom.jpg")
        img4 = img4.resize((450, 150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg = Label(self.root, image=self.photoimg4, bd=0, relief=RIDGE)
        lblimg.place(x=860, y=55, width=450, height=150)


######      ##########show data table
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=300)
 
        Scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.room_table = ttk.Treeview(details_table, column=("contact", "checkin", "checkout", "roomtype", "roomavailable","meal","noOfdays"), xscrollcommand=Scroll_x.set, yscrollcommand=scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)  # bottom me fill ho jaye
        scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Roomtype")
        self.room_table.heading("roomavailable", text="RoomNo")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="Noofdays")


        self.room_table["show"] = "headings"
        #self.room_table.column("ref",width=100)
        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error•,•All fields are requaired",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1111",database="hotelm")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                # jahan hum chahte h wahi ye msg display ho toh parent
                messagebox.showinfo(
                    "Success", "Room Booked", parent=self.root)
            except Exception as es:
                        messagebox.showwarning(
                    "Warning", f"some thing went wrong :{str(es)}", parent=self.root)

    def fetch_data(self): 
        conn = mysql.connector.connect(host="localhost", username="root", password="1111", database="hotelm")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self, event=""): 
        cusrsor_row=self.room_table.focus() 
        content = self.room_table.item(cusrsor_row) 
        row = content["values"]


        self.var_contact.set(row[0]) 
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2]) 
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4]) 
        self.var_meal.set(row[5]) 
        self.var_noofdays.set(row[6])
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Plaease enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1111", database="hotelm")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s", (self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(), self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Customer details has been updated successfully", parent=self.root)
   
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root) 
        if mDelete>0:
            conn = mysql.connector. connect(
                host="localhost", username="root", password="1111", database="hotelm")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    ######reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_total.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")



    




    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Plaese enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1111",database="hotelm")
            my_cursor=conn.cursor()
            query=("select Name from hotel_customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2) 
                showDataframe.place(x=450,y=50,width=370,height=142)
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold")) 
                lblName.place(x=0,y=0)
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lbl.place(x=90,y=0)


                conn=mysql.connector.connect(host="localhost",username="root",password="1111",database="hotelm")
                my_cursor=conn.cursor()
                query=("select Gender from hotel_customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblGender=Label(showDataframe,text="Gender.",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                lb12=Label(showDataframe,text=row,font=("arial",12,"bold")) 
                lb12.place(x=90,y=30)
                #	email 	
                conn=mysql.connector.connect(host="localhost",user="root",password="1111",database="hotelm")
                my_cursor=conn.cursor()
                query=("select Email from hotel_customer where Mobile=%s")
                value=(self.var_contact.get(),) 
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()
                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold")) 
                lblemail.place(x=0,y=60)
                lb13 = Label(showDataframe, text=row,
                             font=("arial", 12, "bold"))
                lb13.place(x=90, y=60)

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="1111", database="hotelm")
                my_cursor = conn.cursor()

                query=("select Nationality from hotel_customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()
                lblNationality=Label(showDataframe, text="Nationality:", font=("arial",12,"bold")) 
                lblNationality.place(x=0, y=90)
                lb14 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lb14.place(x=90, y=90)
        


    def search(self):
        conn = mysql.connector. connect(host="localhost", username="root", password="1111", database="hotelm")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where " +
                          str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
        
    def total(self):

        inDate =self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate =datetime.strptime(inDate,"%d/%m/%Y")
        outDate =datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if(self.var_meal.get()=="breakfast"and self.var_roomtype.get()=="Premium"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.12))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.12)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.11))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.11)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif(self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.12))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.12)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

    

            



if __name__ == '__main__':

    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
