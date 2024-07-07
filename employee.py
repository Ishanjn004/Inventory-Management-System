from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

class employee_class:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x770+370+130")
        self.root.title("Inventory Management System | Made By Ishan Jain")
        self.root.config(bg="#ECF0F1")
        self.root.focus_force()
        # => ALL VARIABLES

        self.search_type=StringVar()
        self.search_txt=StringVar()


        self.emp_id=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.name=StringVar()
        self.dob=StringVar()
        self.doj=StringVar()
        self.email=StringVar()
        self.paswd=StringVar()
        self.utype=StringVar()
        self.salary=StringVar()


        # => SEARCH FRAME
        search_frame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",14,"bold"),bd=2,relief=RIDGE,bg="#ECF0F1")
        search_frame.place(x=300,y=20,width=700,height=70)

        # => OPTIONS
        search_options=ttk.Combobox(search_frame,values=("Select","Emp-ID","Name","E-mail"),textvariable=self.search_type,state='readonly',justify=CENTER,font=('goudy old style',13))
        search_options.place(x=10,y=9,width=180)
        search_options.current(0)

        txt_entry=Entry(search_frame,textvariable=self.search_txt,font=('goudy old style',13),bg="#FAD7A0").place(x=200,y=10,width=300)
        search_btn=Button(search_frame,text="Search",font=('goudy old style',13,"bold"),bg="#009E60",fg="white",cursor="hand2").place(x=510,y=7,width=150,height=30)

        # => title frame
        title=Label(self.root,text="Employee Details",font=('goudy old style',15),bg='#273746',fg='white').place(x=50,y=100,width=1200)


        # => CONTENTS

        # => ROW 1
        lbl_empid=Label(self.root,text="Emp ID",font=('goudy old style',15),bg='#ECF0F1').place(x=50,y=160)
        lbl_gender=Label(self.root,text="Gender",font=('goudy old style',15),bg='#ECF0F1').place(x=450,y=160)
        lbl_contact=Label(self.root,text="Contact",font=('goudy old style',15),bg='#ECF0F1').place(x=900,y=160)

        txt_empid=Entry(self.root,textvariable=self.emp_id,font=('goudy old style',15),bg='#D5D8DC').place(x=150,y=160,width=180)
        # txt_gender=Entry(self.root,textvariable=self.gender,font=('goudy old style',15),bg='#ECF0F1').place(x=600,y=160,width=180)
        gender_select=ttk.Combobox(self.root,values=("Select","Male","Female","Other"),textvariable=self.gender,state='readonly',justify=CENTER,font=('goudy old style',13))
        gender_select.place(x=600,y=160,width=180)
        gender_select.current(0)
        txt_contact=Entry(self.root,textvariable=self.contact,font=('goudy old style',15),bg='#D5D8DC').place(x=1000,y=160,width=180)

        # => ROW 2
        lbl_name=Label(self.root,text="Name",font=('goudy old style',15),bg='#ECF0F1').place(x=50,y=210)
        lbl_dob=Label(self.root,text="D.O.B",font=('goudy old style',15),bg='#ECF0F1').place(x=450,y=210)
        lbl_doj=Label(self.root,text="D.O.J",font=('goudy old style',15),bg='#ECF0F1').place(x=900,y=210)

        txt_name=Entry(self.root,textvariable=self.name,font=('goudy old style',15),bg='#D5D8DC').place(x=150,y=210,width=180)
        txt_dob=Entry(self.root,textvariable=self.dob,font=('goudy old style',15),bg='#D5D8DC').place(x=600,y=210,width=180)
        txt_doj=Entry(self.root,textvariable=self.doj,font=('goudy old style',15),bg='#D5D8DC').place(x=1000,y=210,width=180)

        # => ROW 3
        lbl_email=Label(self.root,text="E-mail",font=('goudy old style',15),bg='#ECF0F1').place(x=50,y=260)
        lbl_paswd=Label(self.root,text="Password",font=('goudy old style',15),bg='#ECF0F1').place(x=450,y=260)
        lbl_utype=Label(self.root,text="User Type",font=('goudy old style',15),bg='#ECF0F1').place(x=900,y=260)

        txt_email=Entry(self.root,textvariable=self.email,font=('goudy old style',15),bg='#D5D8DC').place(x=150,y=260,width=180)
        txt_paswd=Entry(self.root,textvariable=self.paswd,font=('goudy old style',15),bg='#D5D8DC').place(x=600,y=260,width=180)
        # txt_utype=Entry(self.root,textvariable=self.utype,font=('goudy old style',15),bg='#D5D8DC').place(x=1000,y=260,width=180)
        user_type_select=ttk.Combobox(self.root,values=("Admin","Employee"),textvariable=self.utype,state='readonly',justify=CENTER,font=('goudy old style',13))
        user_type_select.place(x=1000,y=260,width=180)
        user_type_select.current(0)

         # => ROW 4
        lbl_address=Label(self.root,text="Address",font=('goudy old style',15),bg='#ECF0F1').place(x=50,y=310)
        lbl_sal=Label(self.root,text="Salary",font=('goudy old style',15),bg='#ECF0F1').place(x=600,y=310)

        self.txt_address=Text(self.root,font=('goudy old style',15),bg='#D5D8DC')
        self.txt_address.place(x=150,y=310,width=380,height=70)
        txt_sal=Entry(self.root,textvariable=self.salary,font=('goudy old style',15),bg='#D5D8DC').place(x=700,y=310,width=180)

        # => MODIFICATION BUTTONS
        btn_save=Button(self.root,text="Save",font=('goudy old style',13,"bold"),bg="#273746",fg="white",cursor="hand2").place(x=600,y=349,width=110,height=28)
        btn_updt=Button(self.root,text="Update",font=('goudy old style',13,"bold"),bg="#0B5345",fg="white",cursor="hand2").place(x=720,y=349,width=110,height=28)
        btn_del=Button(self.root,text="Delete",font=('goudy old style',13,"bold"),bg="#1B4F72",fg="white",cursor="hand2").place(x=840,y=349,width=110,height=28)
        btn_clr=Button(self.root,text="Clear",font=('goudy old style',13,"bold"),bg="#641E16",fg="white",cursor="hand2").place(x=960,y=349,width=110,height=28)


        # => EMPLOYEE DETAILS TABLE
        title=Label(self.root,text="Employee's Added",font=('goudy old style',15),bg='#273746',fg='white').place(x=50,y=410,width=1200)
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=450,relwidth=1,height=319)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.emptable=ttk.Treeview(emp_frame,columns=('eid','name','email','gender','contact','dob','doj','paswd','utype','adrs','sal'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.emptable.xview)
        scrolly.config(command=self.emptable.yview)
        self.emptable.heading('eid',text="E-ID")
        self.emptable.heading('name',text="Name")
        self.emptable.heading('email',text="E-mail")
        self.emptable.heading('gender',text="Gender")
        self.emptable.heading('contact',text="Contact")
        self.emptable.heading('dob',text="D.O.B")
        self.emptable.heading('doj',text="D.O.J")
        self.emptable.heading('paswd',text="Password")
        self.emptable.heading('utype',text="User-Type")
        self.emptable.heading('adrs',text="Address")
        self.emptable.heading('sal',text="Salary")
        
        self.emptable['show']='headings'

        self.emptable.column('eid',width=100)
        self.emptable.column('name',width=100)
        self.emptable.column('email',width=150)
        self.emptable.column('gender',width=100)
        self.emptable.column('contact',width=150)
        self.emptable.column('dob',width=100)
        self.emptable.column('doj',width=100)
        self.emptable.column('paswd',width=150)
        self.emptable.column('utype',width=100)
        self.emptable.column('adrs',width=250)
        self.emptable.column('sal',width=100)
        
        self.emptable.pack(fill=BOTH,expand=1)

if __name__=="__main__":

    root=Tk()
    obj=employee_class(root)
    root.mainloop()