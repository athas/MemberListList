#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, json, smtplib
from email.mime.text import MIMEText

class MemberListList:
	lists = []
	mailmanbindir = ''
	
	def handle_list(self, listname):
		owners = os.popen('%slist_owners %s' % (self.mailmanbindir, listname)).read().replace("\n", ", ")
		owners = 'svip@diku.dk'
		memberlist = os.popen('%slist_members %s' % (self.mailmanbindir, listname)).read()
		efrom = 'boss@dikurevy.dk'
		subject = u"Medlemmer på listen %s, dags dato" % listname
		message = u"""Hej Revyherrer

Her er listen over adresser på %s-listen dags dato:

%s

Med venlig hilsen
En Robot som faktisk ikke kan påbyde venlige hilsner :(""" % (listname, memberlist)
		msg = MIMEText(message.encode('utf-8'))
		msg['Subject'] = subject
		msg['From'] = efrom
		msg['To'] = owners
		t = smtplib.SMTP('localhost')
		t.sendmail(owners, efrom, msg.as_string())
		t.quit()
	
	def run(self):
		for list in self.lists:
			self.handle_list(list)
	
	def __init__(self, configname):
		f = open(configname)
		c = json.loads(f.read())
		f.close()
		self.lists = c['lists']
		self.mailmanbindir = c['mailmanbindir']
		self.run()

def __main__(self):
	MemberListList('config.json')
