resposta = "s"

produtos = []

while resposta == "s":

    print("=== MINHA LOJA ===")

    produto = input("Qual é o produto? ")
    preço = float(input("Qual é o preço? €"))
    quantidade = int(input("Qual é a quantidade? "))

    total = preço * quantidade

    if total >= 200:
        desconto = total * 0.10
        total_final = total - desconto
        mensagem = "Desconto de 10% aplicado"

    elif total <= 180:
        taxa = total * 0.15
        total_final = total + taxa
        mensagem = "Taxa de 15% aplicada"

    else:
        total_final = total
        mensagem = "Sem desconto ou taxa"

    produtos.append([produto, preço, quantidade, total_final])

    print(f"Produto: {produto}")
    print(f"Preço: €{preço:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: €{total:.2f}")
    print(mensagem)
    print(f"Total final: €{total_final:.2f}")

    resposta = input("Quer cadastrar outro produto? s/n ")

print("=== RESUMO DA COMPRA ===")
total_geral = 0
for item in produtos:
    print(f"{item[0]} - {item[2]} unidades - €{item[3]:.2f}")
    total_geral = total_geral + item[3]

print(f"Total geral: €{total_geral:.2f}")