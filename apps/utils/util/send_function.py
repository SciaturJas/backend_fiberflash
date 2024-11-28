import os
import boto3
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from botocore.exceptions import ClientError
from decouple import Csv, config

class EmailObject:
    ses = boto3.client('ses',
                       region_name=config('AWS_SES_REGION_NAME'),
                       aws_access_key_id=config('AWS_ACCESS_KEY'),
                       aws_secret_access_key=config('AWS_SECRET_KEY')
                       )

    def __init__(self, subject, to, source, html_content, path_file):
        self.subject = subject
        self.to = to
        self.source = source
        self.html_content = html_content
        self.path_file = path_file

    def do_sendmail(self):
        message_dict = {
            'Subject': {
                'Data': self.subject,
                'Charset': 'UTF-8',
            },
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': self.html_content,
                },
                'Text': {
                    'Data': '',
                    'Charset': 'UTF-8'
                },
            }
        }
        response = self.ses.send_email(
            Source=self.source,
            Destination={
                'ToAddresses': self.to
            },
            Message=message_dict
        )
        return response

    def do_send_file_mail(self):
        text='hello'
        recipient = self.to
        multipart_content_subtype = 'alternative' if text and self.html_content else 'mixed'
        msg = MIMEMultipart(multipart_content_subtype)
        # Add subject, from and to lines.
        msg['Subject'] = self.subject
        msg['From'] = self.source
        msg['To'] = ', '.join(self.to)
        # Add attachments
        for attachment in self.path_file or []:
            CORE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
            path = os.path.join(CORE_DIR, attachment)
            with open(path, 'rb') as f:
                part = MIMEApplication(f.read())
                part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
                msg.attach(part)
        if text:
            part = MIMEText(text, 'plain')
            msg.attach(part)
        if self.html_content:
            part = MIMEText(self.html_content, 'html')
            msg.attach(part)
        try:
            # Provide the contents of the email.
            response = self.ses.send_raw_email(
                Source=self.source,
                Destinations=recipient,
                RawMessage={
                    'Data': msg.as_string(),
                }
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            return e.response['Error']['Message']
        else:
            print("Email sent! Message ID:"),
            return response['MessageId']
