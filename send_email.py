import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = ""
    password = ""

    receiver = "app8flask@gmail.com"
    context = ssl.create_default_context()

    message= main.titles + main.desc

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
