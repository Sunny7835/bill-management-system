from tkinter import *
from PIL import ImageTk
import math,random
from tkinter import messagebox
import os
import re
import time
#from login import user
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Billing Software")
        self.root.resizable(False,False)
        bg_color='gray'

        self.titleFrame=Frame(self.root)
        self.titleFrame.place(x=0,y=0)
        #time
        self.datetimeLabel=Label(self.titleFrame,font=('time new roman',14,'bold'),fg='red')
        # self.datetimeLabel.grid(x=5,y=5)
        self.datetimeLabel.grid(row=0,column=0,padx=2)
        self.clock()

        self.title=Label(self.titleFrame,text="Billing Software",width=50,bd=8,relief=GROOVE,
        bg=bg_color,fg='white',font=('time new roman',21,'bold'))
        # title.pack(fill=X)
        self.title.grid(row=0,column=1,padx=2,pady=2)
        
        
        self.usernameImage=ImageTk.PhotoImage(file='images/stu.png')
        #username
        self.usernameLabel=Label(self.titleFrame,image=self.usernameImage,width=155,height=37,text="user",
        compound=LEFT,relief=GROOVE,font=('times new roman',18,'bold'),bg=bg_color,bd=6,fg='white')
        self.usernameLabel.grid(row=0,column=2,padx=1,pady=2)

        # logout button
        logoutButton=Button(self.titleFrame,text="Log Out",width=10,bd=6,relief=GROOVE,bg=bg_color,fg='white',
        font=('time new roman',16,'bold'),cursor='hand2',activeforeground='red',command=self.logout)
        # title.pack(fill=X)
        logoutButton.grid(row=0,column=3,padx=1,pady=2)
        # cosmetics variables----------

        self.lipstik=IntVar()
        self.facewash=IntVar()
        self.soap=IntVar()
        self.bodylosan=IntVar()
        self.powder=IntVar()
        self.ishadow=IntVar()
        #grocery variables----------
        self.ata=IntVar()
        self.dal=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.saus=IntVar()
        #cold variables----------
        self.thumsup=IntVar()
        self.frooti=IntVar()
        self.sprite=IntVar()
        self.dew=IntVar()
        self.maaza=IntVar()
        self.nimbooz=IntVar()

        #Total Product Price & Tax Variables
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_price=StringVar()
        #Total Product Tax
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_tax=StringVar()

        #customer --------------------
        self.c_name=StringVar()
        self.name=re.compile("[a-z]+")
        self.c_phn=StringVar()
        self.mob=re.compile("[6-9]\d{9}")
        print(type(self.mob))
        self.bill_no=StringVar()
        
        random_bill_no=random.randint(10000,99999)
        self.bill_no.set(str(random_bill_no))
        self.search_bill=StringVar()

        #custmr Detail Frame
        cdetailLabelFrame=LabelFrame(self.root,text="Customer Details",bg=bg_color,fg='gold',
        font=('time new roman',10,'bold'),pady=2)
        cdetailLabelFrame.place(x=0,y=60,relwidth=1)

        cname_Label=Label(cdetailLabelFrame,text="Customer Name:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        cname_Label.grid(row=0,column=0,padx=5)

        cname_Entry=Entry(cdetailLabelFrame,font=('time new roman', 15),textvariable=self.c_name)
        cname_Entry.grid(row=0,column=1,padx=5)

        cphn_Label=Label(cdetailLabelFrame,text="Mob No:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        cphn_Label.grid(row=0,column=2,padx=5)

        cphn_Entry=Entry(cdetailLabelFrame,font=('time new roman', 15),textvariable=self.c_phn)
        cphn_Entry.grid(row=0,column=3,padx=5)

        cbill_Label=Label(cdetailLabelFrame,text="Bill Number:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        cbill_Label.grid(row=0,column=4,padx=5)

        cbill_Entry=Entry(cdetailLabelFrame,font=('time new roman', 15),textvariable=self.search_bill)
        cbill_Entry.grid(row=0,column=5,padx=5)

        bill_btn=Button(cdetailLabelFrame,command=self.findBill, text='Search',font=('time new roman', 10,'bold'),width=15,cursor='hand2')
        bill_btn.grid(row=0,column=6,padx=10)

        #---Cometics Frame
        cosmetic_itm_LabelFrame=LabelFrame(self.root,text="Comsetics Items",bg=bg_color,fg='gold',
        font=('time new roman',10,'bold'),pady=2)
        cosmetic_itm_LabelFrame.place(x=5,y=120,width=325,height=380)

        lipstik_Label=Label(cosmetic_itm_LabelFrame,text="Lipstick:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        lipstik_Label.grid(row=0,column=0,padx=5,sticky='w')
        lipstik_Entry=Entry(cosmetic_itm_LabelFrame,textvariable=self.lipstik,font=('time new roman', 15),width=10)
        lipstik_Entry.grid(row=0,column=1,padx=5)

        facewash_Label=Label(cosmetic_itm_LabelFrame,text="FaceWash:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        facewash_Label.grid(row=1,column=0,padx=5,sticky='w')
        facewash_Entry=Entry(cosmetic_itm_LabelFrame,textvariable=self.facewash,font=('time new roman', 15),width=10)
        facewash_Entry.grid(row=1,column=1,padx=5)

        soap_Label=Label(cosmetic_itm_LabelFrame,text="Soap:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        soap_Label.grid(row=2,column=0,padx=5,sticky='w')
        soap_Entry=Entry(cosmetic_itm_LabelFrame,textvariable=self.soap,font=('time new roman', 15),width=10)
        soap_Entry.grid(row=2,column=1,padx=5)

        bodylosan_Label=Label(cosmetic_itm_LabelFrame,text="Bodylosan:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        bodylosan_Label.grid(row=3,column=0,padx=5,sticky='w')
        bodylosan_Entry=Entry(cosmetic_itm_LabelFrame,textvariable=self.bodylosan,font=('time new roman', 15),width=10)
        bodylosan_Entry.grid(row=3,column=1,padx=5)

        powder_Label=Label(cosmetic_itm_LabelFrame,text="Cold-Powder:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        powder_Label.grid(row=4,column=0,padx=5,sticky='w')
        powder_Entry=Entry(cosmetic_itm_LabelFrame,textvariable=self.powder,font=('time new roman', 15),width= 10)
        powder_Entry.grid(row=4,column=1,padx=5)

        ishadow_Label=Label(cosmetic_itm_LabelFrame,text="I-Shadow:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        ishadow_Label.grid(row=5,column=0,padx=5,sticky='w')
        ishadow_Entry=Entry(cosmetic_itm_LabelFrame,textvariable=self.ishadow,font=('time new roman', 15),width= 10)
        ishadow_Entry.grid(row=5,column=1,padx=5)

        #---Grocery Frame
        grocery_LabelFrame=LabelFrame(self.root,text="Grocery Items(1Kg)",bg=bg_color,fg='gold',
        font=('time new roman',10,'bold'),pady=2)
        grocery_LabelFrame.place(x=340,y=120,width=325,height=380)

        ata_Label=Label(grocery_LabelFrame,text="Aashirwaad Aata:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        ata_Label.grid(row=0,column=0,padx=5,sticky='w')
        ata_Entry=Entry(grocery_LabelFrame,textvariable=self.ata,font=('time new roman', 15),width=10)
        ata_Entry.grid(row=0,column=1,padx=5)

        dal_Label=Label(grocery_LabelFrame,text="Pulse:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        dal_Label.grid(row=1,column=0,padx=5,sticky='w')
        dal_Entry=Entry(grocery_LabelFrame,textvariable=self.dal,font=('time new roman', 15),width=10)
        dal_Entry.grid(row=1,column=1,padx=5)

        rice_Label=Label(grocery_LabelFrame,text="Baasmati Rice:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        rice_Label.grid(row=2,column=0,padx=5,sticky='w')
        rice_Entry=Entry(grocery_LabelFrame,textvariable=self.rice,font=('time new roman', 15),width=10)
        rice_Entry.grid(row=2,column=1,padx=5)

        oil_Label=Label(grocery_LabelFrame,text="Soyabean Oil:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        oil_Label.grid(row=3,column=0,padx=5,sticky='w')
        oil_Entry=Entry(grocery_LabelFrame,textvariable=self.oil,font=('time new roman', 15),width=10)
        oil_Entry.grid(row=3,column=1,padx=5)

        sugar_Label=Label(grocery_LabelFrame,text="Sugar:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        sugar_Label.grid(row=4,column=0,padx=5,sticky='w')
        sugar_Entry=Entry(grocery_LabelFrame,textvariable=self.sugar,font=('time new roman', 15),width= 10)
        sugar_Entry.grid(row=4,column=1,padx=5)

        saus_Label=Label(grocery_LabelFrame,text="Tamoto-saus:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        saus_Label.grid(row=5,column=0,padx=5,sticky='w')
        saus_Entry=Entry(grocery_LabelFrame,textvariable=self.saus,font=('time new roman', 15),width= 10)
        saus_Entry.grid(row=5,column=1,padx=5)

        #---Colddrink Frame
        colddrink_LabelFrame=LabelFrame(self.root,text="Colddrinks",bg=bg_color,fg='gold',
        font=('time new roman',10,'bold'),pady=2)
        colddrink_LabelFrame.place(x=670,y=120,width=325,height=380)

        thumsup_Label=Label(colddrink_LabelFrame,text="Thums Up:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        thumsup_Label.grid(row=0,column=0,padx=5,sticky='w')
        thumsup_Entry=Entry(colddrink_LabelFrame,textvariable=self.thumsup,font=('time new roman', 15),width=10)
        thumsup_Entry.grid(row=0,column=1,padx=5)

        frooti_Label=Label(colddrink_LabelFrame,text="Frooti:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        frooti_Label.grid(row=1,column=0,padx=5,sticky='w')
        frooti_Entry=Entry(colddrink_LabelFrame,textvariable=self.frooti,font=('time new roman', 15),width=10)
        frooti_Entry.grid(row=1,column=1,padx=5)

        sprite_Label=Label(colddrink_LabelFrame,text="Sprite:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        sprite_Label.grid(row=2,column=0,padx=5,sticky='w')
        sprite_Entry=Entry(colddrink_LabelFrame,textvariable=self.sprite,font=('time new roman', 15),width=10)
        sprite_Entry.grid(row=2,column=1,padx=5)

        dew_Label=Label(colddrink_LabelFrame,text="Dew:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        dew_Label.grid(row=3,column=0,padx=5,sticky='w')
        dew_Entry=Entry(colddrink_LabelFrame,textvariable=self.dew,font=('time new roman', 15),width=10)
        dew_Entry.grid(row=3,column=1,padx=5)

        maaza_Label=Label(colddrink_LabelFrame,text="Maaza:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        maaza_Label.grid(row=4,column=0,padx=5,sticky='w')
        maaza_Entry=Entry(colddrink_LabelFrame,textvariable=self.maaza,font=('time new roman', 15),width= 10)
        maaza_Entry.grid(row=4,column=1,padx=5)

        nimbooz_Label=Label(colddrink_LabelFrame,text="Nimbooz:",bg=bg_color,font=('time new roman', 15,'bold'),fg='white')
        nimbooz_Label.grid(row=5,column=0,padx=5,sticky='w')
        nimbooz_Entry=Entry(colddrink_LabelFrame,textvariable=self.nimbooz,font=('time new roman', 15),width= 10)
        nimbooz_Entry.grid(row=5,column=1,padx=5)

        #bill Area / Section
        billareaFrame=Frame(self.root,bd=10,relief=GROOVE)
        billareaFrame.place(x=1010,y=120,width=350,height=380)
        bill_title=Label(billareaFrame,text='Bill Area',font=('arial 15 bold'),bd=7,relief=GROOVE)
        bill_title.pack(fill=X)
        scrolY=Scrollbar(billareaFrame,orient=VERTICAL)
        self.txtarea=Text(billareaFrame,yscrollcommand=scrolY.set)
        scrolY.pack(side=RIGHT,fill=Y)
        scrolY.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #Bill Menu LebelFrame
        bill_LabelFrame=LabelFrame(self.root,text="Bill Menu",bg=bg_color,fg='gold',
        font=('time new roman',10,'bold'),pady=2)
        bill_LabelFrame.place(x=0,y=560,relwidth=1,height=140)

        total_cometics_Label=Label(bill_LabelFrame,text="Total Cometics Price",bg=bg_color,font=('times new roman', 14, 'bold'),fg='white')
        total_cometics_Label.grid(row=0,column=0,padx=20,pady=1,sticky='w')
        total_cometics_Entry=Entry(bill_LabelFrame,textvariable=self.cosmetic_price,bd=2)
        total_cometics_Entry.grid(row=0,column=1,padx=10,pady=1)

        total_grocery_Label=Label(bill_LabelFrame,text="Total Grocery Price",bg=bg_color,font=('times new roman', 14, 'bold'),fg='white')
        total_grocery_Label.grid(row=1,column=0,padx=20,pady=1,sticky='w')
        total_grocery_Entry=Entry(bill_LabelFrame,textvariable=self.grocery_price,bd=2)
        total_grocery_Entry.grid(row=1,column=1,padx=10,pady=1)

        total_cold_Label=Label(bill_LabelFrame,text="Total Cold Price",bg=bg_color,font=('times new roman', 14, 'bold'),fg='white')
        total_cold_Label.grid(row=2,column=0,padx=20,pady=1,sticky='w')
        total_cold_Entry=Entry(bill_LabelFrame,textvariable=self.cold_price,bd=2)
        total_cold_Entry.grid(row=2,column=1,padx=10,pady=1)

        #Tax
        cosmeticTaxLabel=Label(bill_LabelFrame,text="Cosmetic Tax",bg=bg_color,font=('times new roman', 14, 'bold'),fg='white')
        cosmeticTaxLabel.grid(row=0,column=2,padx=20,pady=1,sticky='w')
        cosmeticTaxEntry=Entry(bill_LabelFrame,textvariable=self.cosmetic_tax,bd=2)
        cosmeticTaxEntry.grid(row=0,column=3,padx=10,pady=1)

        groceryTaxLabel=Label(bill_LabelFrame,text="Grocery Tax",bg=bg_color,font=('times new roman', 14, 'bold'),fg='white')
        groceryTaxLabel.grid(row=1,column=2,padx=20,pady=1,sticky='w')
        groceryTaxEntry=Entry(bill_LabelFrame,textvariable=self.grocery_tax,bd=2)
        groceryTaxEntry.grid(row=1,column=3,padx=10,pady=1)

        coldTaxLabel=Label(bill_LabelFrame,text="Cold-drink Tax",bg=bg_color,font=('times new roman', 14, 'bold'),fg='white')
        coldTaxLabel.grid(row=2,column=2,padx=20,pady=1,sticky='w')
        coldTaxEntry=Entry(bill_LabelFrame,textvariable=self.cold_tax,bd=2)
        coldTaxEntry.grid(row=2,column=3,padx=10,pady=1)

        #TotalButton
        totalFrame=Frame(bill_LabelFrame,bd=2,relief=GROOVE)
        totalFrame.place(x=750,width=580,height=90)
        totalButton=Button(totalFrame,command=self.total,text='Total Bill',bg='gray',fg='white',bd=5,pady=15,width=9,font=('times new roman', 15, 'bold'),cursor='hand2')
        totalButton.grid(row=0,column=0,padx=4,pady=5)
        gButton=Button(totalFrame,text='Generate Bill',width=13,command=self.billArea,bg='gray',fg='white',bd=5,pady=15,font=('times new roman', 15,'bold'),cursor='hand2')
        gButton.grid(row=0,column=1,padx=3,pady=5)
        cButton=Button(totalFrame,text='Clear Bill',command=self.clearData,bg='gray',fg='white',bd=5,pady=15,width=9,font=('times new roman', 15, 'bold'),cursor='hand2')
        cButton.grid(row=0,column=2,padx=3,pady=5)
        eButton=Button(totalFrame,text='Exit',command=self.exit,bg='gray',fg='white',bd=5,pady=15,width=9,font=('times new roman', 15, 'bold'),cursor='hand2')
        eButton.grid(row=0,column=3,padx=3,pady=5)
        self.welcomeBill()
    def total(self):
        #Single Cosmetic Item Price              
        self.lipstikPrice=self.lipstik.get()*40
        self.facewashPrice=self.facewash.get()*120
        self.soapPrice=self.soap.get()*60
        self.bodylosanPrice=self.bodylosan.get()*40
        self.powderPrice=self.powder.get()*180
        self.ishadowPrice=self.ishadow.get()*140
        # total_cosmetic_price
        self.total_cosmetic_price=float(self.lipstikPrice+self.facewashPrice+
        self.soapPrice+self.bodylosanPrice+self.powderPrice+self.ishadowPrice)
            
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.cosmetictax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set(str(self.cosmetictax))

        #Single Grocery Item Price
        self.ataPrice=self.ata.get()*30
        self.dalPrice=self.dal.get()*190
        self.ricePrice=self.rice.get()*60
        self.oilPrice=self.oil.get()*180
        self.sugarPrice=self.sugar.get()*40
        self.sausPrice=self.saus.get()*60

        # total_Grocery_price
        self.total_grocery_price=float(self.ataPrice+self.dalPrice+
        self.ricePrice+self.oilPrice+self.sugarPrice+self.sausPrice)
                  
        self.grocery_price.set(str(self.total_grocery_price))
        self.grocerytax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set(str(self.grocerytax))

        #Single Cold Drinks Item Price
        self.thumsupPrice=self.thumsup.get()*90
        self.frootiPrice=self.frooti.get()*120
        self.spritePrice=self.sprite.get()*80
        self.dewPrice=self.dew.get()*120
        self.maazaPrice=self.maaza.get()*100
        self.nimboozPrice=self.nimbooz.get()*100

        # total_Cold Drinks_price
        self.total_cold_price=float(self.thumsupPrice+ self.frootiPrice+
        
        self.spritePrice+self.dewPrice+self.maazaPrice+self.nimboozPrice)
                    
        self.cold_price.set(str(self.total_cold_price))
        self.coldtax=round((self.total_cold_price*0.05),2)
        self.cold_tax.set(str(self.coldtax))

        #
        self.TotalBill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_cold_price+
        self.cosmetictax+self.grocerytax+self.coldtax)
    def welcomeBill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\t welcome Bill Area")
            self.txtarea.insert(END,f"\n Bill No:{self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone NO:{self.c_phn.get()}")
            self.txtarea.insert(END,f"\n-------------------------------------")
            self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
            self.txtarea.insert(END,f"\n-------------------------------------")
    
    def billArea(self):
      if(self.c_name.get()=="" or self.c_phn.get()==""):
        messagebox.showwarning("Warning","Please Enter Customer Details")
    #   elif(self.c_phn !=self.mob or self.c_name !=self.name):
    #         messagebox.showwarning("Warning","Please Enter correct Customer Details")
      elif(self.cosmetic_price.get()=="0.0" and self.grocery_price.get()=="0.0" and self.cold_price.get()=="0.0" ):
        messagebox.showerror("Error","No Product Purchased")
      else:
        self.welcomeBill()

        # Generate cosmetic bill on text area
        if(self.lipstik.get()!=0):
            self.txtarea.insert(END,f"\n Lipstik\t\t {self.lipstik.get()}\t\t{self.lipstikPrice}")
        if(self.facewash.get()!=0):
            self.txtarea.insert(END,f"\n Facewash\t\t {self.facewash.get()}\t\t{self.facewashPrice}")
        if(self.soap.get()!=0):
            self.txtarea.insert(END,f"\n Soap\t\t {self.soap.get()}\t\t{self.soapPrice}")
        if(self.bodylosan.get()!=0):
            self.txtarea.insert(END,f"\n Bodylosan\t\t {self.bodylosan.get()}\t\t{self.bodylosanPrice}")
        if(self.powder.get()!=0):
            self.txtarea.insert(END,f"\n Cold-Powder\t\t {self.powder.get()}\t\t{self.powderPrice}")
        if(self.ishadow.get()!=0):
            self.txtarea.insert(END,f"\n I-shadow\t\t {self.ishadow.get()}\t\t{self.ishadowPrice}")
        
        # Generate Grocery bill on text area
        if(self.ata.get()!=0):
            self.txtarea.insert(END,f"\n Aata\t\t {self.ata.get()}\t\t{self.ataPrice}")
        if(self.dal.get()!=0):
            self.txtarea.insert(END,f"\n Daal\t\t {self.dal.get()}\t\t{self.dalPrice}")
        if(self.rice.get()!=0):
            self.txtarea.insert(END,f"\n Basmati-Rice\t\t {self.rice.get()}\t\t{self.ricePrice}")
        if(self.oil.get()!=0):
            self.txtarea.insert(END,f"\n Soyabean-Oil\t\t {self.oil.get()}\t\t{self.oilPrice}")
        if(self.sugar.get()!=0):
            self.txtarea.insert(END,f"\n Sugar\t\t {self.sugar.get()}\t\t{self.sugarPrice}")
        if(self.saus.get()!=0):
            self.txtarea.insert(END,f"\n Saus\t\t {self.saus.get()}\t\t{self.sausPrice}")        

         # Generate Grocery bill on text area
        if(self.thumsup.get()!=0):
            self.txtarea.insert(END,f"\n ThumsUp\t\t {self.thumsup.get()}\t\t{self.thumsupPrice}")
        if(self.frooti.get()!=0):
            self.txtarea.insert(END,f"\n Frooti\t\t {self.frooti.get()}\t\t{self.frootiPrice}")
        if(self.sprite.get()!=0):
            self.txtarea.insert(END,f"\n Sprite\t\t {self.sprite.get()}\t\t{self.spritePrice}")
        if(self.dew.get()!=0):
            self.txtarea.insert(END,f"\n Dew\t\t {self.dew.get()}\t\t{self.dewPrice}")
        if(self.maaza.get()!=0):
            self.txtarea.insert(END,f"\n Maaza\t\t {self.maaza.get()}\t\t{self.maazaPrice}")
        if(self.nimbooz.get()!=0):
            self.txtarea.insert(END,f"\n Nimbooz\t\t {self.nimbooz.get()}\t\t{self.nimboozPrice}")
        #tax Area in bill
        self.txtarea.insert(END,f"\n-------------------------------------")
        if(self.cosmetic_tax.get()!='0.0'):
            self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
        if(self.grocery_tax.get()!='0.0'):
            self.txtarea.insert(END,f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")
        if(self.cold_tax.get()!='0.0'):
            self.txtarea.insert(END,f"\n ColdDrinks Tax\t\t\t\t{self.cold_tax.get()}")
        
        self.txtarea.insert(END,f"\n-------------------------------------")
        self.txtarea.insert(END,f"\n Total Bill\t\t\t\t{self.TotalBill}")
        self.txtarea.insert(END,f"\n-------------------------------------")
        self.saveBill()

    def saveBill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if(op>0):
            self.bill_data=self.txtarea.get('1.0',END)
            billfile=open("bill/"+str(self.bill_no.get())+".txt","w")
            billfile.write(self.bill_data)
            billfile.close()
            messagebox.showinfo("Saved Bill",f"Bill No {self.bill_no.get()} saved successfully")
        else:
            return

    def findBill(self):
        present='no'
        d=os.listdir("bill/")
        
        for i in d:
            if(i.split('.')[0]==self.search_bill.get()):
              file=open(f"bill/{i}","r")  
              self.txtarea.delete('1.0',END)
              for d in file:
                self.txtarea.insert(END,d)
              file.close()
              present='yes'
        if(present=='no' ):
            messagebox.showerror("Error","Invalid Bill No.")
    
    def clearData(self):
      op=messagebox.askyesno("Clear Data","Do you want to clear data?")
      if(op>0):
            
        # cosmetics variables----------

        self.lipstik.set(0)
        self.facewash.set(0)
        self.soap.set(0)
        self.bodylosan.set(0)
        self.powder.set(0)
        self.ishadow.set(0)
        #grocery variables----------
        self.ata.set(0)
        self.dal.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.saus.set(0)
        #cold variables----------
        self.thumsup.set(0)
        self.frooti.set(0)
        self.sprite.set(0)
        self.dew.set(0)
        self.maaza.set(0)
        self.nimbooz.set(0)

        #Total Product Price & Tax Variables
        self.cosmetic_price.set('')
        self.grocery_price.set('')
        self.cold_price.set('')
        #Total Product Tax
        self.cosmetic_tax.set('')
        self.grocery_tax.set('')
        self.cold_tax.set('')

        #customer --------------------
        self.c_name.set('')
        self.c_phn.set('')     
        self.bill_no.set('')
        random_bill_no=random.randint(10000,99999)
        self.bill_no.set(str(random_bill_no))
        self.search_bill.set('')
        self.welcomeBill()

    def exit(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        print(op)
        if(op>0):
            self.root.destroy()
    def logout(self):
        op=messagebox.askyesno("Logout","Do you want to really logout")
        if(op>0):
            self.root.destroy()
            import login
        else:
            return
        
        
    def clock(self):
        date=time.strftime('%d/%m/%Y')
        currenttime=time.strftime('%H:%m:%S')
        self.datetimeLabel.config(text=f'Date:{date}\nTime:{currenttime}')
        self.datetimeLabel.after(1000,self.clock)
root=Tk()
obj=Bill_App(root)

root.mainloop()