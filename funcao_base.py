from ultralytics import YOLO
import shutil
import cv2
# Modelo treinado do dataset com base no yolo8n.pt
model = YOLO("C:/Users/Lucas/Desktop/pasta/best.pt")


Arquivo_de_imagem = "1.jpeg"  # Insira o caminho para uma imagem EX: 1.jpeg

nome_arquivo = ""

# Funcao para salvar o nome sem a extensão.
for letra in range(len(Arquivo_de_imagem)):
    char_atual = Arquivo_de_imagem[letra]
    if char_atual != ".":
        nome_arquivo = nome_arquivo + char_atual
    else:
        break

shutil.rmtree("saida")  # Limpa a pasta de saída

result = model.predict(Arquivo_de_imagem, project='saida',
                       name='execucao', save_crop=True)  # Gera o análise na pasta saída + o nome do arquvio

# Lê o arquivo de imagem no python
imagem_lida = cv2.imread(f"saida/execucao/crops/placa_mer/{nome_arquivo}.jpg")
# Exibe o arquivo carregado em uma pequena janela
exibir_imagem = cv2.imshow("Imagem", imagem_lida)
cv2.waitKey(0)  # Requerido para manter a janela aberta
