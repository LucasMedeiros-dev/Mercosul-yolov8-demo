from ultralytics import YOLO
import easyocr
import os
import cv2
import shutil
import re


def use_regex(input_text):   ## Função regex que verifica se o valor retornado foi uma placa de carro padrão mercosul.
    pattern = re.compile(
        r"[A-Za-z][A-Za-z][A-Za-z][0-9]+[A-Za-z][0-9]+[0-9]+", re.IGNORECASE)
    return pattern.match(input_text) # Retorna um objeto do tipo match.


model = YOLO("best.pt") # Modelo treinado do dataset com base no yolo8n.pt

reader = easyocr.Reader(['en', 'pt']) # Inicializa o reconhecimento de placas 
## TODO: Adicionar treinamento para fonte mercosul.


def get_plate_ocr(file): 
    img = cv2.imread(file)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, image_tresh = cv2.threshold(image_gray, 140, 255, cv2.THRESH_BINARY_INV)
    result = reader.readtext(image_tresh)
    for i in range(len(result)):
        for x in range(len(result[i])):

            try:
                teste_placa = use_regex(result[i][x])
                placa = teste_placa.string
                print(placa)
                return placa
            except:
                ...


def yolo_image(img: str):  ## Função para 
    img_without_ext = os.path.splitext(img)[0]
    print(img_without_ext)
    try:
        shutil.rmtree('placas_output/')
    except:
        ...
    result = model.predict(img, project='placas_output',
                           name='latest', save_crop=True)
    print(result)
    file = f'placas_output/latest/crops/placa_mer/{img_without_ext}.jpg'
    get_plate_ocr(file)

    # return result
