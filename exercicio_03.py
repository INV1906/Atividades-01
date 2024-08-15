valorpao = 0.12
valorbroa = 1.50
pao = int(input('Digite a quantidade de pães vendidos hoje: '))
broa = int(input('Digite a quantidade de broas vendidas hoje: '))

totalarrecadado = valorpao * pao + valorbroa * broa

investimento = totalarrecadado * 0.1

print(investimento)
