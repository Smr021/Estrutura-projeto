from models.Endereco import Endereco
from models.Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,cnpj:str, inscricao:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao = inscricao

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f'\nCNPJ {self.cnpj}'
                f'\nInscricao estadual {self.inscricao}'
                )