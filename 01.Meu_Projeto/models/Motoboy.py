from .Endereco import Endereco
from .enums.Setor import Setor
from .enums.Sexo import Sexo
from models.Funcionario import Funcionario

class Motoboy(Funcionario):
    BONIFICACAO = 1.2

    def __init__(self, nome: str, telefone: str,
                  email: str, endereco: Endereco, cpf: str,
                    rg: str, dataNascimento: str, sexo: Sexo,
                      matricula: str, setor: Setor, salario: float,cnh:str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)
        self.cnh = cnh

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f'\nCNH: {self.cnh}')