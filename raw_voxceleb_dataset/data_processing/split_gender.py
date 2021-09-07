import pandas as pd
import sys, time, os, argparse, socket
from tqdm import tqdm

os.sys.path.append('/home/ubuntu/MLData/work/Repos/voxceleb_trainer/')


parser = argparse.ArgumentParser(description = "SpeakerNet");

parser.add_argument('--config',         type=str,   default=None,   help='Config YAML file');
parser.add_argument('--meta_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/vox2_meta.csv",   help='Online Evaluation list');
parser.add_argument('--test_list',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list.txt",   help='Online Evaluation list');
parser.add_argument('--test_list_m',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_m.txt",   help='Evaluation list');
parser.add_argument('--test_list_f',      type=str,   default="/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_f.txt",   help='Evaluation list');

args = parser.parse_args();



def generate_gender_list(args, m_ID_list, f_ID_list):

    lines = []
    with open(args.test_list) as f:
        lines = f.readlines()

    out_m = open(args.test_list_m, "w")
    out_f = open(args.test_list_f, "w")

    m_count, f_count = 0, 0

    for line in tqdm(lines):
        content = line.split()
        ID = line.split()[1].split('/')[0]
        if ID in m_ID_list:
            out_m.write(line);
            m_count += 1
        else:
            out_f.write(line);

            f_count += 1

    out_f.close()
    out_m.close()
    print("Male Count:", m_count)
    print("Female Count:", f_count)
    print("Overall Count:", m_count + f_count)


def main():

    male_list, female_list = [], []
    df = pd.read_csv(args.meta_list)
    
    if "vox1" in args.meta_list:      ### For VoxCeleb1 - Meta Info
        for idx, row in df.iterrows():
            male_list.append(row[0].split()[0]) if row[0].split()[2] == "m" else female_list.append(row[0].split()[0])
    
    else:                             ### For VoxCeleb2 - Meta Info
        for idx, row in df.iterrows():
            male_list.append(row[0].split()[0]) if row[2].split()[0] == "m" else female_list.append(row[0].split()[0])

    print(" ====== Gender Statistics ====== ")
    print("DataSet:", args.meta_list)
    print("Male IDs:", len(set(male_list)))
    print("Female IDs:", len(set(female_list)))
    print("Overall IDs:", len(set(male_list)) + len(set(female_list)))

    generate_gender_list(args, male_list, female_list)


if __name__ == '__main__':
    main()
    