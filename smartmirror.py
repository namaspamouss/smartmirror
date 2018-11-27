#!/usr/bin/python3.6
# -*-coding:utf-8 -*

#fichier a coller dans le raspi du smartmirroir pour afficher date et heure

import time
import datetime
import os
import tkinter
import threading

def quitter(ev=None):
    quit()

def date():
    global date_label
    while True:
        jour_lettre=time.strftime("%A") #recup du jour (ex: monday, tuesday,...)
        jour_lettre=str(jour_lettre) #conversion de la date en francais
        if jour_lettre=="Monday":
            jour_lettre="Lundi"
        if jour_lettre=="Tuesday":
            jour_lettre="Mardi"
        if jour_lettre=="Wednesday":
            jour_lettre="Mercredi"
        if jour_lettre=="Thursday":
            jour_lettre="Jeudi"
        if jour_lettre=="Friday":
            jour_lettre="Vendredi"
        if jour_lettre=="Saturday":
            jour_lettre="Samedi"
        if jour_lettre=="Sunday":
            jour_lettre="Dimanche"

        jour_chiffre=time.strftime("%d") #recup du jour (du 1 au 31)

        mois=time.strftime("%m") #recup du mois
        if mois=="01": # conversion du mois en francais
            mois="Janvier"
        if mois=="02":
            mois="Fevrier"
        if mois=="03":
            mois="mars"
        if mois=="04":
            mois="avril"
        if mois=="05":
            mois="mai"
        if mois=="06":
            mois="juin"
        if mois=="07":
            mois="juillet"
        if mois=="08":
            mois="aout"
        if mois=="09":
            mois="septembre"
        if mois=="10":
            mois="octobre"
        if mois=="11":
            mois="novembre"
        if mois=="12":
            mois="decembre"

        annee=time.strftime("%Y") #recup de l'année
        date_a_afficher=jour_lettre+" "+jour_chiffre+" "+mois+" "+annee #formatage de la date 
        date_label.config(text=date_a_afficher)
        time.sleep(0.1)

def heure():
    global heure_label
    while True:
        heure_actuelle=time.localtime() #recup de l'heure avec conversion des min et sec en format 2 chiffres
        heureh=heure_actuelle[3]
        minute=heure_actuelle[4]
        minute="%02d"%minute
        seconde=heure_actuelle[5]
        seconde="%02d"%seconde
        heure_a_afficher=f"{heureh}:{minute}:{seconde}" #formatage de l'heure avec des ":" pour faire plus joli
        heure_label.config(text=heure_a_afficher)
        time.sleep(0.1)


app=tkinter.Tk() #création de la fenetre
w, h = app.winfo_screenwidth(), app.winfo_screenheight() #redimmensionnement de la fenetre en plein écran
app.overrideredirect(1)
app.geometry("%dx%d+0+0" % (w, h))

app.bind_all("<Escape>",quitter) #commande quitter avec echap

quitter=tkinter.Button(app, text="QUITTER", command=quitter) #bouton tk pour quitter (a enlever pour la version finale)
date_label=tkinter.Label(app, text="", bg="black", fg="white",font=(None,60)) #date affichée en blanc sur fond noir avec une police plus grande
heure_label=tkinter.Label(app, text="", bg="black", fg="white",font=(None,100)) #idem mais pour l'heure

heure_label.pack()
date_label.pack()
app.configure(bg="black") #fond noir sur tk pour garder le reflet du mirroir
quitter.pack()

THheure=threading.Thread(target=heure)
THdate=threading.Thread(target=date)
THheure.setDaemon(True)
THdate.setDaemon(True)
THheure.start()
THdate.start()
app.mainloop()
