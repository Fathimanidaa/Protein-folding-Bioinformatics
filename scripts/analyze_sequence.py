from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt
import os

def analyze_protein(file_path):
    # Read the sequence from the FASTA file
    record = SeqIO.read(file_path, "fasta")
    sequence = str(record.seq)

    # Analyze protein
    analyzer = ProteinAnalysis(sequence)
    length = len(sequence)
    molecular_weight = analyzer.molecular_weight()
    amino_acid_count = analyzer.count_amino_acids()

    # Prepare output folder
    os.makedirs("../output", exist_ok=True)

    # Save report to a text file
    with open("../output/sequence_report.txt", "w") as report:
        report.write(f"Protein ID: {record.id}\n")
        report.write(f"Length: {length} amino acids\n")
        report.write(f"Molecular Weight: {molecular_weight:.2f} Da\n")
        report.write("Amino Acid Composition:\n")
        for aa, count in amino_acid_count.items():
            report.write(f"  {aa}: {count}\n")

    # Plot amino acid frequency
    plt.figure(figsize=(10, 5))
    plt.bar(amino_acid_count.keys(), amino_acid_count.values(), color="skyblue")
    plt.title("Amino Acid Frequency")
    plt.xlabel("Amino Acid")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("../output/amino_acid_frequency.png")
    plt.close()

    print("✅ Analysis complete! Report saved to 'output/' folder.")

# Run the analysis
analyze_protein("../data/sample_protein.fasta")

