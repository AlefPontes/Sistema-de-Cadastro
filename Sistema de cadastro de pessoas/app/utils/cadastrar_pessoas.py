import sqlite3
from termcolor import colored
from app.lib.interface import Interface
from app.lib.validators import Validators

class Cadastrar_pessoa:
    def __init__(self):
        i = Interface(' <<< CADASTRAR NOVAS PESSOAS >>> ', '')
        i.cabeçalho()

    def cadastrar(self):
        banco = sqlite3.connect('D:\\Alef\\Documentos\\Sistema de cadastro de pessoas\\app\\database\\pessoas_cadastradas.db')
        cursor = banco.cursor()

        while True:
            while True:
                try:
                    v = Validators()
                    pessoa = v.verificar_dados()
                    cursor.execute(f"INSERT INTO pessoas VALUES('{pessoa['nome']}', '{pessoa['idade']}', '{pessoa['email']}', '{pessoa['telefone']}', '{pessoa['cpf']}')")
                    banco.commit()
                    break
                except Exception as erro:
                    print(colored('Algo deu errado, tente novamente.', 'red'))
                    print(erro)

            print(colored('Pessoa cadastrada com sucesso!', 'green'))
            while True:
                opção = input(colored('Deseja cadastrar uma nova pessoa? [S/N] ', 'cyan'))
                if opção.upper().startswith('S'):
                    break
                elif opção.upper().startswith('N'):
                    break
                else:
                    print(colored('Opção inválida, tente novamente.', 'red'))
            if opção.upper().startswith('N'):
                    break
        banco.close()
