from tempmail import EMail
from bs4 import BeautifulSoup

email = EMail()
print(email)

msg = email.wait_for_message()
print(f"You got a Mail from : {msg.from_addr}")
print(f"Declaring that {msg.subject}" if msg.subject else "")

if(msg.body):
    soup = BeautifulSoup(msg.body, "html.parser")
    email_plain_text = soup.get_text(separator="\n").strip()
