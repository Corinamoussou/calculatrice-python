
#programme calculatrice

operateur_count = {"+": 0, "-": 0, "*": 0, "/": 0, "**": 0, "%": 0}
calculs = []
result = 0

while True:
    a = input("entrer le premier nombre ou 'exit' pour quitter :")
    if a.lower() == "exit":
        print("opération terminé")
        break
    b = input("entrer le deuxième nombre :")
    operateur = input("entrer un operateur entre (+, -, *, **, /, %) :")
    try:
        a, b = float(a), float (b)
        if operateur in operateur_count : 
            if operateur == "/" or "%":
                if b == 0 :
                   print(f"erreur : {operateur} par Zero impossible")
                   continue
                result = a/b                       
            elif operateur == "+":
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

    
