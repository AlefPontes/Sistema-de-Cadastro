import sqlite3
from time import sleep
from app.lib.validators import *
from app.lib.interface import *
from app.utils.edit_pessoas_cadastradas import *
from termcolor import colored


class Pessoas_cadastradas:
    def __init__(self):
        i = Interface(' <<< PESSOAS CADASTRADAS >>> ', '')
        print(f' {" <<< PESSOAS CADASTRADAS >>> ":-^80} ')


    def mostrar_pessoas(self):
        banco = sqlite3.connect('D:\\Alef\\Documentos\\Sistema de cadastro de pessoas\\app\\database\\pessoas_cadastradas.db')
        cursor = banco.cursor()
        cursor.execute('SELECT nome FROM pessoas')
        nomes = cursor.fetchall()
        if len(nomes) == 0:
            print(colored('No momento, não há ninguém cadastrado no banco de dados.', 'red'))
            return
        id = 0
        for pessoa in nomes:
            print(colored(f'{id+1} | {nomes[id][0]}', 'green'))
            id += 1
        banco.close()
        self.options()
    

    def options(self):
        banco = sqlite3.connect('D:\\Alef\\Documentos\\Sistema de cadastro de pessoas\\app\\database\\pessoas_cadastradas.db')
        cursor = banco.cursor()
        cursor.execute('SELECT nome FROM pessoas')
        nomes = cursor.fetchall()
        while True:
            i = Interface('', '')
            print(i.line())
            global ID
            ID = input('Digite o ID da pessoa que você deseja ver os dados mais completos. (0 para voltar a tela inicial) ')
            try:
                ID = int(ID)
                try:
                    if ID == 0:
                        break
                    elif ID < 0:
                        print(colored('Opção inválida, tente novamente.', 'red'))
                    elif ID > len(nomes):
                        print(colored('Opção inválida, tente novamente.', 'red'))
                    else:
                        cursor.execute('SELECT * FROM pessoas')
                        dados = cursor.fetchall()
                        person = dados[ID-1]
                        dados_formatados = (f'Nome completo: {person[0]}\nIdade: {person[1]}\nEmail: {person[2]}\nTelefone: {person[3]}\nCPF: {person[4]}')
                        print(i.line())
                        print(colored(f"{f'Dados de {person[0]}':^{i.tamanho_fonte}}", 'cyan'))
                        print(dados_formatados)
                        print(f"{' <<< OPÇÕES DISPONÍVEIS >>> ':-^{i.tamanho_fonte}}")
                        avaliable_options = ['Ver os dados de outra pessoa', 'Editar dados', 'Deletar dados', 'Voltar ao menu inicial']
                        c = 1
                        for item in avaliable_options:
                            print(f'\033[33m{c} - \033[36m{item}\033[m')
                            c += 1
                        print(i.line())
                        option = int(i.read_option(avaliable_options))
                        if option == 1:
                            self.options()
                        elif option == 2:
                            e = Edit(ID)
                            e.edit()
                            return
                        elif option == 3:
                            r = Remove(ID)
                            r.remove()
                            return
                        elif option == 4:
                            banco.close()
                            return
                except Exception as erro:
                    print(colored('Algo deu errado, voltando ao menu inicial.'))
                    print(erro)
                    return
            except:
                print(colored('Opção inválida, tente novamente.', 'red'))
            finally:
                banco.close()
