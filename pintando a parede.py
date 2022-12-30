#criar  um programa que leia a largura e a altura de uma parede em metros e ,calcule sua 
#area ea quantidade de tinta necessaria para pintá-la , sabendo que cada litro de tinta,
#pinta um area de 2m quadrados
larg = float (input ('largura da parede:'))
alt = float (input ('Altura da parede :'))
área = larg *alt 
print ('sua parede tem a dimensão de {} x {} e sua area é de {}m²'.format (larg,alt,área))
tinta = área / 2
print ('para pintar essa parede , voce ira precisar de {} litros de tinta' .format (tinta))