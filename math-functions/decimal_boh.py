#Python program to convert decimal to binary, octal and hexadecimal

def decimal_into_binary(decimal_1):
    decimal = int(decimal_1)

    print("The given decimal number", decimal, "in Binary number is: ", bin(decimal))

def decimal_into_octal(decimal_1):
    decimal = int(decimal_1)

    print("The given decimal number", decimal, "in Octal number is: ", oct(decimal))

def decimal_into_hexadecimal(decimal_1):
    decimal = int(decimal_1)

    print("The given decimal number", decimal, "in Hexadecimal number is: ", hex(decimal))

decimal_1 = int(input("Give a number you want to convert: "))
decimal_into_binary(decimal_1)
decimal_into_octal(decimal_1)
decimal_into_hexadecimal(decimal_1)