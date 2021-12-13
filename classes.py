from guizero import *
import sqlite3
import datetime
from time import sleep

#THIS CLASS IS THE 'MASTER' CLASS WHERE I DESIGN EACH SEPARATE GUI APP THAT THE MAIN
#THE MAIN APP LEADS TO AND FROM
class new_Windows:
    
    def __init__(self):
        self = self

    def gui_layout2(self):
        #THE SET UP PART, HERE IS THE INSTANTIATION OF THE NEW APP AND WE LAY OUT THE 
        #THE BOXES IN THEIR GRIDS. 
    
        self.app2 = App(title="Tomar ordenes", layout="grid", width=600, height=800)
        box_1 = Box(self.app2, grid=[0,0])
        tg_mssg = Text(box_1, text="\tTamales Garcia: \n\tSistema de ordenes")
        box_2 = Box(self.app2, layout="grid", grid=[0, 1])
        
        #THIS SETS UP THE TOP PART OF THE ORDER TAKING SYS, WITH CORRESPONDING WIDGTS FOR 
        # NAME AND PHONE NUMBERS. 
        #TO DO
        #I HAVE TO ADD/EDIT THE INSTATIATED WIDGETS(possibly) TO ADD A SERIES OF COMMANDS THAT 
        #THAT TAKES THE WIDGET VALUES AND MAKE IT USABLE

        name_cust = Text(box_2, text="Nombre", grid=[0, 0])
        name_box = TextBox(box_2, width=15, height=1, grid=[1, 0])
        phone_cust = Text(box_2, text="Celular", grid=[0, 1])
        phone_box = TextBox(box_2, width=15, height=1, grid=[1, 1])
        doz_text = Text(box_2, text="Dozenas: ", grid=[2, 1])

        #TXT AND SLIDERS ARE USED HERE TO DENOTE SECTIONS I WILL USE THE VARIABLE NAMES 
        #TO ADD THEM INTO MY DB MAKER APP

        psr_txt = Text(box_2, text="PSR", grid=[0, 2])
        psr_slide = Slider(box_2, start=0, end=12, grid=[1, 2], width=300)
        psr_combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string",command=None, grid=[2, 2])
        
        psv_txt = Text(box_2, text="PSV", grid=[0, 3])
        psv_slide = Slider(box_2, start=0, end=12, grid=[1, 3], width=300)
        psv_Combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string", command=None, grid=[2, 3])

        pork_txt = Text(box_2, text="Puerco", grid=[0, 4])
        pork_slide = Slider(box_2, start=0, end=12, grid=[1, 4], width=300)
        pork_combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string", command=None, grid=[2, 4])

        porkG_txt = Text(box_2, text="Puerco\n verde", grid=[0, 5])
        porkG_slide = Slider(box_2, start=0, end=12, grid=[1, 5], width=300)
        pork_G_combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string", command=None, grid=[2, 5])
        
        elote_txt = Text(box_2, text="\nelote", grid=[0, 6])
        elote_slide = Slider(box_2, start=0, end=12, grid=[1, 6], width=300)
        elote_combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string", command=None, grid=[2, 6])

        rajas_txt = Text(box_2, text="Rajas", grid=[0, 7])
        rajas_slide = Slider(box_2, start=0, end=12, grid=[1, 7], width=300)
        rajas_combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string", command=None, grid=[2, 7])


        pineapple_txt = Text(box_2, text="Pineapple", grid=[0, 8])
        pineapple_slide = Slider(box_2, start=0, end=12, grid=[1, 8], width=300)
        pine_combo = Combo(box_2, options=[0, 1, 2, 3, 4], selected="string", command=None, grid=[2, 8])

        # THE CHECKBOXES HAVE COMMAND PROPERTIES, I NEED TO FIGURE OUT HOW TO SET THEM UP TO CREATE VALUES I CAN ACCESS
        # FROM THE WIDGETS BEING CLICKED 

        paid_Checkbx = CheckBox(box_2, text="Pagados", command=None, grid=[0, 9])
        inPart_Checkbx = CheckBox(box_2, text="Abonado", command=None, grid=[1, 9])
        text_Total = Text(box_2, text="Total $:", grid=[2, 9])
        text_bx_tot = TextBox(box_2, width=7, height=1, grid=[2, 10]) #PLEASE EDIT THIS SECTION TO ADD ANOTHER 
                                                                        #TextBox TO ACCOUNT FOR PAID IN FULL MAYBE? OR WILL THAT BE TOO COMPLEX?
        def submitter():
            date_order = datetime.date.today()
            date_order = str(date_order)

            name_var = name_box.value
            phone_var = phone_box.value
    
            psr_var = psr_slide.value
            psr12_var = psr_combo.value
            psv_var =  psv_slide.value
            psv12_var = psv_Combo.value
            pork_var = pork_slide.value
            pork12_var = pork_combo.value
            porkG_var =  porkG_slide.value
            porkG12_var = pork_G_combo.value
            rajas_var = rajas_slide.value
            rajas_12_var = rajas_combo.value
            elote_var = elote_slide.value
            elote_12_var = elote_combo.value
            pine_var = pineapple_slide.value
            pine_12_var = pine_combo.value
            paid_Chec_var = paid_Checkbx.value
            in_part_check = inPart_Checkbx.value
            total_paid_var = text_bx_tot.value
            #total_paid_var = int(total_paid_var)

            def adder_oftot(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
                tam_cst_1 = 2.25 
                tam_cst_12 = 27
                tam_var1 = a + c + e + g + i + k + m
                tam_var1 = float(tam_var1)
                total_cst_1 = tam_var1 * tam_cst_1
                tam_var2 = int(b) + int(d) + int(f) +  int(h) + int(j) + int(l) + int(n)
                tam_var2 = float(tam_var2)
                total_cst_12 = tam_var2 * tam_cst_12

                total_tam_cst = total_cst_1 + total_cst_12
                #tam_cst_abono = (total_tam_cst - float(z))
                info_var = ("Costo Total: " + str(total_tam_cst) )
                info_total = info("cost info", info_var)
            
            sleep(2)

            adder_oftot(psr_var, psr12_var, psv_var, psv12_var, pork_var, pork12_var, porkG_var, porkG12_var, rajas_var, rajas_12_var, elote_var, elote_12_var, pine_var, pine_12_var)

            databaser.db_additions( date_order, name_var, phone_var, psr_var, psr12_var, psv_var, psv12_var, pork_var, pork12_var, porkG_var, porkG12_var, rajas_var, rajas_12_var, elote_var, elote_12_var, pine_var, pine_12_var, paid_Chec_var, in_part_check, total_paid_var)
                                                               
        sumbit_bttn = PushButton(box_2, text="Poner Orden", command=submitter, width= 15, height=3, grid=[1, 10])
        # SUBMIT BTTN IS MY MAIN ADDER TO THE DATABASE I WANT TO TAKE THE VALUES FROM THE WIDGETS TO ADD THEM HERE. 

        databaser = db_Setup_class()
        databaser.db_maker()

        #THE FOLLOWING ARE VARIABLE NAMES TO ATTEMPT TO CREATE A LIST OF PARAMS TO FEED TO DB_ADDITION

        self.app2.display()


class app3:

    def __init__(self):
        self = self

    def app_3_gui(self):
        self.app3 = App(title="Revisar Ordenes", layout="grid", width=600, height=800 )
        self.box_1 = Box(master=self.app3, layout="grid", grid=[0, 0])
        self.box_2 = Box(master=self.app3, layout="grid", grid=[0, 1])
        self.box_3 = Box(master=self.app3, layout="grid", grid=[0, 2])
        oview_title = Text(self.box_1, text="Revisar Ordenes", grid=[0, 0])
        year_txt = Text(self.box_2, text="Year:\t", grid=[0,1])
        month_txt = Text(self.box_2, text="Month:\t", grid=[1,1])
        day_txt = Text(self.box_2, text="Day:\t", grid=[2,1])
        combo1_yr = Combo(self.box_2, options=["2020", "2021", "2023", "2024"], grid=[0, 2], width=5)
        combo2_month = Combo(self.box_2, options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], grid=[1, 2], width=5)
        combo3_day = Combo(self.box_2, options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"], grid=[2, 2], width=5)
        #day_txtbox = TextBox(self.box_2, width=5, height=2, grid=[2, 2])
        submit_bttn = PushButton(self.box_2, text="Fecha", command=print("Hello"), grid=[3, 2])
       
       #I WILL USE A SIMPLE SEARCH ALGO TO DISPLAY A ROW OF BUTTONS THAT WILL
       #HAVE LINKS TO YET ANOTHER PAGE WITH THE REQUIRED DATA

        val_yr = str(combo1_yr.value)
        val_mnth = str(combo2_month.value)
        val_day = str(combo3_day.value)
        val_day = str(val_day)


        total_date = val_yr + val_mnth + val_day

        databese = db_Setup_class()

        databese.db_id_Selector(total_date)
        explain_txt = Text(self.box_3, text="Por favor selecione la fecha\nlaboral para obtener la lista de ordenes\ndel dia.", font="Times New Roman", grid=[1,0],)
        self.app3.display()

    
class db_Setup_class:

    def __init__(self):
        self = self   
    
    def db_maker(self):
        f = 0

        self.con = sqlite3.connect("tamales_orders.db")

        self.cur = self.con.cursor()


        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS orders ('date' TEXT, 'cust_name' TEXT, 'cust_Phone' INTEGER, 'psr_Unidad' INTEGER, 'psr_Dozena' INTEGER, 'psv_Unidad' INTEGER, 'psv_Dozena' INTEGER, 'pork_Unidad' INTEGER, 'pork_Dozena' INTEGER, 'porkG_Unidad' INTEGER, 'porkG_Dozena' INTEGER, 'elote_Unidad' INTEGER, 'elote_Dozena' INTEGER, 'rajas_Unidad' INTEGER, 'rajas_Dozena' INTEGER, 'pine_Unidad' INTEGER, 'pine_Dozena' INTEGER, 'pagado' INTEGER, 'abonado' INTEGER, 'total' INTEGER);""")

        self.con.commit()

        f = 1

        while f != 1:
            self.con.close()
        

    def db_additions(self, a, b, c , d, e, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        self.q = q
        self.r = r
        self.s = s
        self.t = t
        self.u = u

        list_o_values = [self.a, self.b, self.c, self.d, self.e, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p, self.q, self.r, self.s, self.t, self.u]

        self.u = self.con.cursor()
        self.u.execute("""INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", list_o_values)

        self.con.commit()
        
        f = 1

    def db_id_Selector(self, val):
         f = 0
         self.val = val
         self.cur = self.con.cursor()
         self.cur.execute("""SELECT * FROM moodToday WHERE date=:value""", {"value": self.val})
         self.query_result = self.cur.fetchone()
         f = 1

        