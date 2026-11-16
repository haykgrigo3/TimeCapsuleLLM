import os
import csv
from torch.utils.data import Dataset, DataLoader

class LondonCorpus(Dataset):
    def __init__(self, meta_csv, books_dir, london_multiplier=5):
        
        self.entries = []
        with open(meta_csv, newline='', encoding='utf-8') as f:
           
            reader = csv.DictReader(f)
            for row in reader:
                
                # make sure your metadata.csv has a 'region' column set to "London" 
               
                path = os.path.join(books_dir, row['filename'])
                if not os.path.exists(path):
                    continue
                # Oversample London docs by repeating the path
                multiplier = london_multiplier if row.get('region','') == 'London' else 1
                
                for _ in range(multiplier):
                    self.entries.append(path)

    def __len__(self):
        
        return len(self.entries)

    def __getitem__(self, idx):
        
        path = self.entries[idx]
        # You could tokenize here instead of returning raw text
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        return text

# Usage example
if __name__ == "__main__":
    dataset = LondonCorpus('metadata_london.csv', 'books_london', london_multiplier=5)
    loader  = DataLoader(dataset, batch_size=4, shuffle=True)

    # Iterate one batch of raw texts
    for batch in loader:
        print(batch)   
        break
