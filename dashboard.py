from tkinter import *
from PIL import Image,ImageTk

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Inventory Management System | Made By Ishan Jain")
        self.root.config(bg="#ECF0F1")

        # => TITLE
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Bungasai",40,"bold"),bg="#021A35",fg="white",anchor="w",padx=30).place(x=0,y=0,relwidth=1,height=70)

        # => LOGOUT BUTTON
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#F7DC6F",cursor="hand2").place(x=self.root.winfo_screenwidth() - 100, y=10,height=50,width=120, anchor="ne")

        # => TIME RIBBON
        self.bar_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#616A6B",fg="white")
        self.bar_clock.place(x=0,y=70,relwidth=1,height=30)

        # => LEFT MENU
        self.menuicon=Image.open("images/menu_im.png")
        self.menuicon = self.menuicon.resize((350, 350))
        self.menuicon=ImageTk.PhotoImage(self.menuicon)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#ECF0F1")
        LeftMenu.place(x=0,y=120,width=350,height=800)

        lbl_menulogo=Label(LeftMenu,image=self.menuicon)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",35),bg="#D6EAF8").pack(side=TOP,fill=X)
        
        btn_emp=Button(LeftMenu,text="Employee Details",image=self.icon_side,compound=LEFT,padx=20,anchor='w',font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier Details",image=self.icon_side,compound=LEFT,padx=20,anchor='w',font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=20,anchor='w',font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_prod=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,padx=20,anchor='w',font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=20,anchor='w',font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=20,anchor='w',font=("times new roman",25,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        # => CONTENT
        self.lbl_empoyee=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#E74C3C",fg="white",font=('goudy old style',20,'bold'))
        self.lbl_empoyee.place(x=450,y=200,height=220,width=370)

        self.lbl_spplier=Label(self.root,text="Total Suppliers\n[ 0 ]",bd=5,relief=RIDGE,bg="#8E44AD",fg="white",font=('goudy old style',20,'bold'))
        self.lbl_spplier.place(x=850,y=200,height=220,width=370)

        self.lbl_categ=Label(self.root,text="Total Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="#196F3D",fg="white",font=('goudy old style',20,'bold'))
        self.lbl_categ.place(x=1250,y=200,height=220,width=370)

        self.lbl_prod=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#873600",fg="white",font=('goudy old style',20,'bold'))
        self.lbl_prod.place(x=450,y=500,height=220,width=370)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#B7950B",fg="white",font=('goudy old style',20,'bold'))
        self.lbl_sales.place(x=850,y=500,height=220,width=370)




        # => FOOTER
        bar_footer=Label(self.root,text="Inventory Management System | Developed by Ishan Jain\nFor any Technical Issue Contact: 8595xxxx13",font=("times new roman",15),bg="#616A6B",fg="white").pack(side=BOTTOM,fill=X)

root=Tk()
obj=IMS(root)
root.mainloop()