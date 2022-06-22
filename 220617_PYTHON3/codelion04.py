# from ctypes import addressof
# from curses import tparm
# from smtplib import SMTP
# from ssl import PROTOCOL_TLS
# from typing import Protocol
# from pyrsistent import T

# SMTP
# Sample eMail Transport Protocol
# 간단하게 메일을 보내기 위한 약속

# email client(a) - email server(a@gmail.com)
# SMTP는 client -> email server 보내는 것을 말함.

# email server(a@gmail.com) <-> email server(b@xxx.xxx)   주고 받는 것도 SMTP이다.
# 보통은 이렇게(서버끼리 SMTP로 주고 받음) 진행 된다.

# SMTP, 서버를 이용해서 우리가 원하는 곳으로 메일을 보낼 수 있고 구현하는 것이 우리의 핵심 목표다.

# address:smtp.gmail.com
# port:465
# 문을 열고 들어간다고 이용한다고 보면 됨.

# smtplib 라이브러리로 쉽게 파이썬에서 다룰 수 있다.

# 1. SMTP 메일 서버를 연결한다.
# 2. SMTP 메일 서버에 로그인 한다.
# 3. SMTP 메일

import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

message = EmailMessage() # mime로 바꿔서
message.set_content('코드라이언 수업중입니다.')

message['Subject'] = '이것은 제목 입니다.'
message['from'] = 'suitable1125@gmail.com'

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
# print(smtp)
smtp.login('suitable1125@likelion.org','72258327')
smtp.send_message()
smtp.quit()

# imime로 바꿔서 smtp로 이야기 해야 메일 보내줌.
# 1. 이메일 만든다.
# 2. 이메일 내용을 담는다.






