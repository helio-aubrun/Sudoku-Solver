import json
import time

class ConvertRaw:
    def __init__(self,file_path):

        brute = self.read_file_content (file_path)

        #get rid of the spaces
        self.lines = [line.replace(" ", "") for line in brute.split('\n')]

    #read the content of an .txt file containing the sudoku game
    def read_file_content(self,file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    #return the converted game as a matrix
    def get_converted(self):
        mat = []
        for line in self.lines:
            x = []
            for i in range (len (line)):
                x.append(line[i])
            mat.append(x)

        final = []
        for line in mat:
            final.append (line)

        for i in range (len (final)):
            print (final [i])

        return final

    #save the converted game in a .json with the given name
    def save_to_json(self, filename):
        final = self.get_converted()
        with open(filename  + ".json", 'w') as json_file:
            json.dump(final, json_file)

# Example usage
if __name__ == "__main__":
    start_time = time.time()
    converter = ConvertRaw("sudoku.txt")
    if not converter.get_converted() == None :
        print("Temps d'exécution:", time.time() - start_time, "secondes")