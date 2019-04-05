import multiprocessing
import os

DEBUG = os.getenv('DEBUG', default='0') == '1'

bind = ":8000"
chdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')
workers = 1 if DEBUG else 2 * multiprocessing.cpu_count() + 1
worker_class = "aiohttp.worker.GunicornUVLoopWebWorker"
reload = DEBUG
preload_app = not DEBUG