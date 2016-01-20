import os
import sys
import signal
from tempfile import TemporaryFile
from subprocess import Popen, call, STDOUT

try:
	import Selenium2Library
except ImportError as e:
	print ('Selenium2Library importing failed. Error: %s' % e)
	print ('Make sure you installed it.')
	sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))
MANAGE = os.path.join(ROOT, 'manage.py')

def start_application():
	return Popen(['python', MANAGE, 'runserver'], stdout=TemporaryFile(), stderr=STDOUT, preexec_fn=os.setsid)

def stop_application(process):
	os.killpg(os.getpgid(process.pid), signal.SIGINT)

def run_test(args):
	process = start_application()
	call(['pybot'] + args, shell=(os.sep == '\\'))
	stop_application(process)

def print_help():
	print (__doc__)

def print_usage():
	print ("Usage: python runtests.py datasource")

if __name__ == '__main__':
	action = {'': print_usage}.get('-'.join(sys.argv[1:]))
	if action:
		action()
	else:
		run_test(sys.argv[1:])
