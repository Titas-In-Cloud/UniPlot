def average_len(records):
    """Returns the average length for records"""
    protein_amount = 0
    total_protein_lenght = 0
    for lenght in records:
        protein_amount = protein_amount + 1
        total_protein_lenght = total_protein_lenght + len(lenght.seq)

    avg_protein_lenght = total_protein_lenght / protein_amount

    return avg_protein_lenght

def average_len_taxa(records):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
