import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    """Parses (analyses) the uniprot-xml data file"""
    records = []

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append(record)

    return records
