"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def Encrypt(o):
    vow = "aeiouAEIOU"
    word = ""
    for x in o:
        if x in vow:
            x = ""
        word += x
    return word
print(Encrypt("Computer Science Makes the World go round but it doesn't make the world round itself!"))
NoVowels = Encrypt("Computer Science Makes the World go round but it doesn't make the world round itself!")
"""Write an encryption code that you make up and run it for the variable NoVowels"""
def encrip(s,u):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[u:]+chars[:u]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )
print(encrip(NoVowels, 10))
