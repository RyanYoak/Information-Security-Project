from Mail import Mail
import time
import random

email_names = ["ryan", "ryan.yoak", "sam", "AOL", "badactor"]
email_ats = ["gmail.com", "aol.com", "yahoo.com", "kent.edu"]

subject_safe = ["Hello from us", "How waz the trip", "Help with the project", "Have you seen that video yet?", "Covid-19 update", "How we, a buisness, is responding to covid-19", "Very save email header", "Noting suspicios here"]
subject_malitious = ["urgent action neded",  "Plase fill ut this form", "Data breach detected", "Plese help me wit all this money"]

body_safe = ["I need help getting my grades up...", "How was the trip, we missed you", "Computer security middterm", "Dungeons and Dragons Schedueling"]
body_malitious = ["respond Immediately. [text](link) Use this link to give us all your money", "Banking account information needed", "Revised Vacation & Sick Time Policy", "Very important info inside"]

def getMail(time):
    return Mail(random.choice(email_names) + '@' + random.choice(email_ats), random.choice(subject_safe + subject_malitious), random.choice(body_safe + body_malitious), time, None)
