# e.g. 13-24

import poplib, mailconfig, sys
print('user:', mailconfig.popusername)

from .mailParser import MailParser
from .mailTool import MailTool, SilentMailTool


class DeleteSynchError(Exception): pass
class TopNotSupported(Exception): pass
class MessageSynchError(Exception): pass


class MailFetcher(MailTool):
    def __init__(self, popserver=None, popuser=None, poppswd=None, hastop=True):
        self.popServer = popserver or mailconfig.popservername
        self.popUser = popuser or mailconfig.popusername
        self.srvrHasTop = hastop
        self.popPassword = poppswd

    # Connecting Server
    def connect(self):
        self.trace('Connecting...')
        self.getPassword()
        server = poplib.POP3(self.popServer)
        server.user(self.popUser)
        server.pass_(self.popPassword)
        self.trace(server.getwelcome())
        return server

    def getPassword(self):
        if not self.popPassword:
            try:
                localfile = open(mailconfig.poppasswdfile)
                self.popPassword = localfile.readline()[:-1]
                self.trace('local file password' + repr(self.popPassword))
            except:
                self.popPassword = self.askPopPassword()

    def askPopPassword(self):
        assert False, 'Subclass must define method'

    fetchEncoding = mailconfig.fetchEncoding

    def decodeFullText(self, messageBytes):
        text = None
        kinds = [self.fetchEncoding]
        kinds += ['ascii', 'latin1', 'utf8']
        kinds += [sys.getdefaultencoding()]

        for kind in kinds:
            try:
                text = [line.decode(kind) for line in messageBytes]
                break
            except (UnicodeError, LookupError):
                pass

        if text == None:
            blankline = messageBytes.index(b'')
            hdrsonly = messageBytes[:blankline]
            commons = ['ascii', 'latin1', 'utf8']
            for common in commons:
                try:
                    text = [line.decode(common) for line in hdrsonly]
                    break
                except UnicodeError:
                    pass
            else:
                try:
                    text = [line.decode() for line in hdrsonly]
                except UnicodeError:
                    text = ['From: (sender of unknown Unicode format headers)']
        text += ['', '--Sorry: mailtools cannot decode this mail content!--']
        return text