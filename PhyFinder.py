from Mail import Mail
from spellchecker import SpellChecker
from NeededLists import urgentPhrases
import math
import re

spell = SpellChecker()

class PhyFinder:
    def __init__ (self, trusted_addresses, malicious_addresses, user_name):
        self.trusted_addresses = trusted_addresses
        self.malicious_addresses = malicious_addresses
        self.user_name = user_name
        self.suspicious_phrases = urgentPhrases
        self.suspicious_addresses = {}

    def spellCheck(self, header, body):

        link_location = body.find("[")
        while link_location != -1:
            body = body.replace(body[link_location:body.find(")")+1], "")
            link_location = body.find("[")

        re.sub(r'\W+', '', body)
        re.sub(r'\W+', '', header)

        body_list = body.split()
        header_list = header.split()

        full_list = body_list + header_list

        incorrect = 0
        for word in full_list:
            if word in spell:
                incorrect = incorrect + 1
        percent_incorrect = incorrect / len(body_list)

        percent = percent_incorrect * 100

        if percent > 100:
            return 100

        return percent

    def linkChecker(self, body):
        links = []
        text_start = body.find("[")
        while text_start != -1:
            text_end = body.find("]", text_start)
            text = body[text_start+1:text_end]
            link = body[text_end+2:body.find(")", text_end)]
            links.append((text, link))
            text_start = body.find("[", text_end)
        bad_links = 0
        for link in links:
            if link[0] != link[1]:
                bad_links = bad_links + 1

        if bad_links == 1:
            return 75

        if bad_links > 1:
            return 100

        return 0

    def phrasesChecker(self, header, body):
        phrasesFound = 0
        for phrase in self.suspicious_phrases:
            if phrase.lower() in header.lower():
                phrasesFound = phrasesFound + 1
            if phrase.lower() in body.lower():
                phrasesFound = phrasesFound + 1
        if header.isupper():
            phrasesFound = phrasesFound + 1

        percent = 20 * phrasesFound

        if percent > 100:
            return 100

        return percent

    def addressChecker(self, address, header, body):
        return 0

    def checkMail(self, mail):
        mail.checked = True
        percent_list = []

        if mail.address in self.malicious_addresses:
            mail.phishing = 100
            return

        trusted_addres = 0
        if mail.address not in self.trusted_addresses:
            trusted_addres = 100

        suspicious_percent = 0
        for address in self.suspicious_addresses:
            if address == mail.address:
                suspicious_percent = self.suspicious_addresses[address] * 25
            if suspicious_percent >= 100:
                mail.phishing = 100
                self.malicious_addresses.append(address)
                self.suspicious_addresses.pop(address)
                break



        links_percent = self.linkChecker(mail.body)
        spelling_percent = self.spellCheck(mail.subject, mail.body)
        phrases_percent = self.phrasesChecker(mail.subject, mail.body)

        percent_list.append(trusted_addres)
        percent_list.append(spelling_percent)
        percent_list.append(links_percent)
        percent_list.append(phrases_percent)
        percent_list.append(suspicious_percent)

        percent_list_top = math.floor(len(percent_list) * 0.75)
        percent_list.sort(reverse=True)
        final_sum = 0
        for x in range(percent_list_top):
            final_sum = final_sum + percent_list[x]
        mail.phishing = final_sum / percent_list_top

        if final_sum / percent_list_top > 65:
            alreadySuspicious = False
            for address in self.suspicious_addresses:
                if address == mail.address:
                    self.suspicious_addresses[address] = self.suspicious_addresses[address] + 1
                    alreadySuspicious = True
            if not alreadySuspicious:
                self.suspicious_addresses[mail.address] = 1
