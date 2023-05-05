# Chatbot Conect AI, Atendimento automatizado para provedores de internet.

def prints_tela_inicial(): #Funcao recebe prints_tela_inicial 
     #printar todas as mensagem abaixo para o usuario
    print("Bem vindo ao sistema Connect AI") #Imprima a mensagem
    print("\nSelecione uma opção para atendimento:") # "  "
    print("\n1 - Contratar plano") # "  "
    print("2 - Assistência técnica") # "  "
    print("3 - Financeiro") # "  "
    print("4 - Assinatura de contrato") # "  "
    print("5 - Encerra atendimento") # "  "
    entrada_inicial=int(input("\nSelecione uma opção: ")) #Entrada incial recebe numero inteiro digitado pelo usuario
    return entrada_inicial #Armazena (Captura) entrada_inicial dado pelo usuario

def main(): #Funcao recebe main(menu)
    
    # printa as opções da primeira tela
    # prints_tela_inicial()
    # armazena a escolha uma variável
    entrada_inicial = prints_tela_inicial() #Entrada recebe prints da tela inicial
    
    #print("teste")
    if entrada_inicial == 5: #Se entrada_inicial for igual a 5 
        print("Obrigado e volte sempre!") #imprima a mensagem 
    else: #Senão
        pass #Passa para outra opção abaixo
         
    user_option=0 #User option recebe 0 para atribuir valor a variavel
    while user_option != 4: #Enquanto user_option for diferente de 4 dê as seguintes opcoes abaixo

        # 1 - Contratar plano
        if entrada_inicial == 1: #Se a entrada_inicial for igual a 1
            
            print("Selecione uma das opções disponíveis abaixo:") #imprima a mensagem 
            print("\n1- Plano 1 10Gb | por R$ 49,99 ao mês") # "  "
            print("2- Plano 2 50Gb | por R$ 69,99 ao mês") # "  "
            print("3- Para retornar ao menu inicial") # "  "
            print("4- Para encerrar atendimento") # "  "
            user_option = int(input("\nDigite a opção desejavel: ")) #User_option recebe numero inteiro, de acordo com a opção dada pelo usuario
            
            # Finaliza contratação
            if user_option == 1 or user_option == 2: #Se user_option for igual a 1 ou user_option for igual a 2
                print("\nPlano contratado com sucesso!!!") #Imprima a mensagem
                print("\nDeixe seu whats para que possamos agendar a instalação e forma de pagamento.") # "  "
                whats_user=int(input("\nDigite seu número com ddd: "))  #whats_user recebe numeros inteiros digitado pelo usuario
                print("\nEstamos felizes por ter você como nosso cliente, seja bem-vindo.") #Imprima a mensagem
                break #Interrompe a função

            # chama a função principal e reinicia o ciclo
            elif user_option == 3: #Se user_option for igual a 4
                main()  # retorne a funcao main(menu)
            
        # 2 - Assistência técnica
        elif entrada_inicial == 2:  #Se a entrada_inicial for igual 2 
            print("Selecione uma das opções abaixo")  #Imprima a mensagem
            print("\n1 - Oscilação de internet")  # "  "
            print("2 - Falar com um atendente")  # "  "
            print("3 - Voltar ao menu principal")  # "  "
            print("4 - Encerrar atendimento")  # "  "
            user_option = int(input("Digite uma opção: ")) #User_option recebe numero inteiro da opcao acima digitado pelo usuario
            
            if user_option == 1 or user_option == 2: #Se o user_option for igual a 1 ou user_option for igual a 2 
                print("Encaminhando para o próximo atendente disponível") #Imprima a mensagem
                print("Deixe seu número, entraremos em contato com urgência!")  # "  "
                whats_user=int(input("Número do whats com ddd:")) #Whats_user recebe numeros inteiros digitado pelo usuario
                print("Obrigado, Connect AI agradece seu contato, logo entraremos em contato") #Imprima a mensagem
                break #Interrompe a função
            
            elif user_option == 3: #Se  o user_option for igual a 3
                main()  # chama a função principal e reinicia o ciclo
            # Encerra o while mudando a condição de 5 para 4
            elif user_option == 4: #Se o user_option for igual a 4;
                print("Obrigado e volte sempre!") #Imrpima a mensagem
                break  #Interrompe a função

        # 3 - Financeiro
        elif entrada_inicial == 3:  #Se a entrada_inicial for igual a 3;
            print("Selecione uma das opções disponíveis abaixo") #Imprima a mensagem
            print("1 - Segunda via de conta") # " "
            print("2 - Falar com atendente") # " "
            print("4 - Para retornar ao menu inicial") # " "
            print("5 - Encerrar atendimento") # " "
            user_option = int(input("Digite uma opção: ")) #user_oprtion recebe numeros inteiros digitado pelo usuario
            
            if user_option == 1: #Se user_option for igual a 1
                email_user=str(input("Digite seu email para recebimento: ")) #email recebe string (mensagem) dado pelo usuario. 
                print("Aguarde 30 minutos, agradecemos o contato.") #Imprima a mensagem
                break #Interrompe a função

            elif user_option == 2: #Se o user_option for igual a 2
                print("Encaminhando para o próximo atendente disponível")  #imprima a mensagem
                print("Deixe seu número, entraremos em contato com urgência!") # "  "
                whats_user=int(input("Número whats com ddd:")) #Whats_user recebe numero inteiros digitado pelo usuario
                #print (mensagem de encerramento)
                #falta um break
                 
        # Assinatura de contrato        
        elif entrada_inicial == 4: #Se a entrada_inicial for igual a 4;
            email_user=str(input("Digite seu email para envio na copia assinada")) #Recebe dados do usuario em string(mensagem)
            assinatura=str(input("digite seu nome completo com a frase de segurança enviada por email para assinatura digital")) # "  "
            print("Aguarde 30 minutos, confirmação por email, agradecemos o contato.") #Imprima a mensagem
            break #Interrompe a função

        else: #Senão
            print("Agradecemos o contato.") # Imprima a mensagem
            break #Interrompe a função
# chama a função principal
main()