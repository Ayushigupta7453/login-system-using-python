from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk 
from tkinter import messagebox
import mysql.connector

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
            
                
if __name__=="__main__":
    root=Tk()
    app = Register(root)
    root.mainloop()