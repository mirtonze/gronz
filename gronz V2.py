import random
import pyperclip
from numpy import asarray
from PIL import Image
import tkinter as tk
import win32clipboard
from io import BytesIO
from PIL import ImageGrab

Liste1=['x', 'i', 'D', 'I', 'Z', 'b', 'h', "'", '1', '¤', '(', '3', 'H', 'ê', '2', 'C', '[', 'µ', ';', 'y', 'O', 'G', '5', '=', '$', '°', 'ë', '*', 'g', '/', 'o', 'W', 'è', '!', 'ç', 'J', 'w', 'à', 'ù', '-', 'Q', 'd', '@', 'n', 'û', 'E', 'ô', 'L', 'F', '§', '<', 'é', 'ö', 'ü', 'z', 'X', '+', 'q', '}', '%', 'ä', '_', '~', 'm', 'l', '£', '#', '{', 'A', 'u', '/', '-', ')', 's', 'M', 'r', '7', 'B', ':', 'f', 'î', 'k', '>', 'S', 'N', '8', '&', '6', '|', '.', '.', 'â', 'c', '`', 'P', 'U', 't', 'R', 'e', '4', 'v', 'K', 'a', 'ï', 'p', '*', '^', 'T', ' ', '²', 'j', 'V', '9', 'Y', ']']
Liste2=['8', 'R', '_', '{', 't', 'Q', 'O', '1', '-', '2', 'C', '@', 'T', 'U', 'J', 'Z', 'ë', '.', 'î', 'o', 'è', '&', 'u', ':', '*', 'a', 'X', 'ü', 'Y', '/', ' ', 'g', 'A', '^', '+', '}', 'i', 'F', 'r', '£', 'y', 'v', 'à', '<', 'H', 'P', 'W', 'h', '°', 'S', 's', '-', '|', '9', 'K', 'ç', 'ï', 'j', '[', '6', ']', 'z', 'û', '/', 'V', '%', '.', 'L', '4', 'c', 'B', '=', 'm', '5', 'N', 'e', 'q', 'µ', '²', 'p', "'", ';', 'G', '$', 'ô', 'I', '(', '!', '`', 'w', 'd', 'E', ')', 'ä', 'n', 'â', 'b', '~', '¤', '3', 'ù', 'M', 'k', '§', '#', '>', 'ê', 'l', 'x', 'é', 'ö', 'f', '*', 'D', '7']
Liste3=['W', '[', 'x', ';', 'ï', '.', 'T', '_', '~', 'h', 'î', '$', 'y', 'ä', '²', '(', '{', 'à', '^', 'c', 'r', 'O', 'A', '.', '8', 'B', 'n', 'e', 'd', '!', 'p', 'J', 'û', '9', 's', 'i', 'µ', '-', '/', 'b', 'q', 'M', '}', '/', 'u', 'm', 'w', '|', '@', ' ', '*', 'U', 'g', ']', '2', 'o', 'L', 'P', ')', '4', '-', '+', '¤', 'ê', '°', 'ç', 'S', 'I', '5', 'E', '£', 'ë', '<', 'ô', 'v', 't', '`', 'j', 'è', 'â', 'D', '3', 'ü', '&', 'é', 'k', 'l', ':', 'ù', 'Z', 'f', '#', '§', 'Q', '>', '6', '7', 'ö', "'", 'C', 'z', 'X', 'H', 'N', 'K', 'R', 'G', 'Y', '*', '%', 'F', '=', 'a', '1', 'V']
Liste4=['ï', 'ä', '*', '|', 'î', '.', 'I', 's', '<', 'B', '5', ';', '£', '_', 'M', '`', 'i', '8', 'E', 'ç', 'U', 'Q', 'u', '4', 'a', 'd', 'O', 'b', 'â', 'ë', 'è', '7', '3', ')', 'J', '1', 'P', '²', 'R', '(', 'm', 'h', ':', 'r', 'v', '>', '/', 'Z', '#', 'x', '}', 'ô', 'k', 'c', 'z', 'g', 'f', 'N', 'e', 't', 'F', 'Y', 'ö', '*', '$', '^', '[', 'é', 'p', 'X', 'G', 'û', '=', '{', 'D', 'l', 'w', 'à', 'µ', '9', 'ü', 'j', 'ù', 'y', '¤', '§', 'q', 'n', '!', ']', ' ', 'T', 'W', '/', '6', '2', '+', '~', '%', '&', 'L', 'A', 'S', '°', 'H', 'C', "'", 'K', 'o', '-', '-', '.', 'V', 'ê', '@']
Liste5=['ç', '*', '^', 'A', '}', ';', 'P', '2', '9', 'î', 'G', '3', '`', '!', 'B', '(', '4', '5', '=', 'n', 'R', '#', 'û', '/', 'J', '°', '<', '$', 'f', ')', '7', 'v', '§', '.', '+', '-', 'à', 'T', 'z', 'D', '1', 'ö', 'a', '_', '%', '~', 'y', 'c', 'l', 'b', 'X', 'ù', 'g', 'N', 'j', 'E', 'é', 'è', 'Z', 'r', 'w', 'i', 'W', '[', '²', 'e', 'M', 'O', 'x', 'ü', 'â', 'ô', '|', 't', '8', '.', 'V', 'd', 'S', ':', '*', 'F', 'H', '/', '¤', 'ë', 'h', 'Q', '£', 'ê', 'K', 's', '-', '&', 'p', ']', 'ä', 'C', '@', ' ', '>', 'm', 'L', "'", '{', 'ï', 'I', 'u', '6', 'o', 'k', 'Y', 'µ', 'U', 'q']
Liste6=['ë', 'ü', 'µ', 'î', 'Z', 'R', 'Y', '!', 'P', 'c', 'ê', '-', '°', 'D', 'u', '§', '$', 'ö', 'p', '#', '>', '(', '£', '<', 'è', 'C', ' ', '6', 'A', 'O', 'w', '4', 'I', 'g', 'ù', '*', '5', 'b', 'ô', ']', 'n', '^', 'L', '9', '|', '.', '1', '-', 'G', 'H', 'S', '3', 't', 'ï', 'é', 'à', 'i', 'z', '&', 'h', 'x', 'o', 'T', '@', 'M', 'a', 'W', '8', '~', '=', "'", 'ä', ';', 'k', 'Q', '²', '/', 'q', 'F', ')', '/', 'ç', 'l', '%', 'e', 'm', '¤', '[', 'j', 'f', '_', 'û', '*', '.', '{', 'B', 'X', ':', 'd', '}', 'U', 'r', 'â', 'v', 'E', 'V', '2', 'J', '+', 'K', 'y', 'N', '7', '`', 's']
Liste7=['ü', '°', 'n', 'µ', '£', 'i', ';', 'K', '}', 'f', '3', 'ê', 'c', 'D', '#', 'd', 'ö', 'à', '1', 'u', 'î', 'ç', 'P', '{', '-', 'j', 'J', ']', 'X', '.', '&', 'k', 'q', 'w', 'Q', 'è', 'B', 'N', ':', 'C', '~', '2', '^', '-', '>', 'ù', 'e', 'A', 'U', '*', '<', '=', 'l', '¤', '7', 'H', '.', 'é', ' ', 'o', 'R', '@', 'x', '|', 'r', 'b', '[', 'O', 'g', 'S', 'y', 't', '4', 'ë', 'G', 'v', 'p', 'E', 'ï', '!', '%', 'M', '(', 'm', 'I', 'a', '6', '9', 'û', 'z', 'T', 'Z', 'h', '/', 's', '8', 'F', 'W', '²', 'L', 'ô', '$', '+', ')', 'â', 'V', '/', '5', '*', '`', "'", '_', 'Y', 'ä', '§']
Liste8=['ê', '4', 'e', 'I', '9', 'µ', '+', 'X', 'w', 'O', 'M', 'G', 'J', ':', '1', 'B', '>', '6', 'ô', '-', '8', '2', '`', 'E', 'i', 'F', '!', '=', 'K', 'D', '°', 'q', 'ù', 'l', 'o', 'h', ' ', 'z', '(', '<', 'u', 'R', 'V', 'à', '~', 'd', 'f', 'W', 'ä', '²', '.', 'ï', '7', '}', 'c', 's', '_', 'ç', '£', 'A', '@', 'g', 'a', 'é', 'C', '§', 'P', '&', '%', '|', '#', '5', 'j', 'Q', '.', '/', '$', 'ö', '*', 'n', 'p', 'Z', ']', 'N', '/', 'ë', 'r', '-', 'û', 'S', '¤', 'U', 'T', '3', 'Y', 'H', 'y', 'v', 'è', 'x', ')', 'm', '*', 'î', '{', ';', 'â', 'L', '[', 'b', '^', 'ü', 't', "'", 'k']
Liste9=['â', '7', 'd', '%', ' ', 'L', '9', '1', '&', 'J', 's', '/', 'O', 'ö', '#', "'", 'c', '6', '@', 'è', 'e', 'H', '(', 'G', 'p', 'y', '-', 'a', '}', 'C', 'u', 'z', '+', '`', '.', 'û', '-', '<', '^', 'T', 'ê', '$', 'î', '{', '3', 'é', 'I', ']', 'N', '2', 'W', 'ü', '~', 'A', 'D', 'n', 'F', 'ä', 'U', 'g', 'µ', 'q', ':', 'ë', '8', 'f', 'S', ')', '>', '°', 'P', '£', '_', '[', '=', 'v', 'ï', 'X', 'ù', 'l', '.', '/', 'k', '!', 'M', 'E', '¤', 'i', 'x', '*', '§', '4', 'R', '5', 'h', 'w', 'ç', 'ô', '²', 'B', 'r', 'Y', 'Z', 'j', 'V', 'à', 'Q', '|', '*', ';', 'm', 'o', 'K', 't', 'b']# les listes de 1 à 9 liste de 1 à 9
def cesarcrypt(firstmsg):
    # Choix du décalage
    decalage = random.randint(10, 99)
    #print ("décalage :",decalage)
    liste_choice = random.randint(1, 9)
    #print ("liste n° :",liste_choice)

    if liste_choice == 1:
        liste_ABC = Liste1
    elif liste_choice == 2:
        liste_ABC = Liste2
    elif liste_choice == 3:
        liste_ABC = Liste3
    elif liste_choice == 4:
        liste_ABC = Liste4
    elif liste_choice == 5:
        liste_ABC = Liste5
    elif liste_choice == 6:
        liste_ABC = Liste6
    elif liste_choice == 7:
        liste_ABC = Liste7
    elif liste_choice == 8:
        liste_ABC = Liste8
    elif liste_choice == 9:
        liste_ABC = Liste9
    else:
        print("Erreur : choix de liste invalide")
        exit(0)

    encrypted_message = ""
    for lettre in firstmsg:
        if lettre in liste_ABC:
            position = liste_ABC.index(lettre)
            nouvelle_position = (position + decalage) % len(liste_ABC)
            lettre_cryptee = liste_ABC[nouvelle_position]
            encrypted_message += lettre_cryptee
            decalage += 1
        else:
            encrypted_message += lettre

    decalage = decalage - len(firstmsg)

    return f"{liste_choice}{decalage}{encrypted_message}"
