from Mail import Mail
from Inbox import Inbox
from PhyFinder import PhyFinder
import time

trusted_addresses = ['ryoak@kent.edu', 'ryan.yoak@gmail.com', 'ryanyoak2@gmail.com', 'person@gmail.com', 'person@kent.edu', 'ryan@person.com', 'sam@gmail.com', 'randy@kent.com']
malicious_addresses = ['evil@gmail.com', 'evil@evil.com', 'thisisspam@spam.com', 'givemone@money.give', 'ryan@evil.ryan', 'evil.ryan@aol.com']

MyInbox = Inbox(trusted_addresses, malicious_addresses, "ryan.yoak@gmail.com")
OnlyMail = Mail(malicious_addresses[2], "Give me your money", "Just give me your money", time.time(), None)
MyInbox.send(OnlyMail)

print (MyInbox)
