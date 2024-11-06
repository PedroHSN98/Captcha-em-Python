# Gerador de Captcha em Python
## Pre-visualização 
![image](https://github.com/user-attachments/assets/cb978548-72e6-4377-84cd-79e722dac322)


Este projeto é um exemplo simples de como gerar imagens de CAPTCHA em Python usando a biblioteca `captcha`. Ele cria uma imagem CAPTCHA com o texto escolhido e salva a imagem em um arquivo __PNG__.

## Requisitos

Certifique-se de que você tenha o Python instalado em sua máquina (versão 3.6 ou superior recomendada). Além disso, este projeto requer a instalação da biblioteca `captcha`.

### Instalação da biblioteca necessária

Para instalar a biblioteca `captcha`, execute o seguinte comando:

```bash
pip install captcha
```
# Estrutura do Código

## Este código segue uma estrutura simples:

Configuração da Imagem: Define a largura e altura da imagem CAPTCHA.
Definição do Texto do CAPTCHA: Escolhe o texto que será exibido no CAPTCHA.
Geração da Imagem: Gera a imagem CAPTCHA com o texto selecionado.
Salvamento da Imagem: Salva a imagem gerada no diretório de trabalho com o nome __captcha.png__.

# Explicação do Código

## Aqui está uma explicação linha por linha do código:

```Python
from captcha.image import ImageCaptcha
``` 
Importa a classe `ImageCaptcha` da biblioteca `captcha`, que será usada para criar e personalizar a imagem do CAPTCHA.

```Python
# Configure a imagem
image = ImageCaptcha(width=280, height=90)

```
Configura a imagem do CAPTCHA com uma largura de 280 pixels e uma altura de 90 pixels. Você pode ajustar esses valores para personalizar o tamanho da imagem.

```Python
# Texto escolhido para o captcha
captcha_text = 'BerGusPeh53Dou'
```

Define o texto do CAPTCHA que será exibido na imagem. Este é o texto que os usuários precisarão reconhecer e digitar.

```Python
# Gera a imagem do captcha
data = image.generate(captcha_text)
```

Gera a imagem CAPTCHA com o texto especificado anteriormente.

```Python
# Salva a imagem no caminho escolhido
image.write(captcha_text, 'captcha.png')
```

Salva a imagem gerada no arquivo `captcha.png` no diretório de trabalho. O nome do arquivo e o local de salvamento podem ser alterados conforme desejado.

# Executando o Código

Para executar este código, salve-o em um arquivo Python (`captcha_generator.py`, por exemplo) e execute-o no terminal ou prompt de comando:
```bash
python captcha_generator.py
```
Após a execução, um arquivo chamado `captcha.png` será gerado no mesmo diretório, contendo a imagem do CAPTCHA com o texto especificado.

# Personalização

- **Alterar o Texto do CAPTCHA**: Modifique o valor de `captcha_text` para alterar o texto exibido na imagem CAPTCHA.

- **Modificar o Tamanho da Imagem**: Altere os parâmetros `width` e `height` na linha `ImageCaptcha(width=280, height=90)` para ajustar o tamanho da imagem.

# Contribuição

Sinta-se à vontade para fazer um fork deste projeto, criar melhorias e enviar um pull request!