def crypt(msg, key):
    longmsg = len(msg)  # calcul la longueur du msg
    #print("taille du msg :", longmsg)

    resultats_ascii = []
    resultats_ascii_caract = []
    valeur_ascii_du_text_final = []

    # transphorme toute les lettre du text en nombre ascii et les met dans une liste
    for lettre in msg:
        position_ascii = ord(lettre)  # transforme une lettre en sa position ascii
        resultats_ascii.append(position_ascii)  # Ajoute la valeur ASCII à la liste
    #print("liste des caractères en ASCII du message :", resultats_ascii)

    # créer la clé de chifrement en fonction de la longueur du texte
    keyfinal = (key * longmsg)[:longmsg]
    #print("keyfinal :", keyfinal)

    # passe la clé final en ascii dans une liste
    for caract in keyfinal:
        position_ascii_caract = ord(caract)  # transforme une lettre en sa position ascii
        resultats_ascii_caract.append(position_ascii_caract)  # Ajoute la valeur ASCII à la liste
    #print("clé en forme ASCII :", resultats_ascii_caract)

    #additionne les valeurs ascii du text et de la clé et les met dans une liste
    for i in range(len(resultats_ascii)):
        addition = resultats_ascii[i] + resultats_ascii_caract[i]
        valeur_ascii_du_text_final.append(addition)

    #print("valeurs ASCII du texte final :", valeur_ascii_du_text_final)
    return (valeur_ascii_du_text_final)


    #text_crypte = ""
    #for valeur_ascii in valeur_ascii_du_text_final:
    #    caractere = chr(valeur_ascii)
    #    text_crypte += caractere

    #print("Voici votre texte crypté :", text_crypte.encode('utf-8').decode('utf-8'))
    #print("Sachant que le texte d'origine était :", msg)
    #print("Et la clé utilisée :", key)
    #pyperclip.copy(text_crypte)
