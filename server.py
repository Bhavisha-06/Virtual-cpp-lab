from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuration for sending email
EMAIL_ADDRESS = "bhavichaudhari2005@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "Bh@vi060205"  # Replace with your email password
TO_EMAIL_ADDRESS = "bc2780@srmist.edu.in"

@app.route('/save_login', methods=['POST'])
def save_login():
    data = request.get_json()

    # Get the login details from the request
    username = data['username']
    branch = data['branch']
    registrationNumber = data['registrationNumber']
    year = data['year']

    # Prepare email content
    subject = "New Login Details"
    body = f"Username: {username}\nBranch: {branch}\nRegistration Number: {registrationNumber}\nYear: {year}"

    # Send email
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL_ADDRESS
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL_ADDRESS, text)
        server.quit()

        return jsonify({'success': True})
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)
