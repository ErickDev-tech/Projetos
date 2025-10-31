import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.novaliderinformatica.com.br/hardware")


titulos = driver.find_elements(By.XPATH,"//div[@class='product-name']")

precos = driver.find_elements(By.XPATH,"//span[@class='price-off']")

planilha = openpyxl.Workbook()
planilha.create_sheet('Produtos')
pagina_de_produtos = planilha['Produtos']

pagina_de_produtos['A1'].value = 'Produto'
pagina_de_produtos['B1'].value = 'Preço'
planilha.save('produtos.xlsx')

for titulo, preco in zip(titulos,precos):
    pagina_de_produtos.append([titulo.text,preco.text])

planilha.save('produtos.xlsx')
sleep(1)
driver.close()

