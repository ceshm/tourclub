import json

with open('config.json') as config_file:
    db_credentials = json.load(config_file)["database"]

DB_CONF = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': db_credentials
        },
    },
    'apps': {
        'models': {
            'models': ['__main__'],
            'default_connection': 'default',
        }
    }
}
