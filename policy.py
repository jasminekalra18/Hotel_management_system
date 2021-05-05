from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class policyhotel():
    def __init__(self, root):  # calls constractor
        self.root = root
        self.root.title("Hotel management System")
        self.root.geometry("1295x550+230+220")

        #####title
        lbl_title = Label(self.root, text="Policy ", font=(
            "times new roman", 18, "bold"), bg="purple", fg="Yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # LOGO
        img2 = Image.open(r"C:\Users\HP\Desktop\Hotel_management\logo.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=3, y=0, width=100, height=50)

        ########### label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Policy Details", padx=2, font=(
            "times new roman", 12, "bold"))
        labelframeleft .place(x=5, y=50, width=1280, height=490)

        
if __name__ == '__main__':
    
    root = Tk()
    obj = policyhotel(root)
    root.mainloop()
