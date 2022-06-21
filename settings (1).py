#from ast import pattern
from calendar import c
from cgitb import enable, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from xml.dom.minidom import Entity
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor()

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
def log():
    global user_name1
    user_name1=username1.get()
    passwd1=password1.get()
    if user_name1=="" or passwd1=="":
        Label(text='Plz enter both username and password',fg='red').place(x=85,y=260)
    else:
        sql='SELECT * FROM users WHERE username=%s AND password=%s'
        val=(user_name1,passwd1,)
        fbcursor.execute(sql,val)
        if fbcursor.fetchone()is not None:
            mainpage()
            if user_name1 != "adminstator":
              tab06.destroy()
            else:
              pass
            root.iconify()
        else:
            messagebox.showinfo('Acess denied','Username Or Password Wrong')

  
sql = "select * from users"
fbcursor.execute(sql)
user_log = fbcursor.fetchall()
if not user_log:
  def lo():
    mainpage()
  root=Tk()
  root.geometry("500x250")
  root.resizable(False, False)
  root.eval('tk::PlaceWindow . center')
  Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
  submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("500x200")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("F-Billing Revolution 2022")
    p1 = PhotoImage(file = 'images/fbicon.png')
    root.iconphoto(False,p1)
    username1=StringVar()
    password1=StringVar()

    Label(text='Login F-Billing Revolution 2022',font='arial 13 bold').place(x=120,y=15)
    
  
    sql = "select username from users"
    fbcursor.execute(sql)
    user_log_name = fbcursor.fetchall()
    uss1=Label(text='Username').place(x=120,y=65)
    ee1 = ttk.Combobox(textvariable=username1)
    ee1.place(x=220,y=65)
    ee1["values"] = user_log_name

    pss1=Label(text='Password').place(x=120,y=105)
    ee2=Entry(textvariable=password1,show='*',width=23).place(x=220,y=105)
    
    submitbtn1=Button(text='Login', width=15,command=log,activeforeground="white",
                   activebackground="black").place(x=250,y=150)
    
  
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")

selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")
  
right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")
  
  
photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")

est_logo = PhotoImage(file = "images/company_logo.png")

