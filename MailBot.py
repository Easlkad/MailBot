import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import os

# Set default timeout for socket
socket.setdefaulttimeout(10)

def send_email(to_address, subject, body):
    from_address = "barkant64@gmail.com"  # Use environment variables for security
    password = "avye pwqv hhdk ujjn"


    if not from_address or not password:
        print("Email credentials are not set.")
        return

   
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
       
        server.sendmail(from_address, to_address, text)
        server.quit()
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def get_email_content(person_type):
    if person_type == "student":
        return ("Welcome Student", "Dear Student,\n\nWelcome to our platform. We are excited to have you.")
    elif person_type == "teacher":
        return ("Welcome Teacher", "Dear Teacher,\n\nThank you for joining our platform. We look forward to your contributions.")
    elif person_type == "admin":
        return ("Welcome Admin", "Dear Admin,\n\nYour administrative access has been granted.")
    else:
        return ("Welcome", "Dear User,\n\nWelcome to our platform.")

def main():
    people = [
        {"gmail": "barkant64@gmail.com", "type": "student"},
        {"email": "barkan122_64@hotmail.com", "type": "student"},
        {"email": "barkan_-_64@hotmail.com", "type": "student"},
    ]
    
    for person in people:
        subject, body = get_email_content(person["type"])
        if "gmail" in person and person["gmail"]:
            send_email(person["gmail"], subject, body)
        
        if "email" in person and person["email"]:
            send_email(person["email"], subject, body)

if __name__ == "__main__":
    main()
