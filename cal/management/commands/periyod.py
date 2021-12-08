import datetime
import smtplib
import ssl
from cal.models import Event
from datetime import timedelta 
from django.core.management.base import BaseCommand
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Command(BaseCommand):
    def handle(self, *args, **options):        
        today = datetime.date.today() + timedelta(days=12)
        next_sprint = today + timedelta(days=14)
        events = Event.objects.filter(is_weekend = False, start_time__gte = today, start_time__lt = next_sprint)

        sender_email = "kaancaner.kurtcephe@gmail.com"
        receiver_email = "canerkurtcephe@outlook.com"
        password = "6586-46Kck"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Sprint"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = """\
        Önümüzdeki Sprint içerisinde yer alan eventlerin listesi aşağıdaki gibidir.
        """

        #Formatı düzenlenecek
        html = "Title            Description            Start Time            End Time"
        for event in events:
            html += "\n"
            html += event.title + " " * 13 + event.description + " " * 13 + event.start_time.strftime("%m/%d/%Y") 
            html += " " * 13 + event.end_time.strftime("%m/%d/%Y")
        #html = render_to_string("cal/mail_send.html")

        part = MIMEText(html, "html")

        message.body = text
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
