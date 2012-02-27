import os
import sys
 
# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr
 
from os.path import abspath, dirname, join
sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, abspath(join(dirname(__file__), "../../")))
os.environ['DJANGO_SETTINGS_MODULE'] ='bitdemo.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()