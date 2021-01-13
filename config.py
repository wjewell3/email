# Configuration of this API
# from google.cloud import ndb
from google.cloud import datastore
import os
import re
import yaml

def env(var):
    client = datastore.Client()
    q = client.query(kind='Gmail')
    q.add_filter('name','=',var)
    q_str = str(list(q.fetch())[0])
    startPos = q_str.find(''''value':''') + 10
    endPos = q_str[startPos:].find("'")
    return q_str[startPos:startPos+endPos]

# def env(var):
#     return os.environ[var]

class Config:
    # Currently set up to send from 2 users - feel free to change this
    user1 = env('GMAIL1_USER')
    pw1 = env('GMAIL1_PW')
    name1 = env('GMAIL1_NAME')
    ph1 = env('GMAIL1_PH')
    user2 = env('GMAIL2_USER')
    pw2 = env('GMAIL2_PW')
    name2 = env('GMAIL2_NAME')
    ph2 = env('GMAIL2_PH')
    SENDGRID_API_KEY = env('SENDGRID_API_KEY')
    MAILJET_KEY = env('MAILJET_KEY')
    MAILJET_SECRET = env('MAILJET_SECRET')

    refresh = {'frequency': 1400} # minutes -> 1 day
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    to_addr = env('GMAIL1_USER')

class ProdConfig(Config):
    to_addr = 'COVID19VaccineStandby@Nashville.gov'

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}


# making variables out of app.yaml

path_matcher = re.compile(r'\$\{([^}^{]+)\}')

def path_constructor(loader, node):
    ''' Extract the matched value, expand env variable, and replace the match '''
    value = node.value
    match = path_matcher.match(value)
    env_var = match.group()[2:-1]
    return os.environ.get(env_var) + value[match.end():]


yaml.add_implicit_resolver('!path', path_matcher)
yaml.add_constructor('!path', path_constructor)
with open('app.yaml') as yaml_file:
    try:
        CONFIG = yaml.load(yaml_file)
    except yaml.YAMLError as exc:
        print('Config file load exception')
        print(exc)