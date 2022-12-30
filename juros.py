#crie um algoritmo que o valor a vista tem 10% de desconto eo valor parcelado tem 8 % de juros
produto = float (input ('o valor do produto é R$ '))
avista = produto - (produto *10/100)
parcelado = produto +(produto *8/100 )
print ('produto avista {:.2f} com o desconto de 10% sera R$ {:.2f} valor parcelado com acrescimo de 8% será R$ {:.2f}'.format (produto,avista,parcelado))