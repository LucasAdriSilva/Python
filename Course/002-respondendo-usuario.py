nome = input('Digite o seu nome?')
print('É um prazer te conheçer {}!' .format(nome))

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
s = int(n1) + int(n2)
print('O valor da soma entre {} e {} é {}'.format(n1, n2, s))


print('O valor da soma entre {:>4} e {:<10} é {:=^101}'.format(n1, n2, s))
