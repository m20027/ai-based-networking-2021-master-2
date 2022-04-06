import cv2
import os
import argparse
from tqdm import tqdm
from joblib import Parallel, delayed

parser = argparse.ArgumentParser(description="Preprocessing")
parser.add_argument('-i', '--input', default='.',
        help='Input data directory')
parser.add_argument('-o', '--output', default='.',
        help='Output data directory')
parser.add_argument('--basename', default='frame',
        help='Basename')
#parser.add_argument('--resize', default=1.0, type=float,
        #help='Resize')
#parser.add_argument('--grayscale', action="store_true",
        #help='Grayscale')
parser.add_argument('-j', '--n-jobs', default=1, type=int,
        help='Number of jobs')

args = parser.parse_args()

def to_frames(src, dst_dir, basename, ext='jpg'):
    capture = cv2.VideoCapture(src)

    if not capture.isOpened():
        return

    os.makedirs(dst_dir, exist_ok=True)
    base_path = os.path.join(dst_dir, basename)

    digit = len(str(int(capture.get(cv2.CAP_PROP_FRAME_COUNT))))

def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]

def call_to_frames_func(src_dir, dst_dir, src_files, basename):
    for src_file in tqdm(src_files):
        src = os.path.join(src_dir, src_file)
        target = os.path.join(dst_dir, src_file.split('.')[0])
        to_frames(src, target, basename)
        print(src, target, basename)

def main():
    src_dir      = args.input
    dst_dir      = args.output
    basename     = args.basename
    n_jobs       = args.n_jobs

    src_files = os.listdir(src_dir)
    src_files.sort()
    nrof_files = len(src_files)
    jobs = list(split_list(src_files, nrof_files // n_jobs))

    Parallel(n_jobs=n_jobs)(delayed(call_to_frames_func)(src_dir, dst_dir, src_files, basename) for src_files in jobs)

if __name__ == '__main__':
    main()
