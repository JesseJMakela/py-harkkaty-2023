######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jesse Mäkelä
# Opiskelijanumero:001154586
# Päivämäärä:15.11.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus
import time
import sys

class TIEDOT:
    aikaleima=None
    aikavyohyke=None
    sademaara=None
      
class PAIVITTAISETTIEDOT:
    paiva=None
    sade=None

class KATEGORIAT:
    kategoria1=0
    kategoria2=0
    kategoria3=0
    kategoria4=0

def nimi(kehote):
    nimi=input("Anna "+kehote+" tiedoston nimi: ")
    return nimi

def lueTiedosto(nimi,tiedot):
    try:
        tiedot.clear()
        n=0
        tiedosto=open(nimi, "r", encoding="UTF-8")
        rivi=tiedosto.readline()
        rivi=tiedosto.readline()
        while (len(rivi)>0):
            sarakkeet=rivi.split(";")
            tulos=TIEDOT()
            tulos.aikaleima=sarakkeet[0].strip("\n")
            tulos.aikavyohyke=sarakkeet[1].strip("\n")
            tulos.sademaara=float(sarakkeet[2].strip("\n"))
            tiedot.append(tulos)
            rivi=tiedosto.readline()
            n+=1
        tiedosto.close()
        print("Tiedosto '"+nimi+"' luettu.")
        print("Tiedostosta lisättiin",n,"datariviä listaan.")
    except OSError:
        print("Tiedoston '"+nimi+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return tiedot

def analysoi(tiedot,tulos,nimi):
    try:
        tulos.clear()
        edellinen=0
        pv=0
        n=0
        for alkio in tiedot:
            paiva=PAIVITTAISETTIEDOT()
            alkaika = time.strptime(alkio.aikaleima, "%Y.%m.%d %H:%M")
            aika=time.strftime("%d.%m.%Y",alkaika)
            if (edellinen==0):
                pv+=alkio.sademaara
            elif (edellinen==aika):
                pv+=alkio.sademaara
            elif (edellinen!=aika):
                paiva.paiva=edellinen
                paiva.sade=pv
                n+=1
                tulos.append(paiva)
                pv=0
                pv+=alkio.sademaara
            edellinen=aika
        paiva.paiva=edellinen
        paiva.sade=pv
        n+=1
        tulos.append(paiva)
        print("Päivittäiset summat laskettu",n,"päivälle.")
    except OSError:
        print("Tiedoston '"+nimi+"' käsittelyssä virhe, lopetetaan.")
    return tulos
    
def kategoriaAnalyysi(tulos):
    kategoriat=KATEGORIAT()
    for alkio in tulos:
        sade=alkio.sade
        if (sade>=4.5):
            kategoriat.kategoria1+=1
        elif (1.0<=sade<4.5):
            kategoriat.kategoria2+=1
        elif (0.3<=sade<1.0):
            kategoriat.kategoria3+=1
        elif (0.3>sade):
           kategoriat.kategoria4+=1
    print("Päivät kategorisoitu 4 kategoriaan.")
    return kategoriat

def kirjoitaTulokset(nimi,tulos,kategoriat):
    try:
        tiedosto=open(nimi,"w",encoding="UTF-8")
        rivi1="Kategoria;Päivien lukumäärä:\n"
        rivi2="Kategoria 1;{}\n"
        rivi3="Kategoria 2;{}\n"
        rivi4="Kategoria 3;{}\n"
        rivi5="Kategoria 4;{}\n\n"
        tiedosto.write(rivi1)
        tiedosto.write(rivi2.format(kategoriat.kategoria1))
        tiedosto.write(rivi3.format(kategoriat.kategoria2))
        tiedosto.write(rivi4.format(kategoriat.kategoria3))
        tiedosto.write(rivi5.format(kategoriat.kategoria4))

        rivi7="Kaikki päivittäiset sademäärät:\n"
        rivi8="Pvm;mm\n"
        tiedosto.write(rivi7)
        tiedosto.write(rivi8)
        for alkio in tulos:
            rivi=alkio.paiva+";"+str(round(alkio.sade,1))+"\n"
            tiedosto.write(rivi)
        tiedosto.close()
        print("Tiedosto '"+nimi+"' kirjoitettu.")
    except OSError:
        print("Tiedoston '"+nimi+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def viikonPvAnalyysi(tulos,nimi):
    mon=0.0
    tue=0.0
    wed=0.0
    thu=0.0
    fri=0.0
    sat=0.0
    sun=0.0
    
    for alkio in tulos:
        aika=time.strptime(alkio.paiva,"%d.%m.%Y")
        viikko=aika.tm_wday
        if (viikko==0):
            mon+=alkio.sade
        elif (viikko==1):
            tue+=alkio.sade
        elif (viikko==2):
            wed+=alkio.sade
        elif (viikko==3):
            thu+=alkio.sade
        elif (viikko==4):
            fri+=alkio.sade
        elif (viikko==5):
            sat+=alkio.sade
        elif (viikko==6):
            sun+=alkio.sade
    try:
        tiedosto=open(nimi,"w",encoding="UTF-8")
        rivi1="Viikonpäivä;Sadekertymä\n"
        rivi2="Maanantai;{}\n"
        rivi3="Tiistai;{}\n"
        rivi4="Keskiviikko;{}\n"
        rivi5="Torstai;{}\n"
        rivi6="Perjantai;{}\n"
        rivi7="Lauantai;{}\n"
        rivi8="Sunnuntai;{}\n"

        tiedosto.write(rivi1)
        tiedosto.write(rivi2.format(round(mon,1)))
        tiedosto.write(rivi3.format(round(tue,1)))
        tiedosto.write(rivi4.format(round(wed,1)))
        tiedosto.write(rivi5.format(round(thu,1)))
        tiedosto.write(rivi6.format(round(fri,1)))
        tiedosto.write(rivi7.format(round(sat,1)))
        tiedosto.write(rivi8.format(round(sun,1)))
        tiedosto.close()
        print("Tiedosto '"+nimi+"' kirjoitettu.")
    except OSError:
        print("Tiedoston '"+nimi+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None
# eof