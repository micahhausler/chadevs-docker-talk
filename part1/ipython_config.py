# Configuration file for ipython.

c = get_config()

c.IPKernelApp.exec_lines = [
    'import json',
    'import os',
    'import sys',
]

c.FileNotebookManager.notebook_dir = '/var/www/ipython'
c.NotebookApp.notebook_dir = '/var/www/ipython'

c.NotebookApp.open_browser = False
c.NotebookApp.port = 8000
c.NotebookApp.ip = '0.0.0.0'

c.NotebookApp.enable_mathjax = False
