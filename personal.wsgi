import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/home/think/public_html/personal')
sys.path.insert(0,'/srv/www/personal-site')
from personal import app as application

sys.stdout = sys.stderr
