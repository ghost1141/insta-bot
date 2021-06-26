import os
import platform
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import tarfile
import wget

def check_load():
    if platform.system() == "Windows":
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

    elif platform.system() == "Linux":
        if platform.architecture()[0] == '64bit':
            print('Your System is 64Bit')
            zipurl = 'https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz'
            wget.download(zipurl, (os.getcwd()) + ('/geckodriver'))
            file = tarfile.open(os.getcwd() + '/geckodriver/geckodriver-v0.29.1-linux64.tar.gz')
            file.extractall(os.getcwd() +  '/geckodriver/')
            file.close()
            os.remove(os.getcwd() + '/geckodriver/geckodriver-v0.29.1-linux64.tar.gz')
        else:
            print('Your System is 32Bit')
            zipurl = 'https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux32.tar.gz'
            wget.download(zipurl, (os.getcwd()) + ('/geckodriver'))
            file = tarfile.open(os.getcwd() + '/geckodriver/geckodriver-v0.29.1-linux32.tar.gz')
            file.extractall(os.getcwd() +  '/geckodriver/')
            file.close()
            os.remove(os.getcwd() + '/geckodriver/geckodriver-v0.29.1-linux32.tar.gz')
    else:
        print("Error")
