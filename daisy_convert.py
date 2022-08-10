from skimage import io
import daisy
import glob
import numpy as np
import os
import sys

def get_total_roi(image_dir):

    files = sorted(glob.glob(os.path.join(image_dir, "*.TIF")))

    section_numbers = np.arange(len(files))

    begin = min(section_numbers)
    end = max(section_numbers) + 1

    shape_yx = np.array(io.imread(files[0])).shape

    roi = daisy.Roi((0, 0, 0), voxel_size * (end - begin, shape_yx[0], shape_yx[1]))

    print(f"Total ROI: {roi}")

    return roi, begin


def fill_section(ds, image_dir,block, image_index_offset=0):

    # 0-based image index
    image_index = int(block.read_roi.get_offset()[0] / ds.voxel_size[0])
    image_index += image_index_offset

    image_file = os.path.join(image_dir, f"image_0{image_index}.TIF")

    print(f"image file: {image_file}")
    print(f"Copying section {image_index}...")

    try:
        im = np.array(io.imread(image_file))[np.newaxis, :].astype(ds.dtype)

        if len(im.shape) == 4:
            im = im[..., 0]

        print(f"Im shape: {im.shape}")

        ds[block.write_roi] = im

    except IOError:
        print(f"Skipping section {image_index}, image file does not exist.")
        pass


if __name__ == "__main__":

    raw_dir = 'ExampleFly/images'
    out_file = 'test.zarr'
    voxel_size = daisy.Coordinate((1,)*3)
    out_dataset = "data"
    dtype = np.uint8

    total_roi, image_index_offset = get_total_roi(raw_dir)

    ds = daisy.prepare_ds(
        out_file,
        out_dataset,
        total_roi=total_roi,
        voxel_size=voxel_size,
        write_size=voxel_size * (1, 256, 256),
        dtype=dtype,
    )

    section_roi = daisy.Roi((0, 0, 0), (voxel_size[0],) + total_roi.get_shape()[1:])

    print(f"Copying in chunks of {section_roi}")

    daisy.run_blockwise(
        total_roi=total_roi,
        read_roi=section_roi,
        write_roi=section_roi,
        process_function=lambda b: fill_section(
            ds, raw_dir, b, image_index_offset
        ),
        num_workers=10
    )
