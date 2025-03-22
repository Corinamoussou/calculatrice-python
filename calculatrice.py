
#programme calculatrice

# Dictionnaire pour compter le nombre d'opérations
operateur_count = {"+": 0, "-": 0, "*": 0, "/": 0, "**": 0, "%": 0}
# Liste pour stocker les calculs
calculs = []
result = 0
# tant que c'est vrai terminé l'opération
while True:
    a = input("entrer la valeur de a :")
    if a.lower() == "exit":
        print("opération terminé")
        break
    b = input("entrer la valeur de b :")
    if a.lower() == "exit":
        print("opération terminé")
        break
    operateur = input("entrer un operateur entre (+, -, *, **, /, %) :")
    if operateur.lower == "exit":
        print("opération terminé")
        break
    try:

#convertion des entrés en decimal
        a, b = float(a), float (b)
#Si l'operateur inclut dans la liste d'operateur est "/" ou "%" et b=0, renvoyer une erreur.
        if operateur in operateur_count : 
            if operateur == "/" and b == 0:
                raise ZeroDivisionError("Erreur : division par zero impossoble")
            if operateur == "%" and b == 0:
                raise ZeroDivisionError("Erreur : division par zero impossoble")   
                
#exécuter le calcule         
            if operateur == "+":
                result = a + b
            elif operateur == "-":
                result = a - b
            elif operateur == "*":
                result = a * b
            elif operateur == "**":
                result = a ** b
            elif operateur == "/":
                result = a / b
            elif operateur == "%":
                result = a % b
# Stockage du calcul
            calculs.append(f"{a} {operateur} {b} = {result}")
            operateur_count[operateur] += 1 
#affichege des opérations, l'historique et le nombre de fois 
            print(f"le resultat de {a} {operateur} {b} est de : {result}")
            print("nombre d'opérations éffectué : ",operateur_count)
            print("l'historique de calcul ", calculs)
        else:
            print("Erreur : entrez un opérateur valide parmi (+, -, *, /, **, %).")
            
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
    except ZeroDivisionError as e:
        print(e)    
    
    
