programa {
  funcao inicio() {
    real valor_parte, valor_total, porcentagem

    escreva("Digite o valor Total: ")
    leia(valor_total)

    escreva("Digite a porcentagem a ser calculada: ")
    leia(porcentagem)

    valor_parte = valor_total * (porcentagem / 100)    

    escreva("O valor parte é de: ", valor_parte)
  }
}
