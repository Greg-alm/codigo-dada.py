import random


lukas = list(["Maravilhoso", "Melhor Professor", "pre-historico", "", "Tem que dar 05 na media para o Gregory"])


total_lukas = len(lukas)

print(f"--- VOCE É : ({total_lukas} opções) ---")
print("Digite '1' para sortear ou '0' para sair.")


#O comando while faz com que um conjunto de instruções seja executado enquanto uma condição
# é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida
while True:
    
    comando = input("\nComando: ")

    if comando == "1":
        escolha = random.choice(lukas)
        
        print(f" PARABENS VOCÊ É : {escolha}")
    
    elif comando == "0":
        print("CABO")
        break
    else:
        print("Opção inválida! Digite apenas '1' ou '0'.")