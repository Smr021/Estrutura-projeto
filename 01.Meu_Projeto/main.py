import os
from models.Advogado    import Advogado
from models.Medico      import Medico
from models.Motoboy     import Motoboy
from models.Cliente     import Cliente
from models.Funcionario import Funcionario
from models.Fisica      import Fisica
from models.Juridica    import Juridica
from models.Pessoa      import Pessoa
from models.Endereco    import Endereco
from models.enums.Setor import Setor
from models.enums.Sexo  import Sexo
from models.enums.UnidadeFederativa import UnidadeFederativa

os.system("cls || clear")

advogado = Advogado('Gabriel','795961651','Gabriel.crm@gmail.com',
Endereco('Logo ali',55,'avenida peixe','456798926','salvador',UnidadeFederativa.BAHIA ),
'8654656','64566','24/55/5656',Sexo.MASCULINO,'789',Setor.ENGENHARIA,1000,'456')

medico = Medico('Rafael','795961651','Gabriel.crm@gmail.com',
Endereco('Logo ali',55,'avenida peixe','456798926','salvador',UnidadeFederativa.RIO_DE_JANEIRO ),
'8654656','64566','24/55/5656',Sexo.FEMININO,'789',Setor.JURIDICO,1000,'456')

motoboy = Motoboy('Carlos','795961651','Carlos.crm@gmail.com',
Endereco('Logo ali',55,'avenida peixe','456798926','salvador',UnidadeFederativa.SAO_PAULO ),
'8654656','64566','24/55/5656',Sexo.MASCULINO,'789',Setor.OPERACOES,1000,'7984-4945-544')


#print(advogado)
#print(medico)
print(motoboy)