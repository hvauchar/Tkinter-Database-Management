from tkinter import *
import back
###########################################################
import sqlite3
import matplotlib.pyplot as plt 
import numpy as np
###########################################################
def openapp():
    def admin():
        conn=sqlite3.connect("polio.db")
        cur=conn.cursor()
        cur.execute("SELECT COUNT(Id), address FROM polio GROUP BY address")
        row=cur.fetchall()
        conn.close()
        objects = []
        target = []
        [objects.append(i[0]) for i in row]
        [target.append(i[1]) for i in row]
        print(len(target))
        plt.bar(np.arange(len(objects)),objects,align='center', alpha=0.5)
        plt.xticks(np.arange(len(target)), target)
        plt.show()
        pass
    def get_selected_row(event):
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        entry1.delete(0,END)
        entry1.insert(END,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(END,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(END,selected_tuple[3])
        entry4.delete(0,END)
        entry4.insert(END,selected_tuple[4])
        entry5.delete(0,END)
        entry5.insert(END,selected_tuple[5])
        entry6.delete(0,END)
        entry6.insert(END,selected_tuple[6])

    def view_command():
        list1.delete(0,END)
        for row in back.view():
            list1.insert(END,row)

    def search_command():
        list1.delete(0,END)
        for row in back.search(name_text.get(),address_text.get(),phone_number_text.get(),roomtype_text.get(),noof_text.get(),amount_text.get()):
            list1.insert(END,row)

    def add_command():
        back.insert(name_text.get(),address_text.get(),phone_number_text.get(),noof_text.get(),roomtype_text.get(),amount_text.get())
        list1.delete(0,END)
        list1.insert(END,(name_text.get(),address_text.get(),phone_number_text.get(),noof_text.get(),roomtype_text.get(),amount_text.get()))

    def delete_command():
        back.delete(selected_tuple[0])

    def update_command():
        back.update(selected_tuple[0],name_text.get(),address_text.get(),phone_number_text.get(),roomtype_text.get(),noof_text.get(),amount_text.get())
    window=Tk()
    window.title("Vaccination Management System")
    window.configure(background="pink1")
    label1=Label(window,text="Vaccanation Management System",font=('none 13 bold'))
    label1.grid(row=0,column=2)

    label2=Label(window,text="Child's Name",font=('none 13 bold'))
    label2.grid(row=1,column=0)

    label3=Label(window,text="Address",font=('none 13 bold'))
    label3.grid(row=2,column=0)

    label4=Label(window,text="Phone number",font=('none 13 bold'))
    label4.grid(row=3,column=0)

    label5=Label(window,text="Age",font=('none 13 bold'))
    label5.grid(row=4,column=0)

    label6=Label(window,text="Dose",font=('none 13 bold'))
    label6.grid(row=5,column=0)

    label7=Label(window,text="Volinteer Id",font=('none 13 bold'))
    label7.grid(row=6,column=0)

    name_text=StringVar()
    entry1=Entry(window,textvariable=name_text)
    entry1.grid(row=1,column=1)

    address_text=StringVar()
    entry2=Entry(window,textvariable=address_text)
    entry2.grid(row=2,column=1)

    phone_number_text=StringVar()
    entry3=Entry(window,textvariable=phone_number_text)
    entry3.grid(row=3,column=1)

    noof_text=StringVar()
    entry4=Entry(window,textvariable=noof_text)
    entry4.grid(row=4,column=1)

    roomtype_text=StringVar()
    entry5=Entry(window,textvariable=roomtype_text)
    entry5.grid(row=5,column=1)

    amount_text=StringVar()
    entry6=Entry(window,textvariable=amount_text)
    entry6.grid(row=6,column=1)

    list1=Listbox(window,height=20,width=59)
    list1.grid(row=1,column=3, rowspan=6, columnspan=2)

    scrl=Scrollbar(window)
    scrl.grid(row=1,column=2, sticky='ns',rowspan=6)

    list1.configure(yscrollcommand=scrl.set)
    scrl.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>',get_selected_row)

    b1=Button(window,text="view all",width=12, command=view_command,font=('none 13 bold'),relief=RAISED)
    b1.grid(row=7, column=0)

    b2=Button(window,text="add entry",width=12,fg="green",command=add_command,font=('none 13 bold'),relief=RAISED)
    b2.grid(row=8, column=0)

    b3=Button(window,text="delete entry",width=12,fg="red",command=delete_command,font=('none 13 bold'),relief=RAISED)
    b3.grid(row=10, column=0)

    b6=Button(window,text="Admin View",width=12,fg="SlateBlue1",command=admin,font=('none 13 bold'),relief=RAISED)
    b6.grid(row=10, column=1)


    b4=Button(window,text="search",width=12,command=search_command,font=('none 13 bold'),relief=RAISED)
    b4.grid(row=7, column=1)

    b5=Button(window,text="update",width=12,fg="blue",command=update_command,font=('none 13 bold'),relief=RAISED)
    b5.grid(row=8, column=1)
    
    window.mainloop()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
from tkinter import messagebox as ms
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
        # Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
        #Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            root.destroy()
            openapp()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
        #Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login,bg="gold2").grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr,bg="powder blue").grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    

#create window and application object
root = Tk()
root.title("Vaccanation Management System")
main(root)
root.mainloop()
######################################################################################################