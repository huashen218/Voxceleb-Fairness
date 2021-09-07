import pandas as pd
import sys, time, os, argparse, socket
from tqdm import tqdm
import numpy as np

os.sys.path.append('/home/ubuntu/MLData/work/Repos/voxceleb_trainer/')


parser = argparse.ArgumentParser(description = "SpeakerNet");

parser.add_argument('--config',         type=str,   default=None,   help='Config YAML file');
parser.add_argument('--meta_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/vox2_meta.csv",   help='Online Evaluation list');

parser.add_argument('--test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_H_m.txt",   help='Online Evaluation list');
parser.add_argument('--test_list_label',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_H_m_label.npz",   help='Online Evaluation list');


args = parser.parse_args();

def generate_label(args):

    lines = []
    with open(args.test_list) as f:
        lines = f.readlines()

    labels = []
    for line in tqdm(lines):
        content = line.split()
        label = content[0]
        labels.append(int(label))
    labels = np.array(labels)
    np.savez(os.path.join(args.test_list_label), labels=labels)
    print(labels.shape)



def main():
    generate_label(args)


if __name__ == '__main__':
    main()
    