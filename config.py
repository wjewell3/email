# Configuration of this API
from google.cloud import ndb
from google.cloud import datastore
import os

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

    refresh = {'frequency': 1400} # minutes -> 1 day
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    to_addr = 'jewell.will@gmail.com'

class ProdConfig(Config):
    to_addr = 'COVID19VaccineStandby@Nashville.gov'

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}