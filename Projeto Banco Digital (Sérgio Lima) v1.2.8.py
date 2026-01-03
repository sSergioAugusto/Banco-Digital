import os
import random
import time

# CONTAS ====================
contafixa_nome = 'Visitante'
contafixa_senha = '1234'

login_nome = 'abuu'
login_senha = '1234'
status_login = 'false'
#----------------------------

# TENTATIVAS ----------------
loginerradotentativas = 3
status_cadastro = 'false'

# METODOS DE RECUPERAÇÃO DE SENHA ==============
email = 'abu@gmail.com'
sms = ''
pin = ''
codigoaleatorio = random.randint(1000 , 9999)

app_aberto = 'true'

#INICIO DO APP ==============
while app_aberto != 'false':
    
    escolhendo_conta = 'true'
    while escolhendo_conta != 'false':
        os.system('cls' if os.name == 'nt' else 'clear') #DESIGN ATUALIZADO  - 13 linhas
        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
        print('| Menu     -= BANCO DIGITAL =-         |')
        print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
        print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
        print('|                                      |')
        print('| [1] Login                            |')
        print('|                                      |')
        print('| [2] Cadastrar                        |')
        print('|                                      |')
        print('| [3] Visitante                        |')
        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
        escolher_conta = str(input('\n  -> Escolha:'))

        if escolher_conta == '1': # CONECTANDO A LOGIN =========== DESIGN ATUALIZADO - 13 linhas
            fazenologin_contalogin = 'true'
            while fazenologin_contalogin != 'false':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                print('|  Login   -= BANCO DIGITAL =-         |')
                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                print('|                                      |')
                print('|                                      |')
                print('| [ X ] Voltar ao menu                 |')
                print('|                                      |')
                print('| -Caso não possua uma conta volte e   |')
                print('|  faça seu cadastro gratuito.         |')
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                login_contanome = str(input('\n  -> Nome da conta:'))

                if login_contanome == 'X' or login_contanome == 'x':
                    break

                elif login_contanome != login_nome: #ERROU O NOME (LOGIN) - DESIGN ATUALIZADO - 13 Linhas
                    colocando_nomeloginerrado = 'true'
                    while colocando_nomeloginerrado != 'false':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                        print('|  Login   -= BANCO DIGITAL =-         |')
                        print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                        print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                        print('|                                      |')
                        print('| *Erro: Nome incorreto...             |')
                        print('|                                      |')
                        print('|                                      |')
                        print('| [1] Tentar Novamente                 |')
                        print('| [2] Voltar ao menu de contas         |')
                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                        voltar_nomeerradologin = str(input('\n  -> Escolha:'))
                        if voltar_nomeerradologin == '2':
                            colocando_nomeloginerrado = 'false'
                            fazenologin_contalogin = 'false'
                            colocando_nomelogincerto = 'false'
                            menuposlogin = 'false'
                            
                        elif voltar_nomeerradologin == '1':
                            colocando_nomeloginerrado = 'false'
                        
                        else:
                            invalido1 = 'true'
                            while invalido1 != 'false':
                                os.system('cls' if os.name == 'nt' else 'clear') #DESIGN ATUALIZADO - 13 Linhas
                                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                print('|  Login   -= BANCO DIGITAL =-         |')
                                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                print('|                                      |')
                                print('| *Erro: Inválido...                   |')
                                print('|                                      |')
                                print('|                                      |')
                                print('| [1] Tentar Novamente                 |')
                                print('| [2] Voltar ao menu de contas         |')
                                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                voltar_invalido1 = str(input('\n  -> Escolha:'))
                                if voltar_invalido1 == '1':
                                    invalido1 = 'false'
                                    colocando_nomeloginerrado = 'false'
                                elif voltar_invalido1 == '2':
                                    fazenologin_contalogin = 'false'
                                    colocando_nomeloginerrado = 'false'
                                    invalido1 = 'false'
                                    break


                elif login_contanome == login_nome: #ACERTOU O NOME (LOGIN) - DESIGN ATUALIZADO - 13 Linhas
                    colocando_nomelogincerto = 'true'
                    while colocando_nomelogincerto != 'false':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        esp = ' '
                        quantidadeletra = 30 - len(login_contanome)
                        espacosarrumados = esp * quantidadeletra
                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                        print('|  Login   -= BANCO DIGITAL =-         |')
                        print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                        print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                        print('|                                      |')
                        print('|                                      |')
                        print('| [ X ] Voltar ao menu de contas       |')
                        print('|                                      |')
                        print('|                                      |')
                        print('| -Nome: {}{}|'.format(login_contanome , espacosarrumados))
                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                        login_contasenha = str(input('\n  -> Senha da conta:'))

                        if login_contasenha == login_senha: #ACERTOU A SENHA
                            colocando_nomelogincerto = 'false'
                            fazenologin_contalogin = 'false'
                            escolhendo_conta = 'false'
                            status_login = 'true'
                        
                        elif login_contasenha == 'X' or login_contasenha == 'x':
                            fazenologin_contalogin = 'false'
                            break

                        elif login_contasenha != login_senha: #ERROU A SENHA - DESIGN ATUALIZADO - 13 linhas
                            senhalogin_errada = 'true'
                            while senhalogin_errada != 'false':
                                if loginerradotentativas == 0:
                                    for c in range(300 , 0 , -1):
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                        print('|  Login   -= BANCO DIGITAL =-         |')
                                        print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                        print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                        print('|                                      |')
                                        print('| Bloqueado por 5 minutos (300seg)     |')
                                        print('|                                      |')
                                        print('|                                      |')
                                        print('|                                      |')
                                        print('|                                      |')
                                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                        print('\n     -> Tempo Restante ({}seg) <-      '.format(c))
                                        time.sleep(1)
                                        loginerradotentativas = 3
                                
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                    print('|  Login   -= BANCO DIGITAL =-         |')
                                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                    print('|                                      |')
                                    print('| *Erro: Senha incorreta ({}/3)...      |'.format(loginerradotentativas))
                                    print('|                                      |')
                                    print('| [1] Tentar novamente                 |')
                                    print('| [2] Voltar ao menu de contas         |')
                                    print('| [3] Esqueci minha senha              |')
                                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                    voltar_senhaerradalogin = str(input('\n  -> Escolha:'))
                                    if voltar_senhaerradalogin == '1':
                                        senhalogin_errada = 'false'
                                        loginerradotentativas -= 1
                                    elif voltar_senhaerradalogin == '2':
                                        senhalogin_errada = 'false'
                                        colocando_nomelogincerto = 'false'
                                        fazenologin_contalogin = 'false'
                                        loginerradotentativas -= 1
                                    else:
                                        invalido2 = 'true'
                                        while invalido2 != 'false':
                                            loginerradotentativas -= 1
                                            os.system('cls' if os.name == 'nt' else 'clear') #DESIGN ATUALIZADO - 13 Linhas
                                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                            print('|  Login   -= BANCO DIGITAL =-         |')
                                            print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                            print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                            print('|                                      |')
                                            print('| *Erro: Inválido...                   |')
                                            print('|                                      |')
                                            print('|                                      |')
                                            print('| [1] Tentar Novamente                 |')
                                            print('| [2] Voltar ao menu de contas         |')
                                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                            voltar_invalido2 = str(input('\n  -> Escolha:'))
                                            if voltar_invalido2 == '1':
                                                break
                                                senhalogin_errada = 'false'
                                                break
                                            
                                            elif voltar_invalido2 == '2':
                                                invalido2 = 'false'
                                                senhalogin_errada = 'false'
                                                colocando_nomelogincerto = 'false'
                                                fazenologin_contalogin = 'false'
                                                break
                        else:
                            invalido2 = 'true'
                            while invalido2 != 'false': #DESIGN ATUALIZADO - 13 linhas
                                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                print('|  Login   -= BANCO DIGITAL =-         |')
                                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                print('|                                      |')
                                print('| *Erro: Apenas números...             |')
                                print('|                                      |')
                                print('|                                      |')
                                print('| [1] Tentar Novamente                 |')
                                print('| [2] Voltar ao menu de contas         |')
                                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                voltar_invalido2 = str(input('\n  -> Escolha:'))
                                if voltar_invalido2 == '1':
                                    invalido2 = 'false'
                                    colocando_nomelogincerto = 'false'
                                elif voltar_invalido2 == '2':
                                    invalido2 = 'false'
                                    colocando_nomelogincerto = 'false'
                                    break
                
            


            if status_login == 'true': # MENU PÓS-LOGIN (TESTADO E FUNCIONANDO)
                menuposlogin = 'true'
                while menuposlogin != 'false':
                    esp = ' '
                    esp2 = ' '
                    quantidadeletra = 30 - len(login_contanome)
                    espacosarrumados = esp * quantidadeletra
                    quantidadesenha = 29 - len(login_contasenha)
                    espacosarrumados2 = esp2 * quantidadesenha
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    print('|  Login   -= BANCO DIGITAL =-         |')
                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                    print('|                                      |')
                    print('|                                      |')
                    print('| -Nome: {}{}|'.format(login_contanome , espacosarrumados))
                    print('| -Senha: {}{}|'.format(login_contasenha , espacosarrumados2))
                    print('|                                      |')
                    print('|                                      |')
                    print('| Conectando...                        |')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    time.sleep(4.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    teste = str(input('Testando'))
        
# CADASTRO =================================

        elif escolher_conta == '2': # FAZENDO CADASTRO ========== DESIGN ATUALIZADO - 13 linhas
            fazenocadastro_contacadastro = 'true'
            while fazenocadastro_contacadastro != 'false':
                os.system('cls' if os.name == 'nt' else 'clear') #CADASTRO TELA 1 - DESIGN ATUALIZADO
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                print('| Cadastro -= BANCO DIGITAL =-         |')
                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                print('|                                      |')
                print('|                                      |')
                print('| -Digite [ X ] Para voltar ao menu    |')
                print('|                                      |')
                print('| -Escolha um nome que não esteja      |')
                print('|  cadastrado no banco.                |')
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                escolhernome = str(input('\n  -> Nome da conta (Letras):'))
                if escolhernome == login_nome: #CADASTRO -> CONTA JA EXISTE -  
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    print('| Cadastro -= BANCO DIGITAL =-         |')
                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                    print('|                                      |')
                    print('|                                      |')
                    print('| *Erro: Essa Conta ja existe          |')
                    print('|                                      |')
                    print('|                                      |')
                    print('|                                      |')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    escolhernomeigual = str(input('\n Tentar novamente? (y/n):'))
                    if escolhernomeigual == 'y' or escolhernomeigual == 'Y':
                        continue
                    elif escolhernomeigual == 'n' or escolhernomeigual == 'N':
                        break
                    else:
                        invalido3 = 'true'
                        while invalido3 != 'false': #DESIGN ATUALIZADO - 13 linhas
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                            print('|  Login   -= BANCO DIGITAL =-         |')
                            print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                            print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                            print('|                                      |')
                            print('| *Erro: Inválido...                   |')
                            print('|                                      |')
                            print('|                                      |')
                            print('| [1] Tentar Novamente                 |')
                            print('| [2] Voltar ao menu de contas         |')
                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                            voltar_invalido3 = str(input('\n  -> Escolha:'))
                            if voltar_invalido3 == '1':
                                invalido3 = 'false'
                                break
                            elif voltar_invalido3 == '2':
                                invalido3 = 'false'
                                fazenocadastro_contacadastro = 'false'
                                break
                elif escolhernome == 'X' or escolhernome == 'x': # USUÁRIO QUERER VOLTAR TELA 1
                    break
                os.system('cls' if os.name == 'nt' else 'clear') #CADASTRO - DESIGN ATUALIZADO - 13 linhas
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                print('| Cadastro -= BANCO DIGITAL =-         |')
                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                print('|                                      |')
                print('|                                      |')
                print('| -Digite [ X ] Para voltar ao menu    |')
                print('|                                      |')
                print('| -Escolha uma senha forte, Use Apenas |')
                print('|  4 Números.                          |')
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                escolhersenha = str(input('\n  -> Senha da conta (0000):'))
                tamanhodasenha = int(escolhersenha)
                if tamanhodasenha > 9999:
                    print('\n --> Máximo de números: 4 <--')
                    time.sleep(3.0)
                    break

                esp = ' '
                esp2 = ' '
                quantidadeletra = 30 - len(escolhernome)
                espacosarrumados = esp * quantidadeletra
                quantidadesenha = 29 - len(escolhersenha)
                espacosarrumados2 = esp2 * quantidadesenha
                os.system('cls' if os.name == 'nt' else 'clear') # NOME E SENHA CORRETOS
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                print('| Cadastro -= BANCO DIGITAL =-         |')
                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                print('|                                      |')
                print('|                                      |')
                print('| -Nome: {}{}|'.format(escolhernome , espacosarrumados))
                print('| -Senha: {}{}|'.format(escolhersenha , espacosarrumados2))
                print('|                                      |')
                print('| -Próximo passo: Recuperação          |')
                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                continuar = str(input('\n  -> Pressione Enter para Prosseguir:'))
                incluirrecuperacao = 'true'

                while incluirrecuperacao != 'false': # ADICIONANDO MÉTODO DE RECUPERAÇÃO
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    print('| Cadastro -= BANCO DIGITAL =-         |')
                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                    print('|                                      |')
                    print('| [1] E-Mail                           |')
                    print('| [2] PIN (Altamente Recomendado)      |')
                    print('|                                      |')
                    print('| [ X ] Cancelar                       |')
                    print('|                                      |')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    escolherrecuperacao = str(input('\n  -> Escolha:'))

                    if escolherrecuperacao == '1':# MÉTODO EMAIL (TESTADO E FINALIZADO)
                        adicionandoemail = 'true'
                        while adicionandoemail != 'false':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                            print('| Cadastro -= BANCO DIGITAL =-         |')
                            print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                            print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                            print('|                                      |')
                            print('|                                      |')
                            print('| -Adicione seu E-Mail                 |')
                            print('|                                      |')
                            print('| Digite [ Q ] Para voltar             |')
                            print('| Digite [ X ] para voltar ao menu     |')
                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                            adicionaremail = str(input('\n  -> Introduzir E-mail:'))

                            if adicionaremail == email: #E-MAIL EM USO (TESTADO E FINALIZADO)
                                emailemuso = 'true'
                                while emailemuso != 'false':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                    print('| Cadastro -= BANCO DIGITAL =-         |')
                                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                    print('|                                      |')
                                    print('|                                      |')
                                    print('| *Erro: E-Mail em uso.                |')
                                    print('|                                      |')
                                    print('| Digite [ Q ] para tentar novamente   |')
                                    print('| Digite [ X ] para voltar ao menu     |')
                                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                    voltar_emailemuso = str(input('\n  -> Escolha:'))

                                    if voltar_emailemuso == 'Q' or voltar_emailemuso == 'q': # VOLTAR (TESTADO E FINALIZADO)
                                        emailemuso = 'false'

                                    elif voltar_emailemuso == 'X' or voltar_emailemuso == 'x': # VOLTAR AO MENU (TESTADO E FINALIZADO)
                                        fazenocadastro_contacadastro = 'false'
                                        adicionandoemail = 'false'
                                        incluirrecuperacao = 'false'
                                        break

                                    else: # INVALIDO NA TELA DE EMAIL EM USO (TESTADO E FINALIZADO)
                                        invalido_emailemuso = 'true'
                                        while invalido_emailemuso != 'false':
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                            print('| Cadastro -= BANCO DIGITAL =-         |')
                                            print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                            print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                            print('|                                      |')
                                            print('|                                      |')
                                            print('| *Erro: Inválido...                   |')
                                            print('|                                      |')
                                            print('| Digite [ Q ] para tentar novamente   |')
                                            print('| Digite [ X ] para voltar ao menu     |')
                                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                            voltarinvalidoemailemuso = str(input('\n  -> Escolha:'))
                                        
                                            if voltarinvalidoemailemuso == 'Q' or voltarinvalidoemailemuso == 'q': #VOLTAR (TESTADO E FINALIZADO)
                                                invalido_emailemuso = 'false'
                                                emailemuso = 'false'
                                            
                                            elif voltarinvalidoemailemuso == 'X' or voltarinvalidoemailemuso == 'x': #VOLTAR AO MENU (TESTADO E FINALIZADO)
                                                invalido_emailemuso = 'false'
                                                emailemuso = 'false'
                                                adicionandoemail = 'false'
                                                incluirrecuperacao = 'false'
                                                fazenocadastro_contacadastro = 'false'

                            elif adicionaremail == 'X' or adicionaremail == 'x': # VOLTAR (TESTADO E FINALIZADO)
                                incluirrecuperacao = 'false'
                                adicionandoemail = 'false'
                                fazenocadastro_contacadastro = 'false'
                            
                            elif adicionaremail == 'Q' or adicionaremail == 'q': # VOLTAR AO MENU (TESTADO E FINALIZADO)
                                adicionandoemail = 'false'
                            
                            elif adicionaremail == '' or adicionaremail == ' ': #EMAIL INVALIDO (TESTADO E FINALIZADO)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                print('| Cadastro -= BANCO DIGITAL =-         |')
                                print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                print('|                                      |')
                                print('| *Erro: Inválido...                   |')
                                print('|                                      |')
                                print('|                                      |')
                                print('| -Digite um E-mail Válido             |')
                                print('|                                      |')
                                print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                time.sleep(3.5)


                            else: #EMAIL CADASTRADO E VALIDO (TESTADO E FINALIZADO)
                                email = adicionaremail
                                status_cadastro = 'true'
                                adicionandoemail = 'false'
                                incluirrecuperacao = 'false'
                    
                    elif escolherrecuperacao == '2': # MÉTODO PIN (TESTADO E FINALIZADO)
                        adicionandopin = 'true'
                        while adicionandopin != 'false':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                            print('| Cadastro -= BANCO DIGITAL =-         |')
                            print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                            print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                            print('|                                      |')
                            print('| -Escolha seu PIN (4 Digitos)         |')
                            print('| -Guarde seu PIN Para quando precisar |')
                            print('|  Recuperar a senha.                  |')
                            print('|                                      |')
                            print('| Digite [ 0 ] para voltar             |')
                            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                            escolherpin = int(input('\n  -> Digite o PIN:'))

                            if escolherpin > 9999: #LIMITE EXCEDIDO (TESTADO E FINALIZADO)
                                limitedopin = 'true'
                                while limitedopin != 'false':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                    print('|  Login   -= BANCO DIGITAL =-         |')
                                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                                    print('|                                      |')
                                    print('| *Erro: Limite de 4 Digitos...        |')
                                    print('|                                      |')
                                    print('|                                      |')
                                    print('| [1] Tentar Novamente                 |')
                                    print('| [2] Voltar                           |')
                                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                                    maisque4digitos = str(input('\n  -> Escolha:'))
                                    if maisque4digitos == '1':
                                        limitedopin = 'false'
                                    elif maisque4digitos == '2':
                                        adicionandopin = 'false'
                                        limitedopin = 'false'

                            elif escolherpin == 0: #VOLTAR (TESTADO DE FINALIZADO)
                                break
                            
                            elif escolherpin <= 9999 and escolherpin >= 0000: #PIN VÁLIDO (TESTADO E FINALIZADO)
                                status_cadastro = 'true'
                                pin = escolherpin
                                adicionandopin = 'false'
                                incluirrecuperacao = 'false'

                    elif escolherrecuperacao == 'X' or escolherrecuperacao == 'x': #CANCELAR (TESTADO E FINALIZADO)
                        incluirrecuperacao = 'false'
                        fazenocadastro_contacadastro = 'false'

                if status_cadastro == 'true': # EFETUANDO A CADASTRAÇÃO (TESTADO E FINALIZADO)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    print('| Cadastro -= BANCO DIGITAL =-         |')
                    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                    print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                    print('|                                      |')
                    print('|                                      |')
                    print('| Cadastrando...                       |')
                    print('| Aguarde...                           |')
                    print('|                                      |')
                    print('|                                      |')
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                    login_nome = escolhernome
                    login_senha = escolhersenha
                    time.sleep(3.0)
                    cadastropronto = 'true'

                    while cadastropronto != 'false': #CADASTRO EFETUADO (TESTADO E FINALIZADO)
                        os.system('cls' if os.name == 'nt' else 'clear') 
                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                        print('| Cadastro -= BANCO DIGITAL =-         |')
                        print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
                        print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
                        print('|                                      |')
                        print('|                                      |')
                        print('| -Cadastro efetuado com sucesso!      |')
                        print('|                                      |')
                        print('| -Você ja pode se conectar agora.     |')
                        print('|                                      |')
                        print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
                        voltarcadastro = str(input('\n  -> Pressione X para voltar ao menu:'))

                        if voltarcadastro == 'X' or voltarcadastro == 'x': #VOLTAR AO MENU (TESTADO E FINALIZADO)
                            cadastropronto = 'false'
                            fazenocadastro_contacadastro = 'false'

# PARTE DO MENU ============================

        else: #INVÁLIDO CASO O USUÁRIO NÃO DIGITE ALGUMA DAS 3 OPÇÕES ( TESTADO E FINALIZADO )
            os.system('cls' if os.name == 'nt' else 'clear')
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
            print('|          -= BANCO DIGITAL =-         |')
            print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
            print('| v1.2 | Sérgio Lima (14 Anos) - 2026  |')
            print('|                                      |')
            print('| *Erro: Inválido...                   |')
            print('|                                      |')
            print('|                                      |')
            print('| -Recarregando                        |')
            print('|                                      |')
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|')
            time.sleep(4.0)