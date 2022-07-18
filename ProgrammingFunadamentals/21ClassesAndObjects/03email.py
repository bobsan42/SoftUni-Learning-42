class Email:
    # is_sent = False

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()
while line != 'Stop':
    mail_data = line.split(' ')
    email = Email(mail_data[0], mail_data[1], mail_data[2])
    emails.append(email)
    line = input()

line = input().split(', ')
emails_to_send = [int(x) for x in line]
for x in emails_to_send:
    emails[x].send()

for email in emails:
    print(email.get_info())
