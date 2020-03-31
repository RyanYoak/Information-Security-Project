from Mail import Mail
from PhyFinder import PhyFinder

class Inbox:
    def __init__ (self, trusted_addressed, malicious_addressed, user_name):
        self.Mechanism = PhyFinder(trusted_addressed, malicious_addressed, user_name)
        self.inbox = []
        self.spam = []

    def __str__ (self):
        mail_string = '''Inbox:

        '''
        for mail in self.inbox:
            mail_string = mail_string + str(mail) + '\n'

        mail_string = mail_string + '''Spam:

        '''
        for mail in self.spam:
            mail_string = mail_string + str(mail) + '\n'

        return mail_string

    def send(self, mail):
        self.Mechanism.checkMail(mail)
        if mail.phishing >= 0.9:
            self.spam.append(mail)
            print ("Possible phishing attack detected, please check spam folder.")
        else:
            self.inbox.append(mail)