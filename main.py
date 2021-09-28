from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector


class CRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD OPERATIONS")
        self.root.geometry("800x800+0+0")
        self.root.minsize("800", "600")
        self.root.state("zoomed")
        self.root.resizable(0,0)

# ===== All Variable Declaration ====== #
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.d = StringVar()
        self.e = StringVar()
        self.f = StringVar()
        self.g = StringVar()
        self.h = StringVar()
        self.id = StringVar()

# ====== Header Frame ======= #
        header = Frame(self.root, bg="teal")
        heading = Label(header, text="CRUD", font=(
            'Vernda', 30, 'bold'), fg="#fff", justify=CENTER, bg="teal")
        heading.pack(ipady=15)
        header.pack(fill=X)

# ====== Footer Frame ======= #
        footer = Frame(self.root)
        fheading = Label(footer, text="@CoderAnny", font=(
            'Vernda', 10), fg="#fff",bg="#000")
        fheading.pack(ipady=15,fill=X)
        footer.pack(side=BOTTOM,fill=X)



# ===== Tabs Styling ========#

        style = ttk.Style()

        style.theme_create('mytheme', settings={
            "TNotebook": {
                "configure": {
                    "background": "#000"
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "padding": [30, 20], "font": ('Helevetica', 15, 'bold'), "borderwidth": 0, "background": "#000", "foreground": "#fff"
                }
            },
            # ===== This styling is for Treeview ===== #
            "Treeview": {
                "configure": {
                    "font": ('Helevetica', 10, 'bold'),
                    "background": "#fff",
                    "fieldbackground": "#fff",
                    "rowheight": 30
                }
            },
            "Treeview.Heading": {
                "configure": {
                    "foreground": "#fff", "background": "blue", "font": ('Helevetica', 15, 'bold'), "padding": [10]
                }
            }
        })
        style.theme_use('mytheme')


# ===== Tabs Designing ===== #
        tabs = ttk.Notebook(self.root)

