import os
import glob
import pickle
import collections
from itertools import combinations, product
import random

meta_file = './vox2_meta.pickle'
data_root = '/home/ubuntu/MLData/work/Repos/voxceleb_trainer/data/voxceleb2/'
with open(meta_file, 'rb') as file:
    meta_data = pickle.load(file)

speakers = [spk for spk, v in meta_data.items() if v[1] == 'train']  # 'dev'
speakers = speakers[:100]

spk_utts = {}

for spker in speakers:
    utts = glob.glob(os.path.join(data_root, spker) + '/**/*.wav', recursive=True)
    utts = [utt.replace(data_root,'') for utt in utts]
    spk_utts[spker] = utts

all_positive_trials = []
all_negative_trials = []
num_trials = 50
for s1 in range(len(speakers)):
    print(s1)
    for s2 in range(s1 + 1):
        if s1 == s2:
            utts = spk_utts[speakers[s1]]
            all = list(combinations(utts, 2))
            all_positive_trials += random.sample(all, k=min(len(all), num_trials))
        else:
            utts1 = spk_utts[speakers[s1]]
            utts2 = spk_utts[speakers[s2]]
            all_negative_trials += random.sample(list(product(utts1, utts2)), k=num_trials//10)

print(len(all_negative_trials), len(all_positive_trials))
print(all_negative_trials[:100])
print(all_positive_trials[:100])
random.shuffle(all_positive_trials)
random.shuffle(all_negative_trials)
N = 2000
selected_positive_trials = all_positive_trials[:N]
selected_negative_trials = all_negative_trials[:N]


test_list_name = './test_list_test.txt'

with open(test_list_name,'w') as file:
    for i in range(N):
        pair = selected_positive_trials[i]
        line = f'1 {pair[0]} {pair[1]}'
        file.write(line + '\n')
        pair = selected_negative_trials[i]
        line = f'0 {pair[0]} {pair[1]}'
        file.write(line + '\n')


