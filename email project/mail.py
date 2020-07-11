import smtplib

sender_email = "tarakshah35@gmail.com"
rec_email = "18it127@charusat.edu.in"
password = input(str("Please enter your password : "))
subject = "This is subject"
body="this is body"
message=f'Subject:{subject}\n\n{body}'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email sent")