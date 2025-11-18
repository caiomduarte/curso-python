programa {
  funcao inicio() {
    
        // Declaração de variáveis do tipo real para permitir valores com casas decimais
        real preco_original, porcentagem_desconto, valor_desconto, preco_final

        // Solicita ao usuário o preço original do produto
        escreva("Digite o preço original do produto: ")
        leia(preco_original)

        // Solicita ao usuário a porcentagem de desconto
        escreva("Digite a porcentagem de desconto: ")
        leia(porcentagem_desconto)

        // Calcula o valor do desconto
        valor_desconto = preco_original * (porcentagem_desconto / 100)

        // Calcula o preço final após o desconto
        preco_final = preco_original - valor_desconto

        // Exibe os resultados
        escreva("Valor do desconto: ", valor_desconto)
        escreva("\nPreço final do produto: ", preco_final)
  }
}
