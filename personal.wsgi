import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/html/personal-site')
sys.path.insert(0,'/var/www/html/personal-site')
from personal import app as application

sys.stdout = sys.stderr
