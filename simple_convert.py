import glob
import numpy as np
import zarr
from skimage.io import imread

if __name__ == '__main__':

    files = sorted(glob.glob('ExampleFly/images/*.TIF'))

    data = np.array([imread(i) for i in files])

    out = zarr.open('test.zarr', 'a')

    out['data'] = data
    out['data'].attrs['offset'] = [0]*3
    out['data'].attrs['resolution'] = [1]*3
