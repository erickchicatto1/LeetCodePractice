import string

def caesar(plain_text,shift_num=1):
    
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters,mask)
    
    return plain_text.translate(trantab)

mensaje = "hola"
cifrado = caesar(mensaje,5)
print(cifrado)