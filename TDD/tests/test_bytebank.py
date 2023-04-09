import pytest

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

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bourdon'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_calcular_bonus_receber_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_receber_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
