onLoop = True
while onLoop:
    string = str(input("Enter a string of any character to convert: "))

    toList = list(string)

    toAscii = [ord(char) for char in toList]
    toBinary = [bin(ord(char)) for char in toList]
    toHex = [hex(ord(char)) for char in toList]
    toOctal = [oct(ord(char)) for char in toList]
    print('=======================================================')
    print(f"ASCII: {toAscii}")
    print('=======================================================')
    print(f"Binary: {toBinary}")
    print('=======================================================')
    print(f"Hexadecimal: {toHex}")
    print('=======================================================')
    print(f"Octal: {toOctal}")
    print('=======================================================')

    onLoop = input('Would you care to convert another string? (Y|N): ')
    while True:
        match onLoop:
            case 'Y' | 'y':
                break
            case 'N' | 'n':
                onLoop = False
                print('=======================================================')
                print('\tThank you for using this program!')
                break
            case _:
                onLoop = input('Invalid input. Please choose between between (Y|N): ')
    print('=======================================================')