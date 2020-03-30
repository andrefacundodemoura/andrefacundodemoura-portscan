import socket

portas =range(1,25000)

for porta in portas:
    cliente = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    codigo = cliente.connect_ex(('bancocn.com',porta))

    if codigo == 0:
        print(porta ,'OPEN')
#se retornar codigo 0 DEU CERTO
