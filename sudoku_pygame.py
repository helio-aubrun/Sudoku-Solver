import pygame
import sys
import time
from BruteForce import BruteForce
"""from RecursiveSolver import Recursivesolver"""

class SudokuSolver:
    def __init__(self):

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.GREEN = (0, 128, 0)
        self.RED = (255, 0, 0)


        pygame.init()

        self.WIDTH, self.HEIGHT = 540, 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sudoku Solver")

        self.sudoku_grid = None
        self.selected_button = None
        self.solving_method = None
        self.solve_time = None

    def load_sudoku(self, filename):
        sudoku_grid = []
        with open(filename, 'r') as file:
            for line in file:
                row = [int(num) if num != '_' else 0 for num in line.strip()]
                sudoku_grid.append(row)
        return sudoku_grid

    def draw_sudoku(self, grid):
        cell_size = self.WIDTH // 9
        for i in range(9):
            for j in range(9):
                cell_value = grid[i][j]
                if cell_value != 0:
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(cell_value), True, self.BLACK)
                    text_rect = text_surface.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                    self.SCREEN.blit(text_surface, text_rect)

    def draw_buttons(self):
        font = pygame.font.Font(None, 36)
        button_labels = ["Sudoku 1", "Sudoku 2", "Sudoku 3", "Sudoku 4"]
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
        start_time = time.time()
        solver = BruteForce(grid)
        if solver.resolve():
            return time.time() - start_time, True
        else:
            return 0, False

    """def solve_with_recursion(self, grid):
        start_time = time.time()
        solver = Recursivesolver(grid)
        if solver.solve():
            return time.time() - start_time, True
        else:
            return 0, False"""

    def run(self):
        running = True
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
                        elif event.pos[0] > self.WIDTH // 4 - 100 and event.pos[0] < self.WIDTH // 4 and event.pos[1] > self.HEIGHT - 80 and event.pos[1] < self.HEIGHT - 40:
                            self.solving_method = self.solve_with_brute_force
                        elif event.pos[0] > 3 * self.WIDTH // 4 and event.pos[0] < 3 * self.WIDTH // 4 + 100 and event.pos[1] > self.HEIGHT - 80 and event.pos[1] < self.HEIGHT - 40:
                            self.solving_method = self.solve_with_recursion
                        elif event.pos[0] > self.WIDTH // 2 - 50 and event.pos[0] < self.WIDTH // 2 + 50 and event.pos[1] > self.HEIGHT - 40 and event.pos[1] < self.HEIGHT:
                            self.sudoku_grid = None
                            self.selected_button = None
                            self.solving_method = None

            if self.sudoku_grid:
                if self.solving_method:
                    self.solve_time, _ = self.solving_method(self.sudoku_grid)
                self.draw_sudoku(self.sudoku_grid)
                font = pygame.font.Font(None, 36)
                font_temps= pygame.font.Font(None, 18)
                text_surface1 = font.render("Brute Force", True, self.BLACK)
                text_surface2 = font.render("Recursion", True, self.BLACK)
                text_surface3 = font.render("Retour", True, self.BLACK)
                text_rect1 = text_surface1.get_rect(center=(self.WIDTH // 4 - 50, self.HEIGHT - 60))
                text_rect2 = text_surface2.get_rect(center=(3 * self.WIDTH // 4 + 50, self.HEIGHT - 60))
                text_rect3 = text_surface3.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 20))
                pygame.draw.rect(self.SCREEN, self.RED, (text_rect3.x - 10, text_rect3.y - 10, text_rect3.width + 20, text_rect3.height + 20))
                self.SCREEN.blit(text_surface1, text_rect1)
                self.SCREEN.blit(text_surface2, text_rect2)
                self.SCREEN.blit(text_surface3, text_rect3)
               
                if self.solve_time is not None:
                    solve_time_text = f"Temps de résolution: {self.solve_time:.2f} secondes"
                    solve_time_surface = font_temps.render(solve_time_text, True, self.BLACK)
                    solve_time_rect = solve_time_surface.get_rect(center=(self.WIDTH // 4.7, self.HEIGHT - 8))
                    self.SCREEN.blit(solve_time_surface, solve_time_rect) 

            else:
                self.draw_buttons()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    solver = SudokuSolver()
    solver.run()
