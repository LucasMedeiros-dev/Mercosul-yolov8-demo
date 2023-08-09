# Dos conteúdos desse repositório:
```bash
datasets # Contém arquivos necessários para customização de um modelo.
  |_  /Val # Contém arquivos necessários para a validação.
  |_  /Train # Contém arquivos necessários para o treino.
  |_  train.cache # Cahce de treino.
  |_  val.cache # Cahce de treino.
saida
  |_ ... contém um exemplo de execução.
1.jpeg # Arquivo de entrada para testes de execução.
best.pt # Melhor modelo gerado do dataset com as anotações. Não necessariamente o último.
classes.txt # Classes disponíveis desse modelo.
data_custom.yaml # Personalizar dados para o treinamento. ATENÇÃO*
funcao_base.py # Funcao simplificada ao máximo para demonstrar a execução crua do YOLOV8 e o dataset.
last.pt # Último modelo gerado, não necessáriamente o melhor.
treinar.bat # Script .bat do windows para agilizar os comandos de treinamento com base no dataset
yolov8m.pt # Modelo padrão YoloV8 micro
yolov8n.pt # Modelo padrão YoloV8 nano
```
## ATENÇÃO!
Para efetuar o treino deve-se alterar o arquivo *data_custom.yaml* e substituir o diretório pelo seu diretório completo.
### Padrão:
```yaml
train: {INSIRA O DIRETORIO COMPLETO AQUI}\datasets\train
val: {INSIRA O DIRETORIO COMPLETO AQUI}\datasets\val
nc: 1
names: ["placa_mer"]
```
### Exemplo de correto:
```yaml
train: C:\Users\Lucas\Desktop\pasta\datasets\train
val: C:\Users\Lucas\Desktop\pasta\datasets\val
nc: 1
names: ["placa_mer"]
```
# Do treino
## Necessário seguir os passos do repositório abaixo para instalar as bibliotecas necessárias:
https://github.com/ultralytics/ultralytics
## Configuração padrao para treino
Está contida no arquivo *treinar.bat* o comando necessário para treinar utilizando o dataset provido.
```shell
#Abaixo o comando contido no arquivo.
yolo task=detect mode=train epochs=150 data=data_custom.yaml model=yolov8n.pt imgsz=640
```
## Em seguida ler atentamente o output do terminal e ir ajustando de acordo e ser feliz!
