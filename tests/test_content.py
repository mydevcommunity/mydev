import os
import glob

HERE = os.path.abspath(os.path.dirname(__file__))
CONTENT = os.path.abspath(os.path.join(HERE, '..', 'site', 'content'))

def test_post_has_date():
    for filepath in glob.glob('%s/*.md' % CONTENT):
        file_content = open(filepath, 'r').read()
        assert 'Date:' in file_content

