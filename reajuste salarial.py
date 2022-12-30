# criar um algoritmo que leia o salario de um funcionario e mostre seu novo salario , com 15 % de aumento.
salario = float (input ('qual é o salario do funcionario?R$'))
novo = salario + (salario * 15 / 100)
print ('o funcionario que ganhava {:.2f} com aumento de 15% ganhara{:.2f}'.format(salario,novo))

