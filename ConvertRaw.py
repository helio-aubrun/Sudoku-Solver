import json

class ConvertRaw:
    def __init__(self):
        brute = """_729___3_
                __1__6_8_
                ____4__6_
                96___41_8
                _487_5_96
                __56_8__3
                ___4_2_1_
                85__6_327
                1__85____"""

        self.lignes = [line.replace(" ", "") for line in brute.split('\n')]
    def get_converted(self):
        mat = []
        test = 0
        for ligne in self.lignes:
            x = []
            while test < 9:
                x.append(ligne[test])
                test += 1
            mat.append(x)
            test = 0

        final = ""
        test = 0
        for ligne in mat:
            if test == 0:
                final += ("[" + str(ligne) + ',')
                test += 1
            elif test < 8:
                final += (str(ligne) + ',')
                test += 1
            else:
                final += (str(ligne) + ']')

        return final

    def save_to_json(self, filename):
        final = self.get_converted()
        with open(filename, 'w') as json_file:
            json.dump(final, json_file)

# Example usage
if __name__ == "__main__":
    converter = ConvertRaw()
    converter.save_to_json('final.json')