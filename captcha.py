from captcha.image import ImageCaptcha

#Condigure a imagem
image = ImageCaptcha(width=280, height=90)

# Texto escolhido para o captcha
captcha_text = 'BerGusPeh53Dou'

#Gera a imagem do captcha
data = image.generate(captcha_text)

# Salva a imagem no caminho escolhido
image.write(captcha_text, 'captcha.png')
