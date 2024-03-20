import time

class BruteForce:
    def __init__(self, grid):
        self.grid = grid


    def draw_terminal(self):
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

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def valid_move(self, line, column, number):
        for i in range(9):
            if self.grid[line][i] == number or self.grid[i][column] == number or self.grid[(line // 3) * 3 + i // 3][(column // 3) * 3 + i % 3] == number:
                return False
        return True

    def resolve(self):
        empty_case = self.find_empty()
        if not empty_case:
            return True

        line, column = empty_case

        for number in range(1, 10):
            if self.valid_move(line, column, number):
                self.grid[line][column] = number

                if self.resolve():
                    return True

                self.grid[line][column] = 0

        return False


if __name__ == "__main__":
    sudoku_file = input("Entrez le nom du fichier Sudoku : ")

    try:
        with open(sudoku_file, "r") as file:
            matrix = [[int(num) if num != '_' else 0 for num in line.strip()] for line in file]

        solveur = BruteForce(matrix)
        print("grid de Sudoku à résoudre :")
        solveur.draw_terminal()
        print("\nRésolution en cours...\n")

        start_time = time.time()
        if solveur.resolve():
            print("Sudoku Résolu :")
            solveur.draw_terminal()
            print("Temps d'exécution:", time.time() - start_time, "secondes")
        else:
            print("Pas de solution possible.")
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
