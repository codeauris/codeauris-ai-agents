import mcp_instance
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os
from dotenv import load_dotenv

# import environment variables from .env file
load_dotenv()

mcp = mcp_instance.mcp

@mcp.tool("kodex_academy_chat")
async def kodex_academy_chat(query: str):
    """
    Very simple Q&A over the knowledge_text resource.
    Returns lines that contain the query (case-insensitive).
    """
    try:
        text = await mcp.read_resource("http://localhost/kodex_academy")
        if not text:
            return {"error": "No text resource available"}

        # Extract string
        text_str = str(text)  # now it's a plain string
        lines_list = text_str.split('\n')

        results = [line.strip() for line in lines_list if query.lower() in line.lower()]
        return {
            "query": query,
            "matches": results,
            "count": len(results)
        }
    except Exception as e:
        return {"error": f"Failed to process query: {str(e)}"}


@mcp.tool("send_email_bulk")
def send_email_bulk(subject, recipient, smtp_server="smtp.gmail.com", smtp_port=587):
    """
    Send a newsletter to multiple recipients in a single email using BCC or TO field.

    Args:
        subject (str): Email subject line
        recipient (str): recipient email address
        smtp_server (str): SMTP server address
        smtp_port (int): SMTP server port

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_EMAIL_PASSWORD")
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)

        # Create single email message for all recipients
        msg = MIMEMultipart("alternative")
        msg["From"] = sender_email
        msg["Subject"] = subject
        msg["Date"] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
        msg["To"] = recipient

        path = os.path.join("resources", "email_template.txt")
        with open(path, "r", encoding="utf-8") as f:
            email_body = f.read()

        # Attach the HTML body
        msg.attach(MIMEText(email_body, "html"))

        # Send the email to all recipients at once
        server.sendmail(sender_email, recipient, msg.as_string())

        server.quit()

        print(f"Newsletter sent successfully to {recipient} recipient!")
        return True

    except Exception as e:
        print(f"Error sending newsletter: {e}")
        return False