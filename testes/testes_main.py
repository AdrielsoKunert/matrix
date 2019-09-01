from unittest import TestCase
from unittest.mock import patch , call
from matrix_.matrixv2 import main, attr


class Testes(TestCase):
    @patch('matrix_.matrixv2.sleep')
    @patch('matrix_.matrixv2.Architect')
    @patch('matrix_.matrixv2.texto_efeito_pausa')
    def test_texto_efeito_pausa_chamado_com_argumentos(self, mock2, *_):
        main()
        esperado = [
            call('Conectando a matrix...'), call(attr(0) + '\nDesconectado.')
        ]
        self.assertEqual(mock2.mock_calls, esperado)

    @patch('matrix_.matrixv2.sleep')
    @patch('matrix_.matrixv2.texto_efeito_pausa')
    @patch('matrix_.matrixv2.Architect')
    def test_arquiteto_chamado(self, mock, *_):
        main()
        mock.assert_any_call()

    @patch('matrix_.matrixv2.sleep')
    @patch('matrix_.matrixv2.texto_efeito_pausa')
    @patch('matrix_.matrixv2.Architect.rain')
    def test_rain_chamado(self, mock, *_):
        main()
        mock.assert_any_call()
