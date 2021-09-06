from tkinter import *
from  tkinter import  messagebox

class BMI_Class:
    def __init__(self,root):
        self.root=root
        self.root.title("BMI System")
        self.root.geometry("650x680+320+50")
        self.root.config(bg="#E0FFFF")
        self.root.resizable(width=False, height=False)

        title = Label(self.root, text="BMI Program",font =("Elephant",25),bg="#E0FFFF").pack(side=TOP,fill=X)
        title_bottom = Label(self.root, text="Design by: Richard Nguyen",font =("times new roman",15),bg="gray").pack(side=BOTTOM,fill=X)

#          ======= Variable =========
        self.var_height=StringVar()
        self.var_weight=StringVar()
        self.var_yourBMI=StringVar()
        self.var_status=StringVar()
        self.var_level=StringVar()

        lbl_height=Label(self.root,text="Enter height",font=("goudy old style",20),bg="#E0FFFF").place(x=50,y=100)
        txt_height=Entry(self.root,textvariable=self.var_height,font=("times new roman",15),bg="lightyellow").place(x=250,y=100,width=300,height=40)

        lbl_weight=Label(self.root,text="Enter weight",font=("goudy old style",20),bg="#E0FFFF").place(x=50,y=170)
        txt_weight=Entry(self.root,textvariable=self.var_weight,font=("times new roman",15),bg="lightyellow").place(x=250,y=170,width=300,height=40)

        btn_BMI=Button(self.root,text="Caculate BMI",bg="#47d1d1",command=self.BMI,font=("times new roman",15)).place(x=250,y=240,width=130,height=50)
        btn_clear=Button(self.root,text="Clear",bg="gray",command=self.clear,font=("times new roman",15)).place(x=420,y=240,width=130,height=50)

        lbl_your_BMI = Label(self.root, text="Your BMI", font=("goudy old style", 20), bg="#E0FFFF").place(x=50, y=320)
        txt_your_BMI = Entry(self.root,textvariable=self.var_yourBMI, font=("times new roman", 20), bg="lightyellow",fg="#cc2900",state="readonly").place(x=250, y=320, width=300, height=40)

        lbl_state = Label(self.root, text=" Your status", font=("goudy old style", 20), bg="#E0FFFF").place(x=50, y=400)
        txt_state = Entry(self.root, textvariable=self.var_status, font=("times new roman", 20), bg="lightyellow",fg="#cc2900",state="readonly").place(x=250, y=400, width=300, height=40)

        lbl_weight = Label(self.root, text="Disease level", font=("goudy old style", 20), bg="#E0FFFF").place(x=50, y=480)
        txt_weight = Entry(self.root, textvariable=self.var_level, font=("times new roman", 20), bg="lightyellow",fg="#cc2900",state="readonly").place(x=250, y=480, width=300, height=40)
        btn_exit=Button(self.root,text="Exit",bg="gray",command=self.exit,font=("times new roman",15)).place(x=300,y=540,width=130,height=50)


    def clear(self):
        self.var_height.set("")
        self.var_weight.set("")
        self.var_yourBMI.set("")
        self.var_status.set("")
        self.var_level.set("")


    def BMI(self):
        if self.var_weight.get()=="" or self.var_height.get()=="":
            messagebox.showerror("Error","Please enter your height and weight")
        else:
            self.h=float(self.var_height.get())
            self.w=float(self.var_weight.get())
            self.number=round(self.w/(self.h*self.h))

            if self.number <=18.5:
                self.var_yourBMI.set(self.number)
                self.var_status.set("Thin")
                self.var_level.set("Low")

            elif self.number <=24.9:
                self.var_yourBMI.set(self.number)
                self.var_status.set("Normal")
                self.var_level.set("Medium")

            elif self.number <=29.9:
                self.var_yourBMI.set(self.number)
                self.var_status.set("Lightly Overweight")
                self.var_level.set("A little high")

            elif self.number <=34.9:
                self.var_yourBMI.set(self.number)
                self.var_status.set("Obesity level 1")
                self.var_level.set("High")

            elif self.number <= 39.9:
                self.var_yourBMI.set(self.number)
                self.var_status.set("Obesity level 2")
                self.var_level.set("Very high")
            else:
                self.var_yourBMI.set(self.number)
                self.var_status.set("Obesity level 3")
                self.var_level.set("Dangerous")

    def exit(self):
        op=messagebox.askyesno("Confirm","Do you readly want to exit")
        if op==True:
            self.root.destroy()









if __name__=="__main__":
    root =Tk()
    obj=BMI_Class(root)
    root.mainloop()