import marshal
import os
import tkinter as tk
from tkinter import messagebox

def commands():
    try:
        os.chdir(f"{Entry_1.get()}")
    except:
        messagebox.showinfo('the path is wrong')
    my_file = Entry_2.get()
    open_file = open(my_file , 'r').read()
    compile_file = compile(open_file, '' ,'exec')
    encryt = marshal.dumps(compile_file)
    code = open('New_'+ str(my_file),"w")
    code.write("import marshal\n")
    code.write('exec(marshal.loads('+repr(encryt)+'))')
    print(f"the file name is {my_file} is encrypted ")

    messagebox.showinfo('the file is encryped')

window = tk.Tk()
window.geometry('400x520+340+100')
window.title('Encyption')
icon = tk.PhotoImage (file = r"D:\MSA\Python Projects\Encryption\photos\security.png")
window.iconphoto(False, icon)
window.resizable(False,False)
window.configure(bg="#27408B")

Text_1 = tk.Label(window, text= 'welcome to encryption', fg= 'white', bg= 'black', font= 22)
Text_1.pack(fill= 'x')

image = tk.PhotoImage(file=r"D:\MSA\Python Projects\Encryption\photos\security.png")
resized_image = image.subsample(2)

label = tk.Label(window, image=resized_image, bg='#27408B')
label.pack()

Text_2 = tk.Label(window, text= 'Write the path of folder :', font= 22, bg="#27408B")
Text_2.place(x= 85, y= 300 )

Entry_1 = tk.Entry(window, font= 12, width= 31, bg= '#FFA500', fg= 'black')
Entry_1.place(x= 20, y= 340)

Text_3 = tk.Label(window, text= 'Write the name of the file :', font= 22, bg='#27408B')
Text_3.place(x= 75, y= 380 )

Entry_2 = tk.Entry(window, font= 12, width= 31, bg= '#FFA500', fg= 'black')
Entry_2.place(x= 20, y= 420)

Button = tk.Button(window, text= 'Encrype', fg= 'black', bg= '#4169E1', width= 31, font= 12, command= commands)
Button.place(x= 20, y= 460)

window.mainloop()