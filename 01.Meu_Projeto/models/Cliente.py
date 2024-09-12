from models.Endereco import Endereco
from models.enums.Sexo import Sexo
from models.Fisica import Fisica

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str,
                  endereco: Endereco, cpf: str,
                    rg: str, dataNascimento: str, sexo: Sexo,protocoloAtendimento:int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)

        self.protocoloAtendimento = protocoloAtendimento
    
    def __str__(self) -> str:
        return (f'\nNumero de atendimento: {self.protocoloAtendimento}')
