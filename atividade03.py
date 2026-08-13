#Uma emprese oferece um bônus aos funcionários de acordo com o valor de suas vendas no mês. Crie um algoritmo que solicite o salário e o valor das vendas e informe o salário final de acordo com o desempenho. 

#Considere que: 
#A partir de R$5000 em vendas,  o funcionário recebe um bonus de R$500
#A partir de R$3000 em vendas, o funcionário recebe um bonus de R$250
#Abaixo de R$3000 em vendas, não recebe bonus 
salario=int(input(f'Informe seu salário R$'))
vendas=int(input('Informe suas vendas mensais R$'))

if vendas >= 5000:
    total_comissao= 500
    print(f'Parabéns, você receberá R${total_comissao} em bonus')

elif vendas >=3000:
    total_comissao=300
    print(f'Parabéns, você receberá R${total_comissao} em bônus.')
else:
    print(f'Você não receberá bonûs')

print(f'O seu salário é R${salario}')
print(f'O valor total recebido é de R${total_comissao +salario}')


