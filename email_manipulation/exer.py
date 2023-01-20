import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Haruto Mori"
email['to'] = "###########@gmail.com"
email['subject'] = "You won 1,000,000 dollars!"

email.set_content("I send this email by pyhton!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
   smtp.ehlo()
   smtp.starttls()
   smtp.login("#########@gmail.com", "##########")
   smtp.send_message(email)
   print("all good boss")