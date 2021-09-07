import sys, time, os, argparse, socket
from tqdm import tqdm

parser = argparse.ArgumentParser(description = "SpeakerNet");

parser.add_argument('--config',         type=str,   default=None,   help='Config YAML file');
parser.add_argument('--test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/raw_test_list.txt",   help='Online Evaluation list');
parser.add_argument('--save_test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list.txt",   help='Evaluation list');

args = parser.parse_args();


def main():

    lines       = []

    with open(args.test_list) as f:
        lines = f.readlines()

    outF = open(args.save_test_list, "w")

    for line in tqdm(lines):
        content = line.split()[1]
        idx, filepath = content.split('/')[0], content
        outF.write(idx)
        outF.write(' ')
        outF.write(filepath)
        outF.write("\n")
    outF.close()
    print("save_test_list to:", args.save_test_list)


if __name__ == '__main__':
    main()