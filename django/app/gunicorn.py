import multiprocessing
import os


bind = ":8000"
chdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "aiohttp.worker.GunicornUVLoopWebWorker"
max_requests = 2000
max_requests_jitter = 500
errorlog = '-'
capture_output = True
DEBUG = os.getenv('DEBUG', default='0') == '1'
reload = DEBUG
preload_app = False #not DEBUG