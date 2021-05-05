from tkinter import *
from  PIL import Image ,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class  cust_win():
    def __init__(self, root):  # calls constractor
        self.root = root
        self.root.title("Hotel management System")
        self.root.geometry("1295x550+230+220")
        #height, weight, cordinates  of window
#################variables
        self.var_ref=IntVar()
        x=random.randint(1000,9999)        #will generate random number
        self.var_ref.set(int(x))

        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address = StringVar()



        #####title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="purple", fg="Yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # LOGO
        img2 = Image.open(r"C:\Users\HP\Desktop\Hotel_management\logo.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=3, y=0, width=100, height=50)


        ########### label frame 
        LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2, font=("times new roman", 12, "bold"))
        LabelFrameleft.place(x=5,y=50,width=425,height=525)


        #######labels and entries 
        lbl_cust_ref = Label(LabelFrameleft, text="Ref:", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref = ttk.Entry(LabelFrameleft,textvariable=self.var_ref,width=22,font=("arial", 13, "bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
 ########cust name
        cname = Label(LabelFrameleft, text="Name:", font=( "arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        textcname = ttk.Entry(
            LabelFrameleft,textvariable=self.var_cust_name, width=22, font=("arial", 13, "bold"))
        textcname.grid(row=1, column=1)

        ########father name
        lblfname = Label(LabelFrameleft, text="Father:",font=("arial", 12, "bold"), padx=2, pady=6)
        lblfname.grid(row=2, column=0, sticky=W)

        textfname = ttk.Entry(
            LabelFrameleft,textvariable=self.var_father, width=22, font=("arial", 13, "bold"))
        textfname.grid(row=2, column=1)

        ########gender
        lbl_gender = Label(LabelFrameleft, text="Gender: ",font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gendr = ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,font=("arial", 12, "bold"), width=20, state="readonly")
        combo_gendr["value"]=("Male","Female","other")
        combo_gendr.current(0)
        
        combo_gendr.grid(row=3, column=1)


########Postcode
        lblpc = Label(LabelFrameleft, text="Postcode:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblpc.grid(row=4, column=0, sticky=W)

        textpc = ttk.Entry(LabelFrameleft,textvariable=self.var_post, width=22,
                              font=("arial", 13, "bold"))
        textpc.grid(row=4, column=1)

#########Mobile 
        lblmob = Label(LabelFrameleft, text="Mobile Number:", 
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblmob.grid(row=5, column=0, sticky=W)

        textmob = ttk.Entry(LabelFrameleft,textvariable=self.var_mobile, width=22,
                              font=("arial", 13, "bold"))
        textmob.grid(row=5, column=1)

        ########email

        lblemail = Label(LabelFrameleft, text="email:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)

        textemail = ttk.Entry(LabelFrameleft,textvariable=self.var_email, width=22,
                              font=("arial", 13, "bold"))
        textemail.grid(row=6, column=1)


########nationality name
        lblnationality = Label(LabelFrameleft, text="Nationality :",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblnationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(LabelFrameleft,textvariable=self.var_nationality,font=(
            "arial", 12, "bold"), width=20, state="readonly")
        combo_nationality["value"] = ("Indian", "Other")
        combo_nationality.current(0)

        combo_nationality.grid(row=7, column=1)

        ########idtype
        lblidtype = Label(LabelFrameleft, text="Idproof:",
                               font=("arial", 12, "bold"), padx=2, pady=6)
        lblidtype.grid(row=8, column=0, sticky=W)

        combo_idtype = ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof,  font=(
            "arial", 12, "bold"), width=20, state="readonly")
        combo_idtype["value"] = ("AadharCard", "Pancard","Passport")
        combo_idtype.current(0)

        combo_idtype.grid(row=8, column=1)

########id 
        lblid = Label(LabelFrameleft, text="Idnumber:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblid.grid(row=9, column=0, sticky=W)

        textid = ttk.Entry(LabelFrameleft,textvariable=self.var_id_number, width=22,
                              font=("arial", 13, "bold"))
        textid.grid(row=9, column=1)


########ADDRESS
        lbladdress = Label(LabelFrameleft, text="Address:",
                               font=("arial", 12, "bold"), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)

        textaddress = ttk.Entry(LabelFrameleft,textvariable=self.var_address, width=22,
                                    font=("arial", 13, "bold"))
        textaddress .grid(row=10, column=1)
  

  ##############Btn
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width= 9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
        ###########table frame and search system 
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)
        lblsearchby = Label(table_frame, text="Search by :",
                         font=("arial", 12,   "bold"),bg="red",fg="white" )
        lblsearchby.grid(row=0, column=0, sticky=W,padx=2)

        self.serch_var = StringVar()  

        combo_search=ttk.Combobox(table_frame, textvariable=self.serch_var, font=("“arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2) 
        

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, font=(
            "arial", 13, "bold"), width=24)
        txtsearch.grid(row=0,column=2, padx=2)

            
        """txtSearch=ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial",13,"bold"),width=24) =
        btnSearch=Button(Table_Frame, text="Search", command=self.search, font=("arial",11,"bold"),bg="black",fg="gold",

        btnShowAll=Button|(Table_Frame,text="Show All", command=self.fetch_data, font=(“arial",11,"bold"),bg="black", fg=
        """

        btnsearch = Button(table_frame, text="Search", command=self.Search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall = Button(table_frame, text="Show All",command=self.fetch_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnshowall.grid(row=0, column=4, padx=1)
        

              ##########show data table
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.cust_details_table=ttk.Treeview(details_table,column=("ref","cust_name","father","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=scroll_y.set)
        Scroll_x.pack(side=BOTTOM ,fill=X) #bottom me fill ho jaye 
        scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("cust_name",text="Name")
        self.cust_details_table.heading("father",text="Father Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="PostCode")
        self.cust_details_table.heading("mobile", text="Mobile")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="Id Proof")
        self.cust_details_table.heading("idnumber", text="Id Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"]="headings"
        #self.cust_details_table.column("ref",width=100)
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()
    def add_data(self):
        if self.var_mobile.get()==""or self.var_father=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector. connect (host="localhost", username="root", password="1111", database="hotelm")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hotel_customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_ref.get(), self.var_cust_name.get(), self.var_father.get(),
                    self.var_gender.get(),
                    self.var_post.get(), self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get() ))

                """
                my_cursor=conn.cursor()#mysql database query run krte h """
            


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","custmore has been added",parent=self.root)#jahan hum chahte h wahi ye msg display ho toh parent
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong :{str(es)}",parent=self.root)       


            #isse jo bhi entry feild me data h hum isse lete h 

    def fetch_data(self):
        conn = mysql.connector. connect(
            host="localhost", username="root", password="1111", database="hotelm")


        my_cursor = conn.cursor()
        my_cursor.execute("select * from hotel_customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(
                *self.cust_details_table.get_children())


            for i in rows:

                self.cust_details_table.insert("", END, values=i)

                conn.commit()
        conn.close()

        
    def get_cuersor(self,events=""):
        cusrsor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cusrsor_row)
        row = content["values"]
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
 

    def Update(self):
        if self.var_mobile.get() == "" or self.var_father == "":
            messagebox.showerror("Error", "Please enter youur mobile number",parent=self.root)
        else:
            conn = mysql.connector. connect(
                host="localhost", username="root", password="1111", database="hotelm")
            my_cursor = conn.cursor()
            my_cursor.execute("update hotel_customer set Name=%s,Father=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s", (
                self.var_cust_name.get(),
                self.var_father.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(), self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root) 
        if mDelete>0:
            conn = mysql.connector. connect(
                host="localhost", username="root", password="1111", database="hotelm")
            my_cursor = conn.cursor()
            query="delete from hotel_customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_father.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set("")
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def Search(self):
        conn = mysql.connector. connect(
            host="localhost", username="root", password="1111", database="hotelm")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hotel_customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

        

                
                                                                                                                                                                                      
if __name__ == '__main__':
    
        root=Tk()
        obj=cust_win(root)
        root.mainloop()
 



           
 
