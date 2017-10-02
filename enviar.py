# -*- coding: utf-8 -*-
import smtplib

# Credenciais

remetente = input('informe o email que vai usar: ').lower()
senha = input('digite sua senha: ')

# Informações da mensagem

destinatario = input('informe email do destinatario: ').lower()
assunto = input('escreva o assunto: ')
texto = input('escreva seu texto: ')

# Preparando a mensagem
msg = '\r\n'.join([
    'From: %s' % remetente,
    'To: %s' % destinatario,
    'Subject: %s' % assunto,
    '',
    '%s' % texto
])
print("enviando ... ")


if 'gmail' in remetente:
    # Enviando o email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(remetente, senha)
    print("Saindo do sistema. Bye")
    server.sendmail(remetente, destinatario, msg)
    server.quit()

else:
    server = smtplib.SMTP('smtp.live.com,587')
    server.starttls()
    server.login(remetente, senha)
    print("Saindo do sistema. Bye")
    server.sendmail(remetente, destinatario, msg)
    server.quit()
