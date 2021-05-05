from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):  # calls constractor
        self.root = root
        self.root.title("Hotel management System")
        self.root.geometry("1295x550+230+220")

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

        entry_contact = ttk.Entry(labelframeleft, width=20, font=(
            "arial", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)
        
########Fetch Data 
        btnFetchData=Button(labelframeleft,text="Fetch Data",font=("arial",8,"bold"),bg="purple",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)


 ########cust name
        check_in_date = Label(labelframeleft, font=("arial",12,"bold"),text="Check_in Date: ", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date=ttk.Entry(
        labelframeleft, font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        lbl_Check_out=Label(labelframeleft, font=("arial",12,"bold"),text="Check_Out Date: ", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft, font=("arial",13,"bold"), width=29)
        txt_Check_out.grid(row=2, column=1) 

        label_RoomType = Label(labelframeleft, font=("arial",12,"bold"),text="Room Type: ", padx=2, pady=6)
        label_RoomType. grid(row=3, column=0, sticky=W)
        combo_RoomType=ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"]=("Single", "Double", "Premium")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        lblRoomAvailable=Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        
        lblMeal=Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        lblNoOfDays= Label(labelframeleft, font=(
            "arial", 12, "bold"), text="No.of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        lblNoOfDays = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)

        lblNoOfDays = Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(
            labelframeleft, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=8, column=1)

        lblIdNumber= Label(labelframeleft, font=(
            "arial", 12, "bold"), text="Total Costs:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdnumber = ttk.Entry(
            labelframeleft, font=("arial", 13, "bold"), width=29)
        txtIdnumber.grid(row=9, column=1)

 ##############Btn
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=(
            "arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #########Bill button
        btnbill = Button(labelframeleft, text="Bill", font=(
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
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame,font=(
            "arial", 13, "bold"), width=24)
        txtsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(table_frame, text="Search",font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(table_frame, text="Show All", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnshowall.grid(row=0, column=4, padx=1)

##############right side image
        img3 = Image.open(r"C:\Users\HP\Desktop\Hotel_management\bedroom.jpg")
        img3=img3.resize((450,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=860,y=55,width=450,height=150)
######      ##########show data table
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=300)
 
        Scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.cust_details_table = ttk.Treeview(details_table, column=("contact", "checkin", "checkout", "roomtype", "roomavailable","meal","noOfdays"), xscrollcommand=Scroll_x.set, yscrollcommand=scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)  # bottom me fill ho jaye
        scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("contact", text="Contact")
        self.cust_details_table.heading("checkin", text="Check-in")
        self.cust_details_table.heading("checkout", text="Check-out")
        self.cust_details_table.heading("roomtype", text="Roomtype")
        self.cust_details_table.heading("roomavailable", text="RoomNo")
        self.cust_details_table.heading("meal", text="Meal")
        self.cust_details_table.heading("noOfdays", text="Noofdays")


        self.cust_details_table["show"] = "headings"
        #self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("contact", width=100)
        self.cust_details_table.column("checkin", width=100)
        self.cust_details_table.column("checkout", width=100)
        self.cust_details_table.column("roomtype", width=100)
        self.cust_details_table.column("roomavailable", width=100)
        self.cust_details_table.column("meal",width=100)
        self.cust_details_table.column("noOfdays", width=100)
        self.cust_details_table.pack(fill=BOTH, expand=1)

if __name__ == '__main__':

    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
