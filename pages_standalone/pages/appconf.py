import configparser

conf = configparser.ConfigParser()

conf.read("pages/directoryapp.ini")

print(conf.sections())


def conf_reload():
    conf.read("pages/directoryapp.ini")