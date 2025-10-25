import data as d
import custom as cs
from tkinter import *
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import ttk, messagebox

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class GoogleTranslate:

    def __init__(self,root):
        #window Settings
        self.window = root
        self.window.geometry("900x540")
        self.window.title("Google Translate")
        self.window.resizable(width=False, height=False)
        self.window.configure(bg="white")

        #Frame for showing the Google Translate Logo
        self.frame = Frame(self.window, width=300, height=60)
        self.frame.pack()
        self.frame.place(x=20, y=20)
        #calling the function for showing the logo
        self.DisplayLogo()

        #About Btn
        aboutBtn = Button(self.window, text="About", 
        font=(cs.font2, 8, 'bold'), bg=cs.color2, 
        fg="white", width=5, command=self.About)
        aboutBtn.place(x=800, y=20)

        #Exit Btn
        exitBtn = Button(self.window, text="Exit", 
        font=(cs.font2, 8, 'bold'), bg=cs.color2, 
        fg="white", width=5, command=self.Exit)
        exitBtn.place(x=800, y=60)


        self.MainWindow()


    def DisplayLogo(self):
        logo_path = resource_path("GoogleTranslate.png")

        image= Image.open(logo_path)
        resized_img = image.resize((300,60))

        self.img1 = ImageTk.PhotoImage(resized_img)

        label=Label(self.frame, bg=cs.color1, image=self.img1)
        label.pack()

    def MainWindow(self):
        #String Variable
        self.currLang = StringVar()
        self.currLang.set("Not Detected")

        #label for showing the name of detected language
        self.detectLang = Label(self.window, textvariable=self.currLang, font=(cs.font3,20), bg =cs.color1)
        self.detectLang.place(x=160, y=130)

        #Combo Box To select the language to be translated
        text=StringVar()
        self.toLang=ttk.Combobox(self.window, textvariable=text, font=(cs.font1, 15))
        self.toLang['values']=d.lang_list
        self.toLang.current(0)
        self.toLang.place(x=550, y=130)

        self.fromTextBox = Text(self.window, bg=cs.color3, font=(cs.font1, 15), height=9, width=34)
        self.fromTextBox.place(x=80, y=190)

        self.toTextBox = Text(self.window, bg=cs.color3, relief=GROOVE, font=(cs.font1, 15), height=9, width=34)
        self.toTextBox.place(x=480, y=190)

        translateBtn = Button(self.window, text="Translate",
                              font=(cs.font2, 14, "bold"), bg=cs.color4, fg=cs.color1,
                              command=self.Translator)
        translateBtn.place(x=385, y=430)


    def Translator(self):
        try:

            fromText = self.fromTextBox.get("1.0", "end-1c")

            #Instance of Translator
            translator = Translator()

            dest_lang = self.toLang.get()

            if dest_lang == '':
                messagebox.showwarning("Nothing has Choosen!", "Please Choose a Language")
            else:
                if fromText != '':
                    langType = translator.detect(fromText)

                    result = translator.translate(fromText, dest_lang)

                    self.currLang.set(d._languages[langType.lang.lower()])

                    self.toTextBox.delete("1.0", END)
                    
                    self.toTextBox.insert(INSERT, result.text)
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    
    def About(self):
        messagebox.showinfo("Google Translate - Python", "Developed By Sadhu Sunder")

    
    def Exit(self):
        self.window.destroy()



if __name__ == "__main__":
# Instance of Tk Class
    root = Tk()
    # Object of GoogleTranslator Class
    obj = GoogleTranslate(root)
    root.mainloop()



