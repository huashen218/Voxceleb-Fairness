import pandas as pd
import sys, time, os, argparse, socket
from tqdm import tqdm
import random
import numpy as np

os.sys.path.append('/home/ubuntu/MLData/work/Repos/voxceleb_trainer/')

random.seed(1234)

parser = argparse.ArgumentParser(description = "SpeakerNet");

parser.add_argument('--config',         type=str,   default=None,   help='Config YAML file');
parser.add_argument('--female_test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_f.txt",   help='Online Evaluation list');
parser.add_argument('--male_test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_m.txt",   help='Online Evaluation list');
parser.add_argument('--split_ratio',      type=list,   default=[250, 2250],   help='Online Evaluation list');
parser.add_argument('--test_list_new',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_f1m9.txt",   help='Online Evaluation list');

args = parser.parse_args();



def generate_dict(data_list):

    lines = []
    with open(data_list) as f:
        lines = f.readlines()

    id_utterance = {}
    for line in tqdm(lines):
        id_utterance.setdefault(line.split(' ')[0], []).append(line.split(' ')[1])

    return id_utterance


def generate_validation_list(args):

    female_dict = generate_dict(args.female_test_list)
    male_dict = generate_dict(args.male_test_list)

    female_sample_size, male_sample_size = args.split_ratio
    print("female_sample_size:", female_sample_size)
    print("male_sample_size:", male_sample_size)
    
    female_sampled_speakers = random.sample(female_dict.keys(), female_sample_size)
    male_sampled_speakers = random.sample(male_dict.keys(), male_sample_size)

    speakers = female_sampled_speakers + male_sampled_speakers

    write_new_file = open(args.test_list_new, "w")

    female_pairs, male_pairs = 0, 0
    for id in np.sort(speakers):
        if id in female_sampled_speakers:
            utterances = female_dict[id] 
            female_pairs += len(utterances)
        else:
            utterances = male_dict[id]
            male_pairs += len(utterances)

        for utr in utterances:
            write_new_file.write(f"{id} {utr}");
    print(f"Total Pairs = {female_pairs+male_pairs}, Female Pairs={female_pairs}, Male Pairs={male_pairs}")

    write_new_file.close()



def main():
    generate_validation_list(args)


if __name__ == '__main__':
    main()