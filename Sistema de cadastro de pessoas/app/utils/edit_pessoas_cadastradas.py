import sqlite3
from typing import final
from termcolor import colored
from app.lib.interface import *
from app.lib.validators import *
from termcolor import colored

class Remove:
    def __init__(self, ID):
        self.ID = ID


    def remove(self):
        try:
            banco = sqlite3.connect('D:\\Alef\\Documentos\\Sistema de cadastro de pessoas\\app\\database\\pessoas_cadastradas.db')
            cursor = banco.cursor()
            cursor.execute('SELECT * FROM pessoas')
            dados = cursor.fetchall()
            person = dados[self.ID-1]
            cursor.execute(f"DELETE FROM pessoas WHERE nome='{person[0]}'")
            print(colored('Dados deletados com sucesso!', 'green'))
            banco.commit()
            banco.close()
        except Exception as er:
            print(colored('Perdão, algo deu errado, tente novamente.', 'red'))
            banco.close()
            return


class Edit:
    def __init__(self, ID):
        self.ID = ID
    

    def edit(self):
        try:
            banco = sqlite3.connect('D:\\Alef\\Documentos\\Sistema de cadastro de pessoas\\app\\database\\pessoas_cadastradas.db')
            cursor = banco.cursor()
            cursor.execute('SELECT * FROM pessoas')
            dados = cursor.fetchall()
            person = dados[self.ID-1]
            i = Interface('', '')
            v = Validators()
            while True:
                print(i.line())
                print('Qual dado você quer editar?')
                avaliable_options = ['Nome', 'Idade', 'Email', 'Telefone', 'CPF', 'Voltar ao menu inicial']
                c = 1
                for item in avaliable_options:
                    print(f'\033[33m{c} - \033[36m{item}\033[m')
                    c += 1
                option = int(i.read_option(avaliable_options))
                print(i.line())
                if option == 1:
                    new_name = v.verify_name()
                    cursor.execute(f"UPDATE pessoas SET nome='{new_name}' WHERE nome='{person[0]}'")
                    banco.commit()
                    print(colored('Nome atualizado com sucesso!', 'green'))
                elif option == 2:
                    new_old = int(v.verify_old())
                    cursor.execute(f"UPDATE pessoas SET idade={new_old} WHERE nome='{person[0]}'")
                    print(colored('Idade atualizada com sucesso!', 'green'))
                    banco.commit()
                elif option == 3:
                    new_email = v.verify_email()
                    cursor.execute(f"UPDATE pessoas SET email='{new_email}' WHERE nome='{person[0]}'")
                    print(colored('Email atualizado com sucesso!', 'green'))
                    banco.commit()
                elif option == 4:
                    new_telefone = int(v.verify_number())
                    cursor.execute(f"UPDATE pessoas SET telefone='{new_telefone}' WHERE nome='{person[0]}'")
                    print(colored('Telefone atualizado com sucesso!', 'green'))
                    banco.commit()
                elif option == 5:
                    new_cpf = v.verify_cpf()
                    cursor.execute(f"UPDATE pessoas SET cpf='{new_cpf}' WHERE nome='{person[0]}'")
                    print(colored('CPF atualizado com sucesso!', 'green'))
                    banco.commit()
                else:
                    return

                banco.commit()

                while True:
                    response = str(input(colored('Deseja alterar mais algum dado? [S/N] ', 'yellow'))).upper()
                    if response.startswith('S'):
                        break
                    elif response.startswith('N'):
                        break
                    else:
                        print(colored('Opção inválida, tente novamente.', 'red'))
                if response.startswith('N'):
                    break

        except Exception as er:
            print(colored('Perdão, algo deu errado, tente novamente.', 'red'))
            print(er)
            return

        finally:
            banco.close()
