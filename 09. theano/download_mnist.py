import os
import os.path
import urllib
import gzip
import shutil

if not os.path.exists('mnist'):
    os.mkdir('mnist')

def download_and_gzip(name):
    if not os.path.exists(name + '.gz'):
        urllib.urlretrieve('http://yann.lecun.com/exdb/' + name + '.gz', name + '.gz')
    if not os.path.exists(name):
        with gzip.open(name + '.gz', 'rb') as f_in, open(name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            
download_and_gzip('mnist/train-images-idx3-ubyte')
download_and_gzip('mnist/train-labels-idx1-ubyte')
download_and_gzip('mnist/t10k-images-idx3-ubyte')
download_and_gzip('mnist/t10k-labels-idx1-ubyte')