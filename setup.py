import os
import shutil
import sys
from distutils.core import setup # Need this to handle modules
import py2exe

cli_name = 'loop_key'
cli_version = '0.0.1'
cli_description = 'Para jugar'
cli_author = 'Adriansito'
cli_author_email = 'adrian.ausin@vass.es'

pyexe_options = {
  'bundle_files': 1,
  'dist_dir': './bin/',
  'packages': ['pyautogui']
  }

setup(
  name=cli_name,
  version=cli_version,
  description=cli_description,
  author=cli_author,
  author_email=cli_author_email,
  # http://www.py2exe.org/index.cgi/ListOfOptions
  options={'py2exe': pyexe_options},

  # console: list of scripts to convert into console exes
  console=[{
    'script': 'loop_key.py',
    'dest_base': cli_name
  }]
)