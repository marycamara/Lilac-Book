#This section of code is allows us to send emails in python
import smtplib 
cask = False

#This contains the recivers email information. This section is the email account that will be use to send the email message.
# So it conatins the email,password of the account.
sender_email = "marycamara101@gmail.com" 
password = "happymummy"
reciever_email = "marycamara101@gmail.com" 



print('''

,--.   ,--.,--.                  ,-----.                ,--.        
|  |   `--'|  | ,--,--. ,---.    |  |) /_  ,---.  ,---. |  |,-.     
|  |   ,--.|  |' ,-.  || .--'    |  .-.  \| .-. || .-. ||     /     
|  '--.|  ||  |\ '-'  |\ `--.    |  '--' /' '-' '' '-' '|  \  \     
`-----'`--'`--' `--`--' `---'    `------'  `---'  `---' `--'`--'    
                                                                    

 ''')
                
print ("Welcome To Lilac Book Service")
print ("Lilac book will send you weekly book recommendation from different genre once a week for you to \n\n")

print('''
    ======================= ======================= ======================= =======================
                                          Popular Books 
   ========================= ===================== ======================= =======================
    ''')
    
print(" The Seven Husband Of Evelyan Hugo\n")
print(" They Both Die At The End\n")
print(" Eveything I Ever Told You\n")

print ("To get weekly Book Recommendations\n"
       "Of Latest, Newest And Classic \n")


#Making a connection to gmail server 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
def severinfo():
   server.login(sender_email, password)
   server.sendmail(sender_email, reciever_email, message)
   print("Email has been send to", reciever_email)
   server.sendmail(sender_email, reciever_email, message)
   

userinput=True
while True:
    print("""
    1.Subscribe
    2.Unsubscribe
    """)
    
    userinput = input(str(" To subscribe to Lilac Book Please Enter 1 To Enter Your Email \n To Unsubscribe From Lilac Book Please Enter 2 To Enter Your Email"))
    choice = ""
    if userinput=="1":
        print("\n Subscribed")
        choice = "Subscribed"
    elif userinput=="2":
        print("\n Usubscribed")
        choice = "Unsubscribed"
      
    print ("You Have " + choice + " to Lilac Weekly Book Recommendation")
    reciever_email = input(str("Please enter your email: ")) #in order to access the account
    while cask != True:
        if ".com" in reciever_email:
            cask = True
        else:
            print('please input an email ending in .com')
        break
    message = "You have subscribed to Lilac Book For Weekly recommendation Of Our Latest Books." # the message that the reciever will see
    message = "Welocme To The Club And Happy Reading"

    if choice == "Unsubscribed":
        message = "you have been unsubscribed"

    severinfo()

