import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BergerSchedule:
    def __init__(self, tournament_name):
        self.tournament = tournament_name

    def create_pdf(self, filename, teams, rounds):
        custom_page_size = (2200, 500)
        doc = SimpleDocTemplate(filename, pagesize=custom_page_size)

        # Create table data
        table_data = [["Berger Schedule", self.tournament]] + rounds

        # Create table
        table = Table(table_data)

        # Apply styles to the table
        style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 0), (-1, 0), (0.9, 0.9, 0.9)),
                            ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])
        table.setStyle(style)

        doc.build([table])

class EmailSender:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.smtp_username = os.getenv("SMTP_USERNAME")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.receiver_email = os.getenv("RECEIVER_EMAIL")

    def send_email(self, subject, body, attachment_filename):
        try:
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = self.receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            with open(attachment_filename, "rb") as attachment:
                part = MIMEApplication(attachment.read(), Name=attachment_filename)
                part['Content-Disposition'] = f'attachment; filename="{attachment_filename}"'
                message.attach(part)

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            server.quit()

            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    schedule = BergerSchedule("TOURNAMENT - LIGA")
    teams = [f"ekipa_{i}" for i in range(1, 31)]
    rounds = [
        ["Kolo 1", f"{teams[0]}-{teams[3]}", f"{teams[1]}-{teams[2]}"],
        # Add more rounds here...
    ]

    pdf_filename = "berger_schedule.pdf"
    schedule.create_pdf(pdf_filename, teams, rounds)

    email_sender = EmailSender()
    email_sender.send_email("Berger Schedule", "U prilogu je Berger Schedule", pdf_filename)
