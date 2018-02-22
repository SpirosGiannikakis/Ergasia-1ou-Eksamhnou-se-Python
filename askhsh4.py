#Xartografhsh xarakthrwn
num_map = [(1000000, '-M'), (750000, '-D-C-C-L'), (500000, '-D'), (300000, '-C-C-C'), (100000, '-C'), (90000, '-XC'), (50000, '-L'), (10000, '-X'), (5000, '-V'), (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

#Sunarthsh metatrophs se latinikh morfh
def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman

	
#Test
print("Please insert the number that you would like to romanize\n")
num = int(input())
print("This is your number romanized:")
print(num2roman(num))