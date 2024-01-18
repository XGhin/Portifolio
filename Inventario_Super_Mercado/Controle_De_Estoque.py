class Produtos:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def remover_produto(self):
        self.quantidade -= 1

    def adicionar_produto(self):
        self.quantidade += 1

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def valor_do_estoque(self):
        print(f"O valor do estoque de {self._nome} é R$ {self.preco * self.quantidade} Reais")


