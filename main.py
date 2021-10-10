from copy1 import passgen
import tkinter as tk
def insert_text(arg1):
    textbox.delete("1.0",tk.END)
    s = arg1
    textbox.insert(1.0, s)
    textbox.pack()
def click_button():
    insert_text(passgen(10))
r=tk.Tk()
r.title('Password Generator')
# message
textMsg = 'Testing GUI for password generator'
msg=tk.Message(r,text=textMsg)
msg.config(bg="green")
msg.pack()
# end of message
# button
button=tk.Button(r,text='stop',width=25,command=r.destroy)
button.pack()
# end of button
# text
textbox=tk.Text(r,height=7,width=50)
textbox.pack()
insert_text(passgen(10))
# end of text
reRollButton=tk.Button(r, text='reroll',width=25,command=click_button)
reRollButton.pack()
r.mainloop()

# need to refactor to
# class APP
# not global import
# choose len of password, different alphabets