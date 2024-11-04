# rot13.py
# solution for rot13 exercise @ picoCTF
# clue: cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}


if __name__ == "__main__":
    clue_map = {}
    clue_map["c"] = "p"
    clue_map["v"] = "i"
    clue_map["p"] = "c"
    clue_map["b"] = "o"
    clue_map["P"] = "C"
    clue_map["G"] = "T"
    clue_map["S"] = "F"

    cipher_map = {}
    cipher_map["a"] = "n"
    cipher_map["b"] = "o"
    cipher_map["c"] = "p"
    cipher_map["d"] = "q"
    cipher_map["e"] = "r"
    cipher_map["f"] = "s"
    cipher_map["g"] = "t"
    cipher_map["h"] = "u"
    cipher_map["i"] = "v"
    cipher_map["j"] = "w"
    cipher_map["k"] = "x"    
    cipher_map["l"] = "y"
    cipher_map["m"] = "z"
    cipher_map["n"] = "a"
    cipher_map["o"] = "b"
    cipher_map["p"] = "c"
    cipher_map["q"] = "d"
    cipher_map["r"] = "e"
    cipher_map["s"] = "f"
    cipher_map["t"] = "g"
    cipher_map["u"] = "h"
    cipher_map["v"] = "i"
    cipher_map["w"] = "j"
    cipher_map["x"] = "k"
    cipher_map["y"] = "l"
    cipher_map["z"] = "m"
    cipher_map["A"] = "N"
    cipher_map["B"] = "O"
    cipher_map["C"] = "P"
    cipher_map["D"] = "Q"
    cipher_map["E"] = "R"
    cipher_map["F"] = "S"
    cipher_map["G"] = "T"
    cipher_map["H"] = "U"
    cipher_map["I"] = "V"
    cipher_map["J"] = "W"
    cipher_map["K"] = "X"    
    cipher_map["L"] = "Y"
    cipher_map["M"] = "Z"
    cipher_map["N"] = "A"
    cipher_map["O"] = "B"
    cipher_map["P"] = "C"
    cipher_map["Q"] = "D"
    cipher_map["R"] = "E"
    cipher_map["S"] = "F"
    cipher_map["T"] = "G"
    cipher_map["U"] = "H"
    cipher_map["V"] = "I"
    cipher_map["W"] = "J"
    cipher_map["X"] = "K"
    cipher_map["Y"] = "L"
    cipher_map["Z"] = "M"

    clue = input("Enter clue string: ")

    cleartext = ""
    for ch in clue:
        if ch in cipher_map:
            cleartext += cipher_map[ch]
        else:
            cleartext += ch

    print(cleartext)
    
