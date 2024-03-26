import itertools
import time
from random import randint

class BruteForce:
    def __init__(self, grid):
        self.grid = grid

    #display the grid with a user friendly format
    def disolay_grid(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.grid[i][j])
                else:
                    print(str(self.grid[i][j]) + " ", end="")

    #test if the given number is valid using the given coordonat
    def valid_number(self, ligne, colonne, chiffre):
        for i in range(9):
            if self.grid[ligne][i] == chiffre or self.grid[i][colonne] == chiffre or self.grid[(ligne // 3) * 3 + i // 3][(colonne // 3) * 3 + i % 3] == chiffre:
                return False
        return True

    #fill the soduko and test if its correct
    def resolve_sudoku_brutforce(self):
        cases_vides = [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]
        for combinaison in itertools.product(range(1, 10), repeat=len(cases_vides)):
            valide = True
            for (ligne, colonne), chiffre in zip(cases_vides, combinaison):
                if not self.valid_number(ligne, colonne, chiffre):
                    valide = False
                    break
            if valide:
                for (ligne, colonne), chiffre in zip(cases_vides, combinaison):
                    self.grid[ligne][colonne] = chiffre
                return True
        return False
    
    # !!!require a resolved sudoku!!! empty random location of the sudoku to creat differents games to test the brut force speed 
    def add_empty (self, nb_empty) :
        while nb_empty > 0 :
            random_x = randint (0, 8)
            random_y = randint (0, 8)
            if not self.grid [random_x][random_y] == 0 :
                self.grid [random_x][random_y] = 0
                nb_empty -= 1
            

if __name__ == "__main__":
    #fetching the sudoku from a given .txt file
    fichier_sudoku = input("Entrez le nom du fichier Sudoku : ")

    try:
        
        #transform the given sudoku into the required format
        with open(fichier_sudoku, "r") as file:

            my_matrix = [[int(num) if num != '_' else 0 for num in line.strip()] for line in file]

        
        solveur = BruteForce(my_matrix)
        solveur.add_empty (int (input ("donner le nombre de case a vider : \n")))
        print("grid de Sudoku à résoudre :")
        solveur.disolay_grid()
        print("\nRésolution en cours...\n")

        start_time = time.time()
        if solveur.resolve_sudoku_brutforce():
            print("Sudoku Résolu :")
            solveur.disolay_grid()
            print("Temps d'exécution:", time.time() - start_time, "secondes")
        else:
            print("Pas de solution possible.")
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")