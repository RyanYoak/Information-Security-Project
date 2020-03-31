from Mail import Mail
from Inbox import Inbox
from PhyFinder import PhyFinder
import time

MyInbox = Inbox(["ryan@gmail.com"], ["evil@gmail.com"], "Ryan Yoak")
OnlyMail = Mail("evil@gmail.com", "Give me your money", "Just give me your money", time.time(), None)
MyInbox.send(OnlyMail)

print (MyInbox)
