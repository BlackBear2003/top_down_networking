import asyncore
from smtpd import SMTPServer


class CustomSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Received message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))


def run_server():
    print('Starting SMTP server...')
    server = CustomSMTPServer(('localhost', 2226), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

run_server()