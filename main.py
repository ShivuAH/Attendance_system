from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Attendence_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        # Background Image (with transparency effect)
        bg_img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Images\Engineering.jpg") 
        # Resize to fit window
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        # Convert for Tkinter
        self.photo_bg_img = ImageTk.PhotoImage(bg_img)

        # Place in the center
        bground_img = Label(self.root, image=self.photo_bg_img)
        bground_img.place(x=0, y=0, width=1530, height=790)

        logo_img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Images\alvas-org-logo.png")
        logo_img = logo_img.resize((117, 131), Image.Resampling.LANCZOS)
        self.photo_logo_img=ImageTk.PhotoImage(logo_img)

        logo = Label(self.root, image=self.photo_logo_img)
        logo.place(x=70, y=70, width=117, height=131)


        title_lable=Label(bground_img,text="Alvas Institute of Engineering and Technology",font=("Arial black",40,"bold"),fg="red")
        title_lable.place(x=0,y=0,width=1530,height=55)


if __name__ == "__main__":
    root = Tk()
    obj = Attendence_system(root)
    root.mainloop()
