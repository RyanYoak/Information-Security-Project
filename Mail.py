

class Mail:
    def __init__(self, address, subject, body, time, attachments):
        self.address = address
        self.subject = subject
        self.body = body
        self.time = time
        self.attachments = attachments
        self.read = False
        self.checked = False
        self.phishing = 0

    def __str__(self):
        rounded = round(self.phishing, 2)
        return f'''From: {self.address}
        Time: {self.time}
        Read: {self.read}
        Subject: {self.subject}
        Body:
        {self.body}

        Phishing: {rounded}%
        '''
