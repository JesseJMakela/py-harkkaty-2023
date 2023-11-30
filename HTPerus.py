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
import HTPerusKirjasto

def valikko():
    x=1
    while (x==1):
        print("Valitse haluamasi toiminto:")
        print("1) Lue tiedosto")
        print("2) Analysoi")
        print("3) Kirjoita tiedosto")
        print("4) Analysoi viikonpäivittäiset sademäärät")
        print("0) Lopeta")
        try:
            valinta=int(input("Anna valintasi: "))
            x=0
        except ValueError:
            print("Virhe, valinta ei ollut kokonaisluku.")
            print()
    return valinta

def paaohjelma():
    tiedot=[]
    tulos=[]
    while True:
        valinta=valikko()
        
        if (valinta==1):
            nimi1=HTPerusKirjasto.nimi("luettavan")
            tiedot=HTPerusKirjasto.lueTiedosto(nimi1,tiedot)
        
        elif (valinta==2):
            if (len(tiedot)!=0):
                tulos=HTPerusKirjasto.analysoi(tiedot,tulos,nimi1)
                kategoriat=HTPerusKirjasto.kategoriaAnalyysi(tulos)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif (valinta==3):
            if (len(tulos)!=0):
                nimi2=HTPerusKirjasto.nimi("kirjoitettavan")
                HTPerusKirjasto.kirjoitaTulokset(nimi2,tulos,kategoriat)
            else: 
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")

        elif (valinta==4):
            if (len(tulos)!=0):
                nimi3=HTPerusKirjasto.nimi("kirjoitettavan")
                HTPerusKirjasto.viikonPvAnalyysi(tulos,nimi3)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif (valinta==0):
            print("Lopetetaan.")
            tiedot.clear()
            tulos.clear()
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof