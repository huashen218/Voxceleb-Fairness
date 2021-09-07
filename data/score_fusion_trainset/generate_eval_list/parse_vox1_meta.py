import csv
import multiprocessing
import pickle
info_dict = {}
with open("vox1_meta.csv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    header = next(rd) # skip the header
    for row in rd:
        info_dict[row[0].strip()] = (row[2].strip(), 'train' if row[4].strip() == 'dev' else 'dev')

print(info_dict)

with open('vox1_meta.pickle', 'wb') as file:
    pickle.dump(info_dict, file)