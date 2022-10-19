from pathlib import Path
import pandas as pd 
import os, re

root_dir = Path('./content')

query_str = r'\(https://m.360buyimg.com(.*)\)'


for _path in root_dir.glob('**/*.md'):
    with open(_path, 'r+') as fp:
        _str = fp.read()
        matched = re.findall(query_str, _str) 
