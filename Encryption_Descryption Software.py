from tkinter import*
from tkinter import Tk
from tkinter import ttk
from tkinter import colorchooser
from PIL import ImageTk,Image
import base64
from tkinter import filedialog
import time
root=Tk()
user=StringVar()
my_spin=IntVar()
combo2=StringVar()

combo=StringVar()

password=StringVar()




root.geometry('600x400+400+150')
root.config(bg='#313131')
root.resizable(False,False)
root.title('Login')
root.iconbitmap(r'C:\Users\MCA\Downloads\image2\paractices\icon.ico')
user_entry=Entry(root,width=20,font='Aileronl 17',bd=0,bg='#677868',fg='white',textvariable=user)
user_entry.place(x=170,y=130)
pass_entry=Entry(root,width=20,font='Aileronl 17',bd=0,bg='#677868',fg='white',textvariable=password,show='*')
pass_entry.place(x=170,y=200)
user_lbl=Label(root,text='User name',font='Aileronl 16 ',bg='#313131',fg='white')
user_lbl.place(x=60,y=128)
pass_lbl=Label(root,text='Password',font='Aileronl 16',bg='#313131',fg='white')
pass_lbl.place(x=70,y=200)
st_bar=Label(root,text='',font='Corbel 15',bg='#313131',fg='#eb697c')
I1=Image.open(r'C:\Users\MCA\Downloads\image2\paractices\user3.png')

t1=ImageTk.PhotoImage(I1)
bg_image=Label(root,image=t1,bg='#313131')
bg_image.place(x=245,y=10)

help_img=Image.open(r'C:\Users\MCA\Downloads\image2\paractices\help4.png')
sardar_img=Image.open(r'C:\Users\MCA\Downloads\image2\paractices\sardar3.png')

tel_img=Image.open(r'C:\Users\MCA\Downloads\image2\paractices\telegram5.png')
whats_img=Image.open(r'C:\Users\MCA\Downloads\image2\paractices\whatsapp3.png')



