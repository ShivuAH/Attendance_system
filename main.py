# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk

# class Attendence_system:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Attendece system")

#         #Baground Image
#         bg_img=Image.open(r"C:\Users\shiva\OneDrive\Desktop\Images\alvas_logo.jpeg")
#         bg_img=bg_img.resize((1530,710),Image.Resampling.LANCZOS)

#         self.photo_bg_img=ImageTk.PhotoImage(bg_img)

#         bground_img=Label(self.root,image=self.photo_bg_img)
#         bground_img.place(x=250,y=250,widnith=1530,height=710)





# if __name__=="__main__":
#     root=Tk()
#     obj=Attendence_system(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Attendence_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        # Background Image (with transparency effect)
        bg_img = Image.open(r"C:\Users\shiva\OneDrive\Desktop\Images\alvas_logo.jpeg").convert("RGBA")
        
        # Resize to fit window
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)

        # Apply transparency (adjust alpha value: 255 = solid, 0 = fully transparent)
        alpha = 80  # you can try 80-150 for different transparency levels
        new_data = []
        for item in bg_img.getdata():
            # item = (R, G, B, A)
            new_data.append((item[0], item[1], item[2], alpha))
        bg_img.putdata(new_data)

        # Convert for Tkinter
        self.photo_bg_img = ImageTk.PhotoImage(bg_img)

        # Place in the center
        bground_img = Label(self.root, image=self.photo_bg_img)
        bground_img.place(x=0, y=0, width=1530, height=790)


if __name__ == "__main__":
    root = Tk()
    obj = Attendence_system(root)
    root.mainloop()
