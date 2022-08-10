import daisy
import sys
import json
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger('daisy.datasets').setLevel(logging.DEBUG)

def rechunk_in_block(
        block,
        dataset,
        rechunked_ds):

    logging.info(f'Rechunking in block {block.read_roi}')
    rechunked = dataset.to_ndarray(block.write_roi)

    rechunked_ds[block.write_roi] = rechunked

def rechunk(
        in_file,
        in_ds,
        out_file,
        out_ds,
        num_workers):

    logging.info('Loading dataset...')

    dataset = daisy.open_ds(in_file, in_ds)

    rechunk_roi = dataset.roi
    voxel_size = dataset.voxel_size

    read_roi = daisy.Roi(
            daisy.Coordinate((0,)*3),
            daisy.Coordinate((256,)*3) * voxel_size
        )

    write_roi = read_roi

    logging.info('Creating rechunked dataset...')

    rechunked_ds = daisy.prepare_ds(
                    out_file,
                    out_ds,
                    rechunk_roi,
                    dataset.voxel_size,
                    dtype=dataset.dtype,
                    write_roi=write_roi,
                    num_channels=1)

    logging.info('Writing to dataset...')

    daisy.run_blockwise(
        rechunk_roi,
        read_roi,
        write_roi,
        process_function=lambda b: rechunk_in_block(
            b,
            dataset,
            rechunked_ds),
        fit='shrink',
        num_workers=num_workers,
        read_write_conflict=False)


if __name__ == '__main__':

    in_file = 'test.zarr'
    in_ds = 'data'
    out_file = in_file
    out_ds = 'data_rechunked'
    num_workers = 5

    rechunk(
        in_file,
        in_ds,
        out_file,
        out_ds,
        num_workers)
