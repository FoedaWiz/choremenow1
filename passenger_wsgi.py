import sys
import os

# SiteGround: point to the virtualenv created in cPanel Python App setup
# This path matches what SiteGround creates automatically
app_dir = os.path.dirname(os.path.abspath(__file__))
venv_path = os.path.join(app_dir, 'venv')

INTERP = os.path.join(venv_path, 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, app_dir)

# Load .env file for environment variables
from dotenv import load_dotenv
load_dotenv(os.path.join(app_dir, '.env'))

from app import create_app
application = create_app()
