# Imports

import datetime            # Basic import
delta = datetime.timedelta(days=5)

import datetime as DT      # Renaming the import
delta = DT.timedelta(days=5)

from datetime import timedelta # Pulling it into our namespace
delta = timedelta(days=5)

from datetime import timedelta as TD # Pulling it into our namespace and renaming it
delta = TD(days=5)

import tools.cutters.saw # Importing a module from a nested package
tools.cutters.saw.saw_things() # Call a function on imported package

from tools.cutters.knife import knife_things as cut # Import just a function
cut()
