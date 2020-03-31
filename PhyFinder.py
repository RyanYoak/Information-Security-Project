from Mail import Mail

class PhyFinder:
    def __init__ (self, trusted_addressed, malicious_addressed, user_name):
        self.trusted_addressed = trusted_addressed
        self.malicious_addressed = malicious_addressed
        self.user_name = user_name
        self.suspicious_adresses = None
        self.suspicious_phrases = open("suspicious_phrases.txt","r").readlines()

    def checkMail(self, mail):
        return 0
