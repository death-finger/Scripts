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
    return bodyenc in (None, QP)

class MailSender(MailTool):
    def __init__(self, smtpserver=None, tracesize=256):
        self.smtpServerName = smtpserver or mailconfig.smtpservername
        self.tracesize = tracesize

    def sendMessage(self, From, To, Subj, extrahdrs, bodytext, attaches,
                    saveMailSeparator=(('='*80)+'PY\n'),
                    bodytextEncoding='us-ascii', attachesEncodings=None):
        if fix_text_required(bodytextEncoding):
            if not isinstance(bodytext, str):
                bodytext = bodytext.decode(bodytextEncoding)
        else:
            if not isinstance(bodytext, bytes):
                bodytext = bodytext.encode(bodytextEncoding)

        # 创建基本消息
        if not attaches:
            msg = Message()
            msg.set_payload(bodytext, charset=bodytextEncoding)
        else:
            msg = MIMEMultipart()
            self.addAttachments(msg, bodytext, attaches,
                                bodytextEncoding, attachesEncodings)

        hdrenc = mailconfig.headersEncodeTo or 'utf-8'
        Subj = self.encodeHeader(Subj, hdrenc)
        From = self.encodeAddrHeader(From, hdrenc)
        To = [self.encodeAddrHeader(T, hdrenc) for T in To]
        Tos = ';'.join(To)

        # 将题头添加至基本消息
        msg['From'] = From
        msg['To'] = Tos
        msg['Subject'] = Subj
        msg['Date'] = email.utils.formatdate()
        recip = To
        for name, value in extrahdrs:
            if value:
                if name.lower() not in ['cc', 'bcc']:
                    value = self.encodeHeader(value, hdrenc)
