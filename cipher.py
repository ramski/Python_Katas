import re

def polybius(text):
    cryp = {"A":11, "B":12, "C":13, "D":14, "E":15,
            "F":21, "G":22, "H":23, "I":24, "J":24, "K":25,
            "L":31, "M":32, "N":33, "O":34, "P":35,
            "Q":41, "R":42, "S":43, "T":44, "U":45,
            "V":51, "W":52, "X":53, "Y":54, "Z":55, " ": " "}

    encriptado = []

    for i in text:
        for key in cryp.keys():
            if key == i:
                encriptado.append(cryp[key])

    my_lst_str = ''.join([str(mli) for mli in encriptado])
    
    return my_lst_str