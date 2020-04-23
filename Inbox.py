from Mail import Mail
from PhyFinder import PhyFinder
from TestMail import getMail
import time
import math

class Inbox:
    def __init__ (self, trusted_addresses, malicious_addresses, user_name):
        self.Mechanism = PhyFinder(trusted_addresses, malicious_addresses, user_name)
        self.inbox = []
        self.spam = []
        self.threshold = 51
        self.spam_since_last_checked = 0

    def calibrateThreshold(self):
        malicious_addresses = self.Mechanism.malicious_addresses
        suspicious_addresses = self.Mechanism.suspicious_addresses
        self.Mechanism.use_suspicious_addresses = False
        self.threshold = 0
        tries = 0
        incorrect_above = 1
        incorrect_below = 1
        mail_per_try = 30
        while tries < 1000 or incorrect_above + incorrect_below != 0:
            #print("Loop number ", tries, " the threshold is ", round(self.threshold, 2))
            incorrect_above = 0
            incorrect_below = 0
            test_mail = []
            for x in range(mail_per_try):
                test_mail.append(getMail(time.time()))
            for mail in test_mail:
                self.Mechanism.checkMail(mail[0], self.threshold)
                if (mail[0].phishing > self.threshold and mail[1] == 1):
                    incorrect_above = incorrect_above + 1
                    #print("Mail score is: ", round(mail[0].phishing, 2), ", while threshold is: ", round(self.threshold, 2), ", that is to low.")
                if (mail[0].phishing < self.threshold and mail[1] == -1):
                    incorrect_below = incorrect_below + 1
                    #print("Mail score is: ", round(mail[0].phishing, 2), ", while threshold is: ", round(self.threshold, 2), ", that is to high.")

            if incorrect_above > incorrect_below:
                self.threshold = self.threshold + ((incorrect_above/mail_per_try * 10) * (1/math.log(2.72 + tries)))
                #print("There are ", incorrect_above, " incorrect above and ", incorrect_below, " incorrect below.")
            elif incorrect_below > incorrect_above:
                self.threshold = self.threshold - ((incorrect_below/mail_per_try * 10) * (1/math.log(2.72 + tries)))
                #print("There are ", incorrect_below, " incorrect below and ", incorrect_above, " incorrect above.")

            if self.threshold >= 100:
                #print("Something is very wrong!")
                self.threshold = 100

            if self.threshold <= 0:
                #print("Something is very wrong!")
                self.threshold = 0

            tries = tries + 1

        self.Mechanism.malicious_addresses = malicious_addresses
        self.Mechanism.suspicious_addresses = suspicious_addresses
        self.Mechanism.use_suspicious_addresses = True


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

    def printInbox(self):
        mail_string = '''Inbox:

        '''
        for mail in self.inbox:
            mail_string = mail_string + str(mail) + '\n'
            mail.read = True

        print(mail_string)

    def printSpam(self):
        mail_string = '''Spam:

        '''
        for mail in self.spam:
            mail_string = mail_string + str(mail) + '\n'
            mail.read = True

        print(mail_string)
        print(self.spam_since_last_checked, " spam emails since you last checked.")
        self.spam_since_last_checked = 0

    def send(self, mail):
        self.Mechanism.checkMail(mail, self.threshold)
        #75 is a number that is hardcoded and based on personal observation of the output
        if mail.phishing >= self.threshold:
            self.spam.append(mail)
            self.spam_since_last_checked = self.spam_since_last_checked + 1
        else:
            self.inbox.append(mail)
