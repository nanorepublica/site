import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/home/andrew/personal-site')
from personal import app as application

sys.stdout = sys.stderr
