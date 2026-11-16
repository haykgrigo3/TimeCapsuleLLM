"""
Sample from a trained model (London GPT)
"""
import os
import pickle
import torch
from contextlib import nullcontext
from model import GPTConfig, GPT
from tokenizers import ByteLevelBPETokenizer

# ─── tokenizer setup ────────────────────────────────────────────────
tok_folder = "tokenizer_london"
vocab_path = os.path.join(tok_folder, "vocab.json")
merges_path = os.path.join(tok_folder, "merges.txt")
if not (os.path.isfile(vocab_path) and os.path.isfile(merges_path)):
    raise FileNotFoundError(f"Cannot find tokenizer files in {tok_folder}: {vocab_path}, {merges_path}")

tokenizer = ByteLevelBPETokenizer(vocab_path, merges_path)
encode = lambda s: tokenizer.encode(s).ids
decode = lambda ids: tokenizer.decode(ids)
# ────────────────────────────────────────────────────────────────────

# ─── experiment settings (you can override via CLI) ────────────────
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--out_dir",        default="out_london")
parser.add_argument("--device",         default="cpu")
parser.add_argument("--start",          default="\n")
parser.add_argument("--num_samples",    type=int, default=10)
parser.add_argument("--max_new_tokens", type=int, default=500)
parser.add_argument("--temperature",    type=float, default=0.8)
parser.add_argument("--top_k",          type=int, default=200)
parser.add_argument("--seed",           type=int, default=1337)
parser.add_argument("--compile",        action="store_true")
args = parser.parse_args()

out_dir        = args.out_dir
start          = args.start
num_samples    = args.num_samples
max_new_tokens = args.max_new_tokens
temperature    = args.temperature
top_k          = args.top_k
seed           = args.seed
compile_flag   = args.compile
device_str     = args.device
# ────────────────────────────────────────────────────────────────────

# reproducibility & device
torch.manual_seed(seed)
device = torch.device(device_str)
ctx = nullcontext() if device.type == "cpu" else torch.amp.autocast(device_type=device.type, dtype=torch.float32)

# ─── load model checkpoint ──────────────────────────────────────────
ckpt_path = os.path.join(out_dir, "ckpt.pt")
if not os.path.isfile(ckpt_path):
    raise FileNotFoundError(f"Checkpoint not found: {ckpt_path}")
ckpt = torch.load(ckpt_path, map_location=device)
gptconf = GPTConfig(**ckpt["model_args"])
model   = GPT(gptconf)
sd      = ckpt["model"]
# strip prefix if present
for k in list(sd.keys()):
    if k.startswith("_orig_mod."):
        sd[k[len("_orig_mod."):]] = sd.pop(k)
model.load_state_dict(sd)
model.eval().to(device)
if compile_flag:
    model = torch.compile(model)
# ────────────────────────────────────────────────────────────────────

# prepare prompt tensor
if start.startswith("FILE:"):
    with open(start[5:], "r", encoding="utf-8") as f:
        start = f.read()
ids = encode(start)
x   = torch.tensor([ids], dtype=torch.long, device=device)

# ─── generation ─────────────────────────────────────────────────────
with torch.no_grad(), ctx:
    for i in range(num_samples):
        y = model.generate(x, max_new_tokens, temperature=temperature, top_k=top_k)
        print(decode(y[0].tolist()))
        print("---------------")
# ────────────────────────────────────────────────────────────────────
