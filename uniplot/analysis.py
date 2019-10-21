from . import parse

LOC = "uniprot_receptor.xml.gz"
POC = "./resources/uniprot_sprot_small.xml.gz"

protein_amount = 0
total_protein_lenght = 0
avg_protein_lenght = 0

def proteins_average_lenght(records):
    global protein_amount
    global total_protein_lenght
    for lenght in parse.uniprot_seqrecords(POC):
        protein_amount = protein_amount + 1
        total_protein_lenght = total_protein_lenght + len(lenght)

    avg_protein_lenght = total_protein_lenght / protein_amount

    return avg_protein_lenght
