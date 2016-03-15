import os

DEBUG = True

DEBUG_TB_PROFILER_ENABLED = True

# DEBUG_TB_INTERCEPT_REDIRECTS = False

DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True

HOST = "localhost"

PORT = 4096

UPLOAD_DIR = os.getcwd() + "/coin/static/upload"

MAX_CONTENT_LENGTH = 4 * 1024 * 1024

SQLALCHEMY_TRACK_MODIFICATIONS = True

CACHE_TYPE = "simple"

SECURITY_TRACKABLE = False

SECURITY_CONFIRMABLE = False


