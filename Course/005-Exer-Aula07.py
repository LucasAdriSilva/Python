# Desafio 6
a = float(input('Digite um numero: '))
d = a * a 
t =  a * a * a
r = a**(1/2)

print(f'O dobro é {d} o tripo {t} e  a raiz quadrada é {r}')

# Desafio 7
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print(f'A média entre as notas {n1}! e {n2}! é {(n1 + n2) / 2}')

# Desafio 8
m = float(input('Digite um valor em metros: '))
print(f'Então você tem {m} metro que equivale {m*100} centimentos e {m*1000} milimetros')

# Desafio 9
n = int(input('Digite um valor: '))
aux = 1 
while aux < 10:
    print(f'{aux} x {n} = {aux*n}')
    aux += 1

# Desafio 10
valor= float(input('Quanto money você tem na carteira? '))
dolar = valor/3.27
print(f'Você consegue comprar {dolar:.2f} dolares com {valor} reais \nSabendo que o dollar está no valor de 3,27')

# Desafio 11

x = float(input('Digite a altura da sua parede em metros: '))
y = float(input('Digite a largura da sua parede em metros; '))
res = (x * y) /2
print(f'Sabendo que a área da sua parede é {x * y}, vai ser neecssário {res} litros de tinta para pintar completamente')

# Desafio 12
x = float(input('Digite o preço do produto: '))
desc = x*0.05
print(f'Com o desconto de 5% o eu valor vai para {x - desc}')

# Desafio 13
x = float(input('Digite o seu salário; '))
print(f'O seu salário com 15% de aumento é {x +(x*0.15)}, com um aumeto de {x*0.15}!!!')