def mainpage():
  root.iconify()
  main = Toplevel()
  main.geometry("1360x730")
  p1 = PhotoImage(file = 'images/fbicon.png')
  main.iconphoto(False, p1)
  main.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
  s = ttk.Style()
  s.theme_use('default')
  s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
  tabControl = ttk.Notebook(main)
  tab1 = ttk.Frame(tabControl)
  tab2 = ttk.Frame(tabControl)
  tab3=  ttk.Frame(tabControl)
  tab4 = ttk.Frame(tabControl)
  tab5 = ttk.Frame(tabControl)
  tab6=  ttk.Frame(tabControl)
  tab7 = ttk.Frame(tabControl)
  tab8 = ttk.Frame(tabControl)
  tab9 =  ttk.Frame(tabControl)
  tab10=  ttk.Frame(tabControl)
  tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
  tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
  tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
  tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
  tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
  tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
  tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
  tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
  tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
  tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
  tabControl.pack(expand = 1, fill ="both")
  
  

  
  # def log():
  #   global user_name1
  #   user_name1=username1.get()
  #   passwd1=password1.get()
  #   if user_name1=="" or passwd1=="":
  #       Label(screen2,text='Plz enter both username and password',fg='red').place(x=85,y=260)
  #   else:
  #       sql='SELECT * FROM users WHERE username=%s AND password=%s'
  #       val=(user_name1,passwd1,)
  #       fbcursor.execute(sql,val)
  #       if fbcursor.fetchone()is not None:
  #           root(user_name1)
  #       else:
  #           messagebox.showinfo('Acess denied','Acess denied')
  
  # sql = "select * from users"
  # fbcursor.execute(sql)
  # user_log = fbcursor.fetchall()
  # if not user_log:
  #   pass
  # else:
  #     screen2=Toplevel()
  #     screen2.title('LOGIN')
  #     screen2.geometry('400x300')
  
  #     username1=StringVar()
  #     password1=StringVar()
  
  #     Label(screen2,text='Login Here').pack()
  #     uss1=Label(screen2,text='Username').place(x=50,y=70)
  #     ee1 = Entry(screen2,textvariable=username1).place(x=140,y=70)
  
  #     pss1=Label(screen2,text='Password').place(x=50,y=110)
  #     ee2=Entry(screen2,textvariable=password1).place(x=140,y=110)
  
  #     submitbtn1=Button(screen2,text='Login', width=20,height=2,command=log).place(x=70,y=200)
  
  # def check_empty() :
  #      if entry.get():
  #         pass     #your function where you want to jump
  #      else:
  #         messagebox.showinfo("Information", "Required entry")
  
  
  ######################## FRONT PAGE OF CUSTOMER SECTION   #######################################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  # def upload_filelogo():
  #   global imglogo,filename
  #   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  #   filena = filedialog.askopenfilename(filetypes=f_types)
  #   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
  #   print(filena.split('/')[-1])
  #   image = Image.open(filena)
  #   resize_image = image.resize((280, 160))
  #   imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    # btlogo.place(x=580,y=280)
  global filename
  filename = ""
  def save_company():
    company_name = comname.get()
    company_address = caddent.get(1.0,END)
    company_mail = comemail.get()
    company_salestax =comsalestax.get()
    currency = comcur.get()
    currencysign = comcursign.get()
    currencysign_placement = comcursignpla.get()
    decimal_sepator = comdecsep.get()
    currency_example = comex.get()
    date_format = comdaf.get()
    example_dateformat = exd.get_date()
    tax = radtax.get()
    tax1name = tax1namee.get()
    tax1rate = tax1ratee.get()
    printtax1 = comptax1.get()
    tax2name = tax2namee.get()
    tax2rate = tax2ratee.get()
    printtax2 = comptax2.get()
    printimage = compimg.get()
    win_menu_colour = win_menu.get()
    radiobut = radema.get()
    cbut1 = checkb1.get()
    cbut2 = checkb2.get()
    cbut3 = checkb3.get()
    cbut4 = checkb4.get()
    cbut5 = checkb5.get()
    cbut6 = checkb6.get()
    est_prefix = est_str.get()
    est_header = win_menu1.get()
    est_text1 = est_str1.get()
    est_text2 = est_str2.get()
    est_text3 = est_str3.get()
    est_text4 = est_str4.get()
    est_text5 = est_str5.get()
    est_text6 = est_str6.get()
    est_predefined = est_str7.get(1.0,END)
    est_default = win_menu2.get()
    est_spin1 = spin1.get()
    adv_default = adv_win_menu8.get()

    child = exctree.get_children()
    var = json.dumps(child)
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        print(12)
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
      
  
  addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
  save_setting = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command=save_company, image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  save_setting.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  def wiz_page():
    global filname
    filname = ""
    def upload_cfilelogo():
      global filname
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filname = filedialog.askopenfilename(filetypes=f_types)
      shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
      image = Image.open(filname)
      resize_image = image.resize((280, 140))
      imgclogo = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=imgclogo)
      btclogo.place(x=30,y=240)
      btclogo.photo = imgclogo
    def csave():
      company_name = company_namee.get()
      company_address = company_addresse.get('1.0', 'end-1c')
      company_email = company_emaile.get()
      salestaxregno = salestaxregnoe.get()
      cprint_logopic = cplogopic.get()
      sql = "select image from company"
      fbcursor.execute(sql)
      im = fbcursor.fetchone()
      sql = "select * from company"
      fbcursor.execute(sql)
      i = fbcursor.fetchall()
      if not i:
        if filname == "":
          sql = 'insert into company(name, address, email,salestaxno,printimageornot) values(%s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = 'insert into company(name, address, email,salestaxno,printimageornot,image) values(%s, %s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1],)
          fbcursor.execute(sql, val)
          fbilldb.commit()
      else:
        if filname == "":
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s,image=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
      centry.delete(0, END)
      centry.insert(0, company_name)
      caddent.delete('1.0', END)
      caddent.insert('1.0', company_address)
      cemailentry.delete(0, END)
      cemailentry.insert(0, company_email)
      ste.delete(0, END)
      ste.insert(0, salestaxregno)
      if cprint_logopic == 1:
        primage.select()
      else:
        primage.deselect()
      try:
        image = Image.open("images/"+filname.split('/')[-1])
        resize_image = image.resize((280, 160))
        image = ImageTk.PhotoImage(resize_image)
        btlogo = Button(secondtab,width=280,height=160,image=image)
        btlogo.place(x=580,y=280)
        btlogo.photo = image
      except:
        pass
      wiz.destroy()


      
      

    
    wiz = Toplevel()
    wiz.geometry("500x449+400+167")
    wiz.title("Wellcome to Quick Start Wizard")
    sql = "select * from company"
    fbcursor.execute(sql)
    secctab = fbcursor.fetchone()
    comp_infor = Label(wiz,text="Enter Your Company Information",font='arial 13 bold',fg="blue")
    comp_infor.place(x=15,y=15)
    company_da_laframe = LabelFrame(wiz,text="Company data",height=180, width=460)
    company_da_laframe.place(x=15,y=40)
    company_name = Label(wiz,text="Company name")
    company_name.place(x=30,y=60)
    company_namee = Entry(wiz,width=50)
    company_namee.place(x=160,y=60)
    if  not secctab:
      pass
    else:
      company_namee.insert(0, secctab[1])
  
    company_address = Label(wiz,text="Company address")
    company_address.place(x=30,y=90)
    company_addresse = scrolledtext.ScrolledText(wiz,)
    company_addresse.place(x=160,y=90,width=250,height=60)
    if  not secctab:
      pass
    else:
      company_addresse.insert('1.0', secctab[2])

    company_email = Label(wiz,text="Email address")
    company_email.place(x=30,y=160)
    company_emaile = Entry(wiz,width=50)
    company_emaile.place(x=160,y=160)
    if  not secctab:
      pass
    else:
      company_emaile.insert(0, secctab[3])

    salestaxregno = Label(wiz,text="Sales Tax.Reg.No")
    salestaxregno.place(x=30,y=190)
    salestaxregnoe = Entry(wiz,width=50)
    salestaxregnoe.place(x=160,y=190)
    if  not secctab:
      pass
    else:
      salestaxregnoe.insert(0, secctab[4])
    
    
    company_da_laframe = LabelFrame(wiz,text="Company logo",height=190, width=460)
    company_da_laframe.place(x=15,y=220)
    try:
      image_wiz = Image.open("images/"+secctab[13])
      resize_image = image_wiz.resize((280, 140))
      image_wiza = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=image_wiza)
      btclogo.place(x=30,y=240)
      btclogo.photo = image_wiza
    except:
      pass
    cplogopic = BooleanVar()
    cprint_logopic = Checkbutton(wiz,text='Print logo picture',bg='white',onvalue =1,
                        offvalue = 0,variable=cplogopic)
    cprint_logopic.place(x=320,y=250)
    if  not secctab:
      pass
    else:
      if secctab[14] == 1:
        cprint_logopic.select()
      else:
        cprint_logopic.deselect()
      
    load_img = Button(wiz,text='Load logo image',command=upload_cfilelogo)
    load_img.place(x=320,y=360)
    save_com_wiz = Button(wiz,text='Save',width=10,command=csave)
    save_com_wiz.place(x=370,y=415)

  quick_start_wiz = Button(settframe,compound="top", text="Quick\nStart Wizard ",relief=RAISED,    command=wiz_page, image=photo, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  quick_start_wiz.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  
  
  invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))
  
  global tab06
  m = ttk.Style()
  m.theme_use('default')
  m.configure('one.TNotebook.Tab', background="white", width=20, padding=10)
  tabControl = ttk.Notebook(tab10,style='one.TNotebook.Tab')
  tab01 = ttk.Frame(tabControl)
  tab02 = ttk.Frame(tabControl)
  tab03=  ttk.Frame(tabControl)
  tab04 = ttk.Frame(tabControl)
  tab05 = ttk.Frame(tabControl)
  tab06=  ttk.Frame(tabControl)
  tab07 = ttk.Frame(tabControl)
  tab08 = ttk.Frame(tabControl)
  tab09 =  ttk.Frame(tabControl)
  tab010=  ttk.Frame(tabControl)
  tabControl.add(tab01,image=invoices,compound = LEFT, text ='Miscellaneous',)
  tabControl.add(tab02,image=orders,compound = LEFT, text ='Company settings')
  tabControl.add(tab03,image=estimates,compound = LEFT, text ='Invoiced settings')
  tabControl.add(tab04,image=recurring,compound = LEFT, text ='Order settings')
  tabControl.add(tab05,image=purchase,compound = LEFT, text ='Estimate settings') 
  tabControl.add(tab06,image=expenses,compound = LEFT, text ='Administrator panel')
  tabControl.add(tab07,image=customer,compound = LEFT, text ='Advanced settings')
  tabControl.add(tab08,image=product,compound = LEFT, text ='Email templates')
  tabControl.add(tab09,image=reports,compound = LEFT, text ='Payments')
  tabControl.add(tab010,image=setting,compound = LEFT, text ='Purchase Order')
  tabControl.pack(expand = 1, fill ="both")
  
  ################### tab01 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  
  firsttab1=Frame(tab01, relief=GROOVE, bg="#f8f8f2")
  firsttab1.pack(side="top", fill=BOTH)
  
  firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
  firsttab.pack(side="top", fill=BOTH)
  
  messagelbframe=LabelFrame(firsttab,text="Menu and Window Color Style", height=60, width=180)
  messagelbframe.place(x=5, y=15)
  
  win_menu = StringVar()
  winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
  winstyle.place(x=22 ,y=40)
  winstyle['values'] = ('whidbey','windows XP','windows 7','windows 8','windows 10')
  winstyle.current(0)
  fbill = Label(firsttab,text="F-Billing Revolution 2022",font="arial 12 bold").place(x=220,y=20)
  
  dbhost=LabelFrame(firsttab,text="Database Server Hostname", height=60, width=415)
  dbhost.place(x=5, y=85)
  
  db = Label(firsttab, text="DESKTOP-2K")
  db.place(x=15,y=110)
  
  exc=LabelFrame(firsttab,text="Extra cost name", height=180, width=415)
  exc.place(x=5, y=155)
  
  
  
  def insert_valueexc():
    i = varexc.get()
    if i == "":
      pass
    else:
      entryexc.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into extra_cost_name(companyid,extra_cost_name) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in exctree.get_children():
          exctree.delete(record)
        sql = 'select * from extra_cost_name'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert(parent='', index='end', iid=countp, text='hello', values=(imn))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueexc(event):
    selected_item = exctree.selection()[0]
    temp = list(exctree.item(selected_item , 'values'))
    entryexc.delete(0, END)
    entryexc.insert(0, temp)
  
  def save_valueexc():
    i = entryexc.get()
    if i == "":
      pass
    else:
      selected0 = exctree.focus()
      valuz1= exctree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in exctree.get_children():
            exctree.delete(record)
        fbcursor.execute("select *  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert('', index='end', iid=countp, text='', values=(imn))
          countp += 1
    
    
  
  def del_valueexc():
    itemid = exctree.item(exctree.focus())["values"][0]
    sql = "delete from extra_cost_name where extra_cost_name = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    fbilldb.commit()
    exctree.delete(exctree.selection()[0])
      
      
  
    
    
    
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  exctree = ttk.Treeview(firsttab, columns=("1"),height=40,selectmode='browse', yscrollcommand=scrollbary.set,   xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=exctree.yview)
  scrollbary.place(x=394,y=200,height=125)
  scrollbarx.config(command=exctree.xview)
  scrollbarx.place(x=15,y=310, width=380)
  exctree.heading('1', text="Extra cost name",)
  # exctree.column('#0', stretch=NO, minwidth=0, width=0)
  exctree.column("#0",width=0,anchor='c', stretch=False)
  exctree.column('1',width=378,anchor='c')
  exctree.place(x=15,y=200,height=115,width=380)
  exctree.bind('<Double-Button-1>' , edit_valueexc)
  sql = 'select * from extra_cost_name'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
      print(i[2])
      immm = str(i[2])
      imn = str.replace(immm," ","_")
      exctree.insert(parent='', index='end', iid=countp, text='', values=(imn))
      countp += 1
  # new_value = StringVar()
  
  # def edit_window_box(val):
      
  #     edit_window = Toplevel(root)
  #     edit_window.title("Edit the value or cancel")
  #     edit_window.geometry("1000x250")
  #     label_edit = Label(edit_window , text='Enter value to edit or press cancel', 
  #     font = ("Times New Roman", 10)).grid(column=0,row=1,padx=0, pady = 2)
  #     #create edit box
  #     edit_box = Entry(edit_window)
  #     edit_box.insert(0,val)
  #     edit_box.grid(column=1,row=1,padx=0,pady=2)
  #     #auto select edit window 
  #     edit_window.focus()
      
  #     def value_assignment(event):
  #         printing = edit_box.get()
  #         new_value.set(printing)
  #         #only destroy will not update the value (perhaps event keeps running in background)
  #         #quit allows event to stop n update value in tree but does not close the window in single click 
  #         #rather on dbl click shuts down entire app 
  #         edit_window.quit()
  #         edit_window.destroy()
      
  #     edit_window.bind('<Return>', value_assignment )
  
  #     B1 = Button(edit_window, text="Okay")
  #     B1.bind('<Button-1>',value_assignment)
  #     B1.grid(column=0,row=10,padx=0, pady = 20)
      
  #     B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).grid(column=1,row=10,padx=10,   pady = 20)
  #     edit_window.mainloop()
      
  # #will explain
  # #variable to hold col value (col clicked)
  # shape1 = IntVar()
  # #tracks both col , row on mouse click
  # def tree_click_handler(event):
  #     cur_item = exctree.item(exctree.focus())
  #     col = exctree.identify_column(event.x)[1:]
  #     rowid = exctree.identify_row(event.y)[1:]
  #     #updates list
  #     shape1.set(col)
  #     try:
  #         x,y,w,h = exctree.bbox('I'+rowid,'#'+col)
  #     except:pass
  #     #tree.tag_configure("highlight", background="yellow")
  #     return(col)
      
  # #code linked to event    
  # exctree.bind('<ButtonRelease-1>', tree_click_handler)
  
  # def edit(event):
  #     try:
  #         selected_item = exctree.selection()[0]
  #         temp = list(exctree.item(selected_item , 'values'))
  #         tree_click_handler
  #         col_selected = int(shape1.get())-1
  #         edit_window_box(temp[col_selected])
  #         #do not run if edit window is open
  #         #use edit_window.mainloop() so value assign after window closes
  #         temp[col_selected] = new_value.get()
  #         exctree.item(selected_item, values= temp)
  #     except: pass
      
      
  # #binding allows to edit on screen double click
  # exctree.bind('<Double-Button-1>' , edit)
  varexc = StringVar()
  entryexc = Entry(firsttab,width=25,textvariable=varexc)
  entryexc.place(x=15,y=173)
  
  btexcadd = Button(firsttab,text="Add new line",command=insert_valueexc)
  btexcadd.place(x=175,y=171)
  
  btexcedit = Button(firsttab,text="Edit line   ",command=save_valueexc)
  btexcedit.place(x=260,y=171)
  btexcadd = Button(firsttab,text=" Delete line  ",command=del_valueexc)
  btexcadd.place(x=330,y=171)
  
  exc=LabelFrame(firsttab,text="Predefined text records for header and footer", height=180, width=415)
  exc.place(x=5, y=350)
  
  def insert_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      entrypre.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into header_and_footer(companyid,headerandfooter) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in pretree.get_children():
          pretree.delete(record)
        sql = 'select * from header_and_footer'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
          countp += 1
  # new_value = String
        
        
  
  def edit_valuepre(event):
    selected_item = pretree.selection()[0]
    temp = list(pretree.item(selected_item , 'values'))
    entrypre.delete(0, END)
    entrypre.insert(0, temp)
  
  def save_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      selected0 = pretree.focus()
      valuz1= pretree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in pretree.get_children():
            pretree.delete(record)
        fbcursor.execute("select *  from header_and_footer")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert('', index='end', iid=countp, text='', values=(pre))
          countp += 1
    
    
  
  def del_valuepre():
    itemid = pretree.item(pretree.focus())["values"][0]
    print(itemid)
    sql = "delete from header_and_footer where headerandfooter = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in pretree.get_children():
      pretree.delete(record)
    fbcursor.execute("select *  from header_and_footer")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      pret = str(i[2])
      pre = str.replace(pret," ","_")
      pretree.insert('', index='end', iid=countp, text='', values=(pre))
      countp += 1
    
      
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  pretree = ttk.Treeview(firsttab, columns=("1"),height=400,     selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=pretree.yview)
  scrollbary.place(x=395,y=400,height=115)
  scrollbarx.config(command=pretree.xview)
  scrollbarx.place(x=15,y=510, width=380)
  pretree.heading('1', text="header and footer",)
  pretree.column('#0', stretch=NO, minwidth=0, width=0)
  pretree.column('1', stretch=NO, width=378)
  pretree.place(x=15,y=400,height=115,width=380)
  pretree.bind('<Double-Button-1>' , edit_valuepre)
  sql = 'select * from header_and_footer'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
    pret = str(i[2])
    pre = str.replace(pret," ","_")
    pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
    countp += 1
  prestr = StringVar()
  entrypre = Entry(firsttab,width=25,textvariable=prestr)
  entrypre.place(x=15,y=370)
  btexcadd = Button(firsttab,text="Add new line",command=insert_valuepre)
  btexcadd.place(x=175,y=370)
  btpredit = Button(firsttab,text="Edit line   ",command=save_valuepre)
  btpredit.place(x=260,y=370)
  btexcadd = Button(firsttab,text=" Delete line   ",command=del_valuepre)
  btexcadd.place(x=330,y=370)
  
  ver = Label(firsttab,text="FREE version.Upgrade PRO version for all features and Ad free invoice")
  ver.place(x=480,y=15)
  
  
  chapass=LabelFrame(firsttab,text="Change Password", height=150, width=500)
  chapass.place(x=480, y=40)
  
  enterold = StringVar()
  lenold = Label(firsttab,text="Enter your old password")
  lenold.place(x=495,y=60)
  enold = Entry(firsttab,textvariable=enterold)
  enold.place(x=640,y=60)
  
  enternew = StringVar()
  ennew = Label(firsttab,text="New password")
  ennew.place(x=495,y=90)
  newpass = Entry(firsttab,textvariable=enternew)
  newpass.place(x=640,y=90)
  
  
  cnewpass = StringVar()
  cnp = Label(firsttab,text="Confirm new password")
  cnp.place(x=495,y=120)
  cnewp = Entry(firsttab,textvariable=cnewpass)
  cnewp.place(x=640,y=120)

  def change_pass():
    old_pass = enterold.get()
    new_pass = enternew.get()
    cnew_pass = cnewpass.get()
    usna = username1.get()
    print(usna)
    sql='SELECT * FROM users WHERE username=%s'
    val=(usna,)
    fbcursor.execute(sql,val)
    chpass = fbcursor.fetchone()
    print(chpass)
    if old_pass == "" or new_pass == "" or cnew_pass == "":
        messagebox.showerror('Password Error','Plz enter password')
    elif old_pass == chpass[4]:
      if new_pass == cnew_pass:
        sqll='UPDATE users SET password=%s,confirm_password=%s WHERE userID=%s'
        vall=(new_pass,cnew_pass,chpass[0])
        fbcursor.execute(sqll,vall,)
        fbilldb.commit()
        messagebox.showinfo('Updated','Password updated successfully')
      else:
        messagebox.showerror('Password Error','password is not match')
    else:
      messagebox.showerror('Password Error','Old Password is Incorrect')
  chabtn = Button(firsttab,text="Change password",command=change_pass)
  chabtn.place(x=840,y=150)
  
  termf=LabelFrame(firsttab,text="Terms of payment", height=150, width=500)
  termf.place(x=480, y=190)


  def insert_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      entrytop.delete(0, END)
      entryds.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into terms_of_payment(companyid,terms_of_payment,Date_shift) values(%s,%s,%s)'
        val = (companyid,first,second)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in termtree.get_children():
          termtree.delete(record)
        sql = 'select * from terms_of_payment'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueterm(event):
    itemid = termtree.item(termtree.focus())["values"][0]
    sql = "select * from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    editterm = fbcursor.fetchone()
    entrytop.delete(0, END)
    entryds.delete(0, END)
    entrytop.insert(0, editterm[2])
    entryds.insert(0, editterm[3])
  
  def save_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      itemid = termtree.item(termtree.focus())["values"][0]
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        pass
      else:
        sql = "select * from terms_of_payment where terms_of_payment=%s"
        val = (itemid,)
        fbcursor.execute(sql,val)
        payt = fbcursor.fetchone()
        sql2 = 'update terms_of_payment set terms_of_payment=%s,Date_shift=%s where terms_of_paymentID=%s'
        val2 = (first,second,payt[0])
        fbcursor.execute(sql2,val2)
        fbilldb.commit()
        entrytop.delete(0, END)
        entryds.delete(0, END)
        for record in termtree.get_children():
          termtree.delete(record)
        fbcursor.execute("select *  from terms_of_payment")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
    
    
  
  def del_valueterm():
    itemid = termtree.item(termtree.focus())["values"][0]
    print(itemid)
    sql = "delete from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in termtree.get_children():
        termtree.delete(record)
    fbcursor.execute("select *  from terms_of_payment")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  termtree = ttk.Treeview(firsttab, columns=("1","2"),height=400,selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=termtree.yview)
  scrollbary.place(x=870,y=228,height=100)
  scrollbarx.config(command=termtree.xview)
  scrollbarx.place(x=495,y=313, width=380)
  termtree.heading('1', text="Terms of payment",)
  termtree.heading('2', text="Date shift (days)",)
  termtree.column('#0', stretch=NO, minwidth=0, width=0)
  termtree.column('1', stretch=NO, minwidth=0, width=250)
  termtree.column('2', stretch=NO, minwidth=0, width=128)
  termtree.place(x=495,y=235,height=80,width=380)
  termtree.bind('<Double-Button-1>' , edit_valueterm)

  sql = 'select * from terms_of_payment'
  fbcursor.execute(sql)
  termt = fbcursor.fetchall()
  countp = 0
  for i in termt:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  entrytopstr = StringVar()
  entrytop = Entry(firsttab,width=25,textvariable=entrytopstr)
  entrytop.place(x=495,y=208)
  entrydsstr = StringVar()
  entryds = Entry(firsttab,textvariable=entrydsstr)
  entryds.place(x=670,y=208)
  bttermadd = Button(firsttab,text="Add new line",command=insert_valueterm)
  bttermadd.place(x=800,y=205)
  bttermedit = Button(firsttab,text="     Edit line  ",command=save_valueterm)
  bttermedit.place(x=890,y=205)
  bttermdel = Button(firsttab,text="  Delete line  ",command=del_valueterm)
  bttermdel.place(x=890,y=240)
  
  radem=LabelFrame(firsttab,text="Invoice/Oder/Estimate/P.order Email Attachment file type", height=60,   width=500)
  radem.place(x=480, y=340)
  radema = StringVar()
  radpdf = Radiobutton(firsttab,variable=radema,value="PDF",text='PDF')
  radpdf.place(x= 485, y= 360 )
  radhtml = Radiobutton(firsttab,variable=radema,value="HTML",text='HTML')
  radhtml.place(x= 660, y= 360 )
  if  not sectab:
    pass
  else:
    if sectab[22] == 'PDF':
      radpdf.select()
    elif sectab[22] == 'HTML':
      radhtml.select()
    else:
      pass
  
  checkb1 = IntVar()
  check1 = Checkbutton(firsttab,variable = checkb1, 
                        text="PDF attachment with Embedded Fonts (PDF file size will be larger,but readable on   all devices) ", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check1.place(x=480,y=400)
  if  not sectab:
    pass
  else:
    if sectab[23] == 1:
      check1.select()
    else:
      check1.deselect()
  
  checkb2 = IntVar()
  check2 = Checkbutton(firsttab,variable = checkb2, 
                        text="invoice numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check2.place(x=480,y=420)
  if  not sectab:
    pass
  else:
    if sectab[24] == 1:
      check2.select()
    else:
      check2.deselect()
  
  checkb3 = IntVar()
  check3 = Checkbutton(firsttab,variable = checkb3, 
                        text="Order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check3.place(x=480,y=440)
  if  not sectab:
    pass
  else:
    if sectab[25] == 1:
      check3.select()
    else:
      check3.deselect()
  
  checkb4 = IntVar()
  check4 = Checkbutton(firsttab,variable = checkb4, 
                        text="Estimate numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check4.place(x=480,y=460)
  if  not sectab:
    pass
  else:
    if sectab[26] == 1:
      check4.select()
    else:
      check4.deselect()
  
  checkb5 = IntVar()
  check5 = Checkbutton(firsttab,variable = checkb5, 
                        text="Purchsae order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  check5.place(x=480,y=480)
  if  not sectab:
    pass
  else:
    if sectab[27] == 1:
      check5.select()
    else:
      check5.deselect()
  
  checkb6 = IntVar()
  check6 = Checkbutton(firsttab,variable = checkb6, 
                        text="Confirmation before closing F-billing Revolution", 
                        onvalue =1 ,
                        offvalue = 0,
                      )
  
  check6.place(x=480,y=500)
  if  not sectab:
    pass
  else:
    if sectab[28] == 1:
      check6.select()
    else:
      check6.deselect()
  
  ################### tab02 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  print(sectab)
  
  
  secondtab1=Frame(tab02, relief=GROOVE, bg="#f8f8f2")
  secondtab1.pack(side="top", fill=BOTH)
  
  secondtab=Frame(secondtab1, bg="#f5f3f2", height=700)
  secondtab.pack(side="top", fill=BOTH)
  
  comdata=LabelFrame(secondtab,text="Company data", height=200, width=500)
  comdata.place(x=5, y=15)
  cname = Label(secondtab,text="Company name")
  cname.place(x=20, y =35)
  comname = StringVar()
  centry = Entry(secondtab,textvariable=comname)
  if  not sectab:
    pass
  else:
    centry.insert(0, sectab[1])
  centry.place(x=160,y=35,width=280)
  
  
  cadd = Label(secondtab,text="Company Address")
  cadd.place(x=20, y =65)
  caddent = scrolledtext.ScrolledText(secondtab)
  if  not sectab:
    pass
  else:
    caddent.insert('1.0', sectab[2])
  caddent.place(x=160,y=65,height=80,width=280)
  
  cemail = Label(secondtab,text="E-mail Address")
  cemail.place(x=20, y =160)
  comemail = StringVar()
  cemailentry = Entry(secondtab,textvariable=comemail)
  if  not sectab:
    pass
  else:
    cemailentry.insert(0, sectab[3])
  cemailentry.place(x=160,y=160,width=280)
  
  stl = Label(secondtab,text="sales Tax.Reg.No.")
  stl.place(x=20, y =185)
  comsalestax = StringVar()
  ste = Entry(secondtab,textvariable=comsalestax)
  if  not sectab:
    pass
  else:
    ste.insert(0, sectab[4])
  ste.place(x=160,y=185,width=280)
  
  
  curre=LabelFrame(secondtab,text="Currency", height=125, width=500)
  curre.place(x=5, y=220)
  currl = Label(secondtab,text="Currency")
  currl.place(x=20,y= 240)
  comcur = StringVar()
  currbox = ttk.Combobox(secondtab,width=10,textvariable=comcur)
  currbox['values'] =('ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD','BMD','BOB','BAM','BWP',  'BGN','BRL','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC',  'EUR','FKP','FJD','GHS','GIP','GTQ','GGP','GYD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IMP','ILS','JMD',  'JPY','JEP','KZT','KPW','KRW','KGS','LAK','LBP','LRD','MKD','MYR','MUR','MXN','MNT','MNT','MZN','NAD','NPR',  'ANG','NZD','NIO','NGN','NOK','OMR','PKR','PAB','PYG','PEN','PHP','PLN','QAR','RON','RUB','SHP','SAR','RSD',  'SCR','SGD','SBD','SOS','KRW','ZAR','LKR','SEK','CHF','SRD','SYP','TWD','THB','TTD','TRY','TVD','UAH','AED',  'GBP','USD','UYU','UZS','VEF','VND','YER','ZWD',)
  if  not sectab:
    pass
  elif sectab[5]:
    currbox.insert(0, sectab[5])
  currbox.place(x=80,y=240)
  
  def signpl(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
  
  
  currsignl = Label(secondtab,text="Currency sign")
  currsignl.place(x=180,y=240)
  comcursign = StringVar()
  currsignbox = ttk.Combobox(secondtab,width=10,textvariable=comcursign)
  currsignbox.bind("<<ComboboxSelected>>", signpl)
  currsignbox["values"] = ('Lek','؋','$','ƒ','$','₼','$','$','Br','BZ$','$','$b','KM','P','лв','R$','$','៛',  '$','$','$','¥','$','₡','kn','₱','Kč','kr','RD$','$','£','$','€','£','$','¢','£','Q','£','$','L','$','Ft',  'kr','₹','Rp','﷼','£','₪','J$','¥','£','лв','₩','₩','₭','£','$','ден','RM','₨','$','₮',' د.إ','MT','$','₨',  'ƒ','$','C$','₦','kr','﷼','₨','B/.','Gs','S/.','₱','zł','﷼','lei','₽','£','﷼','Дин.','₨','S','₩','R','₨',  'kr','CHF','£','NT$','฿','TT$','₺','$','₴','د.إ','$U','лв','Bs','₫','﷼','Z$')
  if  not sectab:
    pass
  elif sectab[6]:
    currsignbox.insert(0, sectab[6])
  currsignbox.place(x=265,y=240)
  
  cspl = Label(secondtab,text="Currency sign placement")
  cspl.place(x=20,y=270)
  
  def amountsignspace(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
    
      
      
  comcursignpla = StringVar()
  cspe = ttk.Combobox(secondtab,width=24,textvariable=comcursignpla,)
  cspe.bind("<<ComboboxSelected>>", amountsignspace)
  cspe["values"] = ("before amount","after amount",'before amount with space',"after amount with space")
  if  not sectab:
    pass
  elif sectab[7]:
    cspe.insert(0, sectab[7])
  cspe.place(x=180,y=270)
  
  def decpl(event):
    dec = comdecsep.get()
    ex = comex.get()
    if dec == ",":
      var = str.replace(ex,".",",")
      exbox.delete(0, END)
      exbox.insert(0, var)
    elif dec == ".":
      var1 = str.replace(ex,",",".")
      exbox.delete(0, END)
      exbox.insert(0, var1)
  dsl = Label(secondtab,text="Decimal separator")
  dsl.place(x=20,y=300)
  comdecsep = StringVar()
  currbox = ttk.Combobox(secondtab,width=5,textvariable=comdecsep)
  currbox.bind("<<ComboboxSelected>>",decpl)
  currbox['values'] = ('.',',')
  if  not sectab:
    pass
  elif sectab[8]:
    currbox.insert(0, sectab[8])
  currbox.place(x=130,y=300)
  
  exl = Label(secondtab,text="Example")
  exl.place(x=185,y=300)
  comex = StringVar()
  exbox = Entry(secondtab,width=15,textvariable=comex)
  if  not sectab:
    exbox.insert(0, 84367.26)
  elif sectab[9]:
    exbox.insert(0, sectab[9])
  exbox.place(x=245,y=300)
  
  btred = Button(secondtab,text="Restore Default")
  btred.place(x=400,y=270)
  btsc = Button(secondtab,text="SET CURRENCY")
  btsc.place(x=400,y=300)
  
  datef=LabelFrame(secondtab,text="Date format", height=60, width=500)
  datef.place(x=5, y=355)
  
  def daffun(event):
    dafget = daf.get()
    if dafget == "mm-dd-yyyy":
      exd._set_text(exd._date.strftime('%m-%d-%Y'))
    elif dafget == "dd-mm-yyyy":
      exd._set_text(exd._date.strftime('%d-%m-%Y'))
    elif dafget == "yyy.mm.dd":
      exd._set_text(exd._date.strftime('%Y.%m.%d'))
    elif dafget == "mm/dd/yyyy":
      exd._set_text(exd._date.strftime('%m/%d/%Y'))
    elif dafget == "dd/mm/yyy":
      exd._set_text(exd._date.strftime('%d/%m/%Y'))
    elif dafget == "dd.mm.yyyy":
      exd._set_text(exd._date.strftime('%d.%m.%Y'))
    elif dafget == "yyyy/mm/dd":
      exd._set_text(exd._date.strftime('%Y/%m/%d'))
    
  
  comdaf = StringVar()
  daf = ttk.Combobox(secondtab,textvariable=comdaf)
  daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyy.mm.dd','mm/dd/yyyy','dd/mm/yyy','dd.mm.yyyy','yyyy/  mm/dd')
  daf.bind("<<ComboboxSelected>>",daffun)
  if not sectab:
    pass
  elif sectab[10]:
    daf.insert(0, sectab[10])
  daf.place(x=60,y=380)
  
  
  exd = DateEntry(secondtab,)
  exd.place(x=280,y=380)
  if  not sectab:
    pass
  elif sectab[11]:
    exd.delete(0, END)
    exd.insert(0, sectab[11])
  
  tnr=LabelFrame(secondtab,text="Tax name and rate", height=200, width=500)
  tnr.place(x=560, y=15)
  
  stt=LabelFrame(secondtab,text="Select tax type", height=120, width=180)
  stt.place(x=580, y=30)
  def rtax1():
    ch = radtax.get()
    if ch == 1:
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 2:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 3:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    
  radtax = IntVar()
  rdnotax = Radiobutton(secondtab,text="Do not use TAX",value="1",variable=radtax,command=rtax1)
  rdnotax.place(x=590,y=50)
  
  
  rdtax1 = Radiobutton(secondtab,text="1 level of Tax",value="2",variable=radtax,command=rtax1)
  rdtax1.place(x=590,y=80)
  ptax01 = IntVar()
  tax1namel = Label(secondtab,text="Tax1 name")
  
  
  tax1namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[15]:
    tax1namee.insert(0, sectab[15])
  tax1namee.place(x=60,y=380)
  
  
  tax1ratel = Label(secondtab,text="Tax1 rate")
  
  
  tax1ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[16]:
    tax1ratee.insert(0, sectab[16])
  
  comptax1 = BooleanVar()
  ptax1 = Checkbutton(secondtab,text="Print TAX1" ,onvalue =1 ,offvalue = 0,variable=comptax1)
  if  not sectab:
    pass
  elif sectab[17] == 1:
    ptax1.select()
  else:
    ptax1.deselect()
  
  rdtax2 = Radiobutton(secondtab,text="2 level of Tax",value="3",variable=radtax,command=rtax1)
  rdtax2.place(x=590,y=110)
  
  
  tax2namel = Label(secondtab,text="Tax2 name")
  
  
  tax2namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[18]:
    tax2namee.insert(0, sectab[18])
  
  tax2ratel = Label(secondtab,text="Tax2 rate")
  
  tax2ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[19]:
    tax2ratee.insert(0, sectab[19])
  
  comptax2 = BooleanVar()
  ptax2 = Checkbutton(secondtab,text="Print TAX2" ,onvalue =1 ,offvalue = 0,variable=comptax2)
  if  not sectab:
    pass
  else:
    if sectab[20] == 1:
      ptax2.select()
    else:
      ptax2.deselect()
  
  if  not sectab:
    pass
  else:
    if sectab[12] == "1":
      rdnotax.select()
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif sectab[12] == "2":
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
      rdtax1.select()
    elif sectab[12] == "3":
      rdtax2.select()
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    else:
      pass
  
  
  comlo=LabelFrame(secondtab,text="Comapny Logo", height=260, width=320)
  comlo.place(x=560, y=240)
  
  def upload_filelogo():
    global imglogo,filename
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
    image = Image.open(filename)
    resize_image = image.resize((280, 160))
    imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    btlogo.place(x=580,y=280)
  
  try:
    image = Image.open("images/"+sectab[13])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogo = Button(secondtab,width=280,height=160,image=image)
    btlogo.place(x=580,y=280)
    btlogo.photo = image
  except:
    pass
  
    
  btloadim = Button(secondtab,text="Load logo image",command=upload_filelogo)
  btloadim.place(x=580,y=460)
  
  compimg = BooleanVar()
  primage = Checkbutton(secondtab,text="Print logo image",variable = compimg,onvalue =1 ,offvalue = 0)
  primage.place(x=740,y=460)
  
  ################### tab06 ###################################
  
  def user():
    display = displaystart.get()
    user_name = usernae.get()
    password = userpase.get()
    conformpassword = usercpase.get()
   
    create_inv = creinvbol.get()
    delete_inv = delinvbol.get()
    void_inv = voinvbol.get()
    mark_inv_as_paid = markinvbol.get()
    
    create_ord = creordbol.get()
    delete_ord = delordbol.get()
    turn_inv_ord = turninvbol.get()
    smsnofi = smsinvbol.get()
    
    create_est = creestimatebol.get()
    delete_est = delestimatebol.get()
    turn_est = turnestiinvbol.get()
  
    create_exp = creexpensebol.get()
    delete_exp = delexpensebol.get()
    rebill_exp = rebillexpebol.get()
    
    create_cus = crecusbol.get()
    delete_cus = delcusbol.get()
    imp_cus = impcusbol.get()
  
    create_pros = creprosbol.get()
    delete_pros = delprosbol.get()
    import_pros = impprosbol.get()
  
    runrep = runrepbol.get()
    gen_rec = genrecinvbol.get()
  
    create_pur = crepurbol.get()
    delete_pur = delpurbol.get()
  
    modify_inv = modifyinvbol.get()
    modify_ord = modifyordbol.get()
    modify_est = modifyestibol.get()
  
    if user_name=="" or password=="":
      messagebox.showerror('',"Please complete the form")
    else:
      sql='SELECT * FROM users WHERE username=%s'# selecting entire table from db,taking username , nd check   the existance
      val=(user_name,)
      fbcursor.execute(sql,val)
      if fbcursor.fetchone()is not None:
        sql='SELECT * FROM users WHERE username=%s'
        val=(user_name,)
        fbcursor.execute(sql,val)
        whuser = fbcursor.fetchone()
        print(whuser[0])
        if password == conformpassword:
        # messagebox.showerror('Warming','User name already exist!!')
          sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s,create_invoice=%s,delete_invoice=%s,void_invoice=%s,mark_invoice_as_paid=%s,create_order=%s,delete_order=%s,turn_order_into_invoice=%s,send_sms_nofitication=%s,create_estimate=%s,delete_estimate=%s,turn_oestimate_into_invoice=%s,create_expense=%s,delete_expense=%s,rebill_exprense=%s,create_customer=%s,delete_customer=%s,import_customer=%s,	create_product_service=%s,delete_product_service=%s,import_product_service=%s,run_reports=%s,generate_recurring_invoice=%s,create_purchase_order=%s,delete_purchase_order=%s,modify_invoice_settings=%s,modify_order_settings=%s,modify_estimate_settings=%s WHERE userID=%s'
          vall=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est,whuser[0])
          fbcursor.execute(sqll,vall)
          fbilldb.commit()
        else:
          messagebox.showerror('Warming','Password not match!!')
      else:
        if password == conformpassword:
          sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
          val=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est)
          fbcursor.execute(sql,val)
          fbilldb.commit()
          for record in uactree.get_children():
            uactree.delete(record)
          sql = "select * from users"
          fbcursor.execute(sql)
          sixuactree = fbcursor.fetchall()
          coutset = 0
          for i in sixuactree:
           uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
           coutset += 1
        else:
          messagebox.showerror('Warming','Password not match!!')
        

   
    
  
  
  
  
    
  
    
  sixtab1=Frame(tab06, relief=GROOVE, bg="#f8f8f2")
  sixtab1.pack(side="top", fill=BOTH)
  
  sixtab=Frame(sixtab1, bg="#f5f3f2", height=700)
  sixtab.pack(side="top", fill=BOTH)
  
  displaystart = BooleanVar()
  displaylocsc = Checkbutton(sixtab,text="Display Login screen startup",onvalue =1 ,offvalue = 0,  variable=displaystart)
  displaylocsc.place(x=20,y=30)
  
  userac=LabelFrame(sixtab,text="User Acounts", height=400, width=260)
  userac.place(x=20, y=55)
  
  
  selper = Label(sixtab,text="Select username to modify permissions")
  selper.place(x=30,y=75)
  
  def focususer(event):
    itemid = uactree.item(uactree.focus())["values"][0]
    sql = "select * from users where username = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    sixtabdataback = fbcursor.fetchone()
    print(sixtabdataback)
    usernae.delete(0,END)
    usernae.insert(0,itemid)
    if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
    else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    if not sixtabdataback:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      creinv.deselect()
      delinv.deselect()
      voinv.deselect()
      markinv.deselect()
      creord.deselect()
      delord.deselect()
      turninv.deselect()
      smsinv.deselect()
      creestimate.deselect()
      delestimate.deselect()
      turnestiinv.deselect()
      creexpense.deselect()
      delexpense.deselect()
      rebillexpe.deselect()
      crecus.deselect()
      delcus.deselect()
      impcus.deselect()
      crepros.deselect()
      delpros.deselect()
      imppros.deselect()
      runrep.deselect()
      genrecinv.deselect()
      crepur.deselect()
      delpur.deselect()
      modifyinv.deselect()
      modifyord.deselect()
      modifyesti.deselect()
      if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
      else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      userpase.insert(0, sixtabdataback[4])
      usercpase.insert(0, sixtabdataback[5])
      if sixtabdataback[6] == 1:
        creinv.select()
      else:
        creinv.deselect()
      if sixtabdataback[7] == 1:
        delinv.select()
      else:
        delinv.deselect()
      if sixtabdataback[8] == 1:
        voinv.select()
      else:
        voinv.deselect()
      if sixtabdataback[9] == 1:
        markinv.select()
      else:
        markinv.deselect()
      if sixtabdataback[10] == 1:
        creord.select()
      else:
        creord.deselect()
      if sixtabdataback[11] == 1:
        delord.select()
      else:
        delord.deselect()
      if sixtabdataback[12] == 1:
        turninv.select()
      else:
        turninv.deselect()
      if sixtabdataback[13] == 1:
        smsinv.select()
      else:
        smsinv.deselect()
      if sixtabdataback[14] == 1:
        creestimate.select()
      else:
        creestimate.deselect()
      if sixtabdataback[15] == 1:
        delestimate.select()
      else:
        delestimate.deselect()
      if sixtabdataback[16] == 1:
        turnestiinv.select()
      else:
        turnestiinv.deselect()
      if sixtabdataback[17] == 1:
        creexpense.select()
      else:
        creexpense.deselect()
      if sixtabdataback[18] == 1:
        delexpense.select()
      else:
        delexpense.deselect()
      if sixtabdataback[19] == 1:
        rebillexpe.select()
      else:
        rebillexpe.deselect()
      if sixtabdataback[20] == 1:
        crecus.select()
      else:
        crecus.deselect()
      if sixtabdataback[21] == 1:
        delcus.select()
      else:
        delcus.deselect()
      if sixtabdataback[22] == 1:
        impcus.select()
      else:
        impcus.deselect()
      if sixtabdataback[23] == 1:
        crepros.select()
      else:
        crepros.deselect()
      if sixtabdataback[24] == 1:
        delpros.select()
      else:
        delpros.deselect()
      if sixtabdataback[25] == 1:
        imppros.select()
      else:
        imppros.deselect()
      if sixtabdataback[26] == 1:
        runrep.select()
      else:
        runrep.deselect()
      if sixtabdataback[27] == 1:
        genrecinv.select()
      else:
        genrecinv.deselect()
      if sixtabdataback[28] == 1:
        crepur.select()
      else:
        crepur.deselect()
      if sixtabdataback[29] == 1:
        delpur.select()
      else:
        delpur.deselect()
      if sixtabdataback[30] == 1:
        modifyinv.select()
      else:
        modifyinv.deselect()
      if sixtabdataback[31] == 1:
        modifyord.select()
      else:
        modifyord.deselect()
      if sixtabdataback[32] == 1:
        modifyesti.select()
      else:
        modifyesti.deselect()
         
  
  scrollbarx = Scrollbar(sixtab, orient=HORIZONTAL)
  scrollbary = Scrollbar(sixtab, orient=VERTICAL)
  uactree = ttk.Treeview(sixtab, columns=("1"),height=400,selectmode="extended", yscrollcommand=scrollbary.  set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=uactree.yview)
  scrollbary.place(x=245,y=100,height=300)
  uactree.heading('1', text="Username",)
  uactree.column('#0', stretch=NO, minwidth=0, width=0)
  uactree.column('1', stretch=NO, minwidth=0, width=218)
  uactree.place(x=30,y=100,height=300,width=220)
  uactree.bind('<Double-Button-1>' , focususer)
  sql = "select * from users"
  fbcursor.execute(sql)
  sixuactree = fbcursor.fetchall()
  coutset = 0
  if not sixuactree:
    uactree.insert('', index='end', text='hello', values=("adminstator"))
  else:
    for i in sixuactree:
      uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
      coutset += 1
  
  def adduser():
    uactree.insert('', index='end', text='hello', values=("Rename User"))
  
  btadd = Button(sixtab,text="Add new User",command=adduser)
  btadd.place(x=30,y=415)
  
  def users():
    itemid = uactree.item(uactree.focus())["values"][0]
    if itemid == "adminstator":
      messagebox.showerror('F-Billing Revolution', 'Cannot delete adminstator user.')
    else:
      delusermess = messagebox.askyesno("Delete user", "Are you sure to delete this user?")
      if delusermess == True:
        sql = "delete from users where username = %s"
        val = (itemid, )
        fbcursor.execute(sql, val)
        fbilldb.commit()
        for record in uactree.get_children():
          uactree.delete(record)
        sql = "select * from users"
        fbcursor.execute(sql)
        sixuactree = fbcursor.fetchall()
        coutset = 0
        for i in sixuactree:
          uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
          coutset += 1
      else:
        pass
        
  
  btdus = Button(sixtab,text="Delete User",command=users)
  btdus.place(x=180,y=415)
  
  userpro=LabelFrame(sixtab,text="User Profile", height=400, width=750)
  userpro.place(x=300, y=55)
  
  
  userna = Label(sixtab,text="Username")
  userna.place(x=340,y=90)
  usernae = Entry(sixtab,)
  usernae.place(x=460,y=90)
  
  userpas = Label(sixtab,text="Password")
  userpas.place(x=340,y=120)
  userpase = Entry(sixtab,)
  userpase.place(x=460,y=120)
  
  usercpas = Label(sixtab,text="Confirm Password")
  usercpas.place(x=340,y=150)
  usercpase = Entry(sixtab,)
  usercpase.place(x=460,y=150)
  
  saveuserprofile = Button(sixtab,text="save user profile",command=user)
  saveuserprofile.place(x=650,y=120)
  
  creinvbol = BooleanVar()
  creinv = Checkbutton(sixtab,text="Create invoice",onvalue= 1 ,offvalue= 0,variable=creinvbol)
  creinv.place(x=340,y=200)
  delinvbol = BooleanVar()
  delinv = Checkbutton(sixtab,text="Delete invoice",onvalue= 1 ,offvalue= 0,variable=delinvbol)
  delinv.place(x=340,y=225)
  voinvbol = BooleanVar()
  voinv = Checkbutton(sixtab,text="Void invoice",onvalue= 1 ,offvalue= 0,variable=voinvbol)
  voinv.place(x=340,y=250)
  markinvbol = BooleanVar()
  markinv = Checkbutton(sixtab,text="Mark invoice as Paid",onvalue= 1 ,offvalue= 0,variable=markinvbol)
  markinv.place(x=340,y=275)
  
  creordbol = BooleanVar()
  creord = Checkbutton(sixtab,text="Create Order",onvalue= 1 ,offvalue= 0,variable=creordbol)
  creord.place(x=500,y=200)
  delordbol = BooleanVar()
  delord = Checkbutton(sixtab,text="Delete Order",onvalue= 1 ,offvalue= 0,variable=delordbol)
  delord.place(x=500,y=225)
  turninvbol = BooleanVar()
  turninv = Checkbutton(sixtab,text="Turn order into invoice",onvalue= 1 ,offvalue= 0,variable=turninvbol)
  turninv.place(x=500,y=250)
  smsinvbol = BooleanVar()
  smsinv = Checkbutton(sixtab,text="Send sms nofitication",onvalue= 1 ,offvalue= 0,variable=smsinvbol)
  smsinv.place(x=500,y=275)
  
  creestimatebol = BooleanVar()
  creestimate = Checkbutton(sixtab,text="Create estimate",onvalue= 1 ,offvalue= 0,variable=creestimatebol)
  creestimate.place(x=680,y=200)
  delestimatebol = BooleanVar()
  delestimate = Checkbutton(sixtab,text="Delete estimate",onvalue= 1 ,offvalue= 0,variable=delestimatebol)
  delestimate.place(x=680,y=225)
  turnestiinvbol = BooleanVar()
  turnestiinv = Checkbutton(sixtab,text="Turn estimates into invoice",onvalue= 1 ,offvalue= 0,  variable=turnestiinvbol)
  turnestiinv.place(x=680,y=250)
  
  creexpensebol = BooleanVar()
  creexpense = Checkbutton(sixtab,text="Create expenses",onvalue= 1 ,offvalue= 0,variable=creexpensebol)
  creexpense.place(x=880,y=200)
  delexpensebol = BooleanVar()
  delexpense = Checkbutton(sixtab,text="Delete expenses",onvalue= 1 ,offvalue= 0,variable=delexpensebol)
  delexpense.place(x=880,y=225)
  rebillexpebol = BooleanVar()
  rebillexpe = Checkbutton(sixtab,text="Rebill expenses",onvalue= 1 ,offvalue= 0,variable=rebillexpebol)
  rebillexpe.place(x=880,y=250)
  
  crecusbol = BooleanVar()
  crecus = Checkbutton(sixtab,text="Create customer",onvalue= 1 ,offvalue= 0,variable=crecusbol)
  crecus.place(x=340,y=320)
  delcusbol = BooleanVar()
  delcus = Checkbutton(sixtab,text="Delete customer",onvalue= 1 ,offvalue= 0,variable=delcusbol)
  delcus.place(x=340,y=340)
  impcusbol = BooleanVar()
  impcus = Checkbutton(sixtab,text="Import customer",onvalue= 1 ,offvalue= 0,variable=impcusbol)
  impcus.place(x=340,y=360)
  
  creprosbol = BooleanVar()
  crepros = Checkbutton(sixtab,text="Create product\services",onvalue= 1 ,offvalue= 0,variable=creprosbol)
  crepros.place(x=500,y=320)
  delprosbol = BooleanVar()
  delpros = Checkbutton(sixtab,text="Delete product\services",onvalue= 1 ,offvalue= 0,variable=delprosbol)
  delpros.place(x=500,y=340)
  impprosbol = BooleanVar()
  imppros = Checkbutton(sixtab,text="Import product\services",onvalue= 1 ,offvalue= 0,variable=impprosbol)
  imppros.place(x=500,y=360)
  
  runrepbol = BooleanVar()
  runrep = Checkbutton(sixtab,text="Run reports",onvalue= 1 ,offvalue= 0,variable=runrepbol)
  runrep.place(x=680,y=320)
  genrecinvbol = BooleanVar()
  genrecinv = Checkbutton(sixtab,text="Generate recurring invoices",onvalue= 1 ,offvalue= 0,  variable=genrecinvbol)
  genrecinv.place(x=680,y=340)
  
  crepurbol = BooleanVar()
  crepur = Checkbutton(sixtab,text="Create Purchase order",onvalue =1 ,offvalue = 0,variable=crepurbol)
  crepur.place(x=880,y=320)
  delpurbol = BooleanVar()
  delpur = Checkbutton(sixtab,text="Delete Purchase order",onvalue =1 ,offvalue = 0,variable=delpurbol)
  delpur.place(x=880,y=340)
  
  undersetlab = Label(sixtab,text="Under Settings menu tab")
  undersetlab.place(x=340,y=400)
  
  modifyinvbol = BooleanVar()
  modifyinv = Checkbutton(sixtab,text="Modify invoice settings",onvalue =1 ,offvalue = 0,variable=modifyinvbol)
  modifyinv.place(x=340,y=425)
  
  modifyordbol = BooleanVar()
  modifyord = Checkbutton(sixtab,text="Modify order settings",onvalue =1 ,offvalue = 0,variable=modifyordbol)
  modifyord.place(x=500,y=425)
  
  modifyestibol = BooleanVar()
  modifyesti = Checkbutton(sixtab,text="Modify estimate settings",onvalue =1 ,offvalue = 0,  variable=modifyestibol)
  modifyesti.place(x=680,y=425)

################### tab05 ###################################
  fifthtab1=Frame(tab05, relief=GROOVE, bg="#f8f8f2")
  fifthtab1.pack(side="top", fill=BOTH)

  fifthtab=Frame(fifthtab1, bg="#f5f3f2", height=700)
  fifthtab.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  estdata = fbcursor.fetchone()
  print(estdata)



  ver = Label(fifthtab,text="Estimate# prefix")
  ver.place(x=5,y=40)

  est_str = StringVar() 
  est_entry = Entry(fifthtab, textvariable=est_str)
  est_entry.place(x=100,y=40)
  if not estdata:
    est_str.set('EST')
  else:
    est_entry.insert(0, estdata[29])

  ver = Label(fifthtab,text="Starting estimate number")
  ver.place(x=25,y=80)

  def callback(input):
      
    if input.isdigit():
        print(input)
        return True
                          
    elif input is "":
        print(input)
        return True
  
    else:
        print(input)
        return False

  spin1 = Spinbox(fifthtab,from_=0,to=1000000,width=15)
  reg = fifthtab.register(callback)
  
  spin1.config(validate ="key", 
         validatecommand =(reg, '%S'))
  if not estdata:
    pass
  else:
    spin1.delete(0, END)
    spin1.insert(0,estdata[38])
  spin1.place(x=50,y=100)

  ver = Label(fifthtab,text="Header box background color")
  ver.place(x=5,y=140)

  win_menu1 = StringVar()
  winstyle1 = ttk.Combobox(fifthtab,textvariable=win_menu1)
  #est_win1 = win_menu1.get()
  winstyle1['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not estdata:
    winstyle1.current(0)
  else:
    winstyle1.insert(0, estdata[30])
  winstyle1.place(x=6 ,y=160)
  #winstyle1.current(0)

  ver = Label(fifthtab,text="Customize Estimate text labels")
  ver.place(x=5,y=190)
  
  est_str1 = StringVar() 
  est_lbx1 = Entry(fifthtab, width=30,textvariable=est_str1)
  # est_str1.set('Estimate')
  if not estdata:
    est_str1.set('Estimate')
  else:
    est_lbx1.insert(0, estdata[31])
  est_lbx1.place(x=5,y=220)
  
  est_str2 = StringVar() 
  est_lbx2 = Entry(fifthtab, width=30,textvariable=est_str2)
  if not estdata:
    est_str2.set('Estimate#')
  else:
    est_lbx2.insert(0,estdata[33])
  est_lbx2.place(x=5,y=240)
  
  
  est_str3 = StringVar() 
  est_lbx3 = Entry(fifthtab,width=30,textvariable=est_str3)
  if not estdata:
    est_str3.set('Estimate date')
  else:
    est_lbx3.insert(0, estdata[34])
  est_lbx3.place(x=5,y=260) 

  est_str4 = StringVar() 
  est_lbx4 = Entry(fifthtab,width=30,textvariable=est_str4)
  if not estdata:
    est_str4.set('Due date')
  else:
    est_lbx4.insert(0, estdata[35])
  est_lbx4.place(x=5,y=280)

  est_str5 = StringVar() 
  est_lbx5 = Entry(fifthtab,width=30,textvariable=est_str5)
  if not estdata:
    est_str5.set('Estimate to')
  else:
    est_lbx5.insert(0, estdata[36])
  est_lbx5.place(x=5,y=300)

  est_str6 = StringVar() 
  est_lbx6 = Entry(fifthtab, width=30,textvariable=est_str6)
  if not estdata:
    est_str6.set('Estimate total')
  else:
    est_lbx6.insert(0, estdata[37])
  est_lbx6.place(x=5,y=320)


  ver = Label(fifthtab,text="Default Estimate template(example,click on preview for mouse scrolling)")
  ver.place(x=248,y=55 )

  ver = Label(fifthtab,text="Default Estimate template")
  ver.place(x=619,y=40)



  messagelbframe=LabelFrame(fifthtab,text="Predefined terms and conditions text for estimates", height=70, width=980)
  messagelbframe.place(x=248, y=396)

  
  # est_str7 = StringVar() 
  # entry1=Entry(fifthtab, width=155,textvariable=est_str7)
  # if not estdata:
  #   pass
  # else:
  #   entry1.insert(0, estdata[39])
  # entry1.place(x=260, y=415, height=36)
  
  est_str7 = scrolledtext.ScrolledText(fifthtab)
  if  not estdata:
    pass
  else:
    est_str7.insert('1.0', estdata[39])
  est_str7.place(x=260,y=415,height=38,width=950)


  def restore_defaulttt1():
        est_lbx1.delete(0, 'end')
        est_lbx1.insert(0, 'Estimate')
        est_lbx2.delete(0, 'end')
        est_lbx2.insert(0,'Estimate#')
        est_lbx3.delete(0, 'end')
        est_lbx3.insert(0, 'Estimate date')
        est_lbx4.delete(0, 'end')
        est_lbx4.insert(0, 'Due date')
        est_lbx5.delete(0, 'end')
        est_lbx5.insert(0, 'Estimate to')
        est_lbx6.delete(0, 'end')
        est_lbx6.insert(0, 'Estimate total')

  bttermadd_01 = Button(fifthtab,text="Restore defaults", command=restore_defaulttt1)
  bttermadd_01.place(x=32,y=430)


#------------Professional 1 (logo on left side)-------------
  def maindropmenu(event):
      menuvar=win_menu2.get()
      print(menuvar,"hello")
      sql = "select * from company"
      fbcursor.execute(sql)
      estdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
          
        canvas.config(width=953,height=300)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
          
        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
        canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        else:
          pass
        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)

        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
          

#----------------Professional 2 (logo on right side)------------------
      elif menuvar == 'Professional 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
      
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(215, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
        #T_address_window = canvas.create_window(175, 80, anchor="nw", window=T_address)

        canvas.create_text(215, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
#----------------Simplified 1 (logo on left side)------------------ 
      elif menuvar == 'Simplified 1 (logo on left side)':
        print('hello')
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        #canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

        canvas.create_text(708, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

      
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Simplified 2 (logo on right side)------------------ 
      elif menuvar == 'Simplified 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)

        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)

        canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

          
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Business Classic------------------ 
      elif menuvar == 'Business Classic':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
          
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 70, 800, 70, fill='orange')
        
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  

        canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(485, 220, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

        canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

        canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

        canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=200)
        tree.heading("# 1", text="Product/Service")
        tree.column("# 2", anchor=E, stretch=NO, width=250)
        tree.heading("# 2", text="Description")
        tree.column("# 3", anchor=E, stretch=NO, width=90)
        tree.heading("# 3", text="Unit Price")
        tree.column("# 4", anchor=E, stretch=NO, width=80)
        tree.heading("# 4", text="Quantity")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
      
        window = canvas.create_window(120, 255, anchor="nw", window=tree)

        canvas.create_line(120, 295, 820, 295 )
        canvas.create_line(120, 255, 120, 295 )
        canvas.create_line(320, 255, 320, 295 )
        canvas.create_line(570, 255, 570, 295 )
        canvas.create_line(660, 255, 660, 295 )
        canvas.create_line(740, 255, 740, 295 )
        canvas.create_line(820, 255, 820, 445 )
        canvas.create_line(570, 320, 820, 320 )
        canvas.create_line(570, 345, 820, 345 )
        canvas.create_line(570, 370, 820, 370 )
        canvas.create_line(570, 395, 820, 395 )
        canvas.create_line(570, 420, 820, 420 )
        canvas.create_line(570, 445, 820, 445 )
      
        canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_line(150, 470, 800, 470, fill='orange')
        canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608, fill='orange')
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        pass

  win_menu2 = StringVar()
  winstyle2 = ttk.Combobox(fifthtab,textvariable=win_menu2)
  winstyle2.bind("<<ComboboxSelected>>", maindropmenu)
  winstyle2["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not estdata:
    winstyle2.current(0)
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  
    #canvas.create_image(120,0, anchor=NW, image=est_logo)  
    canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
      
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    # T_address = Text(canvas, height=5, width=20 , font=('Helvetica 10'))
    # T_address.insert(END, estdata[2])
    # T_address_window = canvas.create_window(645, 80, anchor="nw", window=T_address)
    canvas.create_text(700, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    # T = Text(canvas, height=3, width=105, font=('Helvetica 10'))
    # T.insert(END, estdata[39])
    # T_window = canvas.create_window(105, 612, anchor="nw", window=T)


    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 
  elif estdata[32] == 'Professional 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
    canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)

    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Professional 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(225, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(225, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

    canvas.create_text(708, 170, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)

    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Business Classic':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 70, 800, 70, fill='orange')
    
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  

    canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(480, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        
    canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

    canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

    canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=200)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=250)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=90)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=80)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 255, anchor="nw", window=tree)

    canvas.create_line(120, 295, 820, 295 )
    canvas.create_line(120, 255, 120, 295 )
    canvas.create_line(320, 255, 320, 295 )
    canvas.create_line(570, 255, 570, 295 )
    canvas.create_line(660, 255, 660, 295 )
    canvas.create_line(740, 255, 740, 295 )
    canvas.create_line(820, 255, 820, 445 )
    canvas.create_line(570, 320, 820, 320 )
    canvas.create_line(570, 345, 820, 345 )
    canvas.create_line(570, 370, 820, 370 )
    canvas.create_line(570, 395, 820, 395 )
    canvas.create_line(570, 420, 820, 420 )
    canvas.create_line(570, 445, 820, 445 )
      
    canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
    canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
    canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
    canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(150, 470, 800, 470, fill='orange')
    canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608, fill='orange')
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  winstyle2.place(x=770 ,y=40, width=220)
  #winstyle2.current(0)



################### tab07 ###################################
  seventhtab1=Frame(tab07, relief=GROOVE, bg="#f8f8f2")
  seventhtab1.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  advdata = fbcursor.fetchone()
  #print(estdata)


  seventhtab=Frame(seventhtab1, bg="#f5f3f2", height=700)
  seventhtab.pack(side="top", fill=BOTH)

  adv_messagelbframe=LabelFrame(seventhtab,text="Template advanced settings", height=250, width=1150)
  adv_messagelbframe.place(x=2, y=10)

  adv_fbill = Label(seventhtab,text="Template",font="arial 10 bold").place(x=20,y=30)

  adv_ver = Label(seventhtab,text="Professional 1 (logo on left side)")
  adv_ver.place(x=20,y=60)

  adv_ver = Label(seventhtab,text="Professional 2 (logo on right side)")
  adv_ver.place(x=20,y=90)

  adv_ver = Label(seventhtab,text="Simplified 1 (logo on left side)")
  adv_ver.place(x=20,y=120)

  adv_ver = Label(seventhtab,text="Simplified 2 (logo on right side)")
  adv_ver.place(x=20,y=150)

  adv_ver = Label(seventhtab,text="Business Classic")
  adv_ver.place(x=20,y=180)

  adv_fbill = Label(seventhtab,text="Page size",font="arial 10 bold").place(x=255,y=30)

  adv_win_menu3 = StringVar()
  adv_winstyle3 = ttk.Combobox(seventhtab,textvariable=adv_win_menu3)
  adv_winstyle3['values'] = ('Letter','A4')
  adv_win_menu3.set('Letter')
  #adv_winstyle3.current(0)
  adv_winstyle3.place(x=225 ,y=60)
    
  
  adv_win_menu4 = StringVar()
  adv_winstyle4 = ttk.Combobox(seventhtab,textvariable=adv_win_menu4)
  adv_winstyle4.place(x=225,y=90)
  adv_winstyle4['values'] = ("Letter","A4")
  adv_winstyle4.set("Letter")
  adv_winstyle4.current(0)

  adv_win_menu5 = StringVar()
  adv_winstyle5 = ttk.Combobox(seventhtab,textvariable=adv_win_menu5)
  adv_winstyle5.place(x=225,y=120)
  adv_winstyle5['values'] = ("Letter","A4")
  adv_winstyle5.set("Letter")
  adv_winstyle5.current(0)

  adv_win_menu6 = StringVar()
  adv_winstyle6 = ttk.Combobox(seventhtab,textvariable=adv_win_menu6)
  adv_winstyle6.place(x=225,y=150)
  adv_winstyle6['values'] = ("Letter","A4")
  adv_winstyle6.set("Letter")
  adv_winstyle6.current(0)

  adv_win_menu7 = StringVar()
  adv_winstyle7 = ttk.Combobox(seventhtab,textvariable=adv_win_menu7)
  adv_winstyle7.place(x=225,y=180)
  adv_winstyle7['values'] = ("Letter","A4")
  adv_winstyle7.set("Letter")
  adv_winstyle7.current(0)

  adv_fbill = Label(seventhtab,text="Right Margin(mm)",font="arial 10 bold").place(x=450,y=30)

  adv_spin00 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin00.place(x=465,y=60)

  adv_spin01 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin01.place(x=465,y=90)

  adv_spin02 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin02.place(x=465,y=120)

  adv_spin03 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin03.place(x=465,y=150)

  adv_spin04 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin04.place(x=465,y=180)


  adv_fbill = Label(seventhtab,text="'Invoice to'block position shift(mm)",font="arial 10 bold").place(x=650,y=30)

  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=60)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=90)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=120)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=150)

  adv_spin10 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin10.place(x=685,y=60)

  adv_spin11 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin11.place(x=685,y=90)

  adv_spin12 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin12.place(x=685,y=120)

  adv_spin13 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin13.place(x=685,y=150)

  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=60)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=90)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=120)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=150)

  adv_spin20 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin20.place(x=820,y=60)

  adv_spin21 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin21.place(x=820,y=90)

  adv_spin22 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin22.place(x=820,y=120)

  adv_spin23 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin23.place(x=820,y=150)

  adv_bttermadd = Button(seventhtab,image=photo8,compound = LEFT,text="Refresh preview",width=115)
  adv_bttermadd.place(x=1000,y=50)

  adv_bttermadd = Button(seventhtab,image=saves,compound = LEFT,text="Save Settings",width=115)
  adv_bttermadd.place(x=1000,y=140)

  def adv_restore():
    adv_spin10.delete(0,'end')
    adv_spin10.insert(0,"0")
    adv_spin11.delete(0,'end')
    adv_spin11.insert(0,"0")
    adv_spin12.delete(0,'end')
    adv_spin12.insert(0,"0")
    adv_spin13.delete(0,'end')
    adv_spin13.insert(0,"0")
    adv_spin20.delete(0,'end')
    adv_spin20.insert(0,"0")
    adv_spin21.delete(0,'end')
    adv_spin21.insert(0,"0")
    adv_spin22.delete(0,'end')
    adv_spin22.insert(0,"0")
    adv_spin23.delete(0,'end')
    adv_spin23.insert(0,"0")
    adv_spin00.delete(0,'end')
    adv_spin00.insert(0,"10")
    adv_spin01.delete(0,'end')
    adv_spin01.insert(0,"10")
    adv_spin02.delete(0,'end')
    adv_spin02.insert(0,"10")
    adv_spin03.delete(0,'end')
    adv_spin03.insert(0,"10")
    adv_spin04.delete(0,'end')
    adv_spin04.insert(0,"10")
    adv_winstyle3.delete(0,'end')
    adv_winstyle3.insert(0,"Letter")
    adv_winstyle4.delete(0,'end')
    adv_winstyle4.insert(0,"Letter")
    adv_winstyle5.delete(0,'end')
    adv_winstyle5.insert(0,"Letter")
    adv_winstyle6.delete(0,'end')
    adv_winstyle6.insert(0,"Letter")
    adv_winstyle7.delete(0,'end')
    adv_winstyle7.insert(0,"Letter")

  adv_bttermadd = Button(seventhtab,text="Restore defaults",width=16, command=adv_restore)
  adv_bttermadd.place(x=1000,y=180)

  adv_ver = Label(seventhtab,text="By positioning 'Invoice to'block,the customer name/address can be displayed in right place in the windowed envelope. If you networking, you need to setup this on all computer.\nExample:(Left:20 and Top:10 means that shift 'Invoice to'block to right 20mm and shift down 10mm) Original position Left:0 Top:0")
  adv_ver.place(x=50,y=210)

  adv_ver = Label(seventhtab,text="Selected template preview (example, click on preview for mouse scrolling)")
  adv_ver.place(x=230,y=270)

