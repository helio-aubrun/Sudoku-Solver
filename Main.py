import pygame
import sys

class Main:


    def __init__(self, fichier):

        self.fichier = fichier
        self.sudoku = self.read_sudoku(fichier)
        pygame.init()
        self.fenetre = pygame.display.set_mode((450, 500))
        pygame.display.set_caption("Sudoku Solver")
        self.font = pygame.font.Font(None, 26)


    def read_sudoku(self, fichier):
        #replace the _ into 0 for empty case
        with open(fichier, 'r') as file:
            sudoku = []
            for line in file:
                sudoku.append([0 if chiffre == '_' else int(chiffre) for chiffre in line.strip()])
        return sudoku


    def draw_sudoku(self):

        taille_case = 50

        for i in range(9):

            for j in range(9):

                color = (255, 255, 255)
                pygame.draw.rect(self.fenetre, color, pygame.Rect(j * taille_case, i * taille_case, taille_case, taille_case))

                if self.sudoku[i][j] != 0:
                    #draw number in case
                    police = pygame.font.Font(None, 36)
                    texte = police.render(str(self.sudoku[i][j]), True, (0, 0, 0))
                    texte_rect = texte.get_rect(center=(j * taille_case + taille_case // 2, i * taille_case + taille_case // 2))
                    self.fenetre.blit(texte, texte_rect)

        for i in range(10):
            #draw line between case
            pygame.draw.line(self.fenetre, (128, 128, 128), (i * taille_case, 0), (i * taille_case, 450), 2)
            pygame.draw.line(self.fenetre, (128, 128, 128), (0, i * taille_case), (450, i * taille_case), 2)

        for i in range(3):
            #draw line between square
            pygame.draw.line(self.fenetre, (0, 0, 0), (i * 3 * taille_case, 0), (i * 3 * taille_case, 450), 2)
            pygame.draw.line(self.fenetre, (0, 0, 0), (0, i * 3 * taille_case), (450, i * 3 * taille_case), 2)


    def draw_boutons(self):

        bouton_force_brute = pygame.Rect(5, 460, 180, 30)
        bouton_backtracking = pygame.Rect(250, 460, 190, 30)
        pygame.draw.rect(self.fenetre, (200, 200, 200), bouton_force_brute)
        pygame.draw.rect(self.fenetre, (200, 200, 200), bouton_backtracking)
        texte_force_brute = self.font.render("Méthode force brute", True, (0, 0, 0))
        texte_backtracking = self.font.render("Méthode backtracking", True, (0, 0, 0))
        self.fenetre.blit(texte_force_brute, (10, 465))
        self.fenetre.blit(texte_backtracking, (255, 465))


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

            self.fenetre.fill((255, 255, 255))
            self.draw_sudoku()
            self.draw_boutons()
            pygame.display.flip()

if __name__ == "__main__":
    solver = Main('sudoku.txt')
    solver.run()