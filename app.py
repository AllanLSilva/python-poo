from models.restaurantes import Restaurantes
from models.layout.bebidas import Bebidas
from models.layout.prato import Prato
from models.layout.sobremesa import Sobremesa

restaurante_praca = Restaurantes('praça', 'Gourmet')
bebida_suco = Bebidas('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_bolo = Sobremesa('Bolo de cenoura', 8.0, '200g')
sobremesa_bolo.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_bolo)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()