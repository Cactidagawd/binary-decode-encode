import os
import ctypes
clear = lambda: os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("Binary decode/encoder!")
clear()
while True:
    print("        ██████████                ████████")       
    print("       ██░░░░░░░░░░██            ██░░░░░░░░██")      
    print("     ██░░░░░░░░░░░░░░██        ██░░░░░░░░░░░░██")    
    print("   ██░░████░░░░░░░░░░██████████████░░░░░░░░██░░██")   
    print("  ██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░██")
    print("   ██      ██░░      ░░░░░░░░░░░░░░░░░░░░██  ░░██")
    print("   ██░░  ░░            ░░░░░░░░░░░░░░░░░░░░██░░██")
    print("     ████                  ░░░░░░░░░░░░░░░░████")
    print("       ██      ██████            ░░░░██████  ██")
    print("       ██    ████    ██            ██    ██████")
    print("       ██    ████    ██            ██    ████░░██")
    print("     ██      ██████████            ██████████  ██")
    print("   ████████░░  ██████        ░░██    ██████  ░░██████")
    print("     ██░░                                      ██")
    print("    ██████░░                              ░░██████")
    print("   ████                ██    ██    ██        ░░██")
    print("     ██░░░░              ████  ████          ██")
    print("     ██░░░░░░░░                            ████")
    print("   ████░░░░        ██                ██    ░░██") 
    print(" ██░░██░░        ░░  ██            ██        ██") 
    print("   ████        ██░░░░██            ██    ██  ██") 
    print("     ████        ████                ████  ██")     
    print("       ████░░██    ░░░░░░░░            ░░██")      
    print("       ██░░░░░░██████████████████████░░░░░░██")    
    print("         ██████                      ██████")  
    type = input('\n      1. Decode      2. Encode\n\nType:')

    if (type == "1"):
        binaryvalueinput = input('\nBinary:')
        a_binary_string = binaryvalueinput
        binary_values = a_binary_string.split()
        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
        print("\nAnswer: " + ascii_string)
        input("\nPress enter to continue ...")
        clear()
    elif (type == "2"):
        textbeforeconvert = input('\nText:')
        test_value = textbeforeconvert 
        result = ''.join(format(ord(i), '08b') for i in test_value)
        print("\nAnswer: " + str(result))
        input("\nPress enter to continue ...")
        clear()
    else:
        print("\nYou have to enter an input!")
        input("\nPress enter to continue ...")
        clear()
