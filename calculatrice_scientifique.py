import math

def afficher_menu():
    print("\n--- Calculatrice Scientifique ---")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine carrée")
    print("7. Logarithme")
    print("8. Sinus")
    print("9. Cosinus")
    print("10. Tangente")
    print("11. Quitter")

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def puissance(a, b):
    return a ** b

def racine_carre(a):
    if a < 0:
        return "Erreur : racine carrée d'un nombre négatif"
    return math.sqrt(a)

def logarithme(a):
    if a <= 0:
        return "Erreur : le logarithme n'est défini que pour des nombres positifs"
    return math.log(a)

def sinus(a):
    return math.sin(math.radians(a))

def cosinus(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def main():
    while True:
        afficher_menu()
        choix = input("\nChoisissez une option (1-11) : ")

        if choix == "11":
            print("Au revoir !")
            break

        if choix in ["1", "2", "3", "4", "5"]:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le second nombre : "))

            if choix == "1":
                print("Résultat :", addition(a, b))
            elif choix == "2":
                print("Résultat :", soustraction(a, b))
            elif choix == "3":
                print("Résultat :", multiplication(a, b))
            elif choix == "4":
                print("Résultat :", division(a, b))
            elif choix == "5":
                print("Résultat :", puissance(a, b))

        elif choix in ["6", "7", "8", "9", "10"]:
            a = float(input("Entrez un nombre : "))

            if choix == "6":
                print("Résultat :", racine_carre(a))
            elif choix == "7":
                print("Résultat :", logarithme(a))
            elif choix == "8":
                print("Résultat :", sinus(a))
            elif choix == "9":
                print("Résultat :", cosinus(a))
            elif choix == "10":
                print("Résultat :", tangente(a))

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()