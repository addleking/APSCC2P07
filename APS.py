import subprocess
subprocess.run('pip install cryptography', shell=True)
from cryptography.fernet import Fernet

#Bloco 0.0 - Gera a chave unica
priKey = Fernet.generate_key()

#Bloco 0.1 - Escreve a chave unica no arquivo 'key.key'
file = open('.chave\key.key', 'wb')
file.write (priKey)
file.close()

#Bloco 1.0 - Pega a chave preconfigurada no arquivo
file = open('.chave\key.key', 'rb')
key = file.read()
file.close()

#bloco 1.1 - codifica a mensagem
message = input('Digite aqui sua mensagem: ')
encoded = message.encode()

#Bloco 1.2 - Criptografa a mensagem
f = Fernet(key)
encrypted = f.encrypt(encoded)

#Bloco 1.3 -  Mostra a mensagem criptografada
#*Este bloco eh didatico e nao necessariamente estara no programa final
original_message0 = encrypted.decode()
print ("Essa é a mensagem cripitografada: ",original_message0)

#Bloco 2.0 - Le a chave do arquivo pre configurado
file = open('.chave\key.key', 'rb')
key0 = file.read()
file.close()

#Bloco 2.1 - Decriptografa a mensagem
f2 = Fernet (key)
decrypted = decrypted = f2.decrypt(encrypted)

#Bloco 2.2 - Mostra a mensagem
original_message = decrypted.decode()
print ("Essa foi a mensagem enviada: ",original_message)

#Bloco 2.3 - Mostra a chave aplicada.
print ('A chave aplicada foi:',priKey)
