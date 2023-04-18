from Bio import SeqIO
fasta_file = "3AO60469"
for record in SeqIO.parse(fasta_file, "fasta"):
    print(record.id)
    print(record.seq)