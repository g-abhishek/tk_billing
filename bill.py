from tkinter import *

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text = "Billing Software", bd = 12, relief = GROOVE, bg = bg_color, fg = "white", font = ("times new roman", 30, "bold"), pady=5)
        title.pack(fill = X)

        #=============customer details=============
        F1 = LabelFrame(self.root, text= "Customers Details :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F1.place(x = 0, y = 80, relwidth = 1)
            #================cname===========================
        cname_lbl = Label(F1, text = "Customer Name:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "white")
        cname_lbl.grid(row = 0, column = 0, padx = 40, pady = 5)

        cname_input = Entry(F1, width = 18, font = "arial 12", bd = 5, relief = SUNKEN)
        cname_input.grid(row = 0, column = 1, pady = 5, padx = 10)
            #===============cmobile===========================
        cmobile_lbl = Label(F1, text = "Phone No.:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "white")
        cmobile_lbl.grid(row = 0, column = 2, padx = 30, pady = 5)

        cmobile_input = Entry(F1, width = 18, font = "arial 12", bd = 5, relief = SUNKEN)
        cmobile_input.grid(row = 0, column = 3, pady = 5, padx = 10)
            #===============cbill===========================
        cbill_lbl = Label(F1, text = "Bill Number:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "white")
        cbill_lbl.grid(row = 0, column = 4, padx = 30, pady = 5)

        cbill_input = Entry(F1, width = 18, font = "arial 12", bd = 5, relief = SUNKEN)
        cbill_input.grid(row = 0, column = 5, pady = 5, padx = 10)

        search_btn = Button(F1, text = "Search", font = "arial 10 bold", width = 10)
        search_btn.grid(row = 0, column = 6, padx = 10, pady = 10)

        #=============Cosmetics Frame=============
        F2 = LabelFrame(self.root, text= "Cosmetics :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F2.place( y = 165, width = 335, height = 350)

        bath_lbl = Label(F2, text = "Bath Soap:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        bath_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        bath_input = Entry(F2, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        bath_input.grid(row = 0, column = 1, pady = 10, padx = 3)

        face_cream_lbl = Label(F2, text = "Face Cream:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        face_cream_lbl.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        face_cream_input = Entry(F2, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        face_cream_input.grid(row = 1, column = 1, pady = 10, padx = 3)

        face_wash_lbl = Label(F2, text = "Face Wash:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        face_wash_lbl.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        face_wash_input = Entry(F2, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        face_wash_input.grid(row = 2, column = 1, pady = 10, padx = 3)

        hair_shampoo_lbl = Label(F2, text = "Shampoo:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        hair_shampoo_lbl.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        hair_shampoo_input = Entry(F2, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        hair_shampoo_input.grid(row = 3, column = 1, pady = 10, padx = 3)

        hair_gel_lbl = Label(F2, text = "Hair Gel:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        hair_gel_lbl.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        hair_gel_input = Entry(F2, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        hair_gel_input.grid(row = 4, column = 1, pady = 10, padx = 3)

        body_lotion_lbl = Label(F2, text = "Body Lotion:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        body_lotion_lbl.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        body_lotion_input = Entry(F2, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        body_lotion_input.grid(row = 5, column = 1, pady = 10, padx = 3)

        #=============Grocery Frame=============
        F3 = LabelFrame(self.root, text= "Grocery :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F3.place(x = 337, y = 165, width = 300, height = 350)

        rice_lbl = Label(F3, text = "Rice:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        rice_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        rice_input = Entry(F3, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        rice_input.grid(row = 0, column = 1, pady = 10, padx = 3)

        oil_lbl = Label(F3, text = "Olive Oil:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        oil_lbl.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        oil_input = Entry(F3, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        oil_input.grid(row = 1, column = 1, pady = 10, padx = 3)

        Wheat_lbl = Label(F3, text = "Wheat:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        Wheat_lbl.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        Wheat_input = Entry(F3, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        Wheat_input.grid(row = 2, column = 1, pady = 10, padx = 3)

        sugar_lbl = Label(F3, text = "Sugar:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        sugar_lbl.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        sugar_input = Entry(F3, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        sugar_input.grid(row = 3, column = 1, pady = 10, padx = 3)

        tea_lbl = Label(F3, text = "Tea:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        tea_lbl.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        tea_input = Entry(F3, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        tea_input.grid(row = 4, column = 1, pady = 10, padx = 3)

        dal_lbl = Label(F3, text = "Dal:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        dal_lbl.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        dal_input = Entry(F3, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        dal_input.grid(row = 5, column = 1, pady = 10, padx = 3)

        #=============Cold Drink Frame=============
        F4 = LabelFrame(self.root, text= "Cold Drinks :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F4.place(x = 640, y = 165, width = 300, height = 350)

        pepsi_lbl = Label(F4, text = "Pepsi:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        pepsi_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        pepsi_input = Entry(F4, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        pepsi_input.grid(row = 0, column = 1, pady = 10, padx = 3)

        coke_lbl = Label(F4, text = "Coke:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        coke_lbl.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        coke_input = Entry(F4, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        coke_input.grid(row = 1, column = 1, pady = 10, padx = 3)

        frooti_lbl = Label(F4, text = "Frooti:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        frooti_lbl.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        frooti_input = Entry(F4, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        frooti_input.grid(row = 2, column = 1, pady = 10, padx = 3)

        sprite_lbl = Label(F4, text = "Sprite:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        sprite_lbl.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        sprite_input = Entry(F4, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        sprite_input.grid(row = 3, column = 1, pady = 10, padx = 3)

        appy_lbl = Label(F4, text = "Appy:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        appy_lbl.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        appy_input = Entry(F4, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        appy_input.grid(row = 4, column = 1, pady = 10, padx = 3)

        maza_lbl = Label(F4, text = "Maza:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        maza_lbl.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        maza_input = Entry(F4, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        maza_input.grid(row = 5, column = 1, pady = 10, padx = 3)

        #=============Bill Frame=============
        F5 = Frame(self.root,  bd = 10, relief = GROOVE)
        F5.place(x = 945, y = 165, width = 384, height = 350)
        bill_title = Label(F5, text = "Bill Area", font = ("times new roman", 15, "bold"), bd = 7, relief = GROOVE)
        bill_title.pack(fill = X)
        scroll_y = Scrollbar(F5, orient = VERTICAL)
        scroll_y.pack(side = RIGHT, fill = Y)
        txtarea = Text(F5, yscrollcommand = scroll_y.set)
        txtarea.pack(fill = BOTH, expand = 1)
        scroll_y.config(command = txtarea.yview)

        #==========Button Frame=============
        F6 = LabelFrame(self.root, text = "Bill Menu", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_color, bd = 7, relief = GROOVE)
        F6.place(y = 517,relwidth = 1, height = 180)

        tot_cos_lbl = Label(F6, text = "Total Cosmetic Price:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_cos_lbl.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        tot_cos_input = Entry(F6, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_cos_input.grid(row = 0, column = 1, pady = 8, padx = 3)

        tot_gro_lbl = Label(F6, text = "Total Grocery Price:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_gro_lbl.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        tot_gro_input = Entry(F6, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_gro_input.grid(row = 1, column = 1, pady = 8, padx = 3)

        tot_drinks_lbl = Label(F6, text = "Total Drinks Price:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_drinks_lbl.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        tot_drinks_input = Entry(F6, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_drinks_input.grid(row = 2, column = 1, pady = 8, padx = 3)


        tot_cos_tax_lbl = Label(F6, text = "Total Cosmetic Tax:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_cos_tax_lbl.grid(row = 0, column = 2, padx = 8, pady = 5, sticky = "w")
        tot_cos_tax_input = Entry(F6, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_cos_tax_input.grid(row = 0, column = 3, pady = 8, padx = 3)

        tot_gro_tax_lbl = Label(F6, text = "Total Grocery Tax:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_gro_tax_lbl.grid(row = 1, column = 2, padx = 8, pady = 5, sticky = "w")
        tot_gro_tax_input = Entry(F6, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_gro_tax_input.grid(row = 1, column = 3, pady = 8, padx = 3)

        tot_drinks_tax_lbl = Label(F6, text = "Total Drinks Tax:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_drinks_tax_lbl.grid(row = 2, column = 2, padx = 8, pady = 5, sticky = "w")
        tot_drinks_tax_input = Entry(F6, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_drinks_tax_input.grid(row = 2, column = 3, pady = 8, padx = 3)


       


root = Tk()
obj = BillApp(root)
root.mainloop()