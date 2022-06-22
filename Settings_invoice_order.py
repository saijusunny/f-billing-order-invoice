#from ast import pattern
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
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
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbilling", port="3306"
)
fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1300x730")

root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
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

tabControl = ttk.Notebook(root)
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

settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
settingsframe.pack(side="top", fill=BOTH)
  
settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
settframe.pack(side="top", fill=X)

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

    
addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
addcustomerLabel = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command="",image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
addcustomerLabel.pack(side="left", pady=3, ipadx=4)
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

editcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_edit.png"))
editcustomerLabel = Button(settframe,compound="top", text="Quick\nStart Wizard",relief=RAISED,command="",  image=editcustomerIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
editcustomerLabel.pack(side="left")

deletecustomerIcon = ImageTk.PhotoImage(Image.open("images/user_delete.png"))
deletecustomerLabel = Button(settframe,compound="top", text="Company\nManager",relief=RAISED, command="", image=deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
deletecustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

previewinvoiceIcon = ImageTk.PhotoImage(Image.open("images/priewok.png"))
previewinvoiceLabel = Button(settframe,compound="top",command="", text="Optimize\nData tables", relief=RAISED,               image=previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black",  height=55, bd=1, width=55)
previewinvoiceLabel.pack(side="left")

printinvoiceIcon = ImageTk.PhotoImage(Image.open("images/printer.png"))
printinvoiceLabel = Button(settframe,compound="top", text="Repair\nDatabase",relief=RAISED,  command="",  image=printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
printinvoiceLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

emailinviceIcon = ImageTk.PhotoImage(Image.open("images/gmail.png"))
emailinviceLabel = Button(settframe,compound="top",command="", text="Backup\nDatabase", relief=RAISED,               image=emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black",height=55,   bd=1, width=55)
emailinviceLabel.pack(side="left")

refreshcustomerIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
refreshcustomerLabel = Button(settframe,compound="top", command="",text="Restore\nDatabase", relief=RAISED,               image=refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black",  height=55, bd=1, width=55)
refreshcustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

smsIcon = ImageTk.PhotoImage(Image.open("images/text-message.png"))
smsLabel = Button(settframe,compound="top", text="Serach\nfor Updates",command="", relief=RAISED,  image=smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
smsLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

importcustomerIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
importcustomerLabel = Button(settframe,compound="top", text="Enter licence\nKey Code",command="", relief=RAISED, image=importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1,  width=55)
importcustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

exportcustomerIcon = ImageTk.PhotoImage(Image.open("images/export.png"))
exportcustomerLabel = Button(settframe,compound="top", text="Online\nUser Manual",command="",relief=RAISED,   image=exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1,width=55)
exportcustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

customersearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
customersearchLabel = Button(settframe,compound="top",command="", text="Upgrade to\nPro Now!", relief=RAISED,               image=customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black",  height=55, bd=1, width=55)
customersearchLabel.pack(side="left")


invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(20,0))

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


################### tab03 ###################################settings-saiju
Invoice_setting_frame=Frame(tab03, relief=GROOVE, bg="#f8f8f2")
Invoice_setting_frame.pack(side="top", fill=BOTH)

Invoice_setting_frame_cpy=Frame(Invoice_setting_frame, bg="#f5f3f2", height=700)
Invoice_setting_frame_cpy.pack(side="top", fill=BOTH)
ver = Label(Invoice_setting_frame_cpy,text="Invoice# prefix")
ver.place(x=5,y=20)

inv_tp_lf = Listbox(Invoice_setting_frame, height=1)
inv_tp_lf.insert(END, "INV")
inv_tp_lf.place(x=100,y=20)

invset_ver = Label(Invoice_setting_frame_cpy,text="Starting Invoice number")
invset_ver.place(x=25,y=50)

inv_spn_bx = Spinbox(Invoice_setting_frame_cpy,from_=1,to=1000000,width=15)
inv_spn_bx.place(x=50,y=80)

inv_lbl2 = Label(Invoice_setting_frame_cpy,text="Header box background color")
inv_lbl2.place(x=5,y=100)

invset_bg_var = StringVar()
invset_bg_list = ttk.Combobox(Invoice_setting_frame_cpy,textvariable=invset_bg_var)
invset_bg_list.place(x=6 ,y=120)
invset_bg_list['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
invset_bg_list.current(0)

inv_lb22 = Label(Invoice_setting_frame_cpy,text="Customize Invoice text labels")
inv_lb22.place(x=5,y=140)

def lst_bx1(event):
  print("haii")

inv_lst_bx1 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx1.insert(END, "Invoice")

inv_lst_bx1.place(x=5,y=160)
inv_lst_bx2 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx2.insert(END, "Invoice#")
inv_lst_bx2.place(x=5,y=180)
inv_lst_bx3 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx3.insert(END, "Invoice date")
inv_lst_bx3.place(x=5,y=200)
inv_lst_bx4 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx4.insert(END, "Order ref.#")
inv_lst_bx4.place(x=5,y=220)
inv_lst_bx5 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx5.insert(END, "Terms")
inv_lst_bx5.place(x=5,y=240)
inv_lst_bx6 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx6.insert(END, "Invoice to")
inv_lst_bx6.place(x=5,y=260)
inv_lst_bx7 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx7.insert(END, "Ship to")
inv_lst_bx7.place(x=5,y=280)
inv_lst_bx8 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx8.insert(END, "ID/SKU")
inv_lst_bx8.place(x=5,y=300)
inv_lst_bx9 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx9.insert(END, "Product/Service")
inv_lst_bx9.place(x=5,y=320)
inv_lst_bx10 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx10.insert(END, "Quantity")
inv_lst_bx10.place(x=5,y=340)
inv_lst_bx11 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx11.insert(END, "Description")
inv_lst_bx11.place(x=5,y=360)
inv_lst_bx12 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx12.insert(END, "Unit Price")
inv_lst_bx12.place(x=5,y=380)
inv_lst_bx13 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx13.insert(END, "Price")
inv_lst_bx13.place(x=5,y=400)
inv_lst_bx14 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx14.insert(END, "Subtotal")
inv_lst_bx14.place(x=5,y=420)
inv_lst_bx15 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx15.insert(END, "Discount")
inv_lst_bx15.place(x=5,y=440)
inv_lst_bx16 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx16.insert(END, "Discount rate")
inv_lst_bx16.place(x=5,y=460)
inv_lst_bx17 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx17.insert(END, "TAX1")
inv_lst_bx17.place(x=200,y=520)
inv_lst_bx18 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx18.insert(END, "TAX2")
inv_lst_bx18.place(x=400,y=520)
inv_lst_bx19 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx19.insert(END, "Total Paid")
inv_lst_bx19.place(x=600,y=520)
inv_lst_bx20 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx20.insert(END, "Balance")
inv_lst_bx20.place(x=800,y=520)
inv_lst_bx21 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx21.insert(END, "Terms and Conditions")
inv_lst_bx21.place(x=1000,y=520)
inv_lst_bx22 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx22.insert(END, "Tax Exempted")
inv_lst_bx22.place(x=5,y=480)
inv_lst_bx23 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx23.insert(END, "Page")
inv_lst_bx23.place(x=5,y=500)
inv_lst_bx24 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
inv_lst_bx24.insert(END, "of")
inv_lst_bx24.place(x=5,y=520)



invset_s1 = StringVar(Invoice_setting_frame, "Invoice")


invset_ver = Label(Invoice_setting_frame_cpy,text="Default Invoice template(example,click on preview for mouse scrolling)")
invset_ver.place(x=248,y=55 )

invset_ver = Label(Invoice_setting_frame_cpy,text="Default Invoice template")
invset_ver.place(x=619,y=40)

#data=StringVar()

invset_messagelbframe=LabelFrame(Invoice_setting_frame_cpy,text="Predefined terms and conditions text for Invoice", height=100, width=980)
invset_messagelbframe.place(x=248, y=400)

inv_txt = scrolledtext.ScrolledText(Invoice_setting_frame_cpy, undo=True,width=115,height=4)
inv_txt.insert(1.0,"Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods, and agrees to be bound to these contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller.")
inv_txt.place(x=260,y=425)

inv_rst_btn = Button(Invoice_setting_frame_cpy,text="Restore defaults")
inv_rst_btn.place(x=32,y=450)

#------------Professional 1 (logo on left side)-------------
def styl_can_def(event):
    menuvar_lst=logo_just_var.get()
  
    por_sql_st='select * from company'
    fbcursor.execute(por_sql_st)
    cmpy_dtl=fbcursor.fetchone()
    if menuvar_lst == 'Professional 1 (logo on left side)':

      if cmpy_dtl[1] is not None:
        frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        frame_pro1.pack(expand=True, fill=BOTH)
        frame_pro1.place(x=247,y=90)
        inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=inv_pro1_canvas.yview)
        
        inv_pro1_canvas.config(width=953,height=300)
        inv_pro1_canvas.config(yscrollcommand=vertibar.set)
        inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(inv_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = inv_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Invoice#
        win_inv1 = inv_pro1_canvas.create_window(175, 150, anchor="nw", window=lb_inv1)

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Invoicedate
        win_inv1 = inv_pro1_canvas.create_window(175, 170, anchor="nw", window=lb_inv1)
        
        lb_inv1=Label(inv_pro1_canvas,text="Due date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
        win_inv1 = inv_pro1_canvas.create_window(175, 190, anchor="nw", window=lb_inv1)

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
        win_inv1 = inv_pro1_canvas.create_window(175, 210, anchor="nw", window=lb_inv1)

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
        win_inv1 = inv_pro1_canvas.create_window(175, 230, anchor="nw", window=lb_inv1)

        inv_pro1_canvas.create_text(350, 150, text="INV1/2022",justify=LEFT, fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 170, text="03-05-2022",justify=LEFT, fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 190, text="18-05-2022",justify=LEFT, fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(340, 210, text="NET 15",justify=LEFT, fill="black", font=('Helvetica 11'))   
        
        labelcmp=Label(inv_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
        window = inv_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(inv_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
        windowl = inv_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

        
        inv_pro1_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 10'))

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="e",font=('Helvetica 14 bold'),height=1)#invoice
        win_inv1 = inv_pro1_canvas.create_window(725, 200, anchor="nw", window=lb_inv1)

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx22.get(1.0,END), bg="white",anchor="e",font=("Helvetica 10" ),height=1)#TAX EXEMPTED
        win_inv1 = inv_pro1_canvas.create_window(695, 225, anchor="nw", window=lb_inv1)

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
        win_inv1 = inv_pro1_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

        lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
        win_inv1 = inv_pro1_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

        
        # inv_pro1_canvas.create_text(765, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        # inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        # inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        # inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        s = ttk.Style()
        s.configure('Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

        tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))#"ID/SKU"
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))#Product/Service - Description
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))#"Quantity"
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text=inv_lst_bx10.get(1.0,END))#"Unit Price"
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))#"Price"
        
        window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)
        squl_qry='select * from company'
        fbcursor.execute(squl_qry)
        cmpy_tax=fbcursor.fetchone()

        inv_pro1_canvas.create_line(120, 390, 820, 390 )
        inv_pro1_canvas.create_line(120, 340, 120, 365 )
        inv_pro1_canvas.create_line(120, 365, 120, 390 )
        inv_pro1_canvas.create_line(820, 340, 820, 540 )
        inv_pro1_canvas.create_line(740, 340, 740, 540 )
        inv_pro1_canvas.create_line(570, 340, 570, 540 )
        inv_pro1_canvas.create_line(570, 415, 820, 415 )
        inv_pro1_canvas.create_line(570, 440, 820, 440 )
        inv_pro1_canvas.create_line(570, 465, 820, 465 )
        inv_pro1_canvas.create_line(570, 490, 820, 490 )
        inv_pro1_canvas.create_line(570, 515, 820, 515 )
        inv_pro1_canvas.create_line(650, 340, 650, 390 )
        inv_pro1_canvas.create_line(220, 340, 220, 390 )
        inv_pro1_canvas.create_line(570, 540, 820, 540 )

        inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          

        lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
        win_inv2 = inv_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

        lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
        win_inv2 = inv_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

        lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
        win_inv2 = inv_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

        lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
        win_inv2 = inv_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
          

       
        inv_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        inv_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        # if int(cmpy_tax[12])==3:
        #   inv_pro1_canvas.create_line(120, 390, 820, 390 )
        #   inv_pro1_canvas.create_line(120, 340, 120, 365 )
        #   inv_pro1_canvas.create_line(120, 365, 120, 390 )
        #   inv_pro1_canvas.create_line(820, 360, 820, 565 )
        #   inv_pro1_canvas.create_line(740, 340, 740, 565 )
        #   inv_pro1_canvas.create_line(570, 340, 570, 565 )
        #   inv_pro1_canvas.create_line(570, 415, 820, 415 )
        #   inv_pro1_canvas.create_line(570, 440, 820, 440 )
        #   inv_pro1_canvas.create_line(570, 465, 820, 465 )
        #   inv_pro1_canvas.create_line(570, 490, 820, 490 )
        #   inv_pro1_canvas.create_line(570, 515, 820, 515 )
        #   inv_pro1_canvas.create_line(650, 340, 650, 390 )
        #   inv_pro1_canvas.create_line(220, 340, 220, 390 )
        #   inv_pro1_canvas.create_line(570, 540, 820, 540 )
        #   inv_pro1_canvas.create_line(570, 565, 820, 565 )

        #   inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          

        #   lbx_inv=Label(inv_pro1_canvas,text="Subtotal", bg="white",anchor="nw",font=("Helvetica 10"))
        #   win_inv2 = inv_pro1_canvas.create_window(635, 393, anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="TAX1", bg="white",anchor="nw",font=("Helvetica 10"))
        #   win_inv2 = inv_pro1_canvas.create_window(635, 418, anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="TAX2", bg="white",anchor="nw",font=("Helvetica 10"))
        #   win_inv2 = inv_pro1_canvas.create_window(635, 443, anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="Total Paid", bg="white",anchor="nw",font=("Helvetica 10 "))
        #   win_inv2 = inv_pro1_canvas.create_window(630, 518,anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="Balance", bg="white",anchor="nw",font=("Helvetica 10 "))
        #   win_inv2 = inv_pro1_canvas.create_window(635, 543, anchor="nw", window=lbx_inv)
          
          

        #   # inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        #   inv_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        #   inv_pro1_canvas.create_text(792, 455, text="$18.00", fill="black", font=('Helvetica 10'))

        #   inv_pro1_canvas.create_text(650, 480, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(792, 480, text="$20.00", fill="black", font=('Helvetica 10'))

        #   inv_pro1_canvas.create_text(790, 505, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        #   inv_pro1_canvas.create_text(655, 505, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        #   inv_pro1_canvas.create_text(790, 530, text="$100.00", fill="black", font=('Helvetica 10'))
      

        #   inv_pro1_canvas.create_text(790, 553, text="$138.00", fill="black", font=('Helvetica 10'))

        # elif int(cmpy_tax[12])==2:
        #   inv_pro1_canvas.create_line(120, 390, 820, 390 )
        #   inv_pro1_canvas.create_line(120, 340, 120, 365 )
        #   inv_pro1_canvas.create_line(120, 365, 120, 390 )
        #   inv_pro1_canvas.create_line(820, 340, 820, 540 )
        #   inv_pro1_canvas.create_line(740, 340, 740, 540 )
        #   inv_pro1_canvas.create_line(570, 340, 570, 540 )
        #   inv_pro1_canvas.create_line(570, 415, 820, 415 )
        #   inv_pro1_canvas.create_line(570, 440, 820, 440 )
        #   inv_pro1_canvas.create_line(570, 465, 820, 465 )
        #   inv_pro1_canvas.create_line(570, 490, 820, 490 )
        #   inv_pro1_canvas.create_line(570, 515, 820, 515 )
        #   inv_pro1_canvas.create_line(650, 340, 650, 390 )
        #   inv_pro1_canvas.create_line(220, 340, 220, 390 )
        #   inv_pro1_canvas.create_line(570, 540, 820, 540 )

        #   inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          

        #   lbx_inv=Label(inv_pro1_canvas,text="Subtotal", bg="white",anchor="nw",font=("Helvetica 10"))
        #   win_inv2 = inv_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="TAX1", bg="white",anchor="nw",font=("Helvetica 10 "))
        #   win_inv2 = inv_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="Total Paid", bg="red",anchor="nw",font=("Helvetica 10 "))
        #   win_inv2 = inv_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

        #   lbx_inv=Label(inv_pro1_canvas,text="Balance", bg="white",anchor="nw",font=("Helvetica 10 "))
        #   win_inv2 = inv_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
          

        #   # inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))


        #   inv_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        #   inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        #   inv_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        #   inv_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        #   inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        #   inv_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))


        #   inv_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))

        # elif cmpy_tax[12]==1:
        #   pass
        
        

        inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        inv_pro1_canvas.create_text(500, 590, text=inv_lst_bx21.get(1.0,END), fill="black", font=('Helvetica 10'))#"Terms and Conditions"
        inv_pro1_canvas.create_line(150, 600, 795, 600)
        text=inv_txt.get('1.0',END)
        wraped_text="\n".join(wrap(text,130))
   
      
        lbx_inv=Label(inv_pro1_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
        win_inv2 = inv_pro1_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

        inv_pro1_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  

        inv_pro1_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        frame_pro1.pack(expand=True, fill=BOTH)
        frame_pro1.place(x=247,y=90)
        inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=inv_pro1_canvas.yview)
        
        inv_pro1_canvas.config(width=953,height=300)
        inv_pro1_canvas.config(yscrollcommand=vertibar.set)
        inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        inv_pro1_canvas.create_text(195, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(205, 170, text="Invoicedate", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))   
        
        inv_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))

        inv_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        s = ttk.Style()
        s.configure('Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

        tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
        window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

        inv_pro1_canvas.create_line(120, 390, 820, 390 )
        inv_pro1_canvas.create_line(120, 340, 120, 365 )
        inv_pro1_canvas.create_line(120, 365, 120, 390 )
        inv_pro1_canvas.create_line(820, 340, 820, 540 )
        inv_pro1_canvas.create_line(740, 340, 740, 540 )
        inv_pro1_canvas.create_line(570, 340, 570, 540 )
        inv_pro1_canvas.create_line(570, 415, 820, 415 )
        inv_pro1_canvas.create_line(570, 440, 820, 440 )
        inv_pro1_canvas.create_line(570, 465, 820, 465 )
        inv_pro1_canvas.create_line(570, 490, 820, 490 )
        inv_pro1_canvas.create_line(570, 515, 820, 515 )
        inv_pro1_canvas.create_line(650, 340, 650, 390 )
        inv_pro1_canvas.create_line(220, 340, 220, 390 )
        inv_pro1_canvas.create_line(570, 540, 820, 540 )

        inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(610, 372, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(710, 372, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 372, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 404, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(792, 428, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(792, 454, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(790, 479, text="0", fill="black", font=('Helvetica 10 bold'))
        inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        inv_pro1_canvas.create_text(790, 502, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(790, 526, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        inv_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_line(150, 620, 795, 620)
        

        inv_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      

  #----------------Professional 2 (logo on right side)------------------
    elif menuvar_lst == 'Professional 2 (logo on right side)':
      if cmpy_dtl[1] is not None:
        frame_inv_pro2 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        frame_inv_pro2.pack(expand=True, fill=BOTH)
        frame_inv_pro2.place(x=247,y=90)
        
        canvas_pro2=Canvas(frame_inv_pro2, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(frame_inv_pro2, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas_pro2.yview)
        canvas_pro2.config(width=953,height=300)
        
        canvas_pro2.config(yscrollcommand=vertibar.set)
        canvas_pro2.pack(expand=True,side=LEFT,fill=BOTH)
        canvas_pro2.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas_pro2.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(canvas_pro2,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = canvas_pro2.create_window(800, 60, anchor="ne", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          canvas_pro2.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        labelcmp=Label(canvas_pro2,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
        window = canvas_pro2.create_window(150,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(canvas_pro2,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
        windowl = canvas_pro2.create_window(155 ,110, anchor="nw", window=labelcmpl)
        
        canvas_pro2.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
        canvas_pro2.create_text(190, 205, text="Invoice",justify=LEFT, fill="black", font=('Helvetica 14 bold'))

        
        canvas_pro2.create_text(502, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(515, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(505, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(680, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
          
        canvas_pro2.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        canvas_pro2.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas_pro2.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas_pro2.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas_pro2.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(canvas_pro2, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = canvas_pro2.create_window(120, 340, anchor="nw", window=tree)

        canvas_pro2.create_line(120, 390, 820, 390 )
        canvas_pro2.create_line(120, 340, 120, 365 )
        canvas_pro2.create_line(120, 365, 120, 390 )
        canvas_pro2.create_line(820, 340, 820, 540 )
        canvas_pro2.create_line(740, 340, 740, 540 )
        canvas_pro2.create_line(570, 340, 570, 540 )
        canvas_pro2.create_line(570, 415, 820, 415 )
        canvas_pro2.create_line(570, 440, 820, 440 )
        canvas_pro2.create_line(570, 465, 820, 465 )
        canvas_pro2.create_line(570, 490, 820, 490 )
        canvas_pro2.create_line(570, 515, 820, 515 )
        canvas_pro2.create_line(650, 340, 650, 390 )
        canvas_pro2.create_line(220, 340, 220, 390 )
        canvas_pro2.create_line(570, 540, 820, 540 )

        canvas_pro2.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        lbx_inv=Label(canvas_pro2,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
        win_inv2 = canvas_pro2.create_window(630,392, anchor="nw", window=lbx_inv)

        lbx_inv=Label(canvas_pro2,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
        win_inv2 = canvas_pro2.create_window(635,418, anchor="nw", window=lbx_inv)

        lbx_inv=Label(canvas_pro2,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
        win_inv2 = canvas_pro2.create_window(630, 492,anchor="nw", window=lbx_inv)

        lbx_inv=Label(canvas_pro2,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
        win_inv2 = canvas_pro2.create_window(635, 518, anchor="nw", window=lbx_inv)
          

       
        canvas_pro2.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        canvas_pro2.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        canvas_pro2.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        canvas_pro2.create_text(500, 590, text=inv_lst_bx21.get(1.0,END), fill="black", font=('Helvetica 10'))#"Terms and Conditions"
        canvas_pro2.create_line(150, 600, 795, 600)
        text=inv_txt.get('1.0',END)
        wraped_text="\n".join(wrap(text,130))
   
      
        lbx_inv=Label(canvas_pro2,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
        win_inv2 = canvas_pro2.create_window(150, 603,anchor="nw", window=lbx_inv)

        canvas_pro2.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  

        canvas_pro2.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:

        frame_inv_pro2 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        frame_inv_pro2.pack(expand=True, fill=BOTH)
        frame_inv_pro2.place(x=247,y=90)
        
        canvas_pro2=Canvas(frame_inv_pro2, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(frame_inv_pro2, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas_pro2.yview)
        canvas_pro2.config(width=953,height=300)
        
        canvas_pro2.config(yscrollcommand=vertibar.set)
        canvas_pro2.pack(expand=True,side=LEFT,fill=BOTH)
        canvas_pro2.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas_pro2.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        
        canvas_pro2.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        canvas_pro2.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        canvas_pro2.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(225, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        canvas_pro2.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        canvas_pro2.create_text(502, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(515, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(505, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(680, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas_pro2.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
          
        canvas_pro2.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        canvas_pro2.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas_pro2.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas_pro2.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas_pro2.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(canvas_pro2, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = canvas_pro2.create_window(120, 340, anchor="nw", window=tree)

        canvas_pro2.create_line(120, 390, 820, 390 )
        canvas_pro2.create_line(120, 340, 120, 365 )
        canvas_pro2.create_line(120, 365, 120, 390 )
        canvas_pro2.create_line(820, 340, 820, 540 )
        canvas_pro2.create_line(740, 340, 740, 540 )
        canvas_pro2.create_line(570, 340, 570, 540 )
        canvas_pro2.create_line(570, 415, 820, 415 )
        canvas_pro2.create_line(570, 440, 820, 440 )
        canvas_pro2.create_line(570, 465, 820, 465 )
        canvas_pro2.create_line(570, 490, 820, 490 )
        canvas_pro2.create_line(570, 515, 820, 515 )
        canvas_pro2.create_line(650, 340, 650, 390 )
        canvas_pro2.create_line(220, 340, 220, 390 )
        canvas_pro2.create_line(570, 540, 820, 540 )

        canvas_pro2.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        canvas_pro2.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        canvas_pro2.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas_pro2.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_line(150, 620, 795, 620)
        canvas_pro2.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas_pro2.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  #----------------Simplified 1 (logo on left side)------------------ 
    elif menuvar_lst == 'Simplified 1 (logo on left side)':
      if cmpy_dtl[1] is not None:
        smply_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        smply_frame.pack(expand=True, fill=BOTH)
        smply_frame.place(x=247,y=90)
        inv_smply_canvas=Canvas(smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(smply_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=inv_smply_canvas.yview)
        inv_smply_canvas.config(width=953,height=300)

        inv_smply_canvas.config(yscrollcommand=vertibar.set)
        inv_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        inv_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        inv_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(inv_smply_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = inv_smply_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          inv_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        inv_smply_canvas.create_text(202, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(215, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(350, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(350, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        labelcmp=Label(inv_smply_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
        window = inv_smply_canvas.create_window(430,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(inv_smply_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
        windowl = inv_smply_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

        
        inv_smply_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 9'))
        inv_smply_canvas.create_text(765, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))

        
        inv_smply_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(inv_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = inv_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

        inv_smply_canvas.create_line(120, 390, 820, 390 )
        inv_smply_canvas.create_line(120, 340, 120, 365 )
        inv_smply_canvas.create_line(120, 365, 120, 390 )
        inv_smply_canvas.create_line(820, 340, 820, 540 )
        inv_smply_canvas.create_line(740, 340, 740, 540 )
        inv_smply_canvas.create_line(570, 390, 570, 540 )
        inv_smply_canvas.create_line(570, 415, 820, 415 )
        inv_smply_canvas.create_line(570, 440, 820, 440 )
        inv_smply_canvas.create_line(570, 465, 820, 465 )
        inv_smply_canvas.create_line(570, 490, 820, 490 )
        inv_smply_canvas.create_line(570, 515, 820, 515 )
        inv_smply_canvas.create_line(650, 340, 650, 390 )
        inv_smply_canvas.create_line(570, 540, 820, 540 )

        
        inv_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
        win_inv2 = inv_smply_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

        lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
        win_inv2 = inv_smply_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

        lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
        win_inv2 = inv_smply_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

        lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
        win_inv2 = inv_smply_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
          

       
        inv_smply_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        inv_smply_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        inv_smply_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        inv_smply_canvas.create_text(500, 590, text=inv_lst_bx21.get(1.0,END), fill="black", font=('Helvetica 10'))#"Terms and Conditions"
        inv_smply_canvas.create_line(150, 600, 795, 600)
        text=inv_txt.get('1.0',END)
        wraped_text="\n".join(wrap(text,130))
   
      
        lbx_inv=Label(inv_smply_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
        win_inv2 = inv_smply_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

        inv_smply_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  

        inv_smply_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        smply_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        smply_frame.pack(expand=True, fill=BOTH)
        smply_frame.place(x=247,y=90)
        inv_smply_canvas=Canvas(smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(smply_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=inv_smply_canvas.yview)
        inv_smply_canvas.config(width=953,height=300)

        inv_smply_canvas.config(yscrollcommand=vertibar.set)
        inv_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        inv_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        inv_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        inv_smply_canvas.create_text(202, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(215, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(350, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(350, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        inv_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        inv_smply_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        inv_smply_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(750, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        
        inv_smply_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(inv_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = inv_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

        inv_smply_canvas.create_line(120, 390, 820, 390 )
        inv_smply_canvas.create_line(120, 340, 120, 365 )
        inv_smply_canvas.create_line(120, 365, 120, 390 )
        inv_smply_canvas.create_line(820, 340, 820, 540 )
        inv_smply_canvas.create_line(740, 340, 740, 540 )
        inv_smply_canvas.create_line(570, 390, 570, 540 )
        inv_smply_canvas.create_line(570, 415, 820, 415 )
        inv_smply_canvas.create_line(570, 440, 820, 440 )
        inv_smply_canvas.create_line(570, 465, 820, 465 )
        inv_smply_canvas.create_line(570, 490, 820, 490 )
        inv_smply_canvas.create_line(570, 515, 820, 515 )
        inv_smply_canvas.create_line(650, 340, 650, 390 )
        inv_smply_canvas.create_line(570, 540, 820, 540 )

        
        inv_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        inv_smply_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        inv_smply_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        inv_smply_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_line(150, 620, 795, 620)
        inv_smply_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        inv_smply_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #----------------Simplified 2 (logo on right side)------------------ 
    elif menuvar_lst == 'Simplified 2 (logo on right side)':
      if cmpy_dtl[1] is not None:
        smply2_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        smply2_frame.pack(expand=True, fill=BOTH)
        smply2_frame.place(x=247,y=90)

        smply2_canvas=Canvas(smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(smply2_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=smply2_canvas.yview)
        smply2_canvas.config(width=953,height=300)

        smply2_canvas.config(yscrollcommand=vertibar.set)
        smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(smply2_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = smply2_canvas.create_window(800, 60, anchor="ne", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        labelcmp=Label(smply2_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
        window = smply2_canvas.create_window(150,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(smply2_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
        windowl = smply2_canvas.create_window(155 ,110, anchor="nw", window=labelcmpl)
        
        smply2_canvas.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
        smply2_canvas.create_text(190, 205, text="Invoice",justify=LEFT, fill="black", font=('Helvetica 14 bold'))

        smply2_canvas.create_text(502, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(515, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(505, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(680, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        smply2_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

        smply2_canvas.create_line(120, 390, 820, 390 )
        smply2_canvas.create_line(120, 340, 120, 365 )
        smply2_canvas.create_line(120, 365, 120, 390 )
        smply2_canvas.create_line(820, 340, 820, 540 )
        smply2_canvas.create_line(740, 340, 740, 540 )
        smply2_canvas.create_line(570, 390, 570, 540 )
        smply2_canvas.create_line(570, 415, 820, 415 )
        smply2_canvas.create_line(570, 440, 820, 440 )
        smply2_canvas.create_line(570, 465, 820, 465 )
        smply2_canvas.create_line(570, 490, 820, 490 )
        smply2_canvas.create_line(570, 515, 820, 515 )
        smply2_canvas.create_line(650, 340, 650, 390 )
        smply2_canvas.create_line(570, 540, 820, 540 )

        
        smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        lbx_inv=Label(smply2_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
        win_inv2 = smply2_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

        lbx_inv=Label(smply2_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
        win_inv2 = smply2_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

        lbx_inv=Label(smply2_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
        win_inv2 = smply2_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

        lbx_inv=Label(smply2_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
        win_inv2 = smply2_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
          

       
        smply2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        smply2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        smply2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        smply2_canvas.create_text(500, 590, text=inv_lst_bx21.get(1.0,END), fill="black", font=('Helvetica 10'))#"Terms and Conditions"
        smply2_canvas.create_line(150, 600, 795, 600)
        text=inv_txt.get('1.0',END)
        wraped_text="\n".join(wrap(text,130))
   
      
        lbx_inv=Label(inv_smply_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
        win_inv2 = inv_smply_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

        inv_smply_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  

        inv_smply_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        smply2_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        smply2_frame.pack(expand=True, fill=BOTH)
        smply2_frame.place(x=247,y=90)

        smply2_canvas=Canvas(smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(smply2_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=smply2_canvas.yview)
        smply2_canvas.config(width=953,height=300)

        smply2_canvas.config(yscrollcommand=vertibar.set)
        smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        smply2_canvas.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        smply2_canvas.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(225, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))

        smply2_canvas.create_text(502, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(515, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(505, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(680, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        smply2_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

        smply2_canvas.create_line(120, 390, 820, 390 )
        smply2_canvas.create_line(120, 340, 120, 365 )
        smply2_canvas.create_line(120, 365, 120, 390 )
        smply2_canvas.create_line(820, 340, 820, 540 )
        smply2_canvas.create_line(740, 340, 740, 540 )
        smply2_canvas.create_line(570, 390, 570, 540 )
        smply2_canvas.create_line(570, 415, 820, 415 )
        smply2_canvas.create_line(570, 440, 820, 440 )
        smply2_canvas.create_line(570, 465, 820, 465 )
        smply2_canvas.create_line(570, 490, 820, 490 )
        smply2_canvas.create_line(570, 515, 820, 515 )
        smply2_canvas.create_line(650, 340, 650, 390 )
        smply2_canvas.create_line(570, 540, 820, 540 )

        
        smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        smply2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        smply2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        smply2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_line(150, 620, 795, 620)
        smply2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        smply2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #----------------Business Classic------------------ 
    elif menuvar_lst == 'Business Classic':
      if cmpy_dtl[1] is not None:
        bsn_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        bsn_frame.pack(expand=True, fill=BOTH)
        bsn_frame.place(x=247,y=90)
        
        bsn_canvas=Canvas(bsn_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(bsn_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=bsn_canvas.yview)
        bsn_canvas.config(width=953,height=300)
        
        bsn_canvas.config(yscrollcommand=vertibar.set)
        bsn_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        bsn_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        bsn_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_line(150, 70, 800, 70, fill='orange')
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(bsn_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = bsn_canvas.create_window(140, 125, anchor="nw", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          bsn_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        labelcmp=Label(bsn_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=30, height=1)
        window = bsn_canvas.create_window(345,100, anchor="nw", window=labelcmp)

        labelcmpl=Label(bsn_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
        windowl = bsn_canvas.create_window(350 ,130, anchor="nw", window=labelcmpl)
        
        bsn_canvas.create_text(405, 210, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))

        # bsn_canvas.create_text(500, 115, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        # bsn_canvas.create_text(525, 140, text="Address line 1", fill="black", font=('Helvetica 10'))
        # bsn_canvas.create_text(525, 155, text="Address line 2", fill="black", font=('Helvetica 10'))
        # bsn_canvas.create_text(525, 170, text="Address line 3", fill="black", font=('Helvetica 10'))
        # bsn_canvas.create_text(525, 185, text="Address line 4", fill="black", font=('Helvetica 10'))
        # bsn_canvas.create_text(534, 200, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        # bsn_canvas.create_text(534, 215, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))

        
        
        bsn_canvas.create_text(720, 130, text="John Doe\n381 South Beadford Road\nBedford Corner,NY10549\nUnited States", fill="black", font=('Helvetica 11'))

        bsn_canvas.create_text(659, 180, text="Invoice", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(675, 210, text="Invoice date", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(659, 240, text="Due date", fill="black", font=('Helvetica 11'))

        bsn_canvas.create_text(776, 180, text="INV1/2022", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))
        tree=ttk.Treeview(bsn_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = bsn_canvas.create_window(120, 255, anchor="nw", window=tree)
        
        bsn_canvas.create_line(120, 295, 820, 295 )
        bsn_canvas.create_line(120, 255, 120, 295 )
        bsn_canvas.create_line(320, 255, 320, 295 )
        
        bsn_canvas.create_line(740, 255, 740, 445 )
        bsn_canvas.create_line(570, 255, 570, 445 )
        bsn_canvas.create_line(570, 255, 570, 295 )
        bsn_canvas.create_line(660, 255, 660, 295 )
        bsn_canvas.create_line(740, 255, 740, 295 )
        bsn_canvas.create_line(820, 255, 820, 445 )
        bsn_canvas.create_line(570, 320, 820, 320 )
        bsn_canvas.create_line(570, 345, 820, 345 )
        bsn_canvas.create_line(570, 370, 820, 370 )
        bsn_canvas.create_line(570, 395, 820, 395 )
        bsn_canvas.create_line(570, 420, 820, 420 )
        bsn_canvas.create_line(570, 445, 820, 445 )
        
        bsn_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(630, 285, text="$200.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(790, 285, text="$200.00", fill="black", font=('Helvetica 10'))

        bsn_canvas.create_text(790, 310, text="$200.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(795, 335, text="$18.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(795, 360, text="$20.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(790, 385, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        bsn_canvas.create_text(790, 410, text="$100.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(790, 435, text="$138.00", fill="black", font=('Helvetica 10'))

        lbx_inv=Label(bsn_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
        win_inv2 = bsn_canvas.create_window(630,298, anchor="nw", window=lbx_inv)

        lbx_inv=Label(bsn_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
        win_inv2 = bsn_canvas.create_window(635,323, anchor="nw", window=lbx_inv)

        lbx_inv=Label(bsn_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
        win_inv2 = bsn_canvas.create_window(630, 398,anchor="nw", window=lbx_inv)

        lbx_inv=Label(bsn_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
        win_inv2 = bsn_canvas.create_window(635, 423, anchor="nw", window=lbx_inv)

    
        bsn_canvas.create_text(655, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(655, 385, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
    

        bsn_canvas.create_line(150, 470, 800, 470, fill='orange')
        bsn_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
        
        bsn_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_line(150, 620, 795, 620, fill='orange')
        bsn_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:

        bsn_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        bsn_frame.pack(expand=True, fill=BOTH)
        bsn_frame.place(x=247,y=90)
        
        bsn_canvas=Canvas(bsn_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(bsn_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=bsn_canvas.yview)
        bsn_canvas.config(width=953,height=300)
        
        bsn_canvas.config(yscrollcommand=vertibar.set)
        bsn_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        bsn_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        bsn_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_line(150, 70, 800, 70, fill='orange')
        bsn_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        bsn_canvas.create_text(500, 115, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        bsn_canvas.create_text(525, 140, text="Address line 1", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(525, 155, text="Address line 2", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(525, 170, text="Address line 3", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(525, 185, text="Address line 4", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(534, 200, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(534, 215, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))

        
        

        bsn_canvas.create_text(659, 180, text="Invoice", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(675, 210, text="Invoice date", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(659, 240, text="Due date", fill="black", font=('Helvetica 11'))

        bsn_canvas.create_text(776, 180, text="INV1/2022", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        bsn_canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))
        tree=ttk.Treeview(bsn_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = bsn_canvas.create_window(120, 255, anchor="nw", window=tree)

        bsn_canvas.create_line(120, 295, 820, 295 )
        bsn_canvas.create_line(120, 255, 120, 295 )
        bsn_canvas.create_line(320, 255, 320, 295 )
        bsn_canvas.create_line(570, 255, 570, 295 )
        bsn_canvas.create_line(660, 255, 660, 295 )
        bsn_canvas.create_line(740, 255, 740, 295 )
        bsn_canvas.create_line(820, 255, 820, 445 )
        bsn_canvas.create_line(570, 320, 820, 320 )
        bsn_canvas.create_line(570, 345, 820, 345 )
        bsn_canvas.create_line(570, 370, 820, 370 )
        bsn_canvas.create_line(570, 395, 820, 395 )
        bsn_canvas.create_line(570, 420, 820, 420 )
        bsn_canvas.create_line(570, 445, 820, 445 )
        
        bsn_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(630, 285, text="$200.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(790, 285, text="$200.00", fill="black", font=('Helvetica 10'))

        bsn_canvas.create_text(790, 310, text="$200.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(795, 335, text="$18.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(795, 360, text="$20.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(790, 385, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        bsn_canvas.create_text(790, 410, text="$100.00", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(790, 435, text="$138.00", fill="black", font=('Helvetica 10'))

        bsn_canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(615, 385, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        bsn_canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        bsn_canvas.create_line(150, 470, 800, 470, fill='orange')
        bsn_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
        
        bsn_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_line(150, 620, 795, 620, fill='orange')
        bsn_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        bsn_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
    else:
        pass

logo_just_var = StringVar()
inv_cn_stl = ttk.Combobox(Invoice_setting_frame_cpy,textvariable=logo_just_var)
inv_cn_stl.place(x=770 ,y=40, width=220)
inv_cn_stl.bind("<<ComboboxSelected>>", styl_can_def)
inv_cn_stl["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
inv_cn_stl.current(0)
por_sql_st='select * from company'
fbcursor.execute(por_sql_st)
cmpy_dtl=fbcursor.fetchone()
if  cmpy_dtl[1] is not None:      
  pro_mn_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
  pro_mn_frame.pack(expand=True, fill=BOTH)
  pro_mn_frame.place(x=247,y=90)
  pro_mn_canvas=Canvas(pro_mn_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
  vertibar=Scrollbar(pro_mn_frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=pro_mn_canvas.yview)
        
  pro_mn_canvas.config(width=953,height=300)
  pro_mn_canvas.config(yscrollcommand=vertibar.set)
  pro_mn_canvas.pack(expand=True,side=LEFT,fill=BOTH)
  pro_mn_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  pro_mn_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    inv_image = Image.open("images/"+cmpy_dtl[13])
    inv_resize_image = inv_image.resize((200,75))
    inv_image = ImageTk.PhotoImage(inv_resize_image)
  
    inv_logo = Label(pro_mn_canvas,width=200,height=75, bg="white",image = inv_image) 
    inv_window_image = pro_mn_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
    inv_logo.photo = inv_image
  except:
    pro_mn_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
    
        
  pro_mn_canvas.create_text(195, 150, text="Invoice#",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(205, 170, text="Invoicedate",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(200, 190, text="Due date",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(191, 210, text="Terms",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(210, 230, text="Invoice ref.#",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(350, 150, text="INV1/2022",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(350, 170, text="03-05-2022",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(350, 190, text="18-05-2022",justify=LEFT, fill="black", font=('Helvetica 11'))
  pro_mn_canvas.create_text(340, 210, text="NET 15",justify=LEFT, fill="black", font=('Helvetica 11'))   
        
  labelcmp=Label(pro_mn_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
  window = pro_mn_canvas.create_window(430,80, anchor="nw", window=labelcmp)

  labelcmpl=Label(pro_mn_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
  windowl = pro_mn_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

        
  pro_mn_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 9'))
  pro_mn_canvas.create_text(765, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))

  pro_mn_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
  pro_mn_canvas.create_text(205, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
  pro_mn_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  pro_mn_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  pro_mn_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  pro_mn_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
  s = ttk.Style()
  s.configure('Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

  tree=ttk.Treeview(pro_mn_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
  window = pro_mn_canvas.create_window(120, 340, anchor="nw", window=tree)

  pro_mn_canvas.create_line(120, 390, 820, 390 )
  pro_mn_canvas.create_line(120, 340, 120, 365 )
  pro_mn_canvas.create_line(120, 365, 120, 390 )
  pro_mn_canvas.create_line(820, 340, 820, 540 )
  pro_mn_canvas.create_line(740, 340, 740, 540 )
  pro_mn_canvas.create_line(570, 340, 570, 540 )
  pro_mn_canvas.create_line(570, 415, 820, 415 )
  pro_mn_canvas.create_line(570, 440, 820, 440 )
  pro_mn_canvas.create_line(570, 465, 820, 465 )
  pro_mn_canvas.create_line(570, 490, 820, 490 )
  pro_mn_canvas.create_line(570, 515, 820, 515 )
  pro_mn_canvas.create_line(650, 340, 650, 390 )
  pro_mn_canvas.create_line(220, 340, 220, 390 )
  pro_mn_canvas.create_line(570, 540, 820, 540 )

  pro_mn_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

  pro_mn_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

  pro_mn_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

  pro_mn_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

  pro_mn_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  pro_mn_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

  pro_mn_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

  pro_mn_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  pro_mn_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
  pro_mn_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_line(150, 620, 795, 620)
        

  pro_mn_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  pro_mn_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
else:
        frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
        frame_pro1.pack(expand=True, fill=BOTH)
        frame_pro1.place(x=247,y=90)
        inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=inv_pro1_canvas.yview)
        
        inv_pro1_canvas.config(width=953,height=300)
        inv_pro1_canvas.config(yscrollcommand=vertibar.set)
        inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        inv_pro1_canvas.create_text(195, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(205, 170, text="Invoicedate", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
        inv_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))   
        
        inv_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))

        inv_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(750, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
        inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        s = ttk.Style()
        s.configure('Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

        tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
        window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

        inv_pro1_canvas.create_line(120, 390, 820, 390 )
        inv_pro1_canvas.create_line(120, 340, 120, 365 )
        inv_pro1_canvas.create_line(120, 365, 120, 390 )
        inv_pro1_canvas.create_line(820, 340, 820, 540 )
        inv_pro1_canvas.create_line(740, 340, 740, 540 )
        inv_pro1_canvas.create_line(570, 340, 570, 540 )
        inv_pro1_canvas.create_line(570, 415, 820, 415 )
        inv_pro1_canvas.create_line(570, 440, 820, 440 )
        inv_pro1_canvas.create_line(570, 465, 820, 465 )
        inv_pro1_canvas.create_line(570, 490, 820, 490 )
        inv_pro1_canvas.create_line(570, 515, 820, 515 )
        inv_pro1_canvas.create_line(650, 340, 650, 390 )
        inv_pro1_canvas.create_line(220, 340, 220, 390 )
        inv_pro1_canvas.create_line(570, 540, 820, 540 )

        inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(610, 372, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(710, 372, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 372, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(790, 404, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(792, 428, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(792, 454, text="0", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(790, 479, text="0", fill="black", font=('Helvetica 10 bold'))
        inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        inv_pro1_canvas.create_text(790, 502, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(790, 526, text="0", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        inv_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_line(150, 620, 795, 620)
        

        inv_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        inv_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


######################################################################################tab 04 Orders
ord_set_frm=Frame(tab04, relief=GROOVE, bg="#f8f8f2")
ord_set_frm.pack(side="top", fill=BOTH)

ord_set_frm_cpy=Frame(ord_set_frm, bg="#f5f3f2", height=700)
ord_set_frm_cpy.pack(side="top", fill=BOTH)
ord_ver = Label(ord_set_frm_cpy,text="Order# prefix")
ord_ver.place(x=5,y=40)

ord_lft_tp = Listbox(ord_set_frm, height=1)
ord_lft_tp.insert(END, "ORD")
ord_lft_tp.place(x=100,y=40)

ordset_ver = Label(ord_set_frm_cpy,text="Starting estimate number")
ordset_ver.place(x=25,y=80)

ord_spn_bx = Spinbox(ord_set_frm_cpy,from_=1,to=1000000,width=15)
ord_spn_bx.place(x=50,y=100)

ordset_ver = Label(ord_set_frm_cpy,text="Header box background color")
ordset_ver.place(x=5,y=140)

ord_man_var = StringVar()
ord_cmb_bx = ttk.Combobox(ord_set_frm_cpy,textvariable=ord_man_var)
ord_cmb_bx.place(x=6 ,y=160)
ord_cmb_bx['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
ord_cmb_bx.current(0)

ordset_ver = Label(ord_set_frm_cpy,text="Customize Estimate text labels")
ordset_ver.place(x=5,y=190)



ord_lft_tp1 = Text(ord_set_frm, height=1, width=25, font=('Calibri 10'))
ord_lft_tp1.insert(END, "Order")
ord_lft_tp1.place(x=5,y=220)
ord_lft_tp2 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
ord_lft_tp2.insert(END, "Order#")
ord_lft_tp2.place(x=5,y=240)
ord_lft_tp3 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
ord_lft_tp3.insert(END, "Order date")
ord_lft_tp3.place(x=5,y=260) 
ord_lft_tp4 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
ord_lft_tp4.insert(END, "Due date")
ord_lft_tp4.place(x=5,y=280)
ord_lft_tp5 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
ord_lft_tp5.insert(END, "Order to")
ord_lft_tp5.place(x=5,y=300)
ord_lft_tp6 = Text(ord_set_frm, height=3,width=25, font=('Calibri 10'))
ord_lft_tp6.insert(END, "Order total")
ord_lft_tp6.place(x=5,y=320)



ord_s1 = StringVar(ord_set_frm, "Order")


ordset_ver = Label(ord_set_frm_cpy,text="Default Order template(example,click on preview for mouse scrolling)")
ordset_ver.place(x=248,y=55 )

ordset_ver = Label(ord_set_frm_cpy,text="Default Order template")
ordset_ver.place(x=619,y=40)



ordset_messagelbframe=LabelFrame(ord_set_frm_cpy,text="Predefined terms and conditions text for estimates", height=100, width=980)
ordset_messagelbframe.place(x=248, y=400)

ord_scrl_txt = scrolledtext.ScrolledText(ord_set_frm_cpy, undo=True,width=115,height=4)
ord_scrl_txt.place(x=260,y=425)



ordset_bttermadd = Button(ord_set_frm_cpy,text="Restore defaults")
ordset_bttermadd.place(x=32,y=450)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~order drop
def ord_main_mn(event):
    cmp_mn_var=ord_man_var.get()
    por_sql_st='select * from company'
    fbcursor.execute(por_sql_st)
    cmpy_dtls=fbcursor.fetchone()

    if cmp_mn_var == 'Professional 1 (logo on left side)':
      if cmpy_dtls[1] is not None:
        ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_pro1_frame.pack(expand=True, fill=BOTH)
        ord_pro1_frame.place(x=247,y=90)
        ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_pro1_canvas.yview)
        
        ord_pro1_canvas.config(width=953,height=300)
        ord_pro1_canvas.config(yscrollcommand=vertibar.set)
        ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(ord_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = ord_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(350, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        labelcmp=Label(ord_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
        window = ord_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(ord_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
        windowl = ord_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

        
        ord_pro1_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(770, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
     
        ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        s = ttk.Style()
        s.configure('Treeview.Heading', background=''+ ordset_win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
        window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_pro1_canvas.create_line(120, 390, 820, 390 )
        ord_pro1_canvas.create_line(120, 340, 120, 365 )
        ord_pro1_canvas.create_line(120, 365, 120, 390 )
        ord_pro1_canvas.create_line(820, 340, 820, 540 )
        ord_pro1_canvas.create_line(740, 340, 740, 540 )
        ord_pro1_canvas.create_line(570, 340, 570, 540 )
        ord_pro1_canvas.create_line(570, 415, 820, 415 )
        ord_pro1_canvas.create_line(570, 440, 820, 440 )
        ord_pro1_canvas.create_line(570, 465, 820, 465 )
        ord_pro1_canvas.create_line(570, 490, 820, 490 )
        ord_pro1_canvas.create_line(570, 515, 820, 515 )
        ord_pro1_canvas.create_line(650, 340, 650, 390 )
        ord_pro1_canvas.create_line(220, 340, 220, 390 )
        ord_pro1_canvas.create_line(570, 540, 820, 540 )

        ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        ord_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_line(150, 620, 795, 620)
        

        ord_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_pro1_frame.pack(expand=True, fill=BOTH)
        ord_pro1_frame.place(x=247,y=90)
        ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_pro1_canvas.yview)
        
        ord_pro1_canvas.config(width=953,height=300)
        ord_pro1_canvas.config(yscrollcommand=vertibar.set)
        ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(350, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        ord_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        ord_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(750, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
        ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        s = ttk.Style()
        s.configure('Treeview.Heading', background=''+ ordset_win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
        window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_pro1_canvas.create_line(120, 390, 820, 390 )
        ord_pro1_canvas.create_line(120, 340, 120, 365 )
        ord_pro1_canvas.create_line(120, 365, 120, 390 )
        ord_pro1_canvas.create_line(820, 340, 820, 540 )
        ord_pro1_canvas.create_line(740, 340, 740, 540 )
        ord_pro1_canvas.create_line(570, 340, 570, 540 )
        ord_pro1_canvas.create_line(570, 415, 820, 415 )
        ord_pro1_canvas.create_line(570, 440, 820, 440 )
        ord_pro1_canvas.create_line(570, 465, 820, 465 )
        ord_pro1_canvas.create_line(570, 490, 820, 490 )
        ord_pro1_canvas.create_line(570, 515, 820, 515 )
        ord_pro1_canvas.create_line(650, 340, 650, 390 )
        ord_pro1_canvas.create_line(220, 340, 220, 390 )
        ord_pro1_canvas.create_line(570, 540, 820, 540 )

        ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
        ord_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_line(150, 620, 795, 620)
        

        ord_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  #-----------------------------------------------------------------------Professional 2 (logo on right side)
    elif cmp_mn_var == 'Professional 2 (logo on right side)':
      if cmpy_dtls[1] is not None:
        ord_pro2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_pro2_frame.pack(expand=True, fill=BOTH)
        ord_pro2_frame.place(x=247,y=90)
        
        ord_pro2_canvas=Canvas(ord_pro2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(ord_pro2_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_pro2_canvas.yview)
        ord_pro2_canvas.config(width=953,height=300)
        
        ord_pro2_canvas.config(yscrollcommand=vertibar.set)
        ord_pro2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_pro2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_pro2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(ord_pro2_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = ord_pro2_canvas.create_window(800, 60, anchor="ne", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          ord_pro2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        labelcmp=Label(ord_pro2_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
        window = ord_pro2_canvas.create_window(150,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(ord_pro2_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
        windowl = ord_pro2_canvas.create_window(155 ,110, anchor="nw", window=labelcmpl)
        
        ord_pro2_canvas.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
        ord_pro2_canvas.create_text(185, 205, text="Order",justify=LEFT, fill="black", font=('Helvetica 14 bold'))

        ord_pro2_canvas.create_text(205, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        ord_pro2_canvas.create_text(502, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(515, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(505, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(680, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
          
        ord_pro2_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_pro2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_pro2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(ord_pro2_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = ord_pro2_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_pro2_canvas.create_line(120, 390, 820, 390 )
        ord_pro2_canvas.create_line(120, 340, 120, 365 )
        ord_pro2_canvas.create_line(120, 365, 120, 390 )
        ord_pro2_canvas.create_line(820, 340, 820, 540 )
        ord_pro2_canvas.create_line(740, 340, 740, 540 )
        ord_pro2_canvas.create_line(570, 340, 570, 540 )
        ord_pro2_canvas.create_line(570, 415, 820, 415 )
        ord_pro2_canvas.create_line(570, 440, 820, 440 )
        ord_pro2_canvas.create_line(570, 465, 820, 465 )
        ord_pro2_canvas.create_line(570, 490, 820, 490 )
        ord_pro2_canvas.create_line(570, 515, 820, 515 )
        ord_pro2_canvas.create_line(650, 340, 650, 390 )
        ord_pro2_canvas.create_line(220, 340, 220, 390 )
        ord_pro2_canvas.create_line(570, 540, 820, 540 )

        ord_pro2_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_pro2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_pro2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_line(150, 620, 795, 620)
        ord_pro2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        ord_pro2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_pro2_frame.pack(expand=True, fill=BOTH)
        ord_pro2_frame.place(x=247,y=90)
        
        ord_pro2_canvas=Canvas(ord_pro2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(ord_pro2_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_pro2_canvas.yview)
        ord_pro2_canvas.config(width=953,height=300)
        
        ord_pro2_canvas.config(yscrollcommand=vertibar.set)
        ord_pro2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_pro2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_pro2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
        ord_pro2_canvas.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        ord_pro2_canvas.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(225, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
        ord_pro2_canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
        ord_pro2_canvas.create_text(502, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(515, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(505, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(680, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        ord_pro2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
          
        ord_pro2_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_pro2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_pro2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_pro2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(ord_pro2_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = ord_pro2_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_pro2_canvas.create_line(120, 390, 820, 390 )
        ord_pro2_canvas.create_line(120, 340, 120, 365 )
        ord_pro2_canvas.create_line(120, 365, 120, 390 )
        ord_pro2_canvas.create_line(820, 340, 820, 540 )
        ord_pro2_canvas.create_line(740, 340, 740, 540 )
        ord_pro2_canvas.create_line(570, 340, 570, 540 )
        ord_pro2_canvas.create_line(570, 415, 820, 415 )
        ord_pro2_canvas.create_line(570, 440, 820, 440 )
        ord_pro2_canvas.create_line(570, 465, 820, 465 )
        ord_pro2_canvas.create_line(570, 490, 820, 490 )
        ord_pro2_canvas.create_line(570, 515, 820, 515 )
        ord_pro2_canvas.create_line(650, 340, 650, 390 )
        ord_pro2_canvas.create_line(220, 340, 220, 390 )
        ord_pro2_canvas.create_line(570, 540, 820, 540 )

        ord_pro2_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_pro2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_pro2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        ord_pro2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_line(150, 620, 795, 620)
        ord_pro2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_pro2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  #----------------------------------------------------------------------Simplified 1 (logo on left side)
    elif cmp_mn_var == 'Simplified 1 (logo on left side)':
      if cmpy_dtls[1] is not None:
        ord_smply_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_smply_frame.pack(expand=True, fill=BOTH)
        ord_smply_frame.place(x=247,y=90)
        ord_smply_canvas=Canvas(ord_smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(ord_smply_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_smply_canvas.yview)
        ord_smply_canvas.config(width=953,height=300)

        ord_smply_canvas.config(yscrollcommand=vertibar.set)
        ord_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(ord_smply_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = ord_smply_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          ord_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        ord_smply_canvas.create_text(202, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(215, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(350, 150, text="EST1/2022", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(350, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(350, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        labelcmp=Label(ord_smply_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
        window = ord_smply_canvas.create_window(430,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(ord_smply_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
        windowl = ord_smply_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

        
        ord_smply_canvas.create_text(740, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 9'))
        ord_smply_canvas.create_text(765, 205, text="Order", fill="black", font=('Helvetica 14 bold'))

        
        ord_smply_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(ord_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = ord_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_smply_canvas.create_line(120, 390, 820, 390 )
        ord_smply_canvas.create_line(120, 340, 120, 365 )
        ord_smply_canvas.create_line(120, 365, 120, 390 )
        ord_smply_canvas.create_line(820, 340, 820, 540 )
        ord_smply_canvas.create_line(740, 340, 740, 540 )
        ord_smply_canvas.create_line(570, 390, 570, 540 )
        ord_smply_canvas.create_line(570, 415, 820, 415 )
        ord_smply_canvas.create_line(570, 440, 820, 440 )
        ord_smply_canvas.create_line(570, 465, 820, 465 )
        ord_smply_canvas.create_line(570, 490, 820, 490 )
        ord_smply_canvas.create_line(570, 515, 820, 515 )
        ord_smply_canvas.create_line(650, 340, 650, 390 )
        ord_smply_canvas.create_line(570, 540, 820, 540 )

        
        ord_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_smply_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_smply_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_line(150, 620, 795, 620)
        ord_smply_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:

        ord_smply_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_smply_frame.pack(expand=True, fill=BOTH)
        ord_smply_frame.place(x=247,y=90)
        ord_smply_canvas=Canvas(ord_smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(ord_smply_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_smply_canvas.yview)
        ord_smply_canvas.config(width=953,height=300)

        ord_smply_canvas.config(yscrollcommand=vertibar.set)
        ord_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        ord_smply_canvas.create_text(202, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(215, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(350, 150, text="EST1/2022", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(350, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(350, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        ord_smply_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        ord_smply_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(750, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
        
        ord_smply_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(ord_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = ord_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_smply_canvas.create_line(120, 390, 820, 390 )
        ord_smply_canvas.create_line(120, 340, 120, 365 )
        ord_smply_canvas.create_line(120, 365, 120, 390 )
        ord_smply_canvas.create_line(820, 340, 820, 540 )
        ord_smply_canvas.create_line(740, 340, 740, 540 )
        ord_smply_canvas.create_line(570, 390, 570, 540 )
        ord_smply_canvas.create_line(570, 415, 820, 415 )
        ord_smply_canvas.create_line(570, 440, 820, 440 )
        ord_smply_canvas.create_line(570, 465, 820, 465 )
        ord_smply_canvas.create_line(570, 490, 820, 490 )
        ord_smply_canvas.create_line(570, 515, 820, 515 )
        ord_smply_canvas.create_line(650, 340, 650, 390 )
        ord_smply_canvas.create_line(570, 540, 820, 540 )

        
        ord_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_smply_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_smply_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        ord_smply_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_line(150, 620, 795, 620)
        ord_smply_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_smply_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #-------------------------------------------------------------------------------Simplified 2 (logo on right side)
    elif cmp_mn_var == 'Simplified 2 (logo on right side)':
      if cmpy_dtls[1] is not None:
        ord_smply2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_smply2_frame.pack(expand=True, fill=BOTH)
        ord_smply2_frame.place(x=247,y=90)

        ord_smply2_canvas=Canvas(ord_smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(ord_smply2_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_smply2_canvas.yview)
        ord_smply2_canvas.config(width=953,height=300)

        ord_smply2_canvas.config(yscrollcommand=vertibar.set)
        ord_smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(ord_smply2_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = ord_smply2_canvas.create_window(800, 60, anchor="ne", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          ord_smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        labelcmp=Label(ord_smply2_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
        window = ord_smply2_canvas.create_window(150,80, anchor="nw", window=labelcmp)

        labelcmpl=Label(ord_smply2_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
        windowl = ord_smply2_canvas.create_window(155 ,110, anchor="nw", window=labelcmpl)
        
        ord_smply2_canvas.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
        ord_smply2_canvas.create_text(185, 205, text="Order",justify=LEFT, fill="black", font=('Helvetica 14 bold'))

       

        ord_smply2_canvas.create_text(502, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(515, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(505, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(680, 150, text="EST1/2022", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        ord_smply2_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(ord_smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = ord_smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_smply2_canvas.create_line(120, 390, 820, 390 )
        ord_smply2_canvas.create_line(120, 340, 120, 365 )
        ord_smply2_canvas.create_line(120, 365, 120, 390 )
        ord_smply2_canvas.create_line(820, 340, 820, 540 )
        ord_smply2_canvas.create_line(740, 340, 740, 540 )
        ord_smply2_canvas.create_line(570, 390, 570, 540 )
        ord_smply2_canvas.create_line(570, 415, 820, 415 )
        ord_smply2_canvas.create_line(570, 440, 820, 440 )
        ord_smply2_canvas.create_line(570, 465, 820, 465 )
        ord_smply2_canvas.create_line(570, 490, 820, 490 )
        ord_smply2_canvas.create_line(570, 515, 820, 515 )
        ord_smply2_canvas.create_line(650, 340, 650, 390 )
        ord_smply2_canvas.create_line(570, 540, 820, 540 )

        
        ord_smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_smply2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_smply2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_line(150, 620, 795, 620)
        ord_smply2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        ord_smply2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_smply2_frame.pack(expand=True, fill=BOTH)
        ord_smply2_frame.place(x=247,y=90)

        ord_smply2_canvas=Canvas(ord_smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(ord_smply2_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_smply2_canvas.yview)
        ord_smply2_canvas.config(width=953,height=300)

        ord_smply2_canvas.config(yscrollcommand=vertibar.set)
        ord_smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        ord_smply2_canvas.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        ord_smply2_canvas.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(225, 205, text="Order", fill="black", font=('Helvetica 14 bold'))

        ord_smply2_canvas.create_text(502, 150, text="Order#", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(515, 170, text="Order date", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(505, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(680, 150, text="EST1/2022", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
        ord_smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        ord_smply2_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
        ord_smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        ord_smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        ord_smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(ord_smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
        
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
        
        window = ord_smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

        ord_smply2_canvas.create_line(120, 390, 820, 390 )
        ord_smply2_canvas.create_line(120, 340, 120, 365 )
        ord_smply2_canvas.create_line(120, 365, 120, 390 )
        ord_smply2_canvas.create_line(820, 340, 820, 540 )
        ord_smply2_canvas.create_line(740, 340, 740, 540 )
        ord_smply2_canvas.create_line(570, 390, 570, 540 )
        ord_smply2_canvas.create_line(570, 415, 820, 415 )
        ord_smply2_canvas.create_line(570, 440, 820, 440 )
        ord_smply2_canvas.create_line(570, 465, 820, 465 )
        ord_smply2_canvas.create_line(570, 490, 820, 490 )
        ord_smply2_canvas.create_line(570, 515, 820, 515 )
        ord_smply2_canvas.create_line(650, 340, 650, 390 )
        ord_smply2_canvas.create_line(570, 540, 820, 540 )

        
        ord_smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_smply2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

        ord_smply2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        ord_smply2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_line(150, 620, 795, 620)
        ord_smply2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_smply2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #-----------------------------------------------------------------------------------------------Business Classic-
    elif cmp_mn_var == 'Business Classic':
      if cmpy_dtls[1] is not None:
        ord_bs_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_bs_frame.pack(expand=True, fill=BOTH)
        ord_bs_frame.place(x=247,y=90)
        
        ord_bs_canvas=Canvas(ord_bs_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(ord_bs_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_bs_canvas.yview)
        ord_bs_canvas.config(width=953,height=300)
        
        ord_bs_canvas.config(yscrollcommand=vertibar.set)
        ord_bs_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_bs_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_bs_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_line(150, 70, 800, 70, fill='orange')
        try:
          inv_image = Image.open("images/"+cmpy_dtl[13])
          inv_resize_image = inv_image.resize((200,75))
          inv_image = ImageTk.PhotoImage(inv_resize_image)
        
          inv_logo = Label(ord_bs_canvas,width=200,height=75, bg="white",image = inv_image) 
          inv_window_image = ord_bs_canvas.create_window(140, 125, anchor="nw", window=inv_logo)
          inv_logo.photo = inv_image
        except:
          ord_bs_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        labelcmp=Label(ord_bs_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=30, height=1)
        window = ord_bs_canvas.create_window(345,100, anchor="nw", window=labelcmp)

        labelcmpl=Label(ord_bs_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
        windowl = ord_bs_canvas.create_window(350 ,130, anchor="nw", window=labelcmpl)
        
        ord_bs_canvas.create_text(405, 210, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
        
        ord_bs_canvas.create_text(720, 130, text="John Doe\n381 South Beadford Road\nBedford Corner,NY10549\nUnited States", fill="black", font=('Helvetica 11'))

        ord_bs_canvas.create_text(659, 180, text="Order", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(675, 210, text="Order date", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(659, 240, text="Due date", fill="black", font=('Helvetica 11'))

        

        

        ord_bs_canvas.create_text(776, 180, text="ORD1/2022", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))
        tree=ttk.Treeview(ord_bs_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = ord_bs_canvas.create_window(120, 255, anchor="nw", window=tree)

        ord_bs_canvas.create_line(120, 295, 820, 295 )
        ord_bs_canvas.create_line(120, 255, 120, 295 )
        ord_bs_canvas.create_line(320, 255, 320, 295 )
        ord_bs_canvas.create_line(570, 255, 570, 295 )
        ord_bs_canvas.create_line(660, 255, 660, 295 )
        ord_bs_canvas.create_line(740, 255, 740, 295 )
        ord_bs_canvas.create_line(820, 255, 820, 445 )
        ord_bs_canvas.create_line(570, 320, 820, 320 )
        ord_bs_canvas.create_line(570, 345, 820, 345 )
        ord_bs_canvas.create_line(570, 370, 820, 370 )
        ord_bs_canvas.create_line(570, 395, 820, 395 )
        ord_bs_canvas.create_line(570, 420, 820, 420 )
        ord_bs_canvas.create_line(570, 445, 820, 445 )
        
        ord_bs_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(630, 285, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(790, 285, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_bs_canvas.create_text(790, 310, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(795, 335, text="$18.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(795, 360, text="$20.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(790, 385, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_bs_canvas.create_text(790, 410, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(790, 435, text="$138.00", fill="black", font=('Helvetica 10'))

        ord_bs_canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(615, 385, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        ord_bs_canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        ord_bs_canvas.create_line(150, 470, 800, 470, fill='orange')
        ord_bs_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
        
        ord_bs_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_line(150, 620, 795, 620, fill='orange')
        ord_bs_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        ord_bs_frame = Frame(ord_set_frm_cpy, width=953, height=300)
        ord_bs_frame.pack(expand=True, fill=BOTH)
        ord_bs_frame.place(x=247,y=90)
        
        ord_bs_canvas=Canvas(ord_bs_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
        vertibar=Scrollbar(ord_bs_frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=ord_bs_canvas.yview)
        ord_bs_canvas.config(width=953,height=300)
        
        ord_bs_canvas.config(yscrollcommand=vertibar.set)
        ord_bs_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        ord_bs_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        ord_bs_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_line(150, 70, 800, 70, fill='orange')
        ord_bs_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        ord_bs_canvas.create_text(500, 115, text="Your Company Name", fill="black", font=('Helvetica 12 '))
        ord_bs_canvas.create_text(525, 140, text="Address line 1", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(525, 155, text="Address line 2", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(525, 170, text="Address line 3", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(525, 185, text="Address line 4", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(534, 200, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(534, 215, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))

        

        ord_bs_canvas.create_text(659, 180, text="Order", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(675, 210, text="Order date", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(659, 240, text="Due date", fill="black", font=('Helvetica 11'))

        

        

        ord_bs_canvas.create_text(776, 180, text="ORD1/2022", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        ord_bs_canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))
        tree=ttk.Treeview(ord_bs_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
        
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
        
        window = ord_bs_canvas.create_window(120, 255, anchor="nw", window=tree)

        ord_bs_canvas.create_line(120, 295, 820, 295 )
        ord_bs_canvas.create_line(120, 255, 120, 295 )
        ord_bs_canvas.create_line(320, 255, 320, 295 )
        ord_bs_canvas.create_line(570, 255, 570, 295 )
        ord_bs_canvas.create_line(660, 255, 660, 295 )
        ord_bs_canvas.create_line(740, 255, 740, 295 )
        ord_bs_canvas.create_line(820, 255, 820, 445 )
        ord_bs_canvas.create_line(570, 320, 820, 320 )
        ord_bs_canvas.create_line(570, 345, 820, 345 )
        ord_bs_canvas.create_line(570, 370, 820, 370 )
        ord_bs_canvas.create_line(570, 395, 820, 395 )
        ord_bs_canvas.create_line(570, 420, 820, 420 )
        ord_bs_canvas.create_line(570, 445, 820, 445 )
        
        ord_bs_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(630, 285, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(790, 285, text="$200.00", fill="black", font=('Helvetica 10'))

        ord_bs_canvas.create_text(790, 310, text="$200.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(795, 335, text="$18.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(795, 360, text="$20.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(790, 385, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        ord_bs_canvas.create_text(790, 410, text="$100.00", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(790, 435, text="$138.00", fill="black", font=('Helvetica 10'))

        ord_bs_canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(615, 385, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
        ord_bs_canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        ord_bs_canvas.create_line(150, 470, 800, 470, fill='orange')
        ord_bs_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
        
        ord_bs_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_line(150, 620, 795, 620, fill='orange')
        ord_bs_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        ord_bs_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
    else:
        pass

por_sql_st='select * from company'
fbcursor.execute(por_sql_st)
cmpy_dtls=fbcursor.fetchone()
if cmpy_dtls[1] is not None:
  ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
  ord_pro1_frame.pack(expand=True, fill=BOTH)
  ord_pro1_frame.place(x=247,y=90)
  ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
  vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=ord_pro1_canvas.yview)
        
  ord_pro1_canvas.config(width=953,height=300)
  ord_pro1_canvas.config(yscrollcommand=vertibar.set)
  ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
  ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    inv_image = Image.open("images/"+cmpy_dtl[13])
    inv_resize_image = inv_image.resize((200,75))
    inv_image = ImageTk.PhotoImage(inv_resize_image)
  
    inv_logo = Label(ord_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
    inv_window_image = ord_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
    inv_logo.photo = inv_image
  except:
    ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
  ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(350, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

  labelcmp=Label(ord_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
  window = ord_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

  labelcmpl=Label(ord_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
  windowl = ord_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

        
  ord_pro1_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 9'))
  ord_pro1_canvas.create_text(770, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
  
  ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
  ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
  ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
  s = ttk.Style()
  s.configure('Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')

  tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
  window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

  ord_pro1_canvas.create_line(120, 390, 820, 390 )
  ord_pro1_canvas.create_line(120, 340, 120, 365 )
  ord_pro1_canvas.create_line(120, 365, 120, 390 )
  ord_pro1_canvas.create_line(820, 340, 820, 540 )
  ord_pro1_canvas.create_line(740, 340, 740, 540 )
  ord_pro1_canvas.create_line(570, 340, 570, 540 )
  ord_pro1_canvas.create_line(570, 415, 820, 415 )
  ord_pro1_canvas.create_line(570, 440, 820, 440 )
  ord_pro1_canvas.create_line(570, 465, 820, 465 )
  ord_pro1_canvas.create_line(570, 490, 820, 490 )
  ord_pro1_canvas.create_line(570, 515, 820, 515 )
  ord_pro1_canvas.create_line(650, 340, 650, 390 )
  ord_pro1_canvas.create_line(220, 340, 220, 390 )
  ord_pro1_canvas.create_line(570, 540, 820, 540 )

  ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  ord_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

  ord_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
  ord_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_line(150, 620, 795, 620)
        

  ord_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
else:
  ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
  ord_pro1_frame.pack(expand=True, fill=BOTH)
  ord_pro1_frame.place(x=247,y=90)
  ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
  vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=ord_pro1_canvas.yview)
        
  ord_pro1_canvas.config(width=953,height=300)
  ord_pro1_canvas.config(yscrollcommand=vertibar.set)
  ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
  ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
        
  ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(350, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
  ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

  ord_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
  ord_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(750, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
  ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
  ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
  ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
  s = ttk.Style()
  s.configure('Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')

  tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

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
        
  window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

  ord_pro1_canvas.create_line(120, 390, 820, 390 )
  ord_pro1_canvas.create_line(120, 340, 120, 365 )
  ord_pro1_canvas.create_line(120, 365, 120, 390 )
  ord_pro1_canvas.create_line(820, 340, 820, 540 )
  ord_pro1_canvas.create_line(740, 340, 740, 540 )
  ord_pro1_canvas.create_line(570, 340, 570, 540 )
  ord_pro1_canvas.create_line(570, 415, 820, 415 )
  ord_pro1_canvas.create_line(570, 440, 820, 440 )
  ord_pro1_canvas.create_line(570, 465, 820, 465 )
  ord_pro1_canvas.create_line(570, 490, 820, 490 )
  ord_pro1_canvas.create_line(570, 515, 820, 515 )
  ord_pro1_canvas.create_line(650, 340, 650, 390 )
  ord_pro1_canvas.create_line(220, 340, 220, 390 )
  ord_pro1_canvas.create_line(570, 540, 820, 540 )

  ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  ord_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

  ord_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
  ord_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_line(150, 620, 795, 620)
        

  ord_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  ord_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

ord_man_var = StringVar()
ord_cmb_bx_mn = ttk.Combobox(ord_set_frm_cpy,textvariable=ord_man_var)
ord_cmb_bx_mn.place(x=770 ,y=40, width=220)
ord_cmb_bx_mn.bind("<<ComboboxSelected>>", ord_main_mn)
ord_cmb_bx_mn["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
ord_cmb_bx_mn.current(0)

root.mainloop()