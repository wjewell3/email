# Configuration of this API

import os

def env(var):
    return os.environ[var]

class Config:
    user1 = env('GMAIL1_USER')
    pw1 = env('GMAIL1_PW')
    user2 = env('GMAIL2_USER')
    pw2 = env('GMAIL2_PW')

    refresh = {'frequency': 1} # minutes
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    # """Development configuration
    # :param Config: Base class with configurations common to all environments.
    # :type Config: Config
    # """
    # # environment specific settings go here.

    to_addr = 'jewell.will@gmail.com'
    # api = {
    #     'nate_config_url': f"https{env('NATE_CONFIG_ROOT')}{env('NATE_DEV_SUFFIX_OLD')}/api/config/facility"
    #     ,'nate_config_api_key': env('NATE_CONFIG_KEY')
    #     }
    # kafka = {
    #     'offset': 'earliest'
    #     ,'service_name': f"rafael_nadal_{env('_ENV')}_{env('KAFKA_SERVICE_NAME')}"
    #     }
    # write_to_db = {
    #     'db': env('PG_FLOWDEV_DB')
    #     ,'user': env('PG_FLOWDEV_USER')
    #     ,'pw': env('PG_FLOWDEV_PW')
    #     ,'host': env('PG_FLOWDEV_HOST')
    #     }

class ProdConfig(Config):
    # """Production configuration
    # param Config: Base class with configurations common to all environments.
    # :type Config: Config
    # """

    to_addr = 'jewell.will@gmail.com'
    # api = {
    #     'nate_config_url': f"https{env('NATE_CONFIG_ROOT')}{env('NATE_PROD_SUFFIX_NEW')}/api/config/facility"
    #     ,'nate_config_api_key': env('NATE_CONFIG_KEY')
    #     }
    # kafka = {
    #     'offset': 'earliest'
    #     ,'service_name': f"rafael_nadal_{env('_ENV')}_{env('KAFKA_SERVICE_NAME')}"
    #     }
    # write_to_db = {
    #     'db': env('PG_PROD_DB')
    #     ,'user': env('PG_PROD_USER')
    #     ,'pw': env('PG_PROD_PW')
    #     ,'host': env('PG_PROD_HOST')
    #     }

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}