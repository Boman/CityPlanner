import os
import shutil
from pathlib import Path

import requests


def downloadResource(url, file):
    Path(file).parent.mkdir(parents=True, exist_ok=True)
    if not os.path.isfile(file):
        r = requests.get(url, verify=False, stream=True)
        r.raw.decode_content = True
        with open(file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