def pass_(event=None):
    
    a=str(user.get())
    b=str(password.get())
    my_spin=IntVar()
  
   
   
    if a=='Erfan40303' and b=='Mohammad1022':
        
        top=Tk()
        
          
       
      
        
        top.state('zoomed')
        top.config(bg='#313131')
        top.resizable(0,0)
       
        top.title('Secret Notes')
        top.iconbitmap(r'C:\Users\MCA\Downloads\image2\paractices\cyber4.ico')
       
      
       
        
        secret_frame=Frame(top,width=700,height=545,bg="#454545")
        secret_frame.place(x=410,y=100)
        
       
        root.destroy()
        text_box=Text(secret_frame,height=17,width=50,bd=0,bg='#454545',font='Aileronl 19',fg='white',wrap='word' )
        text_box.place(x=0,y=0)
        
        spin_box=Spinbox(top,from_=1,to=100,textvariable=my_spin,width=7,bg='#07e90d',fg='black')
        spin_box.place(x=1380,y=305)
        spin_lbl=Label(top,text='Encryption Frequency : ',font='Aileronl 12 bold',bg='#313131',fg='#07e90d')
        spin_lbl.place(x=1180,y=300)
        
         
        spin_box2=Spinbox(top,from_=1,to=100,textvariable=my_spin,width=7,bg='#07e90d',fg='black')
        spin_box2.place(x=1380,y=355)
        
        spin_lbl2=Label(top,text='Description Frequency : ',font='Aileronl 12 bold',bg='#313131',fg='#07e90d')
        spin_lbl2.place(x=1180,y=350)
        
       
        
      
        
        secret_lbl=Label(top,text='add your Secret Notes',font='Steiner 30',bg='#313131',fg='#07e90d')
        secret_lbl.place(x=520,y=20)
      
        sc_br=Scrollbar(top,jump=1)
        sc_br.config(command=text_box.yview)
        sc_br.pack(side='right',fill=BOTH)
        
       
       
        sc_lbl=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl.place(x=1115,y=83)
        
        sc_lbl2=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl2.place(x=1115,y=460)
        
        sc_lbl3=Label(top,text='S',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl3.place(x=1110,y=150)
        
        sc_lbl4=Label(top,text='E',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl4.place(x=1110,y=200)
        
        sc_lbl5=Label(top,text='C',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl5.place(x=1110,y=250)
        
        sc_lbl6=Label(top,text='R',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl6.place(x=1110,y=300)
        
        sc_lbl7=Label(top,text='E',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl7.place(x=1110,y=350)
        
        sc_lbl8=Label(top,text='T',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl8.place(x=1112,y=400)
      
        sc_lbl9=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl9.place(x=380,y=83)
        
        sc_lbl10=Label(top,text='N',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl10.place(x=373,y=150)
     
        
        sc_lbl11=Label(top,text='O',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl11.place(x=373,y=200)
        
        
        sc_lbl12=Label(top,text='T',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl12.place(x=376,y=250)
        
        sc_lbl12=Label(top,text='E',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl12.place(x=373,y=300)
        
        sc_lbl13=Label(top,text='S',font='Astronaut 40',bg='#313131',fg='#07e90d')
        sc_lbl13.place(x=373,y=350)
        
        sc_lbl14=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl14.place(x=380,y=400)
      
           
        sc_lbl15=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl15.place(x=380,y=478)
        
        
           
           
        sc_lbl16=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl16.place(x=380,y=555)
        
           
        sc_lbl17=Label(top,text='|',font='Steiner 60',bg='#313131',fg='#07e90d')
        sc_lbl17.place(x=1115,y=555)
        
      
       
        
        
      
        
        key_entry=Entry(top,font='Astronaut 17',bg='#454545',fg='white',bd=0,width=20,show='*')
        key_entry.place(x=1225,y=150)
        
        def show2():
            ao=key_entry.config(show='')
            show_key.config(fg='red')
            
        
       
        key_lbl=Label(top,text='Add your key word',font='Steiner 15 bold',bg='#313131',fg='#07e90d')
        key_lbl.place(x=1230,y=100)
       
        
       
          
        
    
           
        warning_lbl=Label(top,text='',font='Aileronl 14 bold',fg='red',bg='#313131')
        
        show_key=Button(top,text='Show',font='Aileronl 10 bold',fg='white',bg='#454545',bd=0,height=1,activebackground='#454545',command=show2)
        show_key.place(x=1402,y=151)
        
        w_lbl=Label(top,text="if you don't have key word,you can't use \n this software beccause it's secret...............",font='Aileronl',bg='#313131',fg='white')
       
       
        def encryption(event=None):
            a=text_box.get(1.0,END)
            text_box.delete(1.0,END)
            sp=int(spin_box.get())
           
            if key_entry.get()=='Yahossein':
                
                for i in range(sp):
                    a=a.encode('ascii')
                    a=base64.b64encode(a)
                    a=a.decode('ascii')
                text_box.insert(END,a)
             
            else:
                warning_lbl.config(text='key word is incorrect')
                warning_lbl.place(x=1240,y=180)
                
        def description():
            a=text_box.get(1.0,END)
            text_box.delete(1.0,END)
            sp=int(spin_box2.get())
            if key_entry.get()=='Yahossein':
                for i in range(sp):
                    a=a.encode('ascii')
                    a=base64.b64decode(a)
                    a=a.decode('ascii')
                text_box.insert(END,a)
            else:
                warning_lbl.config(text='key word is incorrect')
                warning_lbl.place(x=1240,y=180)
                
        def open_():
            mypath=filedialog.askopenfilename(initialfile='Untitled.txt',title='Open File',defaultextension='.txt',filetypes=[('Text Document','*.txt')])
            
            if not mypath:
                return
            
            
            myfile=open(mypath,'r',encoding='utf8')
            textcontent=myfile.read()
            text_box.insert(END,textcontent)
            root.title(mypath)
           
                
                
            
         
         
          
          
            
        def save():
              mypath=filedialog.asksaveasfilename(initialfile='Untitled.txt',title='Save as...',initialdir='/',defaultextension='.txt',filetypes=[('Text Document','*.txt')])
              if not mypath:
                  return
                  
              my_file=open(mypath,'w',encoding='utf8')
              my_text=text_box.get(1.0,END)
              my_file.write(my_text)
              top.title(mypath)
              
                 
             
           
             
           
       
            
            
       
       
        encryption_button=Button(top,text='Encryption',font='Steiner 20 bold',bg='#07e90d',fg='black',bd=0,activebackground='#454545',command=encryption)
        encryption_button.place(x=850,y=680)
        
        description_button=Button(top,text='Descryption',font='Steiner 20 bold',bg='#07e90d',fg='black',activebackground='#454545',bd=0,command=description)
        description_button.place(x=480,y=680)
        
        
        saveas_button=Button(top,text='Save as',font='Steiner 14 bold',bg='#07e90d',fg='black',bd=0,activebackground='#454545',width=15,command=save)
        saveas_button.place(x=79,y=103)
        
        open_button=Button(top,text='open',font='Steiner 14 bold',bg='#07e90d',fg='black',bd=0,activebackground='#454545',width=15,command=open_)
        open_button.place(x=79,y=150)
        
        def delete():
            if key_entry.get()=='Yahossein':
                text_box.delete(1.0,END)
        
        delete_button=Button(top,text='Clear All',font='Steiner 15 bold',bg='red',fg='white',bd=0,activebackground='#454545',width=9,command=delete)
        delete_button.place(x=700,y=688)
        
        time_lbl=Label(top,text='')
        am_lbl=Label(top,text='')
        sayer_lbl=Label(top,text='')
        
        def time_():
            hour=time.strftime('%H')
            minute=time.strftime('%M')
            second=time.strftime('%S')
            am_pm=time.strftime('%p')
            day=time.strftime('%a')
            month=time.strftime('%b')
            month_day=time.strftime('%m')
            year=time.strftime('%Y')
            time_lbl.config(text=hour + ':' + minute + ':' + second,font='digital 30',bg='#313131',fg='#07e90d')
            time_lbl.after(1000,time_)
            time_lbl.place(x=120,y=230)
            am_lbl.config(text=am_pm,font='digital 20',bg='#313131',fg='#07e90d')
            am_lbl.place(x=240,y=240)
            
            sayer_lbl.config(text=day+','+month+','+month_day+','+year,font='Astronaut 20',bg='#313131',fg='#07e90d')
            sayer_lbl.place(x=100,y=270)
        time_()
        
        char_lbl=Label(top,text='')
        def m():
            char=list(text_box.get(1.0,END))
            char_2=str(len(char)-1)
            char_lbl.config(text='characters'+ ' '+':'+' '+char_2,font='Steiner 20 bold',bg='#313131',fg='#07e90d')
            char_lbl.after(1,m)
            char_lbl.place(x=20,y=400)
        
        m()
        
      
     
       
        
        
        def help_():
            if key_entry.get()=='Yahossein':
                window=Tk()
                window.iconbitmap(r'C:\Users\MCA\Downloads\image2\paractices\help_icon2.ico')
                window.resizable(0,0)
                window.geometry('605x500+450+130')
                window.resizable(False,False)
                window.title('help')
                window.config(bg='#313131')
           
            
                convert=ImageTk.PhotoImage(help_img)
                help_lbl=Label(window,image=convert,bg='#313131')
                help_lbl.place(x=190,y=20)
                help_lbl2=Label(window,text="this Software is for encryption and discription texts and it isn't \n suitable for everybody",font='Aileronl 15 bold',bg='#313131',fg='red')
                help_lbl2.place(x=9,y=170)
                encryption_lbl=Label(window,text='Encryption :',font='Steiner 16 bold',bg='#313131',fg='#07e90d')
                encryption_lbl.place(x=9,y=240)
            
                encryption_lbl2=Label(window,text="this item for encryptioning the texts.if key \n word be wrong it doesn't work.                           ",font='Corbel 16 bold',bg='#313131',fg='white')
                encryption_lbl2.place(x=150,y=240)
            
                description_lbl=Label(window,text='Description :',font='Steiner 16 bold',bg='#313131',fg='#07e90d')
                description_lbl.place(x=9,y=310)
            
                description_lbl2=Label(window,text="this option for for descriptioning texts.if key \n word be wrong it doesn't work.                              ",font='corbel 16 bold',bg='#313131',fg='white')
                description_lbl2.place(x=150,y=310)
            
                saveas_lbl=Label(window,text='Save as :',font='Steiner 16 bold',bg='#313131',fg='#07e90d')
                saveas_lbl.place(x=9,y=380)
            
                saveas_lbl2=Label(window,text="you can save your changes with this option.",font='corbel 16 bold',bg='#313131',fg='white')
                saveas_lbl2.place(x=125,y=380)
            
                open_lbl=Label(window,text='Open :',font='Steiner 16 bold',bg='#313131',fg='#07e90d')
                open_lbl.place(x=9,y=450)
            
                open_lbl2=Label(window,text="you can open your text files with this option.",font='corbel 16 bold',bg='#313131',fg='white')
                open_lbl2.place(x=125,y=450)
                window.mainloop()
            
            else:
                warning_lbl.config(text='key word is incorrect')
                warning_lbl.place(x=1240,y=180)
          
           
              
            
      
            top.mainloop()
            
      
           
        def setting_():
            if key_entry.get()=='Yahossein':
                door=Tk()
                door.resizable(0,0)
                door.iconbitmap(r'C:\Users\MCA\Downloads\image2\paractices\set2.ico')
                door.geometry('350x200+570+200')
                door.title('Setting')
                door.config(bg='#454545')
                font_lbl=Label(door,text='Text Font : ',font='Aileronl 15 bold',bg='#454545',fg='#07e90d')
                font_lbl.place(x=20,y=20)
                combo=StringVar()
                categories=['Aileron','Corbel','Steiner','Calibri','Tahoma','Astronaut']
                my_combo=ttk.Combobox(door,textvariable=combo,value=categories)
                my_combo.place(x=150,y=27)
                categories2=['green','blue','white','yellow']
              
                my_combo2=ttk.Combobox(door,textvariable=combo2,value=categories2)
                my_combo2.place(x=150,y=77)
              
                def set_():
                  if my_combo.get()=='Steiner':
                      text_box.config(font='Steiner 16')
                  elif my_combo.get()=='Corbel':
                      text_box.config(font='Corbel 20')
                  elif my_combo.get()=='Aileron':
                      text_box.config(font='Aileronl 19')
                  elif my_combo.get()=='Calibri':
                      text_box.config(font='Calibri 20')
                  elif my_combo.get()=='Tahoma':
                      text_box.config(font='Candara 19')
                  elif my_combo.get()=='Astronaut':
                      text_box.config(font='Astronaut 21')
                  if my_combo2.get()=='green':
                      text_box.config(fg='#07e90d')
                  elif my_combo2.get()=='yellow':
                      text_box.config(fg='yellow')
                  elif my_combo2.get()=='white':
                      text_box.config(fg='white')
                  elif my_combo2.get()=='blue':
                      text_box.config(fg='skyblue')
                  
                 
                      
                set_btn=Button(door,text='Set',font='Aileronl 12 bold',bg='#07e90d',fg='black',width=7,bd=0,activebackground='#07e90d',activeforeground='black',command=set_)
              
                set_btn.place(x=120,y=150)
                enc_lbl=Label(door,text='FontColor:',bg='#454545',fg='#07e90d',font='Aileronl 15 bold')
                enc_lbl.place(x=20,y=70)
                door.mainloop()
            else:
                warning_lbl.config(text='key word is incorrect')
                warning_lbl.place(x=1240,y=180)
              
              
            
           
            
           
            
      
        help_button=Button(top,text='help(?)',fg='white',bg='#313131',font='Corbel 17',bd=0,activebackground='#313131',command=help_)
        help_button.place(x=725,y=730)
        
        setting_button=Button(top,text='(Setting)',font='Corbel 14 bold',bg='#454545',fg='white',bd=0,activebackground='#313131',command=setting_,activeforeground='white',width=10)
        
        setting_button.place(x=20,y=725)
        
        def contact_us():
            if key_entry.get()=='Yahossein':
                open_=Tk()
                open_.resizable(0,0)
                open_.iconbitmap(r'C:\Users\MCA\Downloads\image2\paractices\contact.ico')
                open_.geometry('400x200+550+200')
                open_.title('contact us')
                open_.resizable(0,0)
                open_.config(bg='#454545')
                email_lbl=Label(open_,text='E-mail : ',font='Aileronl 17',bg='#454545',fg='white')
                email_lbl.place(x=10,y=20)
                sy_lbl=Label(open_,text='symrfan@gmail.com',font='Aileronl 17 bold',bg='#454545',fg='#07e90d')
                sy_lbl.place(x=100,y=20)
                phone_lbl=Label(open_,text='Phonenumber : ',font='Aileronl 17 ',bg='#454545',fg='white')
                phone_lbl.place(x=10,y=60)
                sy_lbl=Label(open_,text='09107855814',font='Aileronl 17 bold',bg='#454545',fg='#07e90d')
                sy_lbl.place(x=175,y=60)
                convert2=ImageTk.PhotoImage(tel_img)
                tel_lbl=Label(open_,image=convert2,bg='#454545')
                tel_lbl.place(x=120,y=100)
                convert3=ImageTk.PhotoImage(whats_img)
                whats_lbl=Label(open_,image=convert3,bg='#454545')
                whats_lbl.place(x=200,y=100)
                open_.mainloop()
            else:
                warning_lbl.config(text='key word is incorrect')
                warning_lbl.place(x=1240,y=180)
                
        
        contact_btn=Button(top,text='(contact us)',font='Corbel 14 bold',bg='#454545',fg='white',bd=0,activebackground='#313131',activeforeground='white',width=10,command=contact_us)
        contact_btn.place(x=20,y=765)
       
      
      
            
        
        
        
     
    else:
        st_bar.config(text='username or password is incorrect')
        st_bar.place(x=155,y=240)

def show():
    pass_entry.config(show='')
    show_button.config(fg='#fea9b6')
    

        

sub_button=Button(root,text='Submit',font='Aileronl 15 bold',bg='white',fg='black',bd=0,activebackground='#313131',command=pass_,width=17)
sub_button.place(x=195,y=270)

show_button=Button(root,text='Show',font='Aileronl 10 bold',fg='white',bg='#677868',bd=0,activebackground='#677868',command=show)
show_button.place(x=388,y=202)




exit_button=Button(root,text='Exit',font='Aileronl 13 bold',fg='white',bg='#313131',bd=0,activebackground='#313131',command=root.quit)
exit_button.place(x=5,y=370)
root.mainloop()

