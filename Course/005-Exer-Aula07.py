# Desafio 6
a = float(input('Digite um numero: '))
d = a * a 
t =  a * a * a
r = a**(1/2)

print('O dobro é {} o tripo {} e  a raiz quadrada é {}'.format(d, t, r))

# Desafio 7
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('A média entre as notas {}! e {}! é {}'.format(n1, n2, ((n1+n2)/2)))

# Desafio 8
m = float(input('Digite um valor em metros: '))
print('Então você tem {} metro que equivale {} centimentos e {} milimetros'.format(m, m*100, m*1000))

# Desafio 9
n = int(input('Digite um valor: '))
aux = 1 
while aux < 10:
    print('{} x {} = {}'.format(aux, n, aux*n))
    aux += 1

# Desafio 10
valor= float(input('Quanto money você tem na carteira? '))
dolar = valor/3.27
print('Você consegue comprar {} dolares com {} reais \nSabendo que o dollar está no valor de 3,27'.format(round(dolar, 2), valor ))

# Desafio 11

x = float(input('Digite a altura da sua parede em metros: '))
y = float(input('Digite a largura da sua parede em metros; '))
res = (x * y) /2
print('Sabendo que a área da sua parede é {}, vai ser neecssário {} litros de tinta para pintar completamente'.format(x * y, res))

# Desafio 12
x = float(input('Digite o preço do produto: '))
desc = x*0.05
print('Com o desconto de 5% o eu valor vai para {}'.format(x - desc))

# Desafio 13
x = float(input('Digite o seu salário; '))
print('O seu salário com 15% de aumento é {}, com um aumeto de {}!!!'.format(x +(x*0.15), x*0.15))
