from . import parse

LOC="uniprot_receptor.xml.gz"

protein_amount = 0
total_protein_lenght = 0
avg_protein_lenght = 0

def average_len(records):
    global protein_amount
    global total_protein_lenght
    for lenght in parse.uniprot_seqrecords(LOC):
        protein_amount = protein_amount + 1
        total_protein_lenght = total_protein_lenght + len(lenght)

    avg_protein_lenght = total_protein_lenght / protein_amount

    return avg_protein_lenght
