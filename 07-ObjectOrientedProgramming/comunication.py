from sms import sms
from email import email

sms1=sms(12315672636,41625743573)

sms1.set_message("informuję, że nasze czwartkowe spotkanie zostało odwołane.")
sms1.send()

email1=email("Cebo@Cebo.pl","Cebo2@Cebo2.pl","Spotkanie")
email1.set_message("informuję, że nasze czwartkowe spotkanie zostało odwołane.")
email1.send()
