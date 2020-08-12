import smtplib

sender_email = "tarakshah35@gmail.com"
rec_email = "18it127@charusat.edu.in"

# Connect to the server
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

password=input(str("Please enter your password :"))
#u can write direct pass hear

# Login to the email server
server.login(sender_email, password)
print("Login success")

subject = "This is subject"
body="this is body"
message=f'Subject:{subject}\n\n{body}'

#mail sent
server.sendmail(sender_email,rec_email,message)#mail sent
print("Email sent")

# Logout of the email server
server.quit() There are quite a few ways to attach files to an email, but this is one of the simpler ways.
 This time we will use  MIME objects but we need to encode them with the base64 module from the email module and os.
 path to simply get the filename from the provided path.

# Setup the attachment
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
msg.attach(part)
