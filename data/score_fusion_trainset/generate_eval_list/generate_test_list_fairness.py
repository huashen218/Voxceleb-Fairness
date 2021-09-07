import os
import glob
import pickle
import collections
from itertools import combinations, product
import random
import numpy as np
from tqdm import tqdm



def get_pos_same_pairs(speakers_g1, num_trials):
    all_positive_trials = []

    for s1 in tqdm(range(len(speakers_g1))):
        for s2 in range(s1 + 1):
            if s1 == s2:
                utts = spk_utts[speakers_g1[s1]]
                all = list(combinations(utts, 2))
                all_positive_trials += random.sample(all, k=min(len(all), num_trials))

    return all_positive_trials


def get_neg_same_pairs(speakers_g1, num_trials):
    all_negative_trials = []

    for s1 in tqdm(range(len(speakers_g1))):
        for s2 in range(s1 + 1):
            if s1 != s2:
                utts1 = spk_utts[speakers_g1[s1]]
                utts2 = spk_utts[speakers_g1[s2]]
                all_negative_trials += random.sample(list(product(utts1, utts2)), k=num_trials//10)

    return all_negative_trials



def get_neg_diff_pairs(speakers_g1, speakers_g2, num_trials):
    all_negative_trials = []
    
    for s1 in tqdm(range(len(speakers_g1))):
        for s2 in range(s1 + 1):
            if s1 != s2:
                utts1 = spk_utts[speakers_g1[s1]]
                utts3 = spk_utts[speakers_g2[s2]]
                all_negative_trials += random.sample(list(product(utts1, utts3)), k=num_trials//10) 

    return all_negative_trials



# speaker_num = 1000
num_trials = 300
N = 150000


meta_file = './vox1_meta.pickle'
data_root = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/voxceleb1/'
with open(meta_file, 'rb') as file:
    meta_data = pickle.load(file)

train_list = "/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_H.txt"


with open(train_list) as f:
    lines = f.readlines()

speakers_f = list(set([lines[k].split()[1].split('/')[0] for k in range(len(lines)) if meta_data[lines[k].split()[1].split('/')[0]][0] == "f"]))
speakers_f += list(set([lines[k].split()[2].split('/')[0] for k in range(len(lines)) if meta_data[lines[k].split()[1].split('/')[0]][0] == "f"]))

speakers_m = list(set([lines[k].split()[1].split('/')[0] for k in range(len(lines)) if meta_data[lines[k].split()[1].split('/')[0]][0] == "m"]))
speakers_m += list(set([lines[k].split()[2].split('/')[0] for k in range(len(lines)) if meta_data[lines[k].split()[1].split('/')[0]][0] == "m"]))

# speakers_f = speakers_f[:speaker_num]
# speakers_m = speakers_m[:speaker_num]


## Get speaker utterances
spk_utts = {}
for spker in speakers_f+speakers_m:
    utts = glob.glob(os.path.join(data_root, spker) + '/**/*.wav', recursive=True)
    utts = [utt.replace(data_root,'') for utt in utts]
    spk_utts[spker] = utts



## Generate Female TestSet.
all_pos_same_trials_f = get_pos_same_pairs(speakers_f, num_trials)
print("all_pos_same_trials::", len(all_pos_same_trials_f))

all_neg_same_trials_f = get_neg_same_pairs(speakers_f, num_trials)
print("all_neg_same_trials::", len(all_neg_same_trials_f))

all_neg_diff_trials = get_neg_diff_pairs(speakers_f, speakers_m, num_trials)
print("all_neg_diff_trials::", len(all_neg_diff_trials))

all_pos_same_trials_m = get_pos_same_pairs(speakers_m, num_trials)
print("all_pos_same_trials::", len(all_pos_same_trials_m))

all_neg_same_trials_m = get_neg_same_pairs(speakers_m, num_trials)
print("all_neg_same_trials::", len(all_neg_same_trials_m))


random.shuffle(all_pos_same_trials_f)
random.shuffle(all_neg_same_trials_f)
random.shuffle(all_neg_diff_trials)
random.shuffle(all_pos_same_trials_m)
random.shuffle(all_neg_same_trials_m)

selected_pos_same_trials_f = all_pos_same_trials_f[:N]
selected_neg_same_trials_f = all_neg_same_trials_f[:N]
selected_neg_diff_trials = all_neg_diff_trials[:N]
selected_pos_same_trials_m = all_pos_same_trials_m[:N]
selected_neg_same_trials_m = all_neg_same_trials_m[:N]


### Generate Female Pairs ### 
test_list_name = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_f.txt'
test_list_label_name = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_f_label.npz'

labels = []
with open(test_list_name,'w') as file:
    for i in range(N):
        pair = selected_pos_same_trials_f[i]
        line = f'1 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(1))

        pair = selected_neg_same_trials_f[i]
        line = f'0 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(0))

        pair = selected_neg_diff_trials[i]
        line = f'0 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(0))

np.savez(os.path.join(test_list_label_name), labels=labels)

print(f" == female dataset == ")
print(f" === saving data to file: {test_list_name} === ")
print(f" === saving label to file: {test_list_label_name} === ")




### Generate Male Pairs ### 
test_list_name = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_m.txt'
test_list_label_name = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/test_list_fairness_m_label.npz'

labels = []
with open(test_list_name,'w') as file:
    for i in range(N):
        pair = selected_pos_same_trials_m[i]
        line = f'1 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(1))

        pair = selected_neg_same_trials_m[i]
        line = f'0 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        labels.append(int(0))

        pair = selected_neg_diff_trials[i]
        line = f'0 {pair[1]} {pair[0]}'
        file.write(line + '\n')
        labels.append(int(0))

np.savez(os.path.join(test_list_label_name), labels=labels)

print(f" == male dataset == ")
print(f" === saving data to file: {test_list_name} === ")
print(f" === saving label to file: {test_list_label_name} === ")
