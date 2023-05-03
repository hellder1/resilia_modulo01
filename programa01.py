#!/usr/bin/env python
# coding: utf-8

# ## Step 01

# In[ ]:


def prints_tela_inicial():
    print("Bem vindo ao sistema abcd")
    print("\nSelecione uma opção para atendimento:")
    print("\n1 - Contratar plano")
    print("2 - Assistência técnica")
    print("3 - Financeiro")
    print("4 - Assinatura de contrato")
    print("5 - Encerra atendimento")
    entrada_inicial=int(input("Selecione uma opção: "))
    return entrada_inicial


# ## Step 02

# In[ ]:


def main():
    
    # printa as opções da primeira tela
    #prints_tela_inicial()
    # armazena a escolha uma variável
    entrada_inicial = prints_tela_inicial()
    
    #print("teste")
    if entrada_inicial == 5:
        print("Obrigado e volte sempre!")
    else:
        pass
    
    user_option=0
    while user_option != 5:
        # Contratar plano
        if entrada_inicial == 1:
            print("Selecione uma das opções disponíveis abaixo")
            print("\n*PLANO 1* 10Gb / mês por R$:49,99")
            print("***PLANO 2*** 50Gb / mês por R$:69,99")
            print("\n4 - Para retornar ao menu inicial")
            print("5 - Para encerrar atendimento")
            user_option = int(input("Digite uma opção: "))
            
            # Finaliza contratação
            if user_option == 1 or user_option == 2:
                print("Plano contratado com sucesso!!!")
                print("\n Deixe seu whats para que possamos agendar a instalação e forma de pagamento")
                whats_user=int(input("Digite seu número com ddd:"))
                print("Estamos felizes por escolher o serviço de internet que ajuda a mudar o mundo :)")
                break
            # chama a função principal e reinicia o ciclo
            elif user_option == 4:
                main()
                
        # Assistência técnica
        elif entrada_inicial == 2:
            print("Selecione uma das opções abaixo")
            print("\n1 - Oscilação de internet")
            print("2 - Falar com um atendente")
            print("3 - Voltar ao menu principal")
            print("4 - Encerrar atendimento")
            user_option = int(input("Digite uma opção: "))
            
            if user_option == 1 or user_option == 2:
                print("Encaminhando para o próximo atendente disponível")
                print("Deixe seu número, entraremos em contato com urgência!")
                whats_user=int(input("Número do whats com ddd:"))
            
             # chama a função principal e reinicia o ciclo
            elif user_option == 3:
                main()
            # Encerra o while mudando a condição de 5 para 4
            elif user_option == 4:
                print("Obrigado e volte sempre!")
                break
        # Financeiro
        elif entrada_inicial == 3:
            print("Selecione uma das opções disponíveis abaixo")
            print("1 - Segunda via de conta")
            print("2 - Falar com atendente")
            print("4 - Para retornar ao menu inicial")
            print("5 - Encerrar atendimento")
            user_option = int(input("Digite uma opção: "))
            
            if user_option == 1:
                email_user=str(input("Digite seu email para recebimento: "))
                print("Aguarde 30 minutos, agradecemos o contato.")
                break
            elif user_option == 2:
                print("Encaminhando para o próximo atendente disponível")
                print("Deixe seu número, entraremos em contato com urgência!")
                whats_user=int(input("Número whats com ddd:"))
                
        # Assinatura de contrato        
        elif entrada_inicial == 4:
            email_user=str(input("Digite seu email para envio na copia assianda"))
            assinatura=str(input("digite seu nome completo com a frase de segurança enviada por email para assinatura digital"))
            print("Aguarde 30 minutos, confirmação por email, agradecemos o contato.")
            break
        else:
            print("Agradecemos o contato.")
            break
            


# ## Step 03

# In[ ]:


# chama a função principal
main()


# In[ ]:





# In[ ]:





# In[ ]:




