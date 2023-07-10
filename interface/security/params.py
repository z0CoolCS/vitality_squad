from dotenv import load_dotenv
import os

load_dotenv()


REGION = os.environ['REGION']
PROJECT = os.environ['PROJECT']
DATABASE_INSTANCE = os.environ['DATABASE_INSTANCE']
PASSWORD_DB = os.environ['PASSWORD_DB']
USER_DB = os.environ['USER_DB']
DB_NAME = os.environ['DB_NAME']