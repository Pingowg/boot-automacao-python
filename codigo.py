from numpy import nan
import pyautogui  
import time


pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link) 
pyautogui.press("enter") 
time.sleep(3) 


pyautogui.click(x=685, y=469)
pyautogui.write("pingo.png@hotmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

import pandas 

tabela = pandas.read_csv("produtos.csv") 

for linha in tabela.index:

    pyautogui.click(x=723, y=317)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo) # Codigo do Produto
    pyautogui.press("tab")
    
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca) # Marca do Produto
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo) # Tipo do Produto 
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria) # Categoria do Produto
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario) # Preço Unitario do Produto 
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo) # Custo do Produto  
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) # Observações do Produto 
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)


