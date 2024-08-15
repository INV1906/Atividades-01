peso = int(input("Insira o peso do prato montado:"))
prato = 0.750
pesoacobrar = peso - prato
preçokg = 12

total = pesoacobrar * preçokg
print("O prato está no valor de R$",int(total))