# ========= Menu1 Designing STARTS ========#

        menu1 = Frame(tabs, bg="#fff")
        F1 = Frame(menu1)
        F1.pack(padx=30, pady=20, fill=BOTH, expand=1)

    # Adding Scrollbar to F1 Frame #
        scrolly = Scrollbar(F1, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        t = ttk.Treeview(F1, columns=('Sno', 'Name', 'Class',
                         'City'), yscrollcommand=scrolly.set)
        self.t = t
        scrolly.config(command=t.yview)
    # ==== Heading of column for Treeview ===== #
        t.heading('Sno', text="Roll Number")
        t.heading('Name', text="Student Name")
        t.heading('Class', text="Studnet Class")
        t.heading('City', text="Student City")

    # Content of all Coloumns is aligned to center using 'anchor=N' #
        t.column('Sno', anchor=N)
        t.column('Name', anchor=N)
        t.column('Class', anchor=N)
        t.column('City', anchor=N)
        t['show'] = 'headings'
        t.column('Sno', width=100)
        self.fecthAll()
        t.pack(fill=BOTH, expand=1)


# ========= Menu1 Designing ENDS ========#

# ========= Menu2 Designing STARTS ====== #

        menu2 = Frame(tabs)
        h1 = Label(menu2, text="---- ADD RECORD ----", bg="#f0f0f0",
                   fg="Crimson", font=('Vernda', 15, 'bold'), anchor=W)
        h1.pack(fill=X, ipady=20, padx=20)
        F2 = Frame(menu2, bg="#CAD3C8")
        label1 = Label(F2, text="Name", bg="#CAD3C8",
                       anchor=W, font=('vernda', 15, 'bold'))
        label1.pack(fill=X, ipady=10, padx=10)
        Entry1 = Entry(F2, font=('vernda', 13, 'bold'), width=50,
                       justify=CENTER, textvariable=self.a)
        Entry1.pack(ipady=10)
        label2 = Label(F2, text="Class", bg="#CAD3C8",
                       anchor=W, font=('vernda', 15, 'bold'))
        label2.pack(fill=X, ipady=10, padx=10)
        Entry2 = Entry(F2, font=('vernda', 13, 'bold'), width=50,
                       justify=CENTER, textvariable=self.b)
        Entry2.pack(ipady=10)
        label3 = Label(F2, text="City", bg="#CAD3C8",
                       anchor=W, font=('vernda', 15, 'bold'))
        label3.pack(fill=X, ipady=10, padx=10)
        Entry3 = Entry(F2, font=('vernda', 13, 'bold'), width=50,
                       justify=CENTER, textvariable=self.c)
        Entry3.pack(ipady=10)
        add_btn = Button(F2, text="Add Record", font=(
            'Vernda', 15, 'bold'), fg="#fff", bg="#000", cursor="hand2", justify=CENTER, command=self.add_record)
        add_btn.pack(ipady=8, ipadx=10, pady=20)
        F2.pack(pady=30, ipadx=20)

# ========= Menu2 Designing ENDS ====== #

# ========= Menu3 Designing STARTS ====== #
        menu3 = Frame(tabs)
        h2 = Label(menu3, text="---- UPDATE RECORD ----", bg="#f0f0f0",
                   fg="Green", font=('Vernda', 15, 'bold'), anchor=W)
        h2.pack(fill=X, ipady=20, padx=20)
        F3 = Frame(menu3, bg="#CAD3C8")
        label4 = Label(F3, text="ID", bg="#CAD3C8",
                       anchor=W, font=('vernda', 15, 'bold'))
        label4.pack(fill=X, ipady=10, padx=10)
        Entry4 = Entry(F3, font=('vernda', 13, 'bold'), width=50,
                       justify=CENTER, textvariable=self.d)
        Entry4.pack(ipady=10)
        show_btn = Button(F3, text="Show Record", font=('Vernda', 15, 'bold'), fg="#fff",
                          bg="#000", cursor="hand2", justify=CENTER, command=self.show_record)
        show_btn.pack(ipady=5, ipadx=10, pady=20)
        F3.pack(pady=30, ipadx=20)
# ========= Menu3 Designing ENDS ====== #


# ========= Menu4 Designing STARTS ====== #
        menu4 = Frame(tabs)
        h3 = Label(menu4, text="---- DELETE RECORD ----", bg="#f0f0f0",
                   fg="Red", font=('Vernda', 15, 'bold'), anchor=W)
        h3.pack(fill=X, ipady=20, padx=20)
        F4 = Frame(menu4, bg="#CAD3C8")
        label5 = Label(F4, text="ID", bg="#CAD3C8",
                       anchor=W, font=('vernda', 15, 'bold'))
        label5.pack(fill=X, ipady=10, padx=10)
        Entry5 = Entry(F4, font=('vernda', 13, 'bold'), width=50,
                       justify=CENTER, textvariable=self.e)
        Entry5.pack(ipady=10)
        del_btn = Button(F4, text="Delete Record", font=(
            'Vernda', 15, 'bold'), fg="#fff", bg="#000", cursor="hand2", justify=CENTER, command=self.del_record)
        del_btn.pack(ipady=5, ipadx=10, pady=20)
        F4.pack(pady=30, ipadx=20)

# ========= Menu4 Designing ENDS ====== #

        tabs.add(menu1, text="HOME")
        tabs.add(menu2, text="ADD RECORD")
        tabs.add(menu3, text="UPDATE RECORD")
        tabs.add(menu4, text="DELETE REOCRD")
        tabs.pack(fill=BOTH, expand=1)
        self.root.config(pady=30, padx=40)


# ====================== Function that Fetch All records in Treeview  ======================== #


    def fecthAll(self):
        mydb = mysql.connector.connect(
            host='host_name', user='user_name', password='your_password', database='storedb')
        mydb_cursor = mydb.cursor()
        mydb_cursor.execute("select * from records")
        got_records = mydb_cursor.fetchall()
        if(len(got_records) > 0):
            self.t.delete(* self.t.get_children())
            for i in got_records:
                self.t.insert('', END, values=i)
        mydb.commit()
        self.e.set("")
        mydb.close()


# ====================== Function that Opens new Window for UPDATION ============================ #

    def show_record(self):
        if(self.d.get() == ""):
            msg.showerror("---- ERROR ----", "Input Cannot be blank!!")
            return False
        else:
            r = Toplevel(self.root)
            r.title("UPDATE RECORDS")
            r.focus_force()
            dv = self.d.get()
            try:
                mydb = mysql.connector.connect(
                    host='host_name', user='user_name', password='your_password', database='storedb')
                mydb_cursor = mydb.cursor()
                mydb_cursor.execute(f"select * from records where Sno = {dv}")
                records = mydb_cursor.fetchall()
                if(len(records) > 0):
                    lst = list(records[0])
                    self.f.set(lst[1])
                    self.g.set(lst[2])
                    self.h.set(lst[3])
                else:
                    msg.showerror("--- WRONG ---",
                                  f"No any Record found for Id {dv}")
            except:
                msg.showerror("--- WRONG ---", f"No any Record found")
            mydb.commit()
            mydb.close()
            id = lst[0]
            up_F = Frame(r, bg="#CAD3C8")
            up_label1 = Label(up_F, text="Name", bg="#CAD3C8",
                              anchor=W, font=('vernda', 15, 'bold'))
            up_label1.pack(fill=X, ipady=10, padx=10)
            up_Entry1 = Entry(up_F, font=('vernda', 13, 'bold'),
                              width=50, justify=CENTER, textvariable=self.f)
            up_Entry1.pack(ipady=10, padx=20)
            up_label2 = Label(up_F, text="Class", bg="#CAD3C8",
                              anchor=W, font=('vernda', 15, 'bold'))
            up_label2.pack(fill=X, ipady=10, padx=10)
            up_Entry2 = Entry(up_F, font=('vernda', 13, 'bold'),
                              width=50, justify=CENTER, textvariable=self.g)
            up_Entry2.pack(ipady=10, padx=20)
            up_label3 = Label(up_F, text="City", bg="#CAD3C8",
                              anchor=W, font=('vernda', 15, 'bold'))
            up_label3.pack(fill=X, ipady=10, padx=10)
            up_Entry3 = Entry(up_F, font=('vernda', 13, 'bold'),
                              width=50, justify=CENTER, textvariable=self.h)
            up_Entry3.pack(ipady=10, padx=20)
            up_add_btn = Button(up_F, text="Update Record", font=(
                'Vernda', 15, 'bold'), fg="#fff", bg="#000", cursor="hand2", justify=CENTER, command=lambda: self.update_record(id))
            up_add_btn.pack(ipady=8, ipadx=10, pady=20)
            up_F.pack(pady=30, padx=30)


# ======================= Function that add reocrds to database ============================ #

    def add_record(self):
        try:
            mydb = mysql.connector.connect(
                host='host_name', user='user_name', password='your_password', database='storedb')
            mydb_cursor = mydb.cursor()
            v1 = self.a.get()
            v2 = self.b.get()
            v3 = self.c.get()
            if(v1 == '' or v1 == ' ' or v2 == '' or v2 == ' ' or v3 == '' or v3 == ' '):
                msg.showerror(" --- ERROR ---- ", " All Fileds Required! ")
            else:
                query = "insert into records(Name,Class,City) values(%s,%s,%s)"
                val = (v1, v2, v3)
                mydb_cursor.execute(query, val)
                mydb.commit()
                msg.showinfo(
                    "SUCESS!", "Record added to Database Sucessfully!")
                self.a.set("")
                self.b.set("")
                self.c.set("")
                mydb.close()
                self.fecthAll()
        except:
            msg.showerror("--- ERROR ---", " Connection Failed With Database!")
            mydb.close()


# ========================== Function that Deletes reocrds to database =========================== #

    def del_record(self):
        try:
            mydb = mysql.connector.connect(
                host='host_name', user='user_name', password='your_password', database='storedb')
            mydb_cursor = mydb.cursor()
            v = int(self.e.get())
            if(v == '' or v == ' '):
                msg.showerror(" --- ERROR ---- ", " ID is Required here..! ")
            else:
                mydb_cursor.execute(f"delete from records where Sno = {v}")
                mydb.commit()
                msg.showinfo(
                    "SUCESS!", "Record Deleted to Database Sucessfully!")
                self.e.set("")
                mydb.close()
                self.fecthAll()
        except:
            msg.showerror("--- ERROR ---", " Connection Failed With Database!")
            mydb.close()

# ========================== Function that UPDATES reocrds to database ================================ #
    def update_record(self, id):
        try:
            mydb = mysql.connector.connect(
                host='host_name', user='user_name', password='your_password', database='storedb')
            mydb_cursor = mydb.cursor()
            v1 = self.f.get()
            v2 = self.g.get()
            v3 = self.h.get()
            v4 = id
            if(v1 == '' or v1 == ' ' or v2 == '' or v2 == ' ' or v3 == '' or v3 == ' '):
                msg.showerror(" --- ERROR ---- ", " All Fileds Required! ")
            else:
                q = "update records set Name=%s,Class=%s,City=%s where Sno=%s"
                v = (v1, v2, v3, v4)
                mydb_cursor.execute(q, v)
                mydb.commit()
                msg.showinfo(
                    "SUCESS!", "Record updated to Database Sucessfully!")
                self.f.set("")
                self.g.set("")
                self.h.set("")
                self.d.set("")
                mydb.close()
                self.fecthAll()
        except:
            msg.showerror("--- ERROR ---", " Connection Failed With Database!")
            mydb.close()


# ======= Main Code ======= #
root = Tk()
CRUD(root)
root.mainloop()
