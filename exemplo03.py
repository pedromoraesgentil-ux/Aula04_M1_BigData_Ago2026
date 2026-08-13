#Crie um algoritmo que solicite o tempo de casa, o salário e o setor do funcionário e calcule o novo salário. 
#Considere que - Funcionários do setor A com pelo menos 3 anos de empresa recebem reajustes de 18%
#Os demais funcionários recebem reajuste de 9% 

 #Ao final, informe o valor do aumento, o percentual de reajuste e o salário reajustado. 

tempo= float(input(f'Tempo de casa:'))
salario=float(input(f'Salário R$'))
setor=input(f'Informe o Setor:').upper()#obriga o texto a ficar maiusculo.

if setor == 'A'and tempo >=3:
    aumento=salario*0.18

else:
    aumento=salario*0.09

novo_salario = aumento + salario
print("\\=====RESULTADO=====/")
print(f'O aumento será de R${aumento}')
print(f'O novo salário será de R${novo_salario}')
