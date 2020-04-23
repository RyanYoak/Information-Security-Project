from Mail import Mail
import time
import random

email_names = ["ryan", "ryan.yoak", "sam", "AOL", "badactor", "delozier", "awesomeness", "Wizard"]
email_ats = ["gmail.com", "aol.com", "yahoo.com", "kent.edu", "sanyo.org", "ghost.cs.kent"]

subject_safe = [
    "Hello from us",
    "How waz the trip",
    "Help with the project",
    "Have you seen that video yet?",
    "Covid-19 update",
    "How we, a buisness, are responding to covid-19",
    "Very save email header",
    "Noting suspicios here"]

subject_malitious = [
    "urgent action neded",
    "Please fill out this form",
    "Data breach detected",
    "Plese help me wit all this money"]

body_safe = [
    "I need help getting my grades up...",
    "How was the trip, we missed you",
    "Computer security middterm",
    "Dungeons and Dragons Schedueling"]

body_malitious = [
    "[text](link) Use this link to give us all your money",
    "respond Immediately, we need all your money right now.",
    "Banking account information needed",
    "Revised Vacation & Sick Time Policy",
    "Very important info inside",
    "Netflix is our company and we are Netflix",
    "We are apple so respond Immediatly"]

def getMail(time):
    safe = random.choice([-1, 0, 1])
    if safe == 1:
        return (Mail(random.choice(email_names) + '@' + random.choice(email_ats), random.choice(subject_safe), random.choice(body_safe), time, None), safe)
    if safe == -1:
        return (Mail(random.choice(email_names) + '@' + random.choice(email_ats), random.choice(subject_malitious), random.choice(body_malitious), time, None), safe)
    else:
        return (Mail(random.choice(email_names) + '@' + random.choice(email_ats), random.choice(subject_safe + subject_malitious), random.choice(body_safe + body_malitious), time, None), safe)
