import smtplib
from email.message import EmailMessage

SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=465
smtp=smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("sannah@yonsei.ac.kr","ghdtksgk1!")

message=EmailMessage()
message.set_content("이것은 본문입니다 ^~^")
message["Subject"]="이것은 제목입니다!!"
message["From"]="sannah@yonsei.ac.kr"
message["To"]="hongsy6456@naver.com"

smtp.send_message(message)
smtp.quit()