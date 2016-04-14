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
                    msg[name] = value
                else:
                    value = [self.encodeAddrHeader(V, hdrenc) for V in value]
                    recip += value
                    recip += value
                if name.lower() != 'bcc':
                    msg[name] = ';'.join(value)

        recip = list(set(recip))
        fullText = msg.as_string()

        self.trace('Sending to...' + str(recip))
        self.trace(fullText[:self.tracesize])
        server = smtplib.SMTP(self.smtpServerName)
        self.getPassword()
        self.authenticateServer(server)
        try:
            failed = server.sendmail(From, recip, fullText)
        except:
            server.close()
            raise
        else:
            server.quit()

        self.saveSentMessage(fullText, saveMailSeparator)
        if failed:
            class SomeAddrsFailed(Exception): pass
            raise SomeAddrsFailed('Failed addrs:%s\n' % failed)
        self.trace('Send exit')

    def addAttachments(self, mainmsg, bodytext, attaches,
                       bodytextEncoding, attachesEncodings):

        # 添加主体文本/纯文本部分
        msg = MIMEText(bodytext, _charset=bodytextEncoding)
        mainmsg.attach(msg)

        # 添加附件部分
        encodings = attachesEncodings or (['us-ascii'] * len(attaches))
        for (filename, fileencode) in zip(attaches, encodings):
            if not os.path.isfile(filename):
                continue

            # 根据文件后缀名推测内容类型, 忽略编码
            contype, encoding = mimetypes.guess_type(filename)
            if contype is None or encoding is not None:
                contype = 'application/octet-stream'
            self.trace('Adding' + contype)

            # 组建合适类型的Message子类
            maintype, subtype = contype.split('/', 1)
            if maintype == 'text':
                if fix_text_required(fileencode):
                    data = open(filename, 'r', encoding=fileencode)
                else:
                    data = open(filename, 'rb')
                msg = MIMEText(data.read(), _subtype=subtype, _charset=fileencode)
                data.close()

            elif maintype == 'image':
                data = open(filename, 'rb')
                msg = MIMEImage(data.read(), _subtype=subtype, _encoder=fix_encode_base64)
                data.close()

            elif maintype == 'audio':
                data = open(filename, 'rb')
                msg = MIMEAudio(data.read(), _subtype=subtype, _encoder=fix_encode_base64)
                data.close()

            elif maintype == 'application':
                data = open(filename, 'rb')
                msg = MIMEApplication(data.read(), _subtype=subtype, _encoder=fix_encode_base64)
                data.close()

            else:
                data = open(filename, 'rb')
                msg = MIMEBase(maintype, subtype)
                msg.set_payload(data.read())
                data.close()
                fix_encode_base64(msg)
                #email.encoders.encode_base64(msg)

            basename = os.path.basename(filename)
            msg.add_header('Content-Disposition', 'attachment', filename=basename)
            mainmsg.attach(msg)










