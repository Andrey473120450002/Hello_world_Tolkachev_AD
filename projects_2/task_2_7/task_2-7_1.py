files = ["seq1", "seq2", "seq3", "seq4"]
date = "01.01.2026" 
for name in files:
    new_name = f"{name}_{date}.fasta"
    print(new_name)