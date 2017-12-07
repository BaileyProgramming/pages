from kivy.app import App

class SettingsApp(App):
    def build(self):
        self.use_kivy_settings = False
#        self.settings_cls = SettingsWithSidebar
        return Interface()

    def build_config(self, config):
            config.setdefaults('API', {
                'mc_user': 'User Name',
                'mc_key': 'apikey'})

    def build_settings(self, settings):
    #        config_json = open("config.json").read()
            settings.add_json_panel('Mail Chimp',
                self.config,
                data=settings_json)

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)