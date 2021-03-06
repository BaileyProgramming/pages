
#!/usr/bin/python3
print("loading mychimp")

import pages
from mailchimp3 import MailChimp
import kivy
#kivy.require('1.0.7')
from kivy.app import App
import json
import appconf



mclists_json = {}
mcmembers_json = {}

def set_client():
	client = MailChimp(appconf.conf.get('API', 'mc_user'), appconf.conf.get('API', 'mc_key'))
	return client

def getlists(self):
	client = set_client()

#	print(Config.get('API', 'mc_user'))
	#print(appconf.conf.get('API', 'mc_user'))
	global mclists_json
	global client
	# returns all the lists (only name and id)
	lists_str = json.dumps(client.lists.all(get_all=True, fields="lists.name,lists.id"))
	mclists_json = json.loads(lists_str)
#		print(lists_str)
#	for pl in mclists_json['lists']:
#		print(pl)
	#main.boxi.data = mclists_json

#	print(mclists_json['lists'][0]['name'])
	self.mc_lists.adapter.data = mclists_json['lists'] #["bob"]
	self.mc_lists._trigger_reset_populate()
		
def getmembers(chimplist):
	global mcmembers_json
	client = MailChimp(appconf.conf.get('API', 'mc_user'), appconf.conf.get('API', 'mc_key'))
	#print(json.dumps(client.lists.members.all(chimplist, get_all=True, fields="members.merge_fields, members.email_address")))
	members_str =  json.dumps(client.lists.members.all(chimplist, get_all=True, fields="members.merge_fields,members.email_address"))
	mcmembers_json = json.loads(members_str)
#	print(json.dumps(mcmembers_json))