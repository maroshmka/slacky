import dotenv
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

SLACK_APP_ACCESS_TOKEN = os.environ['SLACK_APP_ACCESS_TOKEN']
