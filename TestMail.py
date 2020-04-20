from Mail import Mail
import time
import random

email_names = ["ryan", "ryan.yoak", "sam", "AOL", "badactor"]
email_ats = ["gmail.com", "aol.com", "yahoo.com", "kent.edu"]

subject_safe = ["Hello from us", "How was the trip", "Help with the project"]
subject_malitious = ["urgent action neded",  "Plase fill ut this form"]

body_safe = ["I need help getting my grades up...", "How was the trip, we missed you"]
body_malitious = ["respond Immediately. [text](link)", "Banking account information needed"]

class TestMail:

    def __init__(self):
        return

    @staticmethod
    def getMail(time):
            return Mail(random.choice(email_names) + '@' + random.choice(email_ats), random.choice(subject_safe + subject_malitious), random.choice(body_safe + body_malitious), time, None)
