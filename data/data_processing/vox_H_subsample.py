import pandas as pd
import sys, time, os, argparse, socket
from tqdm import tqdm
import random
import numpy as np

os.sys.path.append('/home/ubuntu/MLData/work/Repos/voxceleb_trainer/')

# random.seed(1234)

parser = argparse.ArgumentParser(description = "SpeakerNet");

parser.add_argument('--test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_m.txt",   help='Online Evaluation list');
parser.add_argument('--test_list_new',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_m_hard.txt",   help='Online Evaluation list');
parser.add_argument('--test_list_new_label',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_m_hard_label.npz",   help='Online Evaluation list');

args = parser.parse_args();

def generate_validation_list(args):

    lines = []
    with open(args.test_list) as f:
        lines = f.readlines()
    
    labels = []
    with open(args.test_list_new,'w') as file:
        for i in range(len(lines)):
            if i % 3 != 2:
                file.write(lines[i])
                labels.append(int(lines[i].split(' ')[0]))

    np.savez(os.path.join(args.test_list_new_label), labels=labels)


def main():
    generate_validation_list(args)


if __name__ == '__main__':
    main()