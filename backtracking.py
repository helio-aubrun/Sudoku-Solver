from ConvertRaw import  ConvertRaw

class BackTracking :

    def __init__ (self, file_path) :
        self.mat = [
            ["_", "7", "2", "9", "_", "_", "_", "3", "_"], 
            ["_", "_", "1", "_", "_", "6", "_", "8", "_"], 
            ["_", "_", "_", "_", "4", "_", "_", "6", "_"], 
            ["9", "6", "_", "_", "_", "4", "1", "_", "8"], 
            ["_", "4", "8", "7", "_", "5", "_", "9", "6"], 
            ["_", "_", "5", "6", "_", "8", "_", "_", "3"], 
            ["_", "_", "_", "4", "_", "2", "_", "1", "_"], 
            ["8", "5", "_", "_", "6", "_", "3", "2", "7"], 
            ["1", "_", "_", "8", "5", "_", "_", "_", "_"]
            ]

    #display the game with an easely readable format
    def display_terminal (self):
        test = 0
        print ("----------------------")
        for colum in self.jeu_01 :
            for line in colum :
                if test < 8 :
                    if test == 2 or test == 5:
                        print (str (line) + " | " ,end='')
                    else :
                        print (str (line) + " " ,end='')
                    test += 1
                else :
                    print (line)
                    print ("----------------------")
                    test = 0

    #try to find an empty number and return its coordinate or return False if thes is none
    def find_empty (self) :
        for row in range (len (self.mat)) :
            for col in range (len (self.mat [row])) :
                if self.mat [row] [col] == "_" :
                    return (row, col)
        
        return False

    #verify the validity of the given number using its coordinate
    def is_valid(self, number, row, col):
        number = str (number)
        for nimber_row in self.mat[row] :
            if number == nimber_row[0] :
                return False
            
        for nimber_col in self.mat :
            if number == nimber_col[col][0] :
                return False
            
        for i in range(3):
            for j in range(3):
                if(self.mat[i + row][j + col] == number):
                    return True
        return False
        
        return True

    #solving the sudoku
    def solve (self) :
        

if __name__ == "__main__":
    sudoku = BackTracking()
