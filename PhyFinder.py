from Mail import Mail

class PhyFinder:
    def __init__ (self, trusted_addresses, malicious_addresses, user_name):
        self.trusted_addresses = trusted_addresses
        self.malicious_addresses = malicious_addresses
        self.user_name = user_name
        self.suspicious_adresses = None
        self.suspicious_phrases = open("suspicious_phrases.txt","r").readlines()

    def checkMail(self, mail):
        """
            Other ideas:
                Spell checker, the more mispelled the higher the chance
                Link checker, a link to a strange website is suspicious
                Urgent language checker, if they're trying to get info in a hurry
                
        """
        mail.checked = True
        if mail.address in self.malicious_addresses:
            mail.phishing = 100
            return
        mail.phishing = 0
