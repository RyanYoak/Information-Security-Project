from Mail import Mail
from Inbox import Inbox
from PhyFinder import PhyFinder
import time
from TestMail import getMail

MyInbox = Inbox(["ryan.yoak@gmail.com"], [], "ryan.yoak@gmail.com")
MyInbox.calibrateThreshold()
#print("The threshold is: ", round(MyInbox.threshold, 2), "%")

for x in range(10):
    MyInbox.send(getMail(time.time())[0])

user_input = ""
while user_input != 'd':
    user_input = input("[i]nbox, [s]pam, [g]et mail, [d]one.")
    if user_input == 'i':
        MyInbox.printInbox()
    if user_input == 's':
        MyInbox.printSpam()
    if user_input == 'g':
        email_num = input("How many emails would you like to recieve? ")
        for x in range(int(email_num)):
            MyInbox.send(getMail(time.time())[0])
