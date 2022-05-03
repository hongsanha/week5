import smtplib
from email.message import EmailMessage
import re

SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=465
smtp=smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)

# smtp login에서의 password는 보안상의 이유로 임의로 password로 적었습니다! 정상 작동합니다!
smtp.login("sannah@yonsei.ac.kr","password")


message=EmailMessage()
message.set_content("이것은 본문입니다 ^~^ 멋사 10기 홍산하")
message["Subject"]="이것은 제목입니다!! 멋사 10기 홍산하"
message["From"]="sannah@yonsei.ac.kr"
message["To"]="hongsy6456@naver.com"

def sendEmail(addr):
    reg = "^[\w+-_.]+@\w+\.[a-zA-Z]{2,3}$"
    if bool (re.match(reg,addr)):
        smtp.send_message(message)
        smtp.quit()
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

sendEmail("hongsy6456@naver.com")
