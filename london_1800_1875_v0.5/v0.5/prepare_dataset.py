from tokenizers import ByteLevelBPETokenizer
from pathlib import Path
from tqdm import tqdm
import numpy as np
import pickle

# The paths
tokenizer_dir = "tokenizer_london"


corpus_path = "london_corpus_cleaned_merged.txt"

output_dir = Path("gpt_data_london")
output_dir.mkdir(exist_ok=True)

# loads tokenizer
tokenizer = ByteLevelBPETokenizer(
    f"{tokenizer_dir}/vocab.json",
    f"{tokenizer_dir}/merges.txt"
)


with open(corpus_path, "r", encoding="utf-8") as f:
   
    data = f.read()

print(" Encoding text...")
ids = tokenizer.encode(data).ids
ids = np.array(ids, dtype=np.uint16)  

# Split into train/val
split = int(0.9 * len(ids))

train_ids, val_ids = ids[:split], ids[split:]

# .bin
train_ids.tofile(output_dir / "train.bin")

val_ids.tofile(output_dir / "val.bin")

# Save metadata for decoding later
meta = {
    "vocab_size": tokenizer.get_vocab_size(),
    "tokenizer_config": {
        "vocab_file": f"{tokenizer_dir}/vocab.json",
        "merges_file": f"{tokenizer_dir}/merges.txt"
    }
}
with open(output_dir / "meta.pkl", "wb") as f:
    pickle.dump(meta, f)

print("Saved train.bin, val.bin and meta.pkl in:", output_dir)
