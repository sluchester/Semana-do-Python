
#Para tirar dúvidas: (21) 96721-8715

# Passo a passo do Projeto:

# 1. Abrir o sistema da empresa (nesse caso, abrir um site)
    # abrir o navegador
    # entrar no site
    # Objetivo: automatizar mouse e teclado

import time
# terminal: pip install pyautogui
import pyautogui

# fazer uma pausa, em segundos, entre um segundo e outro
pyautogui.PAUSE = 1
# pesquisar no google: pyautogui documentation
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas

# abrir o navegador
pyautogui.press("win")
time.sleep(2)
pyautogui.write("brave")
pyautogui.press("enter")

time.sleep(5)

# entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(5)
pyautogui.press("enter")
# pode ser que demore alguns segundos até abrir o código -> biblioteca time
# time.sleep(5) => na linha, e num lugar específico

time.sleep(5)

# 2. Fazer login
pyautogui.click(x=484, y=371)
pyautogui.write("teste@mail.com")
# passa para o próximo campo
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

# 3. Abrir/importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl - para ler base de dados csv
import pandas as pd
# dando apelido para escrever menos (convenção usada mundialmente)
# tabula transforma pdfs em pandas

# armazenando as informações da base de dados
tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar um produto

# pyautogui.scroll(200) # se for negativo, vai para baixo

# 5. Repetir isso tudo até acabar a lista de produtos
for linha in tabela.index:
    # cadastra tudo até o final
    codigo = tabela.loc[linha, "codigo"]
    # clicar no campo do código do produto
    pyautogui.click(x=457, y=249)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # str porque algumas informacoes, como numero, vai dar erro ao escrever
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(2000)      
    