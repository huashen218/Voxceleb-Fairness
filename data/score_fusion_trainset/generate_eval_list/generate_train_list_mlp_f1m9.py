import os
import glob
import pickle
import collections
from itertools import combinations, product
import random
import numpy as np
from tqdm import tqdm


speaker_num = 1000
num_trials = 500
N = 100000

dataset="f9m1"

meta_file = './vox2_meta.pickle'
data_root = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/voxceleb2/'
with open(meta_file, 'rb') as file:
    meta_data = pickle.load(file)


train_list = f"/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_{dataset}.txt"
with open(train_list) as f:
    lines = f.readlines()

speakers_f = list(set([lines[k].split()[0] for k in range(len(lines)) if meta_data[lines[k].split()[0]][0] == "f"]))
speakers_m = list(set([lines[k].split()[0] for k in range(len(lines)) if meta_data[lines[k].split()[0]][0] == "m"]))

speakers_f = speakers_f[:speaker_num]
speakers_m = speakers_m[:speaker_num]


## Get speaker utterances
spk_utts = {}
for spker in speakers_f+speakers_m:
    utts = glob.glob(os.path.join(data_root, spker) + '/**/*.wav', recursive=True)
    utts = [utt.replace(data_root,'') for utt in utts]
    spk_utts[spker] = utts


def get_all_pairs(all_positive_trials, all_negative_trials, speakers_g1, speakers_g2, num_trials):
    print(" === generating all pairs === ")
    for s1 in tqdm(range(len(speakers_g1))):
        for s2 in range(s1 + 1):
            if s1 == s2:
                utts = spk_utts[speakers_g1[s1]]
                all = list(combinations(utts, 2))
                all_positive_trials += random.sample(all, k=min(len(all), num_trials))
                print("len(all_positive_trials)", len(all_positive_trials))
            else:
                ## same gender negative pairs
                utts1 = spk_utts[speakers_g1[s1]]
                utts2 = spk_utts[speakers_g1[s2]]
                all_negative_trials += random.sample(list(product(utts1, utts2)), k=num_trials//10)
                
                ## different gender negative pairs
                utts3 = spk_utts[speakers_g2[s2]]
                all_negative_trials += random.sample(list(product(utts1, utts3)), k=num_trials//10)   
    
    return all_positive_trials, all_negative_trials



## remove overlap

all_positive_trials = []
all_negative_trials = []
all_positive_trials, all_negative_trials = get_all_pairs(all_positive_trials, all_negative_trials, speakers_f, speakers_m, num_trials)

all_positive_trials, all_negative_trials = get_all_pairs(all_positive_trials, all_negative_trials, speakers_m, speakers_f, num_trials)

random.shuffle(all_positive_trials)
random.shuffle(all_negative_trials)

selected_positive_trials = all_positive_trials[:N]
selected_negative_trials = all_negative_trials[:N]


test_list_name = f'/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_mlp_{dataset}.txt'
test_list_label_name = f'/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/train_list_mlp_label_{dataset}.npz'


labels = []
with open(test_list_name,'w') as file:
    for i in range(N):
        pair = selected_positive_trials[i]
        line = f'1 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(1))
        pair = selected_negative_trials[i]
        line = f'0 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(0))

np.savez(os.path.join(test_list_label_name), labels=labels)

print(f" === saving data to file: {test_list_name} === ")
print(f" === saving label to file: {test_list_label_name} === ")