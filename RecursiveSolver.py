import time

class BackTracking:
    def __init__(self, grid):
        self.grid = grid

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

    def trouver_case_vide(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def valid_number(self, ligne, colonne, chiffre):
        for i in range(9):
            if self.grid[ligne][i] == chiffre or self.grid[i][colonne] == chiffre or self.grid[(ligne // 3) * 3 + i // 3][(colonne // 3) * 3 + i % 3] == chiffre:
                return False
        return True

    def resoudre_sudoku(self):
        case_vide = self.trouver_case_vide()
        if not case_vide:
            return True

        ligne, colonne = case_vide

        for chiffre in range(1, 10):
            if self.valid_number(ligne, colonne, chiffre):
                self.grid[ligne][colonne] = chiffre

                if self.resoudre_sudoku():
                    return True

                self.grid[ligne][colonne] = 0

        return False


if __name__ == "__main__":
    fichier_sudoku = input("Entrez le nom du fichier Sudoku : ")

    try:
        with open(fichier_sudoku, "r") as file:
            my_matrix = [[int(num) if num != '_' else 0 for num in line.strip()] for line in file]

        solveur = BackTracking(my_matrix)
        print("grid de Sudoku à résoudre :")
        solveur.disolay_grid()
        print("\nRésolution en cours...\n")

        start_time = time.time()
        if solveur.resoudre_sudoku():
            print("Sudoku Résolu :")
            solveur.disolay_grid()
            print("Temps d'exécution:", time.time() - start_time, "secondes")
        else:
            print("Pas de solution possible.")
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
