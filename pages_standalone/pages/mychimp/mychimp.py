
#!/usr/bin/python3
print("loading mychimp")

#import main
from mailchimp3 import MailChimp
import kivy
#kivy.require('1.0.7')
from kivy.app import App
import json

client = MailChimp('user', 'api-key')

mclists_json = {}
mcmembers_json = {}

def getlists(self):
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
	global client
	# returns all members inside list '123456'
	#print(json.dumps(client.lists.members.all(chimplist, get_all=True, fields="members.merge_fields, members.email_address"))) 
	mcmembers_json = json.loads(json.dumps(client.lists.members.all(chimplist, get_all=True, fields="members")))
	print(json.dumps(mcmembers_json))