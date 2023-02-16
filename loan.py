from tkinter import*
from tkinter import ttk, messagebox
import pymysql

class customer:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Loan management system')
        self.root.geometry('1350x720+0+0')
        title = Label(self.root,text='Loan management system', 
        font=('times new rommon',40,'bold'),bg='yellow',fg ='red',bd=10,relief=RIDGE)
        title.pack(side=TOP, fill=X)
        # =================Variables==============================
        self.loanId = StringVar()
        self.name = StringVar()
        self.mob = StringVar()
        self.aadhar = StringVar()
        self.add = StringVar()
        self.pin = StringVar()
        self.amount = StringVar()
        self.mpay = StringVar()
        self.tpay = StringVar()
        self.rate = StringVar()
        self.years = StringVar()

        # ==================Details Frame==========================
        Detail_F = Frame(self.root, bd=4, relief=RIDGE,bg='powderblue')
        Detail_F.place(x=10, y=90, width=500, height=600)

        lbl_id = Label(Detail_F,text='Loan Id', font=('times new rommon',18,'bold'))
        lbl_id.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        txt_id = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.loanId)
        txt_id.grid(row=0, column=1)

        lbl_name = Label(Detail_F,text='Full Name', font=('times new rommon',18,'bold'))
        lbl_name.grid(row=1,column=0,padx=20,pady=10,sticky="w")
        txt_name = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.name)
        txt_name.grid(row=1, column=1)

        lbl_mob = Label(Detail_F,text='Mobile No.', font=('times new rommon',18,'bold'))
        lbl_mob.grid(row=2,column=0,padx=20,pady=10,sticky="w")
        txt_mob = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.mob)
        txt_mob.grid(row=2, column=1)

        lbl_aa = Label(Detail_F,text='Aadhar No.', font=('times new rommon',18,'bold'))
        lbl_aa.grid(row=3,column=0,padx=20,pady=10,sticky="w")
        txt_aa = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.aadhar)
        txt_aa.grid(row=3, column=1)

        lbl_add = Label(Detail_F,text='Address', font=('times new rommon',18,'bold'))
        lbl_add.grid(row=4,column=0,padx=20,pady=10,sticky="w")
        txt_add = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.add)
        txt_add.grid(row=4, column=1)

        lbl_pin = Label(Detail_F,text='PinCode', font=('times new rommon',18,'bold'))
        lbl_pin.grid(row=5,column=0,padx=20,pady=10,sticky="w")
        txt_pin = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.pin)
        txt_pin.grid(row=5, column=1)

        lbl_amount = Label(Detail_F,text='Amount of Loan', font=('times new rommon',18,'bold'))
        lbl_amount.grid(row=6,column=0,padx=20,pady=10,sticky="w")
        txt_amount = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.amount)
        txt_amount.grid(row=6, column=1)

        lbl_time = Label(Detail_F,text='Number of years', font=('times new rommon',18,'bold'))
        lbl_time.grid(row=7,column=0,padx=20,pady=10,sticky="w")
        txt_time = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.years)
        txt_time.grid(row=7, column=1)

        lbl_rate = Label(Detail_F,text='Interest Rate', font=('times new rommon',18,'bold'))
        lbl_rate.grid(row=8,column=0,padx=20,pady=10, sticky="w")
        txt_rate = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.rate)
        txt_rate.grid(row=8, column=1)

        lbl_mp = Label(Detail_F,text='Monthly Payment', font=('times new rommon',18,'bold'))
        lbl_mp.grid(row=9,column=0,padx=20,pady=10, sticky="w")
        txt_mp = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.mpay)
        txt_mp.grid(row=9, column=1)

        lbl_tp = Label(Detail_F,text='Total Payment', font=('times new rommon',18,'bold'))
        lbl_tp.grid(row=10,column=0,padx=20,pady=10, sticky="w")
        txt_tp = Entry(Detail_F, font=('times new rommon',15,'bold'),bd=3, relief=GROOVE,textvariable=self.tpay)
        txt_tp.grid(row=10, column=1)

        # ============================Right Frame==========================
        RFrame = Frame(self.root, bd=4,relief=RIDGE)
        RFrame.place(x=535,y=90,width=800,height=520)

        yscroll = Scrollbar(RFrame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(RFrame,column=('empid','name','years','rate','mpayment','Tpayment','mobile'),yscrollcommand=yscroll)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.employee_table.yview)
        self.employee_table.heading('empid',text='Employee Id')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('years',text='Number of Years')
        self.employee_table.heading('rate',text='Interest Rate')
        self.employee_table.heading('mpayment',text='Monthly Payment')
        self.employee_table.heading('Tpayment',text='Total Payment')
        self.employee_table.heading('mobile',text='Mobile No.')
        self.employee_table['show'] = 'headings'

        self.employee_table.column('empid', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('years', width=100)
        self.employee_table.column('rate', width=100)
        self.employee_table.column('mpayment', width=100)
        self.employee_table.column('Tpayment', width=100)
        self.employee_table.column('mobile', width=100)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.fetch()

        # =======================Buttons=====================
        btn_Frame = Frame(self.root, bd=4, relief=RIDGE)
        btn_Frame.place(x=535, y=610, width=810, height=100)

        btn1 = Button(btn_Frame,text='Add record', font='arial 18 bold',bg='lime',width=9,fg='crimson',command=self.addrecord)
        btn1.grid(row=0,column=0, padx=10, pady=10)

        btn2 = Button(btn_Frame,text='Update', font='arial 18 bold',bg='lime',fg='crimson',width=9)
        btn2.grid(row=0,column=1, padx=8, pady=10)

        btn3 = Button(btn_Frame,text='Delete', font='arial 18 bold',bg='lime',fg='crimson',width=9)
        btn3.grid(row=0,column=2, padx=8, pady=10)

        btn4 = Button(btn_Frame,text='Reset', font='arial 18 bold',bg='lime',fg='crimson',width=9)
        btn4.grid(row=0,column=3, padx=8, pady=10)

        btn5 = Button(btn_Frame,text='exit', font='arial 18 bold',bg='lime',fg='crimson',width=9)
        btn5.grid(row=0,column=4, padx=8, pady=10)

    # =======================Functions===================
    def addrecord(self):
        if self.loanId.get() == '':
            messagebox.showerror('Error','Customer details are must')
        else:
            con = pymysql.connect(host='localhost', user='root', password='root')
            cur = con.cursor()

            # query = 'create database emp'
            # cur.execute(query)
            # query = 'use emp'
            # cur.execute(query)
            # query = 'create table customer(Loan_id varchar(100) primary key not null, Name varchar(100) not null, Year int not null, Rate int not null, Monthly_Payment int not null, Total_Payment int not null, MobileNumber int not null, aadharNumber int not null, Address varchar(100) not null, PinCode int not null, Amount int not null)'


            cur.execute("select * from customer")
            rows = cur.fetchall()
            for row in rows():
                if row[0] == self.loanId.get():
                    messagebox.showerror('Error','Duplicate entry not allowed')
            cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.loanId.get(),
                                                                        self.name.get(),
                                                                        self.years.get(),
                                                                        self.rate.get(),
                                                                        self.mpay.get(),
                                                                        self.tpay.get(),
                                                                        self.mob.get(),
                                                                        self.aadhar.get(),
                                                                        self.add.get(),
                                                                        self.pin.get(),
                                                                        self.amount.get(),
                                                                        ))

            con.commit()
            con.close()

    def fetch(self):
        con = pymysql.connect(host='localhost', user='root', password='root')
        cur = con.cursor()
        cur.execute("select * from customer")
        rows = cur.fetchall()   

        for row in rows:
            self.employee_table.insert('',END,values=row)
            con.commit()
            self.fetch()
            con.close()
root = Tk()
obj = customer(root)
root.mainloop()