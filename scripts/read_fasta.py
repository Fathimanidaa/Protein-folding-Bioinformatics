from Bio import SeqIO

def read_fasta(file_path):
    record = SeqIO.read(file_path, "fasta")
    print("Protein ID:", record.id)
    print("Sequence:")
    print(record.seq)

# Example usage
read_fasta("../data/sample_protein.fasta")
