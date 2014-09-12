import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'vendor.zip'))

import pelican
import pelican.tools
import pelican.tools.pelican_themes
pelican.main()
#pelican.tools.pelican_themes.main()
