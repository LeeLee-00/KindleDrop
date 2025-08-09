from fastapi import FastAPI, HTTPException
import smtplib
import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import Dict, Any
import httpx
from models.email_models import EmailRequest, EmailResponse

app = FastAPI(title="Email Service", version="1.0.0")

class EmailService:
    def __init__(self):
        self.providers = {
            'gmail': {'server': 'smtp.gmail.com', 'port': 587},
            'outlook': {'server': 'smtp.office365.com', 'port': 587},
            'yahoo': {'server': 'smtp-mail.yahoo.com', 'port': 587}
        }
    
    async def send_email(self, request: EmailRequest) -> EmailResponse:
        """Send email asynchronously."""
        try:
            # Run email sending in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None, 
                self._send_email_sync, 
                request
            )
            
            return EmailResponse(
                success=True,
                tracking_id=result['tracking_id'],
                message="Email sent successfully"
            )
            
        except Exception as e:
            return EmailResponse(
                success=False,
                error=str(e),
                message="Failed to send email"
            )
    
    def _send_email_sync(self, request: EmailRequest) -> Dict[str, Any]:
        """Synchronous email sending."""
        config = self.providers.get(request.provider, self.providers['outlook'])
        
        msg = MIMEMultipart()
        msg['From'] = request.sender_email
        msg['To'] = request.recipient_email
        msg['Subject'] = request.subject
        
        # Add attachment
        part = MIMEApplication(request.file_content, Name=request.filename)
        part['Content-Disposition'] = f'attachment; filename="{request.filename}"'
        msg.attach(part)
        
        # Send email
        with smtplib.SMTP(config['server'], config['port']) as server:
            server.starttls()
            server.login(request.sender_email, request.sender_password)
            server.sendmail(
                request.sender_email, 
                [request.recipient_email], 
                msg.as_string()
            )
        
        return {'tracking_id': str(uuid.uuid4())}

@app.post("/send-email", response_model=EmailResponse)
async def send_email_endpoint(request: EmailRequest):
    """Send email endpoint."""
    email_service = EmailService()
    return await email_service.send_email(request)