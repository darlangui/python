from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_funcionario_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'
        esperada = 'Carvalho'

        funcionario_teste = Funcionario(entrada, '12/03/2000', 1111)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperada