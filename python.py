def encrypt(str, shiftAmount):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    for character in str:                                                              # iterate the letters through the message
        if character in alphabet:                                                      # check if letter is in alphabet (no special characters)
            position = (alphabet.find(character) + shiftAmount) % len(alphabet)        # formula to check for letter to ciphertext equivalent for encyption (+ sign moves fowards in shift)
            encrypted = encrypted + alphabet[position]                                 # creates the cipher letter and puts it in its list to make the word
        else:
            encrypted = encrypted + character                                          # takes whatever letter is not in the 'alpahabet' to add it into the encyrpted message as its orginal value
    return encrypted                                                                   # finish and return to print statement

def decrypt(str, shiftAmount):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted = ""
    for character in str:
        if character in alphabet:
            position = (alphabet.find(character) - shiftAmount) % len(alphabet)   # formula to check for letter to ciphertext equivalent for decryption (- sign moves back in shift)
            decrypted = decrypted + alphabet[position]
        else:
            decrypted = decrypted + character
    return decrypted

def solve(str, maxShiftValue):
    if maxShiftValue < 0:                                                  #if maxShiftValue is less than 0, it will be positive
        maxShiftValue = maxShiftValue * -1
    
        while maxShiftValue >=0:                                            #iterate through maxShiftValue until 0 but will print 0
            solve = encrypt(str, maxShiftValue)                             #whatver shift its at goes through encrypt function for desired output in assignment (decrpyt flips the list)
            message = print("Ceaser ", maxShiftValue ,":", solve.upper())     #print the respective message
            maxShiftValue -= 1                                              #-1 on maxShiftValue so the while loop doesn't continously loop
        return message
    else:
        while maxShiftValue >=0:                                            #iterate through maxShiftValue until 0 but will print 0
            solve = encrypt(str, maxShiftValue)                             #whatver shift its at goes through encrypt function for desired output in assignment (decrpyt flips the list)
            message = print("Ceaser ",maxShiftValue ,":", solve.upper())     #print the respective message
            maxShiftValue -= 1                                              #-1 on maxShiftValue so the while loop doesn't continously loop
        return message

str = input("Please enter a text you wish to cipher: \n").strip().upper()
shiftAmount = int(input("Please enter the shift pattern: \n"))

print("Cipher encryption: " + encrypt(str, shiftAmount))
print("Cipher decryption: " + decrypt(str, shiftAmount))
print(solve("HAL", 26))
