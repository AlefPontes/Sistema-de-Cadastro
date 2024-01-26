'''from termcolor import colored

cpf_numerado = []

class VerificaCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def numerar_cpf(self):
        for a in self.cpf:
            a = int(a)
            self.cpf_numerado.append(a)

    # Verifica o tamanho do cpf
    def verificar_tamanho_cpf(self):
        if 11 < len(self.cpf) < 11:
            return False
        else:
            return True

    # Verifica o primeiro dígito do cpf
    def primeiro_digito(self):
        if len(self.cpf_numerado) < 11 or len(self.cpf_numerado) > 11:
            return False
        else:
            acumulador = 0
            resultado = 0
            controlador = 10
            for numeros in self.cpf_numerado[0:9]:
                resultado = numeros * controlador
                acumulador += resultado
                controlador -= 1
            acumulador *= 10 % 11
            if acumulador == 10:
                acumulador = 0
            if acumulador == self.cpf_numerado[9]:
                self.cpf_numerado.append(acumulador)
                return True

    def segundo_digito(self):
        if len(self.cpf_numerado) < 11 or len(self.cpf_numerado) > 11:
            return False
        else:
            acumulador2 = 0
            resultado2 = 0
            controlador2 = 11
            for numeros in self.cpf_numerado[0:10]:
                resultado2 = numeros * controlador2
                acumulador2 += resultado2
                controlador2 -= 1
            acumulador2 *= 10 % 11
            if acumulador2 == 10:
                acumulador2 = 0
            if acumulador2 == self.cpf_numerado[10]:
                return True
            else:
                return False

    def verificar_validade(self):
        try:
            self.numerar_cpf()
            self.verificar_tamanho_cpf()
            self.primeiro_digito()
            self.segundo_digito()
            if self.verificar_tamanho_cpf() == True and self.primeiro_digito() == True and self.segundo_digito() == True:
                return True
            else:
                return False
        except:
            print(colored('Número de CPF inválido, tente novamente', 'red'))
'''
import re

class VerificaCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def isCpfValid(self):
        """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

        # Check if type is str
        if not isinstance(self.cpf,str):
            return False

        # Remove some unwanted characters
        self.cpf = re.sub("[^0-9]",'',self.cpf)
        
        # Verify if CPF number is equal
        if self.cpf=='00000000000' or self.cpf=='11111111111' or self.cpf=='22222222222' or self.cpf=='33333333333' or self.cpf=='44444444444' or self.cpf=='55555555555' or self.cpf=='66666666666' or self.cpf=='77777777777' or self.cpf=='88888888888' or self.cpf=='99999999999':
            return False

        # Checks if string has 11 characters
        if len(self.cpf) != 11:
            return False

        sum = 0
        weight = 10

        """ Calculating the first cpf check digit. """
        for n in range(9):
            sum = sum + int(self.cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 -  sum % 11

        if verifyingDigit > 9 :
            firstVerifyingDigit = 0
        else:
            firstVerifyingDigit = verifyingDigit

        """ Calculating the second check digit of cpf. """
        sum = 0
        weight = 11
        for n in range(10):
            sum = sum + int(self.cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 -  sum % 11

        if verifyingDigit > 9 :
            secondVerifyingDigit = 0
        else:
            secondVerifyingDigit = verifyingDigit

        if self.cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
            return True
        return False


    '''def isCnpjValid(self):
        """ If cnpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

        # Check if type is str
        if not isinstance(cnpj,str):
            return False

        # Remove some unwanted characters
        cpf = re.sub("[^0-9]",'',cnpj)

        # Checks if string has 11 characters
        if len(cpf) != 14:
            return False

        sum = 0
        weight = [5,4,3,2,9,8,7,6,5,4,3,2]

        """ Calculating the first cpf check digit. """
        for n in range(12):
            value =  int(cpf[n]) * weight[n]
            sum = sum + value


        verifyingDigit = sum % 11

        if verifyingDigit < 2 :
            firstVerifyingDigit = 0
        else:
            firstVerifyingDigit = 11 - verifyingDigit

        """ Calculating the second check digit of cpf. """
        sum = 0
        weight = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        for n in range(13):
            sum = sum + int(cpf[n]) * weight[n]

        verifyingDigit = sum % 11

        if verifyingDigit < 2 :
            secondVerifyingDigit = 0
        else:
            secondVerifyingDigit = 11 - verifyingDigit

        if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
            return True
        return False'''
