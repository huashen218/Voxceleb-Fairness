dataset="f1m1_f";
nohup python -u split_generate_train_list_mlp.py --dataset $dataset > split_generate_train_list_mlp_$dataset.log 2>&1 &
echo $! > save_pid.txt
