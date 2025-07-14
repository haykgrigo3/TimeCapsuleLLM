import tiktoken
from pathlib import Path

# Load and read your merged corpus
corpus_path = Path("london_corpus_cleaned_merged.txt")

with open(corpus_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Tokenizer settings
vocab_size = 50000  # Just increase for more vocabulary coverage

output_dir = Path("tokenizer_london")

output_dir.mkdir(exist_ok=True)

# training
print("Training tokenizer...")
enc = tiktoken.train_new_bpe(
    raw_text,
    vocab_size=vocab_size,
    special_tokens=["<|endoftext|>"]

)

# saves tokenizer files
enc.save_model(str(output_dir))
print(f"Tokenizer saved to {output_dir}")