#------------Professional 1 (logo on left side)------------- 
  def adv_maindropmenu(event):
      menuvar=adv_win_menu8.get()
      print(menuvar)
      sql = "select * from company"
      fbcursor.execute(sql)
      advdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
              
          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
            
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Professional 2 (logo on right side)------------- 

      elif menuvar == 'Professional 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          #T_address_window = canvas.create_window(95, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
      
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Simplified 1 (logo on left side)------------- 

      elif menuvar == 'Simplified 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  
          #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


#------------Simplified 2 (logo on right side)-------------

      elif menuvar == 'Simplified 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
              
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
        
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #------------Business Classic------------- 

      elif menuvar == 'Business Classic':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 60, 1120, 60, fill="orange")
          #canvas.create_line(1000, 60, 600, 60, fill="grey")

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,100))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
            adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  


          # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
          # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
          # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
          canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

          canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
          canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

          canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="Product/Service")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Unit Price")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Quantity")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
              
          window = canvas.create_window(120, 230, anchor="nw", window=tree)

          canvas.create_line(120, 270, 1120, 270 )
          canvas.create_line(120, 230, 120, 270 )
          canvas.create_line(270, 230, 270, 270 )
          canvas.create_line(670, 230, 670, 270 )
          canvas.create_line(820, 230, 820, 270 )
          canvas.create_line(970, 230, 970, 270 )
          canvas.create_line(1120, 230, 1120, 270)
          canvas.create_line(1120, 270, 1120, 420)
          canvas.create_line(670, 295, 1120, 295)
          canvas.create_line(670, 320, 1120, 320)
          canvas.create_line(670, 345, 1120, 345)
          canvas.create_line(670, 370, 1120, 370)
          canvas.create_line(670, 395, 1120, 395)
          canvas.create_line(670, 420, 1120, 420)

          canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_line(100, 480, 1120, 480, fill="orange")
          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 600, 1120, 600, fill="orange")
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
          pass

  adv_win_menu8 = StringVar()
  adv_winstyle8 = ttk.Combobox(seventhtab,textvariable=adv_win_menu8)
  adv_winstyle8.bind("<<ComboboxSelected>>", adv_maindropmenu)
  adv_winstyle8["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not advdata:
    adv_winstyle8.current(0)
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    # T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    # T_address.tag_configure('tag_name',justify='right')
    # T_address.insert('1.0', advdata[2])
    # T_address.tag_add('tag_name','1.0', 'end')
    # T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
        
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(125, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))
    
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  elif advdata[32] == 'Simplified 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Simplified 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 55, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(135, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
        
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Business Classic':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 60, 1120, 60, fill="orange")
    #canvas.create_line(1000, 60, 600, 60, fill="grey")

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,100))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
      adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  


    # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
    # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
    # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
    canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
    canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

    canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
        
    window = canvas.create_window(120, 230, anchor="nw", window=tree)

    canvas.create_line(120, 270, 1120, 270 )
    canvas.create_line(120, 230, 120, 270 )
    canvas.create_line(270, 230, 270, 270 )
    canvas.create_line(670, 230, 670, 270 )
    canvas.create_line(820, 230, 820, 270 )
    canvas.create_line(970, 230, 970, 270 )
    canvas.create_line(1120, 230, 1120, 270)
    canvas.create_line(1120, 270, 1120, 420)
    canvas.create_line(670, 295, 1120, 295)
    canvas.create_line(670, 320, 1120, 320)
    canvas.create_line(670, 345, 1120, 345)
    canvas.create_line(670, 370, 1120, 370)
    canvas.create_line(670, 395, 1120, 395)
    canvas.create_line(670, 420, 1120, 420)

    canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(100, 480, 1120, 480, fill="orange")
    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 600, 1120, 600, fill="orange")
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  adv_winstyle8.place(x=2 ,y=270, width=220)
  #adv_winstyle8.current(0)


root.mainloop()

