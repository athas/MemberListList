#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, json, smtplib
from email.mime.text import MIMEText

class MemberListList:
	lists = []
	mailmanbindir = ''
	
	def handle_list(self, listname):
		print "Listing %s's members..." % listname
		owners = os.popen('%slist_owners %s' % (self.mailmanbindir, listname)).read().replace("\n", ", ").strip().strip(",")
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
		print msg.as_string()
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

if __name__ == "__main__":
	MemberListList('config.json')
