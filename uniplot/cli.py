import argparse

from . import parse
from . import analysis

LOC="uniprot_receptor.xml.gz"

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def name_list(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def length_test(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(len(record))

def proteins_average_lenght(args):
    print("Average Length is {}".format(analysis.average_len(parse.uniprot_seqrecords(LOC))))

def cli():
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=name_list)
    subparsers.add_parser("test").set_defaults(func=length_test)
    subparsers.add_parser("average").set_defaults(func=proteins_average_lenght)

    args = parser.parse_args()

    args.func(args)
