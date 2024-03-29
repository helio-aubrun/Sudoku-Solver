import pygame
import sys
import time
import random
from py.BruteForce import BruteForce
from py.BackTracking import BackTracking

class SudokuSolver:
    def __init__(self):
        # Defining colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.GREEN = (0, 128, 0)
        self.RED = (255, 0, 0)
        self.input_value = None

        # Initializing Pygame
        pygame.init()

        # Setting screen size
        self.WIDTH, self.HEIGHT = 540, 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sudoku Solver")

        # Initializing variables
        self.sudoku_grid = None
        self.selected_button = None
        self.solving_method = None
        self.solve_time = None

    def load_sudoku(self, filename):
        # Load a Sudoku grid from a text file
        sudoku_grid = []
        with open(filename, 'r') as file:
            for line in file:
                row = [int(num) if num != '_' else 0 for num in line.strip()]
                sudoku_grid.append(row)
        return sudoku_grid

    def draw_sudoku(self, grid, missing_numbers=None):
        # Draw the Sudoku grid on the screen
        cell_size = self.WIDTH // 9
        for i in range(9):
            for j in range(9):
                cell_value = grid[i][j]
                color = self.BLACK
                if missing_numbers and (i, j) in missing_numbers:
                    color = self.RED
                # Draw the digit value if it's not zero
                if cell_value != 0:
                    font = pygame.font.Font(None, 36)
                    text_surface = font.render(str(cell_value), True, color)
                    text_rect = text_surface.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                    self.SCREEN.blit(text_surface, text_rect)
                # Draw the grid
                pygame.draw.rect(self.SCREEN, self.BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    def draw_buttons(self):
        # Draw buttons to select Sudoku grids
        font = pygame.font.Font(None, 36)
        button_labels = ["Sudoku 1", "Sudoku 2", "Sudoku 3", "Sudoku 4", "Sudoku 5", "Brute Force"]
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

    def solve_with_brute_force(self, grid, empty):
        # Solve the Sudoku grid using the brute force method
        start_time = time.time()
        solver = BruteForce(grid)
        solver.add_empty(empty)
        if solver.resolve_sudoku_brutforce():
            end_time = time.time()
            return end_time - start_time, True
        else:
            return 0, False

    def solve_with_recursion(self, grid):
        # Solve the Sudoku grid using the recursion method
        start_time = time.time()
        solver = BackTracking(grid)
        if solver.solve_sudoku():
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
        # Run the main program
        start_program_time = time.time()  # Record program start time
        running = True
        missing_numbers = None
        while running:
            self.SCREEN.fill(self.WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        self.input_value = event.key - pygame.K_0 # Convert key to digit
                        print(self.input_value)
                    elif event.key == pygame.K_RETURN and selected_file == "txt/resolved_matrix1.txt":
                        self.solving_method = self.solve_with_brute_force
                        # Process input here if needed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = event.pos
                        if self.sudoku_grid is None:
                            button_rects = self.draw_buttons()
                            for i, rect in enumerate(button_rects):
                                if rect.collidepoint(event.pos):
                                    self.selected_button = i
                                    if i ==5 :
                                        selected_file = f"txt/resolved_matrix1.txt"
                                        self.sudoku_grid = self.load_sudoku(selected_file)
                                        break
                                    else :
                                        selected_file = f"txt/sudoku{i+1}.txt"
                                        self.sudoku_grid = self.load_sudoku(selected_file)
                                        break
                            self.solving_method = None
                        elif selected_file == "txt/resolved_matrix1.txt":
                            if 548 < y < 592:
                                if 237 < x < 333:
                                    self.sudoku_grid = None
                                    self.selected_button = None
                                    self.solving_method = None
                                    self.solve_time = None
                                    missing_numbers = None
                        elif 548 < y < 592:
                            if 19 < x < 157:
                                self.solving_method = self.solve_with_recursion
                            elif 237 < x < 333:
                                self.sudoku_grid = None
                                self.selected_button = None
                                self.solving_method = None
                                self.solve_time = None
                                missing_numbers = None
                        if event.button == 1:
                            cell_size = self.WIDTH // 9

            if self.sudoku_grid:
                if self.solving_method and self.solve_time is None:
                    missing_numbers = self.compare_grids(self.sudoku_grid)
                    start_solve_time = time.time()
                    if selected_file == "txt/resolved_matrix1.txt":
                        success, solved_grid = self.solving_method(self.sudoku_grid,self.input_value)
                    else :
                        success, solved_grid = self.solving_method(self.sudoku_grid)
                    end_solve_time = time.time()
                    self.solve_time = end_solve_time - start_solve_time
                    if success:
                        self.draw_sudoku(self.sudoku_grid, missing_numbers)
                    else:
                        print("Resolution failed.")
                if missing_numbers:
                    self.draw_sudoku(self.sudoku_grid, missing_numbers)
                else:
                    self.draw_sudoku(self.sudoku_grid)
                font = pygame.font.Font(None, 36)
                font_time = pygame.font.Font(None, 18)
                text_surface1 = font.render("BackTracking", True, self.BLACK)
                text_surface2 = font.render("BruteForce", True, self.BLACK)
                text_surface3 = font.render("Back", True, self.BLACK)
                text_rect1 = text_surface1.get_rect(center=(self.WIDTH // 4 - 50, self.HEIGHT - 30))
                text_rect2 = text_surface2.get_rect(center=(self.WIDTH // 4 - 50, self.HEIGHT - 30))
                text_rect3 = text_surface3.get_rect(center=(self.WIDTH // 1.9, self.HEIGHT - 30))
                pygame.draw.rect(self.SCREEN, self.RED, (text_rect3.x - 10, text_rect3.y - 10, text_rect3.width + 20, text_rect3.height + 20))
                if selected_file == "txt/resolved_matrix1.txt":
                    if self.input_value is not None:
                        text_surface = pygame.font.Font(None, 36).render(str(self.input_value), True, self.BLACK)
                        text_rect = text_surface.get_rect(center=(self.WIDTH // 4 - 50, self.HEIGHT - 30))
                        self.SCREEN.blit(text_surface, text_rect)
                    pygame.draw.rect(self.SCREEN, self.BLACK, (text_rect2.x - 10, text_rect2.y - 10, text_rect2.width + 20, text_rect2.height + 20), 2)
                else :
                    self.SCREEN.blit(text_surface1, text_rect1)
                self.SCREEN.blit(text_surface3, text_rect3)
            
                if self.solve_time is not None:
                    solve_time_text = f"Solving Time: {self.solve_time:.4f} s"
                    solve_time_surface = font_time.render(solve_time_text, True, self.BLACK)
                    solve_time_rect = solve_time_surface.get_rect(center=(self.WIDTH // 1.9 + 160, self.HEIGHT - 28))
                    self.SCREEN.blit(solve_time_surface, solve_time_rect) 

            else:
                self.draw_buttons()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    solver = SudokuSolver()
    solver.run()