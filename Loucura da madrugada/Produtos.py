class Produtos:
    def __init__(self, nome:str, preco:float, quantidade:int):
        self._nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def adicionar_produto(self):
        self.quantidade += 1
    
    def adicionar_multiplas_quantidades(self, quantidade):
        self.quantidade += quantidade
        
    def remover_produto(self):
        self.quantidade -= 1
    
    def remover_multiplas_quantidades(self, quantidade):
        self.quantidade -= quantidade
    
    def redefenir_preco(self, novo_preco):
        self.preco = novo_preco
        
    def capital_atual(self):
        capital_atual = self.preco * self.quantidade
        print(f"o capital atual do produto {self._nome} é {capital_atual}")

