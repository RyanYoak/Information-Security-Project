from Mail import Mail
from Inbox import Inbox
from PhyFinder import PhyFinder
import time
from TestMail import TestMail

MyInbox = Inbox(["ryan.yoak@gmail.com"], [], "ryan.yoak@gmail.com")
for x in range(10):
    MyInbox.send(TestMail.getMail(time.time()))

print (MyInbox)
