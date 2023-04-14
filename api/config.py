# import configparser
# from sqlalchemy import create_engine

# # Read the config.ini file
# config = configparser.ConfigParser()
# config.read('configs.ini')

# # Get the PostgreSQL settings from the config.ini file
# pg_settings = config['database']
# host = pg_settings['host']
# port = pg_settings['port']
# dbname = pg_settings['dbname']
# user = pg_settings['user']
# password = pg_settings['password']

# # Create the connection string for the PostgreSQL database
# # different backend can be found here = https://docs.sqlalchemy.org/en/20/core/engines.html
# connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'

# connection2 = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# # Create the SQLAlchemy engine
# engine = create_engine(connection_string)


# import configparser


# Load configuration from 'config.ini'
# config = configparser.ConfigParser()
# config.read('configs.ini')

# db_uri = f"postgresql://{config.get('database', 'user')}:{config.get('database', 'password')}@{config.get('database', 'host')}:{config.get('database', 'port')}/{config.get('database', 'dbname')}"

# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False