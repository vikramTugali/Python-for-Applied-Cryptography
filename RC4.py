import codecs
print('This is Implementation of RC4 Algorithm')

def get_generating_keystream(key):
    D = Key_Scheduling_Algorithm(key)
    return Pseudo_Random_Number_Genarator(D)
def __init__(self, key):
        self.key = key
def Logic_Behind_Encryption(key, text):
    key = [ord(str ) for str in key]
    key_stream = get_generating_keystream(key)
    result = []
    for str in text:
        resulting_value = ("%02X" % (str  ^ next(key_stream)))  
        result.append(resulting_value)
    return ''.join(result)
def encrypt(key, plain_text):
    plain_text = [ord(str) for str in plain_text]
    return Logic_Behind_Encryption(key, plain_text)
       
def decrypt(key, cipher_text):    
    cipher_text = codecs.decode(cipher_text, 'hex_codec')
    result = Logic_Behind_Encryption(key, cipher_text)
    return codecs.decode(result, 'hex_codec').decode('utf-8').strip()

def Pseudo_Random_Number_Genarator(D):    
    A = 0
    B = 0
    while True:
        A = (A + 1) % 256
        B = (B + D[A]) % 256
        D[A], D[B] = D[B], D[A]  
        yield D[(D[A] + D[B]) % 256]

def Key_Scheduling_Algorithm(key):
    key_length = len(key)
    D = list(range(256))  
    B = 0
    for A in range(256):
        B = (B + D[A] + key[A % key_length]) % 256
        D[A], D[B] = D[B], D[A]  
    return D

def main():
    plain_text = 'You can meet me during office hours. No appointment is required.'
    key = 'Cybr-625-RC4-Implmentation' 
    print('given plaintext:', plain_text)
    print('Key used:',key) 
    cipher_text = encrypt(key, plain_text)
    print('ciphertext after encryption:', cipher_text)
    decrypted = decrypt(key, cipher_text)
    print('text after decryption:', decrypted)

if __name__ == '__main__':
    main()
