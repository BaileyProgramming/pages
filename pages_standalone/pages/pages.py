#!/usr/bin/python3
import json

#import kivy
#kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.settings import SettingsWithSidebar
#from kivy.uix.label import Label
#from kivy.uix.accordion import Accordion
#from kivy.uix.recycleview import RecycleView
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import ObjectProperty


import mychimp.mychimp as MyChimp
import yoursql.yoursql as YourSql
#from settingsjson import settings_json
from settingsmc import settings_mailchimp
from settingsdatabase import settings_database
import appconf


class listbutton(ListItemButton):
    pass

class TheDirectory(GridLayout):
    mc_lists = ObjectProperty()

    mc_adapter = ListAdapter(
            data=[],
            cls=listbutton,
            args_converter=lambda row_index, rec:
            {'text': rec['name'],
            'on_press': lambda y:MyChimp.getmembers(rec['id']),
            'size_hint_y': None,
            'height':25 },
            )
    mc_adapter.bind(on_selection_change=lambda x:print(x.selection))
    
    def mc_lists_sync():
#        global sqllists_json
#        global mclists_json
#        print(MyChimp.mclists_json['lists'])
#        print(YourSql.sqllists_json)
        for each in MyChimp.mclists_json['lists']:
#            print (each['id'] + " - " + each['name'])
            x = 0
            match = 0
#            print (YourSql.sqllists_json)
            while x < len(YourSql.sqllists_json):
                if each['id'] == YourSql.sqllists_json[x]['list_chimp_id']:
                    match += 1
                    print("Match Found")
                x+=1
            if match < 1:
                print ("No Match Found")
                YourSql.call_mlist_add(each['name'], each['id'])
        
#        print(json.dumps(YourSql.sqllists_json))
#        print("syncing......")
#        print(self)


    def mc_members_sync():
#        global sqllists_json
#        global mclists_json
#        print(MyChimp.mclists_json['lists'])
#        print(YourSql.sqllists_json)
        for each in MyChimp.mcmembers_json['lists']:
#            print (each['id'] + " - " + each['name'])
            x = 0
            match = 0
#            print (YourSql.sqllists_json)
            while x < len(YourSql.sqllists_json):
                if each['id'] == YourSql.sqllists_json[x]['list_chimp_id']:
                    match += 1
                    print("Match Found")
                x+=1
            if match < 1:
                print ("No Match Found")
                YourSql.call_mlist_add(each['name'], each['id'])
        
#        print(json.dumps(YourSql.sqllists_json))
#        print("syncing......")
#        print(self)

class directoryapp(App):
    def build(self):
        self.title = 'Pages'
        self.settings_cls =  SettingsWithSidebar
        self.use_kivy_settings = False

        return TheDirectory();


    def build_config(self, config):
            config.setdefaults('API', {
                'mc_user': 'User Name',
                'mc_key': 'apikey'})
            config.setdefaults('SQL', {
                'sql_server': '127.0.0.1',
                'sql_user': 'User Name',
                'sql_key': 'Password'})

    def build_settings(self, settings):
    #       config_json = open("config.json").read()            
            settings.add_json_panel('MailChimp', self.config, data=settings_mailchimp)
            settings.add_json_panel('Database', self.config, data=settings_database)

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)
        appconf.conf_reload()


if __name__ == '__main__':
    directoryapp().run()
        