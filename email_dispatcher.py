import os
import time
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import random

def generate_feedback(gemini_model):
    feedback_types = [
        'very_satisfied',
        'satisfied',
        'neutral',
        'dissatisfied',
        'product_issue',
        'delivery_issue',
        'service_issue',
        'payment_issue',
        'return_issue',
        'website_issue',
        'app_issue',
        'other_issue'
    ]
    
    selected_type = random.choice(feedback_types)
    
    prompts = {
    'very_satisfied': """Generate an enthusiastic customer feedback email about a recent purchase. 
        Mention specific product features you loved, excellent delivery time, and outstanding customer service experience.
        Include details about product quality and why you would recommend it. Fill in fake details. 
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",
        
    'satisfied': """Generate a positive customer feedback email that highlights good product experience.
        Mention what met your expectations about the product, delivery, and overall service.
        Include one minor suggestion for improvement. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",
        
    'neutral': """Generate a balanced customer feedback email about your purchase.
        Discuss both positive aspects (like product features or delivery) and areas needing improvement.
        Be specific about what worked and what didn't. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",
        
    'dissatisfied': """Generate a professional but critical customer feedback email.
        Address specific issues with the product, delivery delays, or service problems.
        Clearly state what went wrong and what resolution you expect. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",
        
    'product_issue': """Generate a detailed customer complaint email about product quality issues.
        Describe specific problems encountered, when they started, and their impact.
        Request specific resolution (replacement, refund, or repair) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'delivery_issue': """Generate a customer complaint email about delivery problems.
        Describe the delivery delay, missing items, or damaged package.
        Request specific resolution (replacement, refund, or compensation) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'service_issue': """Generate a customer complaint email about poor service experience.
        Describe the issue with customer service representative, response time, or lack of resolution.
        Request specific resolution (apology, compensation, or escalation) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'payment_issue': """Generate a customer complaint email about payment problems.
        Describe the payment error, double charge, or refund delay.
        Request specific resolution (refund, confirmation, or investigation) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'return_issue': """Generate a customer complaint email about return process issues.
        Describe the return rejection, refund delay, or return shipping problem.
        Request specific resolution (refund, replacement, or return label) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'website_issue': """Generate a customer complaint email about website usability issues.
        Describe the problem with navigation, search, or checkout process.
        Request specific resolution (fix, refund, or discount) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'app_issue': """Generate a customer complaint email about mobile app functionality issues.
        Describe the app crash, login error, or payment failure.
        Request specific resolution (update, refund, or support) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line.""",

    'other_issue': """Generate a customer complaint email about other issues not listed.
        Describe the problem encountered, its impact, and your expectations.
        Request specific resolution (refund, replacement, or compensation) and timeline expectations. Fill in fake details.
        Don't use placeholders. Write in plain text, don't use formating, **only use newline characters (\n) to beautify the email**. Don't wrirte the subject line."""

}
    
    response = gemini_model.generate_content(prompts[selected_type])
    return response.text

def send_bulk_feedback_emails(sender_email, app_password, recipient_email, num_emails, api_key):
    # List of fake sender emails for testing
    fake_senders = [
        'customer1@example.com',
        'happy.buyer@example.com',
        'regular.client@example.com',
        'new.customer@example.com',
        'loyal.shopper@example.com',
        'first.time@example.com',
        'return.buyer@example.com',
        'verified.purchase@example.com',
        'old.customer@example.com',
        'big.buyer@example.com'
    ]
    
    # Configure Gemini with provided API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Email setup
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, app_password)
            
            for i in range(num_emails):
                
                current_sender = fake_senders[i % len(fake_senders)]
                # Generate feedback using Gemini
                feedback_message = generate_feedback(model)                
                
                # Create email message
                msg = MIMEMultipart('alternative')
                msg['Subject'] = f"Customer Feedback #{i+1}"
                msg['From'] = current_sender
                msg['To'] = recipient_email

                text_part = MIMEText(feedback_message, 'plain')
                html_feedback_message = feedback_message.replace("\n", "<br>")
                html_part = MIMEText(f'<html><body><p>{html_feedback_message}</p></body></html>', 'html')                
                msg.attach(text_part)
                msg.attach(html_part)

                server.send_message(msg)
                print(f"Email {i+1} sent successfully")
                time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")

GEMINI_API_KEY = 'api_key'  # Replace with actual API key

SENDER_EMAIL = 'customer@example' # customer email
APP_PASSWORD = 'password'
RECIPIENT_EMAIL = 'company@example.com' # company email

send_bulk_feedback_emails(
    sender_email=SENDER_EMAIL,
    app_password=APP_PASSWORD,
    recipient_email=RECIPIENT_EMAIL,
    num_emails=10,
    api_key=GEMINI_API_KEY
)