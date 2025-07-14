from tokenizers import ByteLevelBPETokenizer
from pathlib import Path

# path to your merged and cleaned text file

corpus_path = "london_corpus_cleaned_merged.txt"

# Output directory for tokenizer files
output_dir = "tokenizer_london"


Path(output_dir).mkdir(exist_ok=True)

# Initialize and train tokenizer
tokenizer = ByteLevelBPETokenizer()

print("Training tokenizer...")
tokenizer.train(files=[corpus_path], vocab_size=50000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

# save tokenizer files
tokenizer.save_model(output_dir)


print(f" Tokenizer saved to: {output_dir}")
