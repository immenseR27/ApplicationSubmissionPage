import utils


class APP_props:
    HOST = utils.get_config().get('application', 'HOST')
    PORT = int(utils.get_config().get('application', 'PORT'))


class DB_props:
    HOST = utils.get_config().get('database', 'HOST')
    DB = utils.get_config().get('database', 'DB')
    USER = utils.get_config().get('database', 'USER')
    PWD = utils.get_config().get('database', 'PWD')


class FTP_props:
    HOST = utils.get_config().get('ftp', 'HOST')
    PORT = int(utils.get_config().get('ftp', 'PORT'))
    USER = utils.get_config().get('ftp', 'USER')
    PWD = utils.get_config().get('ftp', 'PWD')


