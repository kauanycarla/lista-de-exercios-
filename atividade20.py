#24. Sejam 𝑏 e 𝑏 os catetos de um triangulo, onde a hipotenusa é obtida pela equação 
#ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √𝑎2 + 𝑏². Faça um programa que receba os valores de 𝑎 e 𝑏 e calculo 
#o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

A = float(input('Digite o cateto oposto:'))

B = float(input('Diggite o cateto adjacente:'))

HIPOTENUSA =  (B** 2 + A * 2 ) * (1/2)

print('='*50)

print('O valor da hipotenusa é: {:.2f}'.format(HIPOTENUSA))