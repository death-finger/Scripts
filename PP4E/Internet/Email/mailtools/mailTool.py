# e.g. 13-22
# 公用超类, 用于开启/关闭消息追踪

class MailTool:
    def trace(self, message):
        print(message)


class SilentMailTool:
    def trace(self, message):
        pass

