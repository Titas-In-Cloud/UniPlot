def average_len(records):
    """Returns the average length for records"""
    protein_amount = 0
    total_protein_lenght = 0
    for lenght in records:
        protein_amount = protein_amount + 1
        total_protein_lenght = total_protein_lenght + len(lenght.seq)

    avg_protein_lenght = total_protein_lenght / protein_amount

    return avg_protein_lenght

def average_len_taxa(records, depth):
    """Returns the average length of proteins categorized by taxa"""
    record_by_taxa = {}

    depth = int(input("Please, enter the depth level of taxa: "))
    depth = depth - 1

    for r in records:
        try:
            taxa = r.annotations["taxonomy"][depth]
            record_by_taxa.setdefault(taxa, []).append(r)

        except IndexError:
            ()

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
