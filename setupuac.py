# ...
# ModuleFinder can't handle runtime changes to __path__, but win32com uses them
try:
# py2exe 0.6.4 introduced a replacement modulefinder.
# This means we have to add package paths there, not to the built-in
# one.  If this new modulefinder gets integrated into Python, then
# we might be able to revert this some day.
# if this doesn't work, try import modulefinder
	try:
		import py2exe.mf as modulefinder
	except ImportError:
		import modulefinder
	import win32com, sys
	for p in win32com.__path__[1:]:
		modulefinder.AddPackagePath("win32com", p)
	for extra in ["win32com.shell"]: #,"win32com.mapi"
		__import__(extra)
		m = sys.modules[extra]
	for p in m.__path__[1:]:
		modulefinder.AddPackagePath(extra, p)
except ImportError:
# no build path setup, no worries.
	pass

from distutils.core import setup
import py2exe

t1 = dict(script="usmt_sid-6-git.py",
          dest_base="not_specified")
# targets with different values for requestedExecutionLevel
t2 = dict(script="usmt_sid-6-git.py",
          dest_base="as_invoker",
          uac_info="asInvoker")
t3 = dict(script="usmt_sid-6-git.py",
          dest_base="highest_available",
          uac_info="highestAvailable")
t4 = dict(script="usmt_sid-6-git.py",
          dest_base="require_admin",
          uac_info="requireAdministrator")
console = [t1, t2, t3, t4]

# hack to make windows copies of them all too, but
# with '_w' on the tail of the executable.
windows = [t1.copy(), t2.copy(), t3.copy(), t4.copy()]
for t in windows:
    t['dest_base'] += "_w"




setup(
    version = "0.1",
    description = "py2exe user-access-control sample script",
    name = "py2exe samples",
    # targets to build
    windows = windows,
    console = console,
    )








#setup(windows=['software.py'])


