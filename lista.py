x=[]
z=[]

print("-------------------------------------------")
print(" ")
print("NÚMEROS PARES E ÍMPARES")
print(" ")
print("-------------------------------------------")
print("> Insira 5 valores a serem classificados")
print("-------------------------------------------")

for i in range(5):
    i=int(input("> Insira um valor: "))
    if i%2==0:
        print("*",i," é um número PAR*")
        x.append(i)
    else:
        print("*",i, " é um número ÍMPAR*")
        z.append(i)

print("------------------------------------------")
print("> Lista de números PARES: ",x)
print("> Lista de números ÍMPARES: ",z)
print("------------------------------------------")