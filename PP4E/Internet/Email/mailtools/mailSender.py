# e.g. 13-23
# 发送消息, 添加附件

import mailconfig
import smtplib, os, mimetypes       # mime
import email.utils, email.encoders      # 日期字符串, base64格式
from .mailTool import MailTool, SilentMailTool


from email.message import Message       # 普通消息, 对象->文本
from email.mime.multipart import MIMEMultipart      # 类型特异的消息
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication


def fix_encode_base64(msgobj):
    linelen = 76        # mime标准规定
    from email.encoders import encode_base64
    encode_base64(msgobj)
    text = msgobj.get_payload()
    if isinstance(text, bytes):
        text = text.decode('ascii')
    lines = []
    text = text.replace('\n', '')
    while text:
        line, text = text[:linelen], text[linelen:]
        lines.append(line)
    msgobj.set_payload('\n'.join(lines))

def fix_text_required(encodingname):
    from email.charset import Charset, BASE64, QP

    charset = Charset(encodingname)
    bodyenc = charset.body_encoding
