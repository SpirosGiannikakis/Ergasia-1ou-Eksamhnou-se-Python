def rot13(s):
    result = ""

    #epanalhpsh xarakthrwn
    for v in s:
        # metatroph arithmou me thn ord
        c = ord(v)

        # Shift twn arithmo pros ta mpros h pros ta pisw
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        # Append to apotelesma
        result += chr(c)

    # Return thn metatroph
    return result

# Test 
text = input("Please insert the text that you would like to encrypt ") 
print("This is your text encrypted\n")
print(rot13(text))