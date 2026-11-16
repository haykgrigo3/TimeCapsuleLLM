out_dir = 'out_london'
eval_interval = 100
eval_iters = 20
log_interval = 10

always_save_checkpoint = False

dataset = 'gpt_data_london'
gradient_accumulation_steps = 2
batch_size = 4
block_size = 128

n_layer = 4
n_head = 4
n_embd = 256
dropout = 0.0

learning_rate = 1e-3
max_iters = 2000
lr_decay_iters = 2000
min_lr = 1e-4

warmup_iters = 100
device = 'cpu'  # Change to 'cuda' if you have GPU, or 'mps' for Mac

tokenizer_name = 'tokenizer_london'
vocab_size = None
