alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
s_alphabet=[]
encrypt_word=[]

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#shift-=1
def encrypt(text, shift):
    for z in range(0,26):
        if z+shift < 25:
            s_alphabet.append(alphabet[z+shift])
        else:
            s_alphabet.append(alphabet[z+shift - 26])
        print(s_alphabet[z])

    print(len(text))

    for y in range(0,len(text)):
        for x in range(0,26):
            if text[y]==alphabet[x]:
                encrypt_word.append(s_alphabet[x])
    
    print(encrypt_word)
    print(''.join(encrypt_word))


encrypt(text, shift)





    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  

    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 