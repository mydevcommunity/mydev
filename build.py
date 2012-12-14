import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'packages.zip'))

import pelican
pelican.main()
