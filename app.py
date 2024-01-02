# acredito que já esteja em python

# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import threading

# inicianilza o navegador
driver = webdriver.Chrome()

# define o url a ser ascessado
driver.get('https://www.cobasi.com.br/pesquisa?terms=peixe')

# obtendo lista de nomes dos produtos de aquário
produtos = driver.find_elements(By.XPATH, "//div[@class='MediaMatch-sc-8d15xu-0 kBZFEW']/h3[@class='styles__Title-sc-1ac06td-4 dPsqyZ']")

# obtendo lista de preço dos produtos de aquário
precos = driver.find_elements(By.XPATH, "//div[@class='styles__PriceBox-sc-1ac06td-6 bMeYMI']//span[@class='card-price']")

# obtendo lista de preços por compra programada
compras = driver.find_elements(By.XPATH, "//div[@class='styles__SubscriptionPrice-sc-1ac06td-10 ctrFNt']//span[@class='card-price']")

# cria arquivo no excel 
workbook = openpyxl.Workbook()

# cria planilha de produtos
workbook.create_sheet('Produtos')

# atribui a planilha de produtos a um objeto
sheet_produtos = workbook['Produtos']

# atribuindo nomes aos campos
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'
sheet_produtos['C1'].value = 'Preço com desconto (compra programada)'

# atribuindo o conteúdo das listas à planilha
for produto, preco, compra in zip(produtos, precos, compras):
    sheet_produtos.append([produto.text, preco.text, compra.text])

# salvando a planilha
workbook.save('Produtos de aquário.xlsx')