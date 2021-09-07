import csv
import multiprocessing
import pickle
info_dict = {}
with open("vox2_meta.csv") as fd:
    rd = csv.reader(fd, delimiter=",", quotechar='"')
    header = next(rd) # skip the header
    for row in rd:
        info_dict[row[0].strip()] = (row[2].strip(), 'train' if row[3].strip() == 'dev' else 'dev')

print(info_dict)

with open('vox2_meta.pickle', 'wb') as file:
    pickle.dump(info_dict, file)