def hide(msg, image_name):


    # try:
    #     img = ImageGrab.grabclipboard()
    #     if img is None:
    #         print("Aucune image trouvée dans le presse-papiers")
    #     else:
    #         print("Image trouvée dans le presse-papiers")
    #         # Vous pouvez maintenant utiliser la variable `img` pour manipuler l'image
    # except Exception as e:
    #     print(f"Erreur lors de la récupération de l'image du presse-papiers: {e}")

    image = Image.open(image_name)
    data = asarray(image).copy()


    # Convertir le message en octet
    final_message = ""
    for lettre in msg:
        position_ascii = ord(lettre)
        binaire = bin(position_ascii)[2:]
        while len(binaire) < 8:
            binaire = "0" + binaire
        final_message += binaire
    #print("Messsage encodé en binaire :", final_message)

    # Recupère la longueur et l'inscrit sur 2 octet (16bits)
    longueur = len(final_message)
    binaire = bin(longueur)[2:]
    while len(binaire) < 16:
        binaire = "0" + binaire
    #print("Taille a encoder :", binaire)
    result_message = binaire + final_message
    #print('Result message', result_message)
    # data[y][x][rgb]
    #print(data[0][3])
    tour = 0
    y = 0
    for line in data:
        x = 0
        for colonne in line:
            rgb = 0
            for couleur in colonne:
                valeur = data[y][x][rgb]
                binaire = bin(valeur)[2:]
                binaire_list = list(binaire)
                del binaire_list[-1]
                binaire_list.append(result_message[tour])
                decimal = int("".join(binaire_list), 2)
                data[y][x][rgb] = decimal
                tour += 1
                rgb += 1
                if tour >= len(result_message):
                    break
            x += 1
            if tour >= len(result_message):
                break
        y += 1
        if tour >= len(result_message):
            break
    imagefinal = Image.fromarray(data)

    repvalide = False
    pressimage = ""

    while repvalide != True:
        print("voulez vous mettre l'image dans le presse papier ? (oui ou non)")  # mettre l'image dans le press papier
        pressimage = input("->")
        if pressimage.lower() == "oui":
            print()

            # Ouvrir l'image enregistrée et la convertir en un objet Image
            image = Image.open(image_name)

            # Copier l'objet Image dans le presse-papiers
            output = BytesIO()
            image.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]
            output.close()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()

            print("votre image est copiée dans le press papier")
            repvalide = True

        elif pressimage.lower() == "non":
            print()
            print("votre image ne sera pas copié dans le press papier")
            print()
            repvalide = True

        else:
            print("invalide sintax")
            print()


    print("rentrez exit pour annuler la création de l'image")  # annulation de la création de l'image
    annulation_de_création_de_limage = input("->")

    if annulation_de_création_de_limage == "exit":
        print()

    else:
        print()
        imagefinal.save(nom_de_limage )
