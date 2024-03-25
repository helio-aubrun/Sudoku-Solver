import itertools
import time

class BruteForce:
    def __init__(self, grille):
        self.grille = grille

    def afficher_grille(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.grille[i][j])
                else:
                    print(str(self.grille[i][j]) + " ", end="")

    def est_coup_valide(self, ligne, colonne, chiffre):
        for i in range(9):
            if self.grille[ligne][i] == chiffre or self.grille[i][colonne] == chiffre or self.grille[(ligne // 3) * 3 + i // 3][(colonne // 3) * 3 + i % 3] == chiffre:
                return False
        return True

    def resoudre_sudoku_bruteforce(self):
        cases_vides = [(i, j) for i in range(9) for j in range(9) if self.grille[i][j] == 0]
        for combinaison in itertools.product(range(1, 10), repeat=len(cases_vides)):
            valide = True
            for (ligne, colonne), chiffre in zip(cases_vides, combinaison):
                if not self.est_coup_valide(ligne, colonne, chiffre):
                    valide = False
                    break
            if valide:
                for (ligne, colonne), chiffre in zip(cases_vides, combinaison):
                    self.grille[ligne][colonne] = chiffre
                return True
        return False

if __name__ == "__main__":
    fichier_sudoku = input("Entrez le nom du fichier Sudoku : ")

    try:
        with open(fichier_sudoku, "r") as file:
            ma_matrice = [[int(num) if num != '_' else 0 for num in line.strip()] for line in file]

        solveur = BruteForce(ma_matrice)
        print("Grille de Sudoku à résoudre :")
        solveur.afficher_grille()
        print("\nRésolution en cours...\n")

        start_time = time.time()
        if solveur.resoudre_sudoku_bruteforce():
            print("Sudoku Résolu :")
            solveur.afficher_grille()
            print("Temps d'exécution:", time.time() - start_time, "secondes")
        else:
            print("Pas de solution possible.")
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
