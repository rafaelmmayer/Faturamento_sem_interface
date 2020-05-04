import pandas as pd
import xlsxwriter
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Produtos:
    def __init__(self, tipo, nome, preco):
        self.tipo = tipo
        self.nome = nome
        self.preco = preco

def ftr_total():
    ftr_total = df['Valor'].sum()
    print("Faturamento do dia: ", ftr_total)
    return ftr_total

def gerar_excel():
    df.to_excel('FATURAMENTO.xlsx',  sheet_name='Faturamento do dia')

def mandarEmail():
    try:
        fromaddr = "mayer.rafa@outlook.com"
        toaddr = 'tania.mayer@uol.com.br'
        msg = MIMEMultipart()

        msg['From'] = fromaddr 
        msg['To'] = toaddr
        msg['Subject'] = "Faturamento"

        body = "\nSegue em anexo o Faturamento do dia"

        msg.attach(MIMEText(body, 'plain'))

        filename = 'FATURAMENTO.xlsx'

        attachment = open('FATURAMENTO.xlsx','rb')


        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.starttls()
        server.login(fromaddr, "mostermago09")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('\nEmail enviado com sucesso!')
    except:
        print("\nErro ao enviar email")

def criar_produtos():
    produtos.append( Produtos("Café", "Expresso", 4.9) )
    produtos.append( Produtos("Café", "Café com leite Médio", 5.7) )
    produtos.append( Produtos("Café", "Café com Chantilly", 8) )
    produtos.append( Produtos("Café", "Café Duplo", 8.5) )
    produtos.append( Produtos("Café", "Café com Cointreau", 8.5) )
    produtos.append( Produtos("Café", "Café Italiano", 8.5) )
    produtos.append( Produtos("Café", "Cappuccino pequeno", 5.5) )
    produtos.append( Produtos("Café", "Cappuccino grande", 8) )
    produtos.append( Produtos("Café", "Cappuccino Gelado", 14.5) )
    produtos.append( Produtos("Café", "Latte Macchiatto", 7) )
    produtos.append( Produtos("Café", "Chai Latte", 9.5) )
    produtos.append( Produtos("Café", "Café Vienense", 19.3) )
    produtos.append( Produtos("Bebidas", "Refrigerante Garrafa (290ml)", 4.5) ) 
    produtos.append( Produtos("Bebidas", "Refrigerante Lata (350ml)", 5) )  
    produtos.append( Produtos("Bebidas", "Refrigerante Caçulinha (200ml)", 3) )
    produtos.append( Produtos("Bebidas", "Água de coco (copo)", 6.5) )
    produtos.append( Produtos("Bebidas", "Água Garrafa (310ml)", 3.9) )
    produtos.append( Produtos("Bebidas", "Schweppes", 5) )
    produtos.append( Produtos("Bebidas", "Sucos", 8) )
    produtos.append( Produtos("Bebidas", "Misto (duas frutas)", 10) )
    produtos.append( Produtos("Bebidas", "Misto (três frutas)", 13) )
    produtos.append( Produtos("Bebidas", "Vitamina com Laranja ou Leite", 10) )
    produtos.append( Produtos("Bebidas", "Limonada Suíça", 13) )
    produtos.append( Produtos("Bebidas", "Chás", 5) )
    produtos.append( Produtos("Lanche", "Americano com queijo muçarela", 13.9) )
    produtos.append( Produtos("Lanche", "Americano com queijo branco", 16.9) )
    produtos.append( Produtos("Lanche", "Bauru Salada com queijo muçarela", 12.8) )
    produtos.append( Produtos("Lanche", "Bauru Salada com queijo branco", 15.8) )
    produtos.append( Produtos("Lanche", "Bauru com queijo muçarela", 11.8) )
    produtos.append( Produtos("Lanche", "Bauru com queijo branco", 14.8) )
    produtos.append( Produtos("Lanche", "Queijo frio com queijo muçarela", 7) )
    produtos.append( Produtos("Lanche", "Queijo frio com queijo branco", 10) )
    produtos.append( Produtos("Lanche", "Queijo quente com queijo muçarela", 8) )
    produtos.append( Produtos("Lanche", "Queijo quente com queijo branco", 11) )
    produtos.append( Produtos("Lanche", "Misto quente com queijo muçarela", 10.3) )
    produtos.append( Produtos("Lanche", "Misto quente com queijo branco", 13.3) )
    produtos.append( Produtos("Lanche", "Misto frio com queijo muçarela", 9.3) )
    produtos.append( Produtos("Lanche", "Misto frio com queijo branco", 12.3) )
    produtos.append( Produtos("Lanche", "Pão quente com manteiga", 3) )
    produtos.append( Produtos("Lanche", "Pão quente com catupity", 5.7) )
    produtos.append( Produtos("Lanche", "Lanche natural de frango", 15) )
    produtos.append( Produtos("Lanche", "Lanche natural de peito de peru", 15) )
    produtos.append( Produtos("Lanche", "Frango 1", 16.6) )
    produtos.append( Produtos("Lanche", "Frango 2", 23.6) )
    produtos.append( Produtos("Lanche", "Mignon 1", 19.6) )
    produtos.append( Produtos("Lanche", "Mignon 2", 26.6) )
    produtos.append( Produtos("Lanche", "X-Burguer", 13.7) )
    produtos.append( Produtos("Lanche", "X-Salada", 15.7) )
    produtos.append( Produtos("Lanche", "X-Egg", 18.4) )
    produtos.append( Produtos("Lanche", "X-Bacon", 21.9) )
    produtos.append( Produtos("Lanche", "X-Tudo", 23.4) )
    produtos.append( Produtos("Beirute", "Beirute Light", 23) )
    produtos.append( Produtos("Beirute", "Beirute Frango", 28.4) )
    produtos.append( Produtos("Beirute", "Beirute Frango Especial", 37.4) )
    produtos.append( Produtos("Beirute", "Beirute Mignon", 43.2) )
    produtos.append( Produtos("Beirute", "Beirute Mignon Especial", 49.2) )
    produtos.append( Produtos("Beirute", "Beirute Americano", 25.6) )
    produtos.append( Produtos("Refeição", "Salada Mista com grelhado de Frango", 15.5) )
    produtos.append( Produtos("Refeição", "Salada Mista com grelhado de File Mignon", 21) )
    produtos.append( Produtos("Refeição", "Strogonoff de Frango", 20) )
    produtos.append( Produtos("Refeição", "Strogonoff de Carne", 28) )
    produtos.append( Produtos("Massas", "Agnolotti de Molho Rose", 27) )
    produtos.append( Produtos("Massas", "Fettuccine", 24) )
    produtos.append( Produtos("Massas", "Lasanha", 24) )
    produtos.append( Produtos("Massas", "Lasanha Verde ao Molho de Champignon", 27) )
    produtos.append( Produtos("Massas", "Manicaretti Caprese", 24) )
    produtos.append( Produtos("Massas", "Manicaretti Integral", 27) )
    produtos.append( Produtos("Massas", "Nhoque", 24) )
    produtos.append( Produtos("Massas", "Nhoque ao Molho Branco", 24) )
    produtos.append( Produtos("Massas", "Penne", 24) )
    produtos.append( Produtos("Massas", "Raviole ao Molho branco", 27) )
    produtos.append( Produtos("Tapioca", "Tapioca 1", 13) )
    produtos.append( Produtos("Tapioca", "Tapioca 2", 15) )
    produtos.append( Produtos("Tapioca", "Tapioca 3", 15) )
    produtos.append( Produtos("Tapioca", "Tapioca 4", 15) )
    produtos.append( Produtos("Tapioca", "Tapioca 5", 15) )
    produtos.append( Produtos("Salgado", "Salgado Simples", 5) )
    produtos.append( Produtos("Salgado", "Salgado Normal", 6.5) )
    produtos.append( Produtos("Salgado", "Salgado Especial", 7) )
    produtos.append( Produtos("Salgado", "Pão de queijo Pequeno", 2) )
    produtos.append( Produtos("Salgado", "Pão de queijo Grande", 4) )
    produtos.append( Produtos("Bolo", "Bolo de cenoura", 7) )
    produtos.append( Produtos("Bolo", "Bolo Recheado", 11) )
    produtos.append( Produtos("Bolo", "Bolo Inteiro", 115) )
    produtos.append( Produtos("Bebidas", "Suco Detox", 11) )
    produtos.append( Produtos("Refeição", "Omelete", 15) )
    produtos.append( Produtos("Doce", "Sonho de Valsa", 2) )
    produtos.append( Produtos("Doce", "Strogoff de chocolate", 9) )
    produtos.append( Produtos("Bebidas", "Refrigerante 600ml", 6) )
    produtos.append( Produtos("Doce", "Tic-Tac", 3) )
    produtos.append( Produtos("Doce", "Trident", 3) )
    produtos.append( Produtos("Doce", "Dadinho", 0.2) )
    produtos.append( Produtos("Doce", "Bala", 0.1) )

