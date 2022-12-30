#criar um pg que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais ele
#foi alugado .calcule o preço a pagar , sabendo que o carro carro custa R$ 60 por dia e R$0,15 por km rodado.

dias = int (input ('quantos dias alugados ?'))
km = float (input ('quantos km rodados ?'))
pago =  (dias *60) + (km * 0.15)
print ('O TOTAL A PAGAR É : R$ {:.2F}'.format(pago))