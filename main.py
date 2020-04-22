from Mail import Mail
from Inbox import Inbox
from PhyFinder import PhyFinder
import time
from TestMail import getMail

MyInbox = Inbox(["ryan.yoak@gmail.com"], [], "ryan.yoak@gmail.com")
for x in range(10):
    MyInbox.send(getMail(time.time()))

user_input = ""
while user_input != 'd':
    user_input = input("[i]nbox, [s]pam, [d]one.")
    if user_input == 'i':
        MyInbox.printInbox()
    if user_input == 's':
        MyInbox.printSpam()
