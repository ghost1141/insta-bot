import os
import platform
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

def check_load():
    if platform.architecture()[0] == '64bit':
        print('Your System is 64Bit')
        zipurl = 'https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win64.zip'
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zf:
                zf.extractall((os.getcwd()) + ('/geckodriver'))
    else:
        print('Your System is 32Bit')
        zipurl = 'https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win32.zip'
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zf:
                zf.extractall((os.getcwd()) + ('/geckodriver'))