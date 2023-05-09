import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#exemplo
#password = "senha"
#salt = b"1234567890123456"
#derivacão de chave PBKDF2HMAC 
def generate_key(password, salt):
    """Gera uma chave de criptografia a partir de uma senha e um salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = Fernet(base64.urlsafe_b64encode(kdf.derive(password.encode())))
    return key



def decrypt_message(file, key):
    """Descriptografa uma mensagem utilizando a chave fornecida"""
    with open(file, 'rb') as arq:
        message = arq.read()
        
    if message:
        decrypted = key.decrypt(message)
    
        return decrypted.decode()
    return False

def encrypt_message(file, key, message = False, file_message = False):
    """Criptografa uma mensagem utilizando a chave fornecida"""
    
    if message:
        data = decrypt_message(file,key)
        if data:
            data += f'\n{message}'
            
        else: data = message
        
    elif file_message:
        with open(file_message, 'r') as arq:
            message = arq.read()
            
        data = decrypt_message(file,key)
        if data:
            data += f'\n{message}'
            
        else: data = message
    
    else: return False
        
    
    encrypted = key.encrypt(data.encode()) # type: ignore
    print(encrypted)
    
    with open(file, 'wb') as arq:
        arq.write(encrypted)
        
    return True

if __name__ == '__main__':
    key = generate_key('marcos',b'12345')
    print(encrypt_message('teste.txt', key, file_message='base.txt'))
    print('-',decrypt_message('teste.txt', key),'-')