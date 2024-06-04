from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk 
from tkinter import messagebox
import mysql.connector

def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")  # Set the window to full screen
        self.image = Image.open("D:/starappproject2-loginsystem/images/bgimg.jpg")

        # Resize the image to fit the window while maintaining aspect ratio
        self.width, self.height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.image = self.image.resize((self.width, self.height))  # Use ANTIALIAS for smoother resizing

        # Convert the image to PhotoImage
        self.bg = ImageTk.PhotoImage(image=self.image)

        # Create a label with the image and stretch it to fill the window
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
       
        frame= Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"D:\starappproject2-loginsystem\images\img1.jpg")
        #img1=img1.resize((self.width, self.height))
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black", bg="white")
        get_str.place(x=95,y=100)
        
        username_lbl= Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black", bg="white")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_lbl.place(x=70, y=225)
        self.txtpassword = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpassword.place(x=40, y=250, width=270)

        loginbtn = Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="blue")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        registerbtn = Button(frame,text="New user Register",command=self.register_window,font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="red",activebackground="white")
        registerbtn.place(x=15,y=350,width=160,height=35)

        registerbtn = Button(frame,text="Forgot Password",command = self.forgot_password_window,font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="red",activebackground="white")
        registerbtn.place(x=180,y=350,width=160,height=35)

    
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Register(self.new_window)
                

    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.txtuser.get()=="ayushi" or self.txtpassword.get()=="ayushi0987":
            messagebox.showinfo("success","welcome to ayushi's web")
        else:
            connection = mysql.connector.connect(
            host='localhost',
            database='register',
            user='root',
            password='Ayushi@0987'
            )
    
            cur = connection.cursor()
            cur.execute("select * from register where email=%s and password=%s",(
                self.var_email.get(),
                self.var_password.get()
            ))
            
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("error","invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Register(self.new_window)
                else:
                    if not open_main:
                        return
            connection.commit()
            connection.close()
            
            
    def reset_pass(self):
        if self.combo_securityQ.get()=="Select":
            messagebox.showerror("error","selct the valid security question",parent=self.root2)
        elif self.txtsecurityA.get()=="":
            messagebox.showerror("error","please enter security answer",parent=self.root2)  
        elif self.txt_newpass.get()=="":
            messagebox.showerror("error","enter new password",parent=self.root2)  
        else:
            connection = mysql.connector.connect(
            host='localhost',
            database='register',
            user='root',
            password='Ayushi@0987'
            )
    
            cur = connection.cursor()
            query =("select * from register where email=%s and security question=%s")
            value=(self.txtuser.get(),self.combo_securityQ.get(),self.txt_securityA)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("error","please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                cur.execute(query,value)  
                connection.commit()
                connection.close()
                messagebox.showinfo("info","your password has been reset",parent=self.root2)   
                self.root2.destroy()
                  
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("error","please enter the username")
        else:
            connection = mysql.connector.connect(
            host='localhost',
            database='register',
            user='root',
            password='Ayushi@0987'
            )
    
            cur = connection.cursor()   
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            print(row)
            if row==None:
                messagebox.showerror("error","enter the valid username")
            else:
                connection.close()
                self.root2=Toplevel()
                self.root2.title("forgot password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman", 12, "bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                
            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.width, self.height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.image = Image.open("D:/starappproject2-loginsystem/images/bgimg2.jpg")
        self.image = self.image.resize((self.width, self.height))  # Use ANTIALIAS for smoother resizing
        
        #### variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_check=IntVar()
       
        # Convert the image to PhotoImage
        self.bg = ImageTk.PhotoImage(image=self.image)

        # Create a label with the image and stretch it to fill the window
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
       
        #frame
        frame = Frame(self.root,bg="black")
        frame.place(x=400,y=100,width=800,height=550)
        
        register_lbl =Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="red",bg="black")
        register_lbl.place(x=120,y=20)
        
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        fname.place(x=50,y=100)
        
        fname_entry= ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        lname.place(x=470,y=100)
        
        self.txt_lname= ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",10,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row2
        email=Label(frame,text="email",font=("times new roman",15,"bold"),fg="white",bg="black")
        email.place(x=50,y=170)
        
        self.txt_email= ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",10,"bold"))
        self.txt_email.place(x=50,y=200,width=250)
    
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),fg="white",bg="black")
        contact.place(x=370,y=170)
        
        self.txt_contact= ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",10,"bold"))
        self.txt_contact.place(x=370,y=200,width=250)
    
        #row3
        security_Q=Label(frame,textvariable=self.var_securityQ,text="Security Question",font=("times new roman",15,"bold"),fg="white",bg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",10,"bold"),state="randomly")
        self.combo_security_Q["values"]=("Select","your birth place","you pet name","your favourite food")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
       
        security_ans=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="black")
        security_ans.place(x=370,y=240)
    
        self.txt_security= ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",10,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
       
       #row4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=50,y=310)
        
        self.txt_password= ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",10,"bold"))
        self.txt_password.place(x=50,y=340,width=250)
    
       
        #################checkbutton
        
        checkbtn = Checkbutton(frame,text="I agree to Terms and Conditions",font=("times new roman",15,"bold"),bg="black",onvalue=1,offvalue=0,fg="white",variable=self.var_check)
        checkbtn.place(x=50,y=380)
        
        registerbtn = Button(frame,command=self.register_data,text="New user Register",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="red",activebackground="white")
        registerbtn.place(x=40,y=450,width=160,height=35)
   
        loginbtn = Button(frame,text="login",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="blue",activebackground="white")
        loginbtn.place(x=250,y=450,width=160,height=35)

    
        ###### functionality
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
           messagebox.showerror("error","all fields are required ")
        elif self.var_check.get()==0:
           messagebox.showerror("agree to terms and conditions first")   
        else:
            connection = mysql.connector.connect(
            host='localhost',
            database='register',
            user='root',
            password='Ayushi@0987'
            )
    
            cur = connection.cursor()
            query =("select * from register_table where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("error","user already exist")
      
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_fname.get(),
                                                                                   self.var_lname.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_contact.get(),
                                                                                   self.var_securityQ.get(),
                                                                                   self.var_securityA.get(),
                                                                                   self.var_password.get()
                ))
            connection.commit()
            connection.close()
            messagebox.showinfo("success","registered successfully")
            
    def return_login(self):
        self.root.destroy()
        
if __name__=="__main__":
   main()