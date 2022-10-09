from tkinter import *
import playsound


##

root = Tk()
def click():
    
    myLabel = Label(root, text = "AHHADHAH")
    myLabel.pack()

def main():
    
    search_bar = Entry(root,width = 50)
    search_bar.pack()
    playsound.playsound('sample.mp3')
    
    
    image = PhotoImage(file="ratteled.png")
    ##image = image.resize((20, 20))
    ##image = ImageTK.PhotoImage(image)
    
    label = Label(root, image = image)
    label.pack()
    
    myButton = Button(width = 100, height = 20, image=image ,command=click)
    myButton.pack(padx = 20,pady = 50 )
    root.mainloop()
    
main()
