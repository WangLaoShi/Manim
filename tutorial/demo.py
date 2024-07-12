import os
from pathlib import Path

import pypandoc
import nbformat

os.environ.setdefault('PYPANDOC_PANDOC', '/opt/homebrew/bin/pandoc')

# With an input file: it will infer the input format from the filename
output = pypandoc.convert_file('README.md', 'ipynb')