def discover(image_name):
    image = Image.open(image_name)
    data = asarray(image).copy()

    tour = 0
    taille = ""
    message = ""
    taille_new = 12673
    y = 0
    for line in data:
        x = 0
        for colonne in line:
            rgb = 0
            for color in colonne:
                valeur = data[y][x][rgb]
                binaire = bin(valeur)[2:]
                last = binaire[-1]
                if tour < 16:
                    taille += last
                if tour == 16:
                    taille_new = int(taille, 2)
                if tour - 16 < taille_new:
                    message += last
                if tour - 16 >= taille_new:
                    break
                tour += 1
                rgb += 1
            if tour - 16 >= taille_new:
                break
            x += 1
        if tour - 16 >= taille_new:
            break
        y += 1
    #print(message)
    octet = []
    for i in range(len(message) // 8):
        octet.append(message[i * 8:(i + 1) * 8])
    #print(octet)
    result = ""
    for oct in octet:
        index = int(oct, 2)
        lettre_ascii = chr(index)
        #print(lettre_ascii)
        result += lettre_ascii
    #print("MESSAGE:", str(result)[2:])
    result_image_ascii = (str(result)[2:])
    return result_image_ascii
def decrypt(valeur_ascii_du_text_final, key):
    resultats_ascii_caract = []
    resultats_ascii_decrypt = []

    # Passe la clé finale en ASCII dans une liste
    for caract in key:
        position_ascii_caract = ord(caract)  # Transforme une lettre en sa position ASCII
        resultats_ascii_caract.append(position_ascii_caract)  # Ajoute la valeur ASCII à la liste

    # Répète la clé si elle est plus courte que le texte
    if len(resultats_ascii_caract) < len(valeur_ascii_du_text_final):
        repetitions = len(valeur_ascii_du_text_final) // len(resultats_ascii_caract) + 1
        resultats_ascii_caract *= repetitions

    # Soustrait les valeurs ASCII du texte final avec les valeurs ASCII de la clé
    for i in range(len(valeur_ascii_du_text_final)):
        soustraction = valeur_ascii_du_text_final[i] - resultats_ascii_caract[i]
        resultats_ascii_decrypt.append(soustraction)

    texte_decrypte = ""
    for valeur_ascii in resultats_ascii_decrypt:
        caractere = chr(valeur_ascii)
        texte_decrypte += caractere

    return texte_decrypte
def cesardecrypt(encrypted_message):
    # Extraire le numéro de liste, le décalage et le message crypté
    liste_choice = int(encrypted_message[0])
    decalage = int(encrypted_message[1:3])
    message_crypte = encrypted_message[3:]

    if liste_choice == 1:
        liste_ABC = Liste1
    elif liste_choice == 2:
        liste_ABC = Liste2
    elif liste_choice == 3:
        liste_ABC = Liste3
    elif liste_choice == 4:
        liste_ABC = Liste4
    elif liste_choice == 5:
        liste_ABC = Liste5
    elif liste_choice == 6:
        liste_ABC = Liste6
    elif liste_choice == 7:
        liste_ABC = Liste7
    elif liste_choice == 8:
        liste_ABC = Liste8
    elif liste_choice == 9:
        liste_ABC = Liste9
    else:
        print("Erreur : choix de liste invalide")
        exit(0)

    decrypted_message = ""
    for lettre in message_crypte:
        if lettre in liste_ABC:
            position = liste_ABC.index(lettre)
            ancienne_position = (position - decalage) % len(liste_ABC)
            lettre_decryptee = liste_ABC[ancienne_position]
            decrypted_message += lettre_decryptee
            decalage += 1
        else:
            decrypted_message += lettre

    return decrypted_message



boucle = "reste"
while boucle != "exit":# lancement de la boucle pour le programme
    print("      ___           ___           ___           ___           ___      ")
    print("     /\  \         /\  \         /\__\         /\  \         /\  \     ")
    print("    /::\  \       /::\  \       /::\  \       /::|  |        \:\  \   ")
    print("   /:/\:\  \     /:/\:\  \     /:/\:\  \     /:|:|  |         \:\  \  ")
    print("  /:/  \:\  \   /::\~\:\  \   /:/  \:\  \   /:/|:|  |__        \:\  \ ")
    print(" /:/__/_\:\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/ |:| /\__\ _______\:\__\ ")
    print(" \:\  /\ \/__/ \/_|::\/:/  / \:\  \ /:/  / \/__|:|/:/  / \::::::::/__/")
    print("  \:\ \:\__\      |:|::/  /   \:\  /:/  /      |:/:/  /   \:\~~\~~    ")
    print("   \:\/:/  /      |:|\/__/     \:\/:/  /       |::/  /     \:\  \     ")
    print("    \::/  /       |:|  |        \::/  /        /:/  /       \:\__\    ")
    print("     \/__/         \|__|         \/__/         \/__/         \/__/    ")# titre gronz
    print ()
    print ()
    print ("Voulez vous crypter ou décrypter ?")
    print ("Répondre par <crypter> ou <decrypter> ou le programme sera annulé")
    crypt_or_decrypt = input ("->")
    print ()# menu de départ
    if crypt_or_decrypt == "crypter":
        print ("Que voulez-vous crypter ? :")
        message = input("->")
        print ()
        print ("donnez un mot de passe / clé de chiffrement que vous devrez retenir :")
        mdp = input("->")
        print ()
        encrypted_message = cesarcrypt(message) # cesar
        print("Message :", message) # message originel
        #print("1er message crypté :", encrypted_message) # message crypter avec cesar
        #print ()
        rep = crypt(encrypted_message, mdp)
        print("votre message crypté est : ", rep)
        #print("2ème message crypté",rep)
        pyperclip.copy(str(rep))
        print("Et il a été mis dans votre presse papier.")
        print()
        print("voulez vous crypter dans une image ?(oui ou non)")
        crypt_in_image=input("->")
        if crypt_in_image=="oui":

            print ()
            print("quel nom voulez vous donner à votre image cryptée ? (n'oubliez pas le .png à la fin)") #phrase à changer
            nom_de_limage = input("->")
            print()
            print("quelle image voulez vous crypter ?")
            image_de_ref=input ("->")
            print()
            hide(str(rep), image_de_ref)

        else:
            print()
            print ("annulation de la mise en image")

        print()
        print ("voulez-vous quitter gronz ou recommencer ? (répondre <exit> ou <reste>)")
        boucle = input("->")# cryptage

    elif crypt_or_decrypt == "decrypter":
        print ("voulez vous décrypter une [image] ou un [message]")
        imgormess=input("->")
        print()
        if imgormess == "image":
            print ("quel est le nom de votre image ? (avec l'extention precisée à la fin) :")
            nom_de_limage2 =""
            nom_de_limage2 = input("->")
            decryptimage = discover(nom_de_limage2)

            valeur_ascii_du_text_final_str =  decryptimage #input("valeur ascii du texte à décrypter : ")
            valeur_ascii_du_text_final = eval(valeur_ascii_du_text_final_str)
            print ("key :")
            key = input("->")
            print ()

            texte_decrypte = decrypt(valeur_ascii_du_text_final, key)
            # pyperclip.copy(texte_decrypte)
            decrypted_message = cesardecrypt(texte_decrypte)
            print("Message décrypté :", decrypted_message)
            print()


            print("voulez-vous quitter gronz ou recommencer ? (répondre <exit> ou <reste>)")
            boucle = input("->")# décryptage

        elif imgormess == "message":
            print ("veuillez rentrer le texte crypté")
            valeur_ascii_du_text_final_str=input("->")
            valeur_ascii_du_text_final = eval(valeur_ascii_du_text_final_str)
            print("key :")
            key = input("->")
            print()

            texte_decrypte = decrypt(valeur_ascii_du_text_final, key)
            # pyperclip.copy(texte_decrypte)
            decrypted_message = cesardecrypt(texte_decrypte)
            print("Message décrypté :", decrypted_message)
            print()
            print("voulez-vous quitter gronz ou recommencer ? (répondre <exit> ou <reste>)")
            boucle = input("->")  # décryptage

        elif crypt_or_decrypt.lower() == "jsp" or crypt_or_decrypt.lower() == "je ne sais pas" or crypt_or_decrypt.lower() == "je sais pas":
            print("mince")
            print("dommage")
            print("...")
            print("a+")
            boucle = "exit"  # rep jsp

        else:
            print("réponse mal orthographiée")
            print("fin du programme")
            exit(0)  # mauvaise orthographe

    elif crypt_or_decrypt.lower() == "jsp" or crypt_or_decrypt.lower() == "je ne sais pas" or crypt_or_decrypt.lower() == "je sais pas":
        print ("mince")
        print ("dommage")
        print("...")
        print ("a+")
        boucle = "exit"# rep jsp

    else :
        print("réponse mal orthographiée")
        print ("fin du programme")
        exit (0)# mauvaise orthographe
