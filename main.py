from tkinter import *
import webbrowser
from PIL import Image,ImageTk  # image libraries
from tkinter import messagebox
root=Tk()
root.title('Whatsapp Message Sender Application')
root.iconbitmap('C:/Users/harsh/Git_Files_Projects/MessangerApp/whatsapp_icon.ico')
root.configure(background='#008080')
root.geometry('1290x650+0+0')

photo = Image.open('C:/Users/harsh/Git_Files_Projects/MessangerApp/image/3d-whatsapp.jpg')
photo= photo.resize((1290,650))
image= ImageTk.PhotoImage(photo)
# code to create Background Image Label
bg_image=Label(root,image=image)
bg_image.pack()


#------------------------------------------[TOP 1 FEAME  MESSAGE BOX CODE]--------------------------------------------------------------
frame1=Frame(root,width=515,height=40,bg='MediumSeaGreen')
frame1.place(x=80,y=50)
#-------------------------------------
frame1_0=Frame(root,width=515,height=500,bg='black')
frame1_0.place(x=80,y=90)

#-------------------| Heading MESSAGE BOX |------------------

lbl_messege=Label(frame1,text='Whatsapp Message Service',bg='MediumSeaGreen',fg='white',font=('Bahnschrift Light',16,'bold'))
lbl_messege.place(x=110,y=6)
#----------------------------------------------------------


def send_it():
    webbrowser.open_new("https://web.whatsapp.com/send?phone='"+str(phone_number.get())+"'&text='"+message.get('1.0','end'))

def clear_textbox():
    phone_number.set("")
    message.delete('1.0', 'end')

phone_label = Label(frame1_0, text='Enter The Mobile Number',bg='black',fg='white',font=('Bahnschrift Light',16,'bold'))
phone_label.place(x=10,y=40)
phone_label = Label(frame1_0, text='(Phone number with country code required)',fg='white',bg='black',font=('Comic Sans MS',8))
phone_label.place(x=10,y=70)

phone_number = StringVar()

num_in_put = Entry(frame1_0,textvariable=phone_number,border=0,fg='white',bg='black',font=('Times New Roman',14))
num_in_put.place(x=10,y=100)
frame_Border=Frame(frame1_0,width=360,height=2,bg='white')
frame_Border.place(x=10,y=125)


message_label = Label(frame1_0,text='Enter Message',bg='black',fg='white',font=('Bahnschrift Light',16,'bold'))
message_label.place(x=10,y=170)
message = Text(frame1_0,width=45,height=4,bg='#bfd9ea',fg='black',bd=2)
message.place(x=10,y=220)


btn_send = Button(frame1_0,width=20,height=2, text='Send',bg='MediumSeaGreen',command=send_it)
btn_send.place(x=40,y=400)

bt_cler = Button(frame1_0,width=20 ,text='Clear',height=2,bg='MediumSeaGreen',command=clear_textbox)
bt_cler.place(x=270,y=400)

#-------------------------------------------|End Msg Box code Developd By Harshal Langote|------------------------------------------------------------
root.mainloop()