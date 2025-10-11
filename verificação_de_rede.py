from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime
from fpdf import FPDF


#*Bot de verificação de rede*

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=1000,1000',
                '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,  # Desabilita notificações
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = iniciar_driver()

#1-- entrar no site (https://www.speedtest.net/pt/result/18284608214)
driver.get("https://www.speedtest.net/pt/result/18284608214")

#2 --clicar no botão iniciar
botão_iniciar = driver.find_element(By.CLASS_NAME,"start-text")
botão_iniciar.click()

sleep(60)

#3 -- pegar as informações(download, Upload , ping , id , servidor ,operadora, data e hora do teste)
#5 -- guarda as informações
download_upload = driver.find_elements(
    By.CSS_SELECTOR, ".result-data-large.number.result-data-value"
)

download = download_upload[0].text
upload = download_upload[1].text

dados = driver.find_elements(By.CSS_SELECTOR,".result-data-value")

sleep(20)

ping = dados[2].text
jitter = dados[3].text
pacotes_perdidos = dados[4].text

teste_id = driver.current_url.split("/")[-1]

servidor = driver.find_element(By.CLASS_NAME,"js-data-sponsor").text

data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

operadora = driver.find_element(By.CSS_SELECTOR, ".result-label.js-data-isp").text



#4 -- coparar o download , se estiver menor que 10  mps = ruim
download_num = float(download.replace(",","."))

if download_num < 10:
    status = "Ruim"
else:
    status = "Bom"

#6 -- criar o pdf
pdf  = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)


# Título
pdf.set_font("Arial", "B", 18)
pdf.cell(0, 10, "Relatório de Teste de Velocidade", ln=True, align="C")
pdf.ln(5)

# Linha separadora
pdf.set_draw_color(0, 0, 0)
pdf.line(10, 30, 200, 30)
pdf.ln(10)

# Dados em colunas
pdf.set_font("Arial", "", 12)

pdf.cell(50, 10, "Data/Hora:", border=0)
pdf.cell(0, 10, data_hora, border=0, ln=True)

# Download com cor
if status == "Bom":
    pdf.set_text_color(0, 128, 0)  # verde
else:
    pdf.set_text_color(255, 0, 0)  # vermelho

pdf.cell(50, 10, "Download:", border=0)
pdf.cell(0, 10, f"{download} Mbps - {status}", border=0, ln=True)

pdf.set_text_color(0, 0, 0)  # voltar para preto

pdf.cell(50, 10, "Upload:", border=0)
pdf.cell(0, 10, f"{upload} Mbps", border=0, ln=True)

pdf.cell(50, 10, "Ping:", border=0)
pdf.cell(0, 10, f"{ping} ms", border=0, ln=True)

pdf.cell(50, 10, "Jitter:", border=0)
pdf.cell(0, 10, f"{jitter} ms", border=0, ln=True)

pdf.cell(50, 10, "Pacotes Perdidos:", border=0)
pdf.cell(0, 10, f"{pacotes_perdidos}", border=0, ln=True)

pdf.cell(50, 10, "Servidor:", border=0)
pdf.cell(0, 10, servidor, border=0, ln=True)

pdf.cell(50, 10, "Operadora:", border=0)
pdf.cell(0, 10, operadora, border=0, ln=True)

# Linha final
pdf.ln(10)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())

# Salvar PDF
arquivo_pdf = "relatorio_speedtest.pdf"
pdf.output(arquivo_pdf)

print("PDF criado com sucesso!")


input("")

