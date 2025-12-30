import hashlib
# 1- Verificar os algoritimos disponiveis
print(hashlib.algorithms_available)
print("----------------------------------------------")
# 1- Verificar os algoritimos de acordo com o SO.
print(hashlib.algorithms_guaranteed)
print("----------------------------------------------")
# 1- Verificar o SHA256
algoritimo = hashlib.sha256()
print(algoritimo.digest())
message = "Eliana Nunes da Silva".encode()
algoritimo.update(message)
print(algoritimo.hexdigest())
print("----------------------------------------------")
