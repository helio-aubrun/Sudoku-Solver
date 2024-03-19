import pygame
import sys

class Main:


    def __init__(self, file_sudoku):

        self.file_sudoku = file_sudoku
        self.sudoku = self.read_sudoku(file_sudoku)
        pygame.init()
        self.screen = pygame.display.set_mode((450, 500))
        pygame.display.set_caption("Sudoku Solver")
        self.font = pygame.font.Font(None, 26)


    def read_sudoku(self, file_sudoku):
        #replace the _ into 0 for empty case
        with open(file_sudoku, 'r') as file:
            sudoku = []
            for line in file:
                sudoku.append([0 if number == '_' else int(number) for number in line.strip()])
        return sudoku


    def draw_sudoku(self):

        height_case = 50

        for i in range(9):

            for j in range(9):

                color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, pygame.Rect(j * height_case, i * height_case, height_case, height_case))

                if self.sudoku[i][j] != 0:
                    #draw number in case
                    police = pygame.font.Font(None, 36)
                    text = police.render(str(self.sudoku[i][j]), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(j * height_case + height_case // 2, i * height_case + height_case // 2))
                    self.screen.blit(text, text_rect)

        for i in range(10):
            #draw line between case
            pygame.draw.line(self.screen, (128, 128, 128), (i * height_case, 0), (i * height_case, 450), 2)
            pygame.draw.line(self.screen, (128, 128, 128), (0, i * height_case), (450, i * height_case), 2)

        for i in range(3):
            #draw line between square
            pygame.draw.line(self.screen, (0, 0, 0), (i * 3 * height_case, 0), (i * 3 * height_case, 450), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 3 * height_case), (450, i * 3 * height_case), 2)


    def draw_boutons(self):

        bouton_force_brute = pygame.Rect(5, 460, 180, 30)
        bouton_backtracking = pygame.Rect(250, 460, 190, 30)
        pygame.draw.rect(self.screen, (200, 200, 200), bouton_force_brute)
        pygame.draw.rect(self.screen, (200, 200, 200), bouton_backtracking)
        texte_force_brute = self.font.render("Méthode force brute", True, (0, 0, 0))
        texte_backtracking = self.font.render("Méthode backtracking", True, (0, 0, 0))
        self.screen.blit(texte_force_brute, (10, 465))
        self.screen.blit(texte_backtracking, (255, 465))


    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    #buttons
                    if 461 <= y <= 490 :
                        if 5 <= x <= 186:
                            print ("force brute utilisé")
                        elif 250 <= x <= 440:
                            print ("backtracking utilisé")

            self.screen.fill((255, 255, 255))
            self.draw_sudoku()
            self.draw_boutons()
            pygame.display.flip()

if __name__ == "__main__":
    solver = Main('sudoku.txt')
    solver.run()