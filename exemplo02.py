#Criar um alboritmo que solicite a pontuação do participante e, de acordo com os pontos obtidos, informe seu desempenho e acrescente um bônus à sua pontuação.

#Considere a partir de 100 pontos, o bonûs é de 10 pontos 
#Considere a partir de 50 pontos, o bonus é de 5 pontos 
#considere a partir de <50 pontos não tem bonus 

pontos=int(input('Informe os pontos:'))
if pontos >= 100:
    total_pontos=pontos+10  
    print(f'Excelente! Você tem agora {total_pontos} pontos')     

elif pontos >=50:
    total_pontos=pontos + 5
    print(f'Bom desempenho! Você tem agora {total_pontos} pontos')     

elif pontos >=30:
    total_pontos=pontos +1
    print(f'O seu desempenho foi satisfatório, mas pode melhorar! Agora você tem {total_pontos} pontos')

else: 
    print(f'Voce não terá bônus.Pontuação{pontos}')    

