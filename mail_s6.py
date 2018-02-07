import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("srrajesh113@gmail.com", "")



#Send the mail
msg = "Hello!"


server.sendmail("srrajesh113@gmail.com", "rajesh.17cs@cmr.edu.in", msg)
