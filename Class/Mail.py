import smtplib, ssl, sys

def send_mail(msg):
    # on rentre les renseignements pris sur le site du fournisseur
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    # on rentre les informations sur notre adresse e-mail
    email_adress = 'botswzennyth@gmail.com'
    email_password = '95amGXeY7Xy5'

    # on rentre les informations sur le destinataire
    email_receiver = 'matsfox@orange.fr'
    # on crée la connexion
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(email_adress, email_password)
        # envoi du mail
        server.sendmail(email_adress, email_receiver, msg)
