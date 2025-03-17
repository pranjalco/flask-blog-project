import smtplib
MY_MAIL = "Your mail address"
MY_PASSWORD = "Your generated App Password for your mail"


def send_mail(name, email, phone_number, message):
    """This function is used to send email."""
    my_message = f"subject:Successful\n\nName: {name}, Mail:{email}, Phone number: {phone_number}, Message: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg=my_message)