#fazer um programa que leia quantos a pessoa tem na carteira   e mostre quantos dolares 
#ela pode compra
#Cosidere us$1,0 = 5,29

real= float (input ('quantos voce tem em real na sua carteira? :R$ '))
dolar = real / 5.29
euro = real / 5.66
peso_argentino = real /0.030
iene = real / 0.040

print ('com R${:.2f} voce pode comprar dolar {:.2f}'.format(real, dolar ))
print ('com R${:.2f} voce pode comprar euro  {:.2f}'.format(real, euro) )
print ('com R${:.2f} voce pode comprar peso_argentino {:.2F}'.format (real,peso_argentino))
print ('com R$ {:.2f} voce compra iene {:.2F}'.format (real,iene))
