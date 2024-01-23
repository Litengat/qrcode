from tkinter import *
from PIL import ImageGrab, ImageTk, Image
from ReadCode import *

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

root = Tk()
root.title('Code Reader')
root.geometry("1000x700")


def UpdateUi():
    img = ImageGrab.grabclipboard()
    ratio = img.width/img.height
    Resized_img = img.resize((int(400*ratio), 400))

    img.save('IMG/Code.png', 'PNG')
    Resized_img.save('IMG/Resized.png', 'PNG')    

    ResizedImage = PhotoImage(file='IMG/Resized.png')

    Label(
        root,
        image=ResizedImage,
    ).grid(row =1)

    Button(
        root,
        text="Read Code!",
        command=ButtonReadCode
    ).grid(row=2, column=1 )

    root.mainloop()

def ButtonReadCode():
    CropFromPhoto()
    Message = BinaryToText(ReadFromImage())
    label1 = Label(root, text=Message)
    label1.grid(row=3)
    root.mainloop()


Header = Label(root, text="My Code Reader...", font=("Arial", 20))

button = Button(root, text="Paste from my Clipboard", command=UpdateUi)
Header.grid(row=0)
button.grid(row=2, column=0)


root.mainloop()