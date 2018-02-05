from tkinter import *                         # Import tkinter
root=Tk()                                     # Create an instance using Tk()
b=Button(root,justify = LEFT)                 # Create a button
photo=PhotoImage(file="verde.gif")           # Give photo an image
b.config(image=photo,width="100",height="100")  # Configure the earlier instance to use the photo
b.pack(side=LEFT)                             # Pack up the button
root.mainloop()