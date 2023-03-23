pais = '10'
type(pais)

if(pais == 10):
    print('Aqui')
else:
    print('nop')

name1 = 'Nome'
name2 = 'Sobrenome'

print(name1, name2, sep=" ")

if(pais == 10):
    if(pais > 9):
        print('Isso é algo')
    elif(pais < 9):
        print('menor')
    elif(pais > 9):
        print('algo')

usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")


for i in range(1, 11, 3):
    print(i)

i = True
while(i):
    print('new while')
    break

while(i):
    if(i == True):
        i = False
        break
    if(i == False):
        continue

