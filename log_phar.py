# En tete
from tkinter import  *

from tkinter import messagebox #, ttk
import tkinter as tk
from tkinter import ttk
import tempfile
import random
from time import strftime
#from PIL import ImageTk
#from PIL import  Image
import os
class SuperMarche:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacie ")
        self.root.geometry("1720x950")
        
        # titre de l'interface........
        titre = Label(self.root, text="Pharmacie",  font=("Algerian", 40) , bg="cyan", fg="black")
        titre.pack(side=TOP, fill=X)
        
        def heure():
            heur = strftime("%H:%M:%S")
            lbheur.config(text=heur)
            lbheur.after(100, heure)
            
        lbheur= Label(self.root, text="HH:MM:SS",  font=("times new roman", 15, "bold") , bg="cyan", fg="black" )
        lbheur.place(x=8, y=15, width=120, height=45)
        
        heure()
        
        #-------- variable------------
        self.c_nom = StringVar()
        self.c_pre = StringVar()
        self.c_tel = StringVar()
        
        self.fact = StringVar()
        z = random.randint(1000, 9999)
        self.fact.set(z)
        
        self.c_email = StringVar()
        self.rech_fact = IntVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.qte = IntVar()
        self.totalbruite = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar() 
        
        #----------------------------- liste des type_maladie--------------------------
        self.type_maladie = [ "selection","Maladies_infectieuses", "Maladies_non_transmissibles"]
        
        #-----------------------------Maladies infectieuses----------------------------
        
        self.liste_categorie_maladie_inf = ["selection", "Paludisme", "VIH", "Tuberculose", "infection Urinaire"]
        
        #------------------------------PALU--------------------------
        
        self.liste_souscategorie_palu = ["------", "pal_medic_1", "pal_medic_2", "pal_medic_3"]
        
        self.pal_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        
        self.pal_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.pal_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 64
        self.price_nms_3 = 946
        
        #-------------------VIH---------------
        
        self.liste_souscategorie_VIH = ["------", "V_medic_1", "V_medic_2", "V_medic_3"]
        
        self.V_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        
        self.V_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.V_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 64
        self.price_nms_3 = 946
        
        #------------------------TUBERCULOSE--------------------
        
        self.liste_souscategorie_TUBERCULOSE = ["------", "T_medic_1", "T_medic_2", "T_medic_3"]
        
        self.T_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.T_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.T_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 64
        self.price_nms_3 = 946
        
        #-----------------------------infecton urinaire------------------------------
        self.liste_souscategorie_urinaire = ["------", "U_medic_1", "U_medic_2", "U_medic_3"]
        
        self.U_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.U_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.U_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 64
        self.price_nms_3 = 946
        
        
        
        #----------------------------- liste des Maladies non transmissibles----------------
        
        self.liste_categorie_maladie_non_trans = [ "selection", "Cancer", "Cardio-vasculaire",  "DIARRHEES", "Mentale", "Respiratoire", "Metabolique"]
        
         #----------------------------- liste des medicaments -----------------
         
         #---------------------------"Cancer"--------------------------------
        
        self.liste_medicament_cancer = ["------", "cancer_medic_1", "cancer_medic_2", "cancer_medic_3"]
        
        self.cancer_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        
        self.cancer_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.cancer_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 64
        self.price_nms_3 = 946
        
         #---------------------------"Cardio-vasculaire"--------------------------------
        self.liste_souscategorie_Cardio_vascul = ["------", "Cardio_medic_1", "Cardio_medic_2", "Cardio_medic_3"]
        
        self.Cardio_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.Cardio_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.Cardio_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 9560
        self.price_nms_2 = 6400
        self.price_nms_3 = 9460
        
        #---------------------------"DIARRHEES"--------------------------------
        
        self.liste_souscategorie_DIARRHEES = ["------", "DIARR_medic_1", "DIARR_medic_2", "DIARR_medic_3"]
        
        self.DIARR_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.DIARR_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.DIARR_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 640
        self.price_nms_3 = 946
        
        #---------------------------"Mentale"--------------------------------
        
        self.liste_souscategorie_Mental = ["------", "Mental_medic_1", "Mental_medic_2", "Mental_medic_3"]
        
        self.Mental_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.Mental_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 752
        self.price_nm_2 = 825
        self.price_nm_3 = 236
        
        self.Mental_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 9056
        self.price_nms_2 = 6040
        self.price_nms_3 = 1946
        
        #---------------------------"Respiratoire"--------------------------------
        
        self.liste_souscategorie_Respir = ["------", "R_medic_1", "R_medic_2", "R_medic_3"]
        
        self.R_medic_1 = ["------", "R_nom_1", "R_nom_2", "R_nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.R_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 1752
        self.price_nm_2 = 2825
        self.price_nm_3 = 3236
        
        self.R_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 3264
        self.price_nms_3 = 5946
         
        #---------------------------"Metabolique"--------------------------------
        
        self.liste_souscategorie_MetaboL = ["------", "M_medic_1", "M_medic_2", "M_medic_3"]
        
        self.M_medic_1 = ["------", "nom_1", "nom_2", "nom_3"]
        self.price_nom_1 = 13000
        self.price_nom_2 =28342
        self.price_nom_3 = 19265
        
        self.M_medic_2 = ["------", "nm_1", "nm_2", "nm_3"]
        self.price_nm_1 = 6702
        self.price_nm_2 = 4825
        self.price_nm_3 = 3236
        
        self.M_medic_3 = ["------", "nms_1", "nms_2", "nms_3"]
        self.price_nms_1 = 956
        self.price_nms_2 = 664
        self.price_nms_3 = 1946
        
        #########----------------------------Section--------------------------------------
        
        Main_Frame = Frame(self.root, bd=3, relief=GROOVE, bg="white")
        Main_Frame.place(x=10, y=100, width=1690, height=820)
        
        ########-----------------------------Expace client--------------------------------
        client_Fram= LabelFrame(Main_Frame, text="Client",font=("Algerian", 20) , bg="white", fg="black") # font=("times new roman", 15 ),  bg="white")
        client_Fram.place(x=8, y=15, width=350, height=200)
        
        #########-----------------------------info client-------------------------------
        self.lbnom = Label(client_Fram, text="NOM :", font=("times new roman", 15 ),  bg="white")
        self.lbnom.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        self.lbpre = Label(client_Fram, text="PRENOM :", font=("times new roman", 15 ),  bg="white")
        self.lbpre.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        
        self.lbtel = Label(client_Fram, text="CONTACT :", font=("times new roman", 15 ),  bg="white")
        self.lbtel.grid(row=4, column=0, sticky=W, padx=5, pady=2)
        
        self.lbmail = Label(client_Fram, text="EMAIL :", font=("times new roman", 15 ),  bg="white")
        self.lbmail.grid(row=5, column=0, sticky=W, padx=5, pady=2)
        
        
        self.txt_lbnom = Entry(client_Fram, font=("times new roman", 15 ), bg="white", fg="black")
        self.txt_lbnom.grid(row=0, column=2, sticky=W, padx=5, pady=1)
       
         
        self.txt_lbpre = Entry(client_Fram, font=("times new roman", 15 ), bg="white", fg="black")
        self.txt_lbpre.grid(row=3, column=2)
        
        self.txt_lbtel = Entry(client_Fram, font=("times new roman", 15 ), bg="white", fg="black")
        self.txt_lbtel.grid(row=4, column=2, sticky=W, padx=5, pady=2)
        
        self.txt_lbmail = Entry(client_Fram, font=("times new roman", 15 ), bg="white", fg="black")
        self.txt_lbmail.grid(row=5, column=2, sticky=W, padx=5, pady=2)
        
        
        #------------------------------Expace Produit--------------------
        produit_Fram= LabelFrame(Main_Frame, text="Produits",font=("Algerian", 20) , bg="white", fg="black") # font=("times new roman", 15 ),  bg="white")
        produit_Fram.place(x=400, y=15, width=700, height=200)
        
        #------------------------------info Produit-----------------------
        
        self.lbseltyp_malad = Label(produit_Fram, text="Type de Maladies :", font=("times new roman", 15 ),  bg="white")
        self.lbseltyp_malad.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        self.lbselcat = Label(produit_Fram, text="Selectionne Maladie :", font=("times new roman", 15 ),  bg="white")
        self.lbselcat.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        
        self.lbSscateg = Label(produit_Fram, text="Medicaments :", font=("times new roman", 15 ),  bg="white")
        self.lbSscateg.grid(row=4, column=0, sticky=W, padx=5, pady=2)
        
        self.lbNpro = Label(produit_Fram, text="Nom Produit :", font=("times new roman", 15 ),  bg="white")
        self.lbNpro.grid(row=5, column=0, sticky=W, padx=5, pady=2)
        
        self.lbpris = Label(produit_Fram, text="Prix :", font=("times new roman", 15 ),  bg="white")
        self.lbpris.grid(row=6, column=0, sticky=W, padx=5, pady=2)
        
        self.lbqt = Label(produit_Fram, text="Quantité :", font=("times new roman", 15 ),  bg="white")
        self.lbqt.grid(row=0, column=4, sticky=W, padx=5, pady=2)
        
        #--------------------------------------------------------------------------------------------------------------
        
        self.txt_lbseltyp_malad = ttk.Combobox (produit_Fram, font=("times new roman", 15 ), values=self.type_maladie)
        self.txt_lbseltyp_malad.grid(row=0, column=2)
        self.txt_lbseltyp_malad.current(0)
        self.txt_lbseltyp_malad.bind("<<ComboboxSelected>>", self.fonctiontype_maladie )
        
        self.txt_lbselcat = ttk.Combobox (produit_Fram, font=("times new roman", 15 ), values=[" "])
        self.txt_lbselcat.grid(row=3, column=2)
        self.txt_lbselcat.current(0)
        self.txt_lbselcat.bind("<<ComboboxSelected>>", self.fonctionmaladie )
        
        self.txt_lbsscat = ttk.Combobox (produit_Fram, font=("times new roman", 15 ), values=[" "])
        self.txt_lbsscat.grid(row=4, column=2)
        self.txt_lbsscat.current(0)
        self.txt_lbsscat.bind("<<ComboboxSelected>>", self.fonctionmedicament)
        
        self.txt_lbnpr = ttk.Combobox (produit_Fram, textvariable=self.produit, font=("times new roman", 15 ), values=[" "])
        self.txt_lbnpr.grid(row=5, column=2)
        self.txt_lbnpr.current(0)
        self.txt_lbnpr.bind("<<ComboboxSelected>>", self.fonction_nom_medicament)
        
        self.txt_lbpriss = ttk.Combobox (produit_Fram, textvariable= self.prix  , font=("times new roman", 15 )) #, values=[" "])
        self.txt_lbpriss.grid(row=6, column=2) 
        #self.txt_lbpriss.current(0)
        #self.txt_lbpriss.bind("<<ComboboxSelected>>", self."")
        
        
        self.txt_lbqtentr= ttk.Combobox(produit_Fram, textvariable= self.qte , font=("times new roman", 12 )) #, bg="white", fg="black")
        self.txt_lbqtentr.grid(row=0, column=5) 
        #self.txt_lbqtentr.current(0)


    
       ##########-----------------------------ZONE DE BOUTTONS--------------------------------------
         
        Bouton_Fram = LabelFrame(Main_Frame, text="Bouttons",font=("Algerian", 20) ,bg="cyan",  fg="black") # font=("times new roman", 15 ),  bg="white")
        Bouton_Fram.place(x=8, y=600, width=1660, height=210)
         
        #########----------------------------ELEMENTS-------------------------------
        
        self.totalbrute = Label(Bouton_Fram, text=" ", font=("times new roman", 15 ),  bg="white")
        self.totalbrute.grid(row=9, column=0) 
        
        self.totalbrut = Label(Bouton_Fram, text="TOTAL BRUTE", font=("times new roman", 15 ), bg="cyan") # bg="white")
        self.totalbrut.grid(row=9, column=0) 
        
        self.tas = Label(Bouton_Fram, text="TAXE", font=("times new roman", 15 ), bg="cyan") # bg="white")
        self.tas.grid(row=14, column=0, sticky=W, padx=5, pady=2)
        
        self.lb_totalnet = Label(Bouton_Fram, text="TOTAL NET", font=("times new roman", 15 ), bg="cyan") # bg="white")
        self.lb_totalnet.grid(row=20, column=0, sticky=W, padx=5, pady=2)
        
        #----------------------- 
        
        self.txt_brut= Entry (Bouton_Fram, textvariable= self.totalbruite, font=("times new roman", 17 ), bg="white", fg="black")
        self.txt_brut.grid(row=9, column=2) 
        
        self.txt_tas= Entry (Bouton_Fram, textvariable= self.taxe, font=("times new roman", 17 ), bg="white", fg="black")
        self.txt_tas.grid(row=14, column=2)
        
        self.txt_net= Entry (Bouton_Fram, textvariable= self.totalnet, font=("times new roman", 17 ), bg="white", fg="black")
        self.txt_net.grid(row=20, column=2)
         
        
        
    #------------------------------------------------------------------image------------------------------
    #------------------------------------------------------------------image------------------------------#
    
        
         #--------------------------------------Espace fature---------------------
    
        recherche = Label(Main_Frame, text="N° Facture", font=("Algerian", 20) , bg="white", fg="black")
        recherche.place(x=1120, y=50, ) #width=520, height=500)
        
        rechentr= Entry(Main_Frame,  font=("times new roman", 17 ), bg="white", fg="black" )
        rechentr.place(x=1280, y=50) #width=520, height=500)
        
        boutrech = Button(Main_Frame, text="Recherche", command=self.recherches, font=("Algerian", 15) , bg="yellow", fg="black" )
        boutrech.place(x=1510, y=45) #width=520, height=500)
    
        Facture_Fram = LabelFrame(Main_Frame, text="Facture",font=("Algerian", 20) , bg="white", fg="black") # font=("times new roman", 15 ),  bg="white")
        Facture_Fram.place(x=1120, y=100, width=550, height=500)
        
        srol = Scrollbar(Facture_Fram, orient=VERTICAL)
        self.textera = Text(Facture_Fram, yscrollcommand=srol.set, font=("times new roman", 15 ), bg="white", fg="blue" )
        srol.pack(side=RIGHT, fill=Y)
        srol.config(command=self.textera.yview )
        self.textera.pack(fill=BOTH, expand=1)
    
    
    #--------------------------------------------les boutons de validation----------------------------------------------------
    #--------------------------------------------les boutons de validation----------------------------------------------------
   
    
        self.ajoutcard = Button(Bouton_Fram, text="Ajouter Panier", command= self.Ajoutcrd, font=("Algerian", 20) , bg="green", fg="yellow") 
        self.ajoutcard.place(x=400, y= 5) #grid(row=14, column=5)
        
        self.valide = Button(Bouton_Fram, text="Valider", command=self.valider, font=("Algerian", 20) , bg="green", fg="yellow") 
        self.valide.place(x=670, y= 5) #grid(row=14, column=5)
        
        self.sauvegad = Button(Bouton_Fram, text="Sauvegarder", command=self.Sauvegader, font=("Algerian", 20) , bg="green", fg="yellow") 
        self.sauvegad.place(x=831, y= 5) 
        
        self.imprim = Button(Bouton_Fram, text="Imprimers", command=self.Imprimer, font=("Algerian", 20) , bg="green", fg="yellow") 
        self.imprim.place(x=1073, y= 5) 
        
        self.renitial = Button(Bouton_Fram, text="Renitialiser", font=("Algerian", 20) , bg="green", fg="yellow") 
        self.renitial.place(x=1248, y= 5) 
        
        self.Bienvenu()
        self.l =[]
        
    #-------------------------------------fonction_des_bouttons-----------------------------------------------------------
    #-------------------------------------fonction_des_bouttons-----------------------------------------------------------
    
    def Bienvenu (self ):
        self.textera.delete(1.0, END)
        self.textera.insert(END, "\t\t Bienvenu à la pharcie bonne étoile ")
        self.textera.insert(END, f"\n\n Numéro de la facture : {self.fact.get()}")
        self.textera.insert(END, f"\n\n Nom du client : {self.c_nom.get()} ")
        self.textera.insert(END, f"\n\n Télephone : {self.c_tel.get()} ")
        self.textera.insert(END, "\n\n********************************************************** ")
        self.textera.insert(END, "\nProduits\t\t\tQte\t\tPrix")
        self.textera.insert(END, "\n********************************************************** ")
        
        
    def Sauvegader (self): 
        op= messagebox.askyesno("sauvegader", "voulez-vous sauvegader la facture ?")
        if op== True:
            self.donneFacture = self.textera.get(1.0, END)
            f1 = open("C:/Users/hp/Videos/different projet/super_marche/Facture/"+str(self.fact.get())+".txt", "w")
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarder", f"La facture Numéro { self.fact.get()} a été enregistrer avec succèes")
            f1.close()
            
            
        
        
    def Ajoutcrd (self):
       self.n = self.prix.get()
       self.m = self.qte.get() * self.n
       self.l.append(self.m)
       if self.produit.get()== " ":
           messagebox.showerror("erreur", "selectionnez un produit")
       else:
           self.textera.insert(END, f"\n {self.produit.get()}\t\t\t{self.qte.get()}\t\t{self.m}" )
           self.totalbruite.set(str("Rs.%.2f"%(sum(self.l))))
           self.taxe.set(str("Rs.%.2f"%((((sum(self.l))-(self.prix.get()))*1)/100)))
           self.totalnet.set(str("Rs.%.2f"%(((sum(self.l))+((((sum( self.l))- (self.prix.get()))*1)/100)))))
   
    ##-------------------------------------Valider---------------------- 
    def valider(self ):
        if self.produit.get()== " ":
            messagebox.showerror("erreur", "Ajouter d'abord un produit")
        else :
            text= self.textera.get(10.0, (10.0+float(len(self.l))))
            #self.Bienvenu()
            #text= self.textera.insert(END, text)
            self.textera.insert(END, f"\n\n********************************************************** ")
            self.textera.insert(END, f"\n\nTotal Bruite : \t\t\t {self.txt_brut.get()} ")
            self.textera.insert(END, f"\nTaxe : \t\t\t { self.txt_tas.get()} ")
            self.textera.insert(END, f"\nTotal Net : \t\t\t {self.txt_net.get()} ")
            
            
    def Imprimer(self ): 
        fichier = tempfile.mkdtemp(".txt")
        open(fichier, "w").write(self.textera.get("1.0", END))
        os.startfile(fichier, "print")
        
        
    def recherches(self ):
        trouver = "non"
        for i in os.listdir("C:/Users/hp/Videos/different projet/super_marche/Facture/"):
            if i.split('.')[0]==self.rech_fact.get():
                f1 = open("C:/Users/hp/Videos/different projet/super_marche/Facture/ {i}", "r")
                self.textera.delete(1.0, END)
                for d in f1:
                    self.textera.insert(END, d)
                    f1.close
                    trouver = "oui"
        if trouver =="non" :
            messagebox.showerror('erreur', "la facture n'existe pas")
            
            
    ##-------------------------------------recherche--------------- 
    
    
#--------------------------------fonction_de_produit------------------------
    

    def fonctiontype_maladie(self, even=""):
        if self.txt_lbseltyp_malad.get() == "Maladies_infectieuses":
            self.txt_lbselcat.config(values=self.liste_categorie_maladie_inf)
            self.txt_lbselcat.current(0)
            
        if self.txt_lbseltyp_malad.get() == "Maladies_non_transmissibles":
            self.txt_lbselcat.config(values=self.liste_categorie_maladie_non_trans)
            self.txt_lbselcat.current(0)
            
       #self.type_maladie = [ "selection","Maladies_infectieuses", "Maladies_non_transmissibles"]
          
    #--------------------liste_categorie_maladie_inf-------------
              
    def fonctionmaladie (self, even=" "):
        if self.txt_lbselcat.get() == "Paludisme":
            self.txt_lbsscat.config(values=self.liste_souscategorie_palu)
            self.txt_lbsscat.current(0)
            
        if self.txt_lbselcat.get() == "VIH":
            self.txt_lbsscat.config(values=self.liste_souscategorie_VIH)
            self.txt_lbsscat.current(0)
        
        if self.txt_lbselcat.get() == "Tuberculose":
            self.txt_lbsscat.config(values=self.liste_souscategorie_TUBERCULOSE)
            self.txt_lbsscat.current(0)
        
        if self.txt_lbselcat.get() == "infection Urinaire":
            self.txt_lbsscat.config(values=self.liste_souscategorie_urinaire)
            self.txt_lbsscat.current(0)
        
       # self.liste_categorie_maladie_inf = ["selection", "Paludisme", "VIH", "Tuberculose", "infection Urinaire"]
       
       #-------------liste_categorie_maladie_sans tr------------------
       
        if self.txt_lbselcat.get() == "Cancer":
            self.txt_lbsscat.config(values=self.liste_medicament_cancer)
            self.txt_lbsscat.current(0)
            
        if self.txt_lbselcat.get() == "Cardio-vasculaire":
            self.txt_lbsscat.config(values=self.liste_souscategorie_Cardio_vascul)
            self.txt_lbsscat.current(0)
            
        if self.txt_lbselcat.get() == "DIARRHEES":
            self.txt_lbsscat.config(values=self.liste_souscategorie_DIARRHEES)
            self.txt_lbsscat.current(0)
            
        if self.txt_lbselcat.get() == "Mentale":
            self.txt_lbsscat.config(values=self.liste_souscategorie_Mental)
            self.txt_lbsscat.current(0)
            
        if self.txt_lbselcat.get() == "Respiratoire":
            self.txt_lbsscat.config(values=self.liste_souscategorie_Respir)
            self.txt_lbsscat.current(0)
            
        if self.txt_lbselcat.get() == "Metabolique":
            self.txt_lbsscat.config(values=self.liste_souscategorie_MetaboL)
            self.txt_lbsscat.current(0)
    
    #######self.liste_categorie_maladie_non_trans = [ "selection", "Cancer", "Cardio-vasculaire",  "DIARRHEES", "Mentale", "Respiratoire", "Metabolique"]        
    
       #####-----------------------liste_souscategorie_palu---------------
       
    def fonctionmedicament (self, even=""):
        
        # self.liste_souscategorie_palu = ["pal_medic_1", "pal_medic_2", "pal_medic_3"]
        
        if self.txt_lbsscat.get() == "pal_medic_1":
            self.txt_lbnpr.config(values=self.pal_medic_1)
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "pal_medic_2":
            self.txt_lbnpr.config(values=self.pal_medic_2)
            
        if self.txt_lbsscat.get() == "pal_medic_3":
            self.txt_lbnpr.config(values=self.pal_medic_3)
            self.txt_lbnpr.current(0)
        
      #  self.liste_souscategorie_VIH = ["V_medic_1", "V_medic_2", "V_medic_3"]
      
        if self.txt_lbsscat.get() == "V_medic_1":
            self.txt_lbnpr.config(values=self.V_medic_1)
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "V_medic_2":
            self.txt_lbnpr.config(values=self.V_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "V_medic_3":
            self.txt_lbnpr.config(values= self.V_medic_3 )
            self.txt_lbnpr.current(0)
            
  
            
       
 #------------self.liste_souscategorie_TUBERCULOSE = ["T_medic_1", "T_medic_2", "T_medic_3"]
 
        if self.txt_lbsscat.get() == "T_medic_1":
            self.txt_lbnpr.config(values=self.T_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "T_medic_2":
            self.txt_lbnpr.config(values=self.T_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "T_medic_3":
            self.txt_lbnpr.config(values=self.T_medic_3 )
            self.txt_lbnpr.current(0)
 
 

 #-----------------self.liste_souscategorie_urinaire = ["U_medic_1", "U_medic_2", "U_medic_3"]
 
        if self.txt_lbsscat.get() == "U_medic_1":
            self.txt_lbnpr.config(values=self.U_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "U_medic_2":
            self.txt_lbnpr.config(values=self.U_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "U_medic_3":
            self.txt_lbnpr.config(values=self.U_medic_3 )
            self.txt_lbnpr.current(0)
            
 ##--------self.liste_medicament_cancer = ["cancer_medic_1", "cancer_medic_2", "cancer_medic_3"]
 
        if self.txt_lbsscat.get() == "cancer_medic_1":
            self.txt_lbnpr.config(values=self.cancer_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "cancer_medic_2":
            self.txt_lbnpr.config(values=self.cancer_medic_3)
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "cancer_medic_3":
            self.txt_lbnpr.config(values=self.cancer_medic_3 )
            self.txt_lbnpr.current(0)
 
     
 
 #------------self.liste_souscategorie_Cardio_vascul = ["Cardio_medic_1", "Cardio_medic_2", "Cardio_medic_3"]
 
 
        if self.txt_lbsscat.get() == "Cardio_medic_1":
            self.txt_lbnpr.config(values=self.Cardio_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "Cardio_medic_2":
            self.txt_lbnpr.config(values=self.Cardio_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "Cardio_medic_3":
            self.txt_lbnpr.config(values=self.Cardio_medic_3 )
            self.txt_lbnpr.current(0)
 
  #-------------------self.liste_souscategorie_DIARRHEES = ["DIARR_medic_1", "DIARR_medic_2", "DIARR_medic_3"]
   
        if self.txt_lbsscat.get() == "DIARR_medic_1":
            self.txt_lbnpr.config(values=self.DIARR_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "DIARR_medic_2":
            self.txt_lbnpr.config(values=self.DIARR_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "DIARR_medic_3":
            self.txt_lbnpr.config(values=self.DIARR_medic_3 )
            self.txt_lbnpr.current(0)
  
 #----------------self.liste_souscategorie_Mental = ["Mental_medic_1", "Mental_medic_2", "Mental_medic_3"]
 
        if self.txt_lbsscat.get() == "Mental_medic_1":
            self.txt_lbnpr.config(values=self.Mental_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "Mental_medic_2":
            self.txt_lbnpr.config(values=self.Mental_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "Mental_medic_3 ":
            self.txt_lbnpr.config(values=self.Mental_medic_3 )
            self.txt_lbnpr.current(0)
 
 #-----------------self.liste_souscategorie_MetaboL = ["M_medic_1", "M_medic_2", "M_medic_3"] 
 
        if self.txt_lbsscat.get() == "M_medic_1":
            self.txt_lbnpr.config(values=self.M_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "M_medic_2":
            self.txt_lbnpr.config(values=self.M_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "M_medic_3":
            self.txt_lbnpr.config(values=self.M_medic_3 )
            self.txt_lbnpr.current(0)
            
            
    ###------------------  self.liste_souscategorie_Respir = ["R_medic_1", "R_medic_2", "R_medic_3"]
       
        
        if self.txt_lbsscat.get() == "R_medic_1":
            self.txt_lbnpr.config(values=self.R_medic_1 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "R_medic_2":
            self.txt_lbnpr.config(values=self.R_medic_2 )
            self.txt_lbnpr.current(0)
            
        if self.txt_lbsscat.get() == "R_medic_1":
            self.txt_lbnpr.config(values=self.R_medic_3 )
            self.txt_lbnpr.current(0)
    
    ####---------------------------------------------------------############       
                      
     #if self.txt_lbsscat.get() == " ":
            #self.txt_lbnpr.config(values= )
            #self.txt_lbnpr.current(0)
            
        #if self.txt_lbsscat.get() == " ": 
            #self.txt_lbnpr.config(values= )
            #self.txt_lbnpr.current(0)
            
        #if self.txt_lbsscat.get() == " ":
            #self.txt_lbnpr.config(values= )
            #self.txt_lbnpr.current(0)
    
  
  
  #####--------------------fonction affichage du prix ----------------------------

    def fonction_nom_medicament(self, even=" "):
        if self.txt_lbnpr.get() == "nom_1":
            self.txt_lbpriss.config(values=self.price_nom_1)
            self.txt_lbpriss.current(0)
       
            
        if self.txt_lbnpr.get() == "nom_2":
            self.txt_lbpriss.config(values=self.price_nom_2)
            self.txt_lbpriss.current(0)
            
        
        if self.txt_lbnpr.get() == "nom_3":
            self.txt_lbpriss.config(values= self.price_nom_3)
            self.txt_lbpriss.current(0)
        
        
    #####--------------------self.pal_medic_1 = ["nom_1", "nom_2", "nom_3"]----------------------------
        
    
if __name__=="__main__":
    roots=Tk()
    obj = SuperMarche(roots)
    roots.mainloop()