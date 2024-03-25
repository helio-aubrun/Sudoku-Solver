import pygame
import sys
import time
import random
from BruteForce import BruteForce
from RecursiveSolver import BackTracking

class SudokuSolver:
    def __init__(self):
        # Définition des couleurs
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.GREEN = (0, 128, 0)
        self.RED = (255, 0, 0)

        # Initialisation de Pygame
        pygame.init()

        # Définition de la taille de l'écran
        self.WIDTH, self.HEIGHT = 540, 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sudoku Solver")

        # Initialisation des variables
        self.sudoku_grid = None
        self.selected_button = None
        self.solving_method = None
        self.solve_time = None

    def load_sudoku(self, filename):
        # Charger une grid Sudoku à partir d'un fichier texte
        sudoku_grid = []
        with open(filename, 'r') as file:
            for line in file:
                row = [int(num) if num != '_' else 0 for num in line.strip()]
                sudoku_grid.append(row)
        return sudoku_grid

    def draw_sudoku(self, grid, missing_numbers=None):
        # Dessiner la grid Sudoku sur l'écran
        cell_size = self.WIDTH // 9
        for i in range(9):
            for j in range(9):
                cell_value = grid[i][j]
                color = self.BLACK
                if missing_numbers and (i, j) in missing_numbers:
                    color = self.RED
                # Dessiner la valeur du chiffre s'il est différent de zéro
                if cell_value != 0:
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(cell_value), True, color)
                    text_rect = text_surface.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                    self.SCREEN.blit(text_surface, text_rect)
                # Dessiner la grid
                pygame.draw.rect(self.SCREEN, self.BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    def draw_buttons(self):
        # Dessiner les boutons pour sélectionner les grids Sudoku
        font = pygame.font.Font(None, 36)
        button_labels = ["Sudoku 1", "Sudoku 2", "Sudoku 3", "Sudoku 4"]  # Ajout de "Sudoku 5"
        button_rects = []
        button_height = 60
        for i, label in enumerate(button_labels):
            text_surface = font.render(label, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 100 + i * (button_height + 20)))
            if self.selected_button == i:
                pygame.draw.rect(self.SCREEN, self.GREEN, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20))
            else:
                pygame.draw.rect(self.SCREEN, self.GRAY, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20))
            self.SCREEN.blit(text_surface, text_rect)
            button_rects.append(text_rect)
        return button_rects

    def solve_with_brute_force(self, grid):
        # Résoudre la grid Sudoku en utilisant la méthode de la force brute
        start_time = time.time()
        solver = BruteForce(grid)
        if solver.resolve_sudoku_brutforce():
            end_time = time.time()
            return end_time - start_time, True
        else:
            return 0, False

    def solve_with_recursion(self, grid):
        # Résoudre la grid Sudoku en utilisant la méthode de la récursion
        start_time = time.time()
        solver = BackTracking(grid)
        if solver.resoudre_sudoku():
            end_time = time.time()
            return end_time - start_time, True
        else:
            return 0, False

    def compare_grids(self, original_grid):
        missing_numbers = []
        for i in range(9):
            for j in range(9):
                if original_grid[i][j] == 0 :
                    missing_numbers.append((i, j))
        return missing_numbers

    def run(self):
        # Lancer le programme principal
        start_program_time = time.time()  # Enregistrer le temps de départ du programme
        running = True
        missing_numbers = None
        while running:
            self.SCREEN.fill(self.WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.sudoku_grid is None:
                            button_rects = self.draw_buttons()
                            for i, rect in enumerate(button_rects):
                                if rect.collidepoint(event.pos):
                                    self.selected_button = i
                                    selected_file = f"sudoku{i+1}.txt"
                                    self.sudoku_grid = self.load_sudoku(selected_file)
                                    break
                            self.solving_method = None
                        elif event.pos[0] > self.WIDTH // 4 - 100 and event.pos[0] < self.WIDTH // 4 and event.pos[1] > self.HEIGHT - 80 and event.pos[1] < self.HEIGHT - 30:
                            self.solving_method = self.solve_with_brute_force
                        elif event.pos[0] > 3 * self.WIDTH // 4 and event.pos[0] < 3 * self.WIDTH // 4 + 100 and event.pos[1] > self.HEIGHT - 80 and event.pos[1] < self.HEIGHT - 30:
                            self.solving_method = self.solve_with_recursion
                        elif event.pos[0] > self.WIDTH // 2 - 50 and event.pos[0] < self.WIDTH // 2 + 50 and event.pos[1] > self.HEIGHT - 30 and event.pos[1] < self.HEIGHT:
                            self.sudoku_grid = None
                            self.selected_button = None
                            self.solving_method = None
                            self.solve_time = None
                            missing_numbers = None
                        if event.button == 1:  # L'utilisateur clique avec le bouton gauche de la souris
                            cell_size = self.WIDTH // 9

            if self.sudoku_grid:
                if self.solving_method and self.solve_time is None:
                    missing_numbers = self.compare_grids(self.sudoku_grid)
                    start_solve_time = time.time()
                    success, solved_grid = self.solving_method(self.sudoku_grid)
                    end_solve_time = time.time()
                    self.solve_time = end_solve_time - start_solve_time
                    if success:
                        self.draw_sudoku(self.sudoku_grid, missing_numbers)
                    else:
                        print("La résolution a échoué.")
                if missing_numbers:
                    self.draw_sudoku(self.sudoku_grid, missing_numbers)
                else:
                    self.draw_sudoku(self.sudoku_grid)
                font = pygame.font.Font(None, 36)
                font_temps = pygame.font.Font(None, 18)
                text_surface1 = font.render("Brute Force", True, self.BLACK)
                text_surface2 = font.render("Recursion", True, self.BLACK)
                text_surface3 = font.render("Retour", True, self.BLACK)
                text_rect1 = text_surface1.get_rect(center=(self.WIDTH // 4 - 50, self.HEIGHT - 30))
                text_rect2 = text_surface2.get_rect(center=(3 * self.WIDTH // 4 + 50, self.HEIGHT - 30))
                text_rect3 = text_surface3.get_rect(center=(self.WIDTH // 1.9, self.HEIGHT - 30))
                pygame.draw.rect(self.SCREEN, self.RED, (text_rect3.x - 10, text_rect3.y - 10, text_rect3.width + 20, text_rect3.height + 20))
                self.SCREEN.blit(text_surface1, text_rect1)
                self.SCREEN.blit(text_surface2, text_rect2)
                self.SCREEN.blit(text_surface3, text_rect3)
            
                if self.solve_time is not None:
                    solve_time_text = f"Temps de résolution: {self.solve_time:.4f} secondes"
                    solve_time_surface = font_temps.render(solve_time_text, True, self.BLACK)
                    solve_time_rect = solve_time_surface.get_rect(center=(self.WIDTH // 4.7, self.HEIGHT - 8))
                    self.SCREEN.blit(solve_time_surface, solve_time_rect) 

            else:
                self.draw_buttons()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def get_input(self):
        # Obtenir l'entrée de l'utilisateur pour remplir une case vide
        input_value = None
        font = pygame.font.Font(None, 48)
        input_text = ""
        input_rect = pygame.Rect(self.WIDTH // 4, self.HEIGHT - 50, self.WIDTH // 2, 40)
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        input_text += chr(event.key)
                    elif event.key == pygame.K_RETURN:
                        if input_text.isdigit() and 1 <= int(input_text) <= 9:
                            input_value = int(input_text)
                            active = False
                            break
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]

            pygame.draw.rect(self.SCREEN, self.WHITE, input_rect)
            text_surface = font.render(input_text, True, self.BLACK)
            text_rect = text_surface.get_rect(midleft=input_rect.midleft)
            self.SCREEN.blit(text_surface, text_rect)
            pygame.display.flip()

        return input_value

if __name__ == "__main__":
    solver = SudokuSolver()
    solver.run()