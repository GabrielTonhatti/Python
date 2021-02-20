'''Peça para o usuário digitar a hora atual(inteira). Se for maior que 5h e antes das 12h mostre a mensagem de "Bom dia".
Se for de 12h às 18h mostre "boa tarde". Se for as 19h até as 23h mostre "boa noite". Se for das 0h às 5h
mostre a mensagem de "vá dormir!".'''

horas = int(input('Digite a hora atual: \n'))

if horas > 5 and horas < 12:
    print('Bom dia!')
elif horas >= 12 and horas <= 18:
    print('Boa tarde!')
elif horas >= 19 and horas <= 23:
    print('Boa noite!')
elif horas >= 00 and horas <= 5:
    print('Vá Dormir!')