produtos = []

lista_nome = []
lista_preco = []
lista_tipo = []
lista_qtd = []
lista_valor = []

criar_produtos()

for produto in produtos:
    lista_nome.append(produto.nome)
    lista_preco.append(produto.preco)
    lista_tipo.append(produto.tipo)
    lista_qtd.append(0)
    lista_valor.append(0)

df = pd.DataFrame({'Produto': lista_nome, 'Preço': lista_preco, 'Tipo': lista_tipo, 'Quantidade': lista_qtd, 'Valor': lista_valor})

c = 0
while (c!= 999):

    teste = False
    while (teste == False):
        try:
            c = int(input("Digite o código "))
            teste = True
        except ValueError:
            print("Digite um número")
            teste = False

    if (c == 1234):
        ftr_total()
    elif (c == 4567):
        gerar_excel()
    elif (c == 999):
        gerar_excel()
        # mandarEmail()
        
    else:

        compra = 0
        teste_compra = 0
        test = 0
        controle = 0
        while(teste_compra == 0):
            
            if(controle != 0):
                print(f"Valor da compra parcial: {compra}")
                teste = False
                while (teste == False):
                    try:
                        c = int(input("Digite o código "))
                        teste = True
                    except ValueError:
                        print("Digite um número")
                        teste = False
            controle = controle + 1

            teste = False
            while (teste == False):
                try:
                    q = int(input(f'Quantos {lista_nome[c]}? '))
                    teste = True
                except ValueError:
                    print("Digite um número")
                    teste = False

            confirma = input(f"{q} {lista_nome[c]} Confirma? ")

            if (confirma != ''):
                while (confirma != ''):
                    teste = False
                    while (teste == False):
                        try:
                            c = int(input("Digite o código "))
                            teste = True
                        except ValueError:
                            print("Digite um número")
                            teste = False
                    
                    teste = False
                    while (teste == False):
                        try:
                            q = int(input(f'Quantos {lista_nome[c]}? '))
                            teste = True
                        except ValueError:
                            print("Digite um número")
                            teste = False
                    
                    
                    confirma = input(f"{q} {lista_nome[c]} Confirma? ")

            lista_qtd[c] = lista_qtd[c] + q
            lista_valor[c] = lista_preco[c] * lista_qtd[c]
            compra = lista_preco[c]*q + compra
            df = pd.DataFrame({'Produto': lista_nome, 'Preço': lista_preco, 'Tipo': lista_tipo, 'Quantidade': lista_qtd, 'Valor': lista_valor})
            print(f"Valor da compra parcial: {compra}")
        
            if (input("Continuar a compra ") != ''):
                teste_compra += 1


            os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Valor da compra: {compra}")
        gerar_excel()








        
