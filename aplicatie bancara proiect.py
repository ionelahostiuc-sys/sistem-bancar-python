def creeaza_tranzactie(zi,suma,tip):
    if zi<1 or zi>31:
        raise ValueError("Ziua trebuie sa fie intre 1 si 31")
    if suma<0:
        raise ValueError("Suma trebuie sa fie mai mare de 0")
    if tip not in ["intrare", "iesire"]:
        raise ValueError("Tipul introdus trebuie sa fie doare intrare sau iesire")
    return {"zi": zi, "suma": suma,"tip" :tip}
def pentru_undo(lista_tranzactii,istoric_undo):
    copie_lista=[]
    for x in lista_tranzactii:
        copie_lista.append({"zi":x["zi"], "suma":x["suma"], "tip":x["tip"]})

    istoric_undo.append(copie_lista)
def adauga_tranzactie(lista_tranzactii,istoric_undo):
    print("\n---1.Adauga tranzactie---")
    try:
        zi=int(input("introduceti zi: "))
        suma=int(input("introduceti suma: "))
        tip=input("introduceti tip: ")
        noua_tranzactie=creeaza_tranzactie(zi,suma,tip)
        pentru_undo(lista_tranzactii,istoric_undo)
        lista_tranzactii.append(noua_tranzactie)
        print("Felicitari!Ati introdus o noua tranzactie")
    except ValueError as eroare:
        print(f'Eroare: {eroare}')
def actualizare_tranzactie(lista_tranzactii,istoric_undo):
    print("\n---2.Actualizare tranzactie---")
    if len(lista_tranzactii)==0:
        print("Eroare.Nu exista tranzactie in lista")
        return
    try:
        index=int(input("introduceti index: "))
        if index<0 or index>len(lista_tranzactii):
            print('Eroare, acest index nu exista')
            return
        print('introduceti noile date: ')
        zi=int(input("introduceti noua zi: "))
        suma=int(input("introduceti noua suma: "))
        tip=input("introduceti noul tipul(intrare-iesire): ")
        tranzactie_noua=creeaza_tranzactie(zi,suma,tip)
        pentru_undo(lista_tranzactii,istoric_undo)

        lista_tranzactii[index]=tranzactie_noua
        print("Felicitari!Ati actualizare tranzactie cu succes!")
    except ValueError as eroare:
        print(f"Eroare:{eroare} ")
def stergere_tranzactie(lista_tranzactii,istoric_undo):
    print("\n---3.Stergere tranzactie---")
    print("a. Sterge toate tranzactiile dintr-o zi")
    print("b. Sterge toate tranzactiile dintr-o perioada")
    print("c. Sterge toate tranzactiile de un anumit tip")
    optiune=input("Alegeti o optiune(a,b,c): ")
    if optiune == "a":
        try:
            zi = int(input("introduceti zi: "))
            pentru_undo(lista_tranzactii, istoric_undo)
            i = len(lista_tranzactii) - 1
            while i >= 0:
                if lista_tranzactii[i]["zi"] == zi:
                    lista_tranzactii.pop(i)
                i -= 1

            print("Ati sters cu succes tranzactiile din ziua aleasa")
        except ValueError:
            print("Eroare ")

    elif optiune=="b":
        try:
            zi_inceput=int(input("introduceti ziua de inceput: "))
            zi_sfarsit=int(input("introduceti ziua de sfarsit: "))
            pentru_undo(lista_tranzactii,istoric_undo)
            i=len(lista_tranzactii)-1
            while i>=0:
                if zi_inceput<=lista_tranzactii[i]["zi"]<=zi_sfarsit:
                    lista_tranzactii.pop(i)
                i-=1
            print("Ati sters cu succes tranzactiile din perioada aleasa!")
        except ValueError:
            print("Eroare ")
    elif optiune=="c":
        tip=input("introduceti tip: ")
        if tip in ["intrare","iesire"]:
            pentru_undo(lista_tranzactii,istoric_undo)
            i=len(lista_tranzactii)-1
            while i>=0:
                if lista_tranzactii[i]["tip"]==tip:
                    lista_tranzactii.pop(i)
                i-=1
            print("Ati sters cu succes tranzactile de tipul selectat")
        else:
            print("Tip invalid")
    else:
        print("Eroare ")


def cautari(lista_tranzactii):
    print("\n--- 4. Căutări ---")
    print("a. Tranzacții cu sume mai mari decât o sumă dată")
    print("b. Tranzacții efectuate înainte de o zi și mai mari decât o sumă")
    print("c. Tranzacții de un anumit tip")
    sub_optiune = input("Alegeți opțiunea (a/b/c): ")

    if sub_optiune == "a":
        suma_data = float(input("Introduceți suma: "))
        for t in lista_tranzactii:
            if t["suma"] > suma_data:
                print(f"Ziua: {t['zi']} | Suma: {t['suma']} | Tip: {t['tip']}")

    elif sub_optiune == "b":
        zi_data = int(input("Înainte de ziua: "))
        suma_data = float(input("Și cu suma mai mare decât: "))
        for t in lista_tranzactii:
            if t["zi"] < zi_data and t["suma"] > suma_data:
                print(f"Ziua: {t['zi']} | Suma: {t['suma']} | Tip: {t['tip']}")

    elif sub_optiune == "c":
        tip_dat = input("Tipul (intrare/iesire): ")
        for t in lista_tranzactii:
            if t["tip"] == tip_dat:
                print(f"Ziua: {t['zi']} | Suma: {t['suma']} | Tip: {t['tip']}")


def rapoarte(lista_tranzactii):
    print("\n--- 5. Rapoarte ---")
    print("a. Suma totală a tranzacțiilor de un anumit tip")
    print("b. Soldul contului la o dată specificată")
    print("c. Tipărește tranzacțiile de un anumit tip ordonate după sumă")
    sub_optiune = input("Alegeți opțiunea(a,b,c): ")

    if sub_optiune == "a":
        tip = input("Tipul: ")
        total = 0.0
        for t in lista_tranzactii:
            if t["tip"] == tip:
                total += t["suma"]
        print(f"Suma totală pentru '{tip}' este: {total}")

    elif sub_optiune == "b":
        zi = int(input("Introduceți ziua: "))
        sold = 0.0
        for t in lista_tranzactii:
            if t["zi"] <= zi:
                if t["tip"] == "intrare":
                    sold += t["suma"]
                else:
                    sold -= t["suma"]
        print(f"Soldul contului la sfârșitul zilei {zi} este: {sold}")

    elif sub_optiune == "c":
        tip = input("Tipul (intrare/iesire): ")
        filtrate = []
        for t in lista_tranzactii:
            if t["tip"] == tip:
                filtrate.append(t)

        for i in range(len(filtrate)):
            for j in range(i + 1, len(filtrate)):
                if filtrate[i]["suma"] > filtrate[j]["suma"]:
                    filtrate[i], filtrate[j] = filtrate[j], filtrate[i]

        print(f"Tranzacții de tip {tip} ordonate după sumă:")
        for t in filtrate:
            print(f"Ziua: {t['zi']} | Suma: {t['suma']}")


def filtrare(lista_tranzactii, istoric_undo):
    print("\n--- 6. Filtrare ---")
    print("a. Elimină toate tranzacțiile care NU sunt de un anumit tip")
    print("b. Elimină tranzacțiile mai mici decât o sumă dată care au tipul specificat")
    sub_optiune = input("Alegeți opțiunea (a/b): ")

    if sub_optiune == "a":
        tip = input("Păstrează doar tipul (intrare/iesire): ")
        if tip in ["intrare", "iesire"]:
            pentru_undo(lista_tranzactii, istoric_undo)
            i = len(lista_tranzactii) - 1
            while i >= 0:
                if lista_tranzactii[i]["tip"] != tip:
                    lista_tranzactii.pop(i)
                i -= 1
            print("Filtrare completă.")

    elif sub_optiune == "b":
        suma_limita = float(input("Elimină sumele mai mici decât: "))
        tip_specificat = input("Pentru tipul: ")

        pentru_undo(lista_tranzactii, istoric_undo)
        i = len(lista_tranzactii) - 1
        while i >= 0:
            if lista_tranzactii[i]["tip"] == tip_specificat and lista_tranzactii[i]["suma"] < suma_limita:
                lista_tranzactii.pop(i)
            i -= 1
        print("Filtrare completă.")


def undo(lista_tranzactii, istoric_undo):
    print("\n--- 7. Undo ---")
    if len(istoric_undo) == 0:
        print("Nu se mai poate face undo! Ești la starea inițială.")
        return lista_tranzactii
    ultima_stare = istoric_undo.pop()
    print("Undo realizat cu succes! Ultima operație a fost anulată.")
    return ultima_stare


def porneste_aplicatia():
    lista_tranzactii = []
    istoric_undo = []

    while True:
        print("--- MENIU CONT BANCAR ---")
        print("1. Adăugare de noi tranzacții")
        print("2. Actualizare tranzactie")
        print("3. Stergere")
        print("4. Cautari")
        print("5. Rapoarte")
        print("6. Filtrare")
        print("7. Undo")
        print("0. Ieșire")

        optiune = input("Alegeți o opțiune (0-7): ")

        if optiune == "1":
            adauga_tranzactie(lista_tranzactii, istoric_undo)
        elif optiune == "2":
            actualizare_tranzactie(lista_tranzactii, istoric_undo)
        elif optiune == "3":
            stergere_tranzactie(lista_tranzactii, istoric_undo)
        elif optiune == "4":
            cautari(lista_tranzactii)
        elif optiune == "5":
            rapoarte(lista_tranzactii)
        elif optiune == "6":
            filtrare(lista_tranzactii, istoric_undo)
        elif optiune == "7":
            lista_tranzactii=undo(lista_tranzactii, istoric_undo)
        elif optiune == "0":
            print("Aplicația s-a închis. La revedere!")
            break
        else:
            print("Opțiune invalidă! Încearcă din nou.")

porneste_aplicatia()
