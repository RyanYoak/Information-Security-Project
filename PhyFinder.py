from Mail import Mail
from spellchecker import SpellChecker
from NeededLists import urgentPhrases, companyInformation
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
        self.use_suspicious_addresses = True

    def spellCheck(self, header, body):

        link_location = body.find("[")
        while link_location != -1:
            body = body.replace(body[link_location:body.find(")")+1], "")
            link_location = body.find("[")

        re.sub(r'\W+', '', body)
        re.sub(r'\W+', '', header)

        full_list = body.split() + header.split()

        incorrect = 0
        for word in full_list:
            if word not in spell:
                incorrect = incorrect + 1
        percent_incorrect = incorrect / len(full_list)

        percent = (percent_incorrect * 100) * 5

        if percent > 100:
            return 100

        return percent

    def linkChecker(self, body, threshold):
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

        percent = 0
        if bad_links == 1:
            percent = threshold * 1.5

        if bad_links > 1:
            percent = 100

        if percent > 100:
            return 100

        return percent

    def phrasesChecker(self, header, body):
        phrasesFound = 0
        in_header = False
        in_body = False
        for phrase in self.suspicious_phrases:
            if phrase.lower() in header.lower():
                phrasesFound = phrasesFound + 1
                in_header = True
            if phrase.lower() in body.lower():
                phrasesFound = phrasesFound + 1
                in_body = True
        if header.isupper():
            phrasesFound = phrasesFound + 1

        percent = 20 * phrasesFound

        if in_header and in_body:
            percent = percent * 2

        if percent > 100:
            return 100

        return percent

    def addressChecker(self, address, header, body):
        for company in companyInformation:
            if company.lower() in body.lower() or company.lower() in header.lower():
                if address == companyInformation[company]:
                    return 0
                else:
                    return 100
        return 0

    def checkMail(self, mail, threshold):
        mail.checked = True
        percent_list = []

        if mail.address in self.malicious_addresses:
            mail.phishing = 100
            return

        trusted_address = 0
        if mail.address not in self.trusted_addresses:
            trusted_address = threshold

        suspicious_percent = 0
        for address in self.suspicious_addresses:
            if address == mail.address:
                suspicious_percent = self.suspicious_addresses[address] * 25
            if suspicious_percent >= 100:
                mail.phishing = 100
                self.malicious_addresses.append(address)
                self.suspicious_addresses.pop(address)
                break


        address_percent = self.addressChecker(mail.address, mail.subject, mail.body)
        links_percent = self.linkChecker(mail.body, threshold)
        spelling_percent = self.spellCheck(mail.subject, mail.body)
        phrases_percent = self.phrasesChecker(mail.subject, mail.body)

        percent_list.append(trusted_address)
        percent_list.append(spelling_percent)
        percent_list.append(links_percent)
        percent_list.append(phrases_percent)
        percent_list.append(suspicious_percent)
        percent_list.append(address_percent)


        percent_list_top = math.floor(len(percent_list) * 0.5)
        percent_list.sort(reverse=True)
        final_sum = 0
        for x in range(percent_list_top):
            final_sum = final_sum + percent_list[x]
        mail.phishing = final_sum / percent_list_top


        if self.use_suspicious_addresses:
            if final_sum / percent_list_top > threshold:
                alreadySuspicious = False
                for address in self.suspicious_addresses:
                    if address == mail.address:
                        self.suspicious_addresses[address] = self.suspicious_addresses[address] + 1
                        alreadySuspicious = True
                if not alreadySuspicious:
                    self.suspicious_addresses[mail.address] = 1
