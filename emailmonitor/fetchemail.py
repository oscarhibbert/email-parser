import sys
import imaplib
import getpass
import mailparser
import datetime
import base64
import time
from flanker import mime
from pathlib import Path


def getunseen(emailuser,emailpw,imapserver,imaplabel):

    # 1. create an IMAP4 instance, preferably the SSL variant for security,
    # connected to the Gmail server at imap.gmail.com
    M = imaplib.IMAP4_SSL(imapserver)

    # 2. Next we can attempt to login. If the login fails,
    # an exception of type imaplib.IMAP4.error: will be raised:
    try:
        M.login(emailuser, emailpw)
    except imaplib.IMAP4.error:
        print ("LOGIN FAILURE")

    # 3. If the login is successful, we can now do IMAPy things with our IMAP4 object. 
    # Most methods of IMAP4 return a tuple where the first element is the 
    # return status of the operation (usually 'OK' for success), 
    # and the second element will be either a string or tuple 
    # with data from the operation.

    # For example, to get a list of mailboxes on the server, we can call list()
    # With Gmail, this will return a list of labels
    # (rv is status (index 0) and mailboxes (index1))
    rv, mailboxes = M.list()
    if rv == 'OK':
        print ("Mailboxes:")
        print (mailboxes)

    # 5. So with the mailbox selected, we can now get the emails within it. 
    # For example, we can get all the emails in the selected mailbox and 
    # for each one output the message number, subject, and date:
    def process_mailbox(M):
        rv, data = M.search(None, "UNSEEN")
        if rv != 'OK':
            print("No messages found!")
            return

        for num in data[0].split():
            rv, data = M.fetch(num, '(RFC822)')
            if rv != 'OK':
                print ("ERROR getting message"), num
                return
            rawemail = data[0][1]
            #   stremail = rawemail.decode('utf-8')
            email = mime.from_string((rawemail))
            for part in email.parts:
                print('Content-Type: {} Body: {}'.format(part, part.body))
            filename = email.clean_subject.replace(" ", "").replace("?","question")
            f=open(f"./tempdata/{filename}.html",'w',encoding='utf-8')
            f.write(str(email.parts[1].body))
            return filename

    # 4. To open one of the mailboxes/labels, call select():
    rv, data = M.select(imaplabel)
    if rv == 'OK':
        print ("Processing mailbox...\n")
        return process_mailbox(M) # ... do something with emails, see code above ...
    M.close()
    M.logout()


