import argparse
from uniplot import plot

from . import parse
from . import analysis

LOC = "uniprot_receptor.xml.gz"
POC = "./resources/uniprot_sprot_small.xml.gz"

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def name_list(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def proteins_average_lenght(args):
    print("Average Length is {}".format(analysis.average_len(parse.uniprot_seqrecords(LOC))))

def bar_plot_average_by_taxa(args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def cli():
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=name_list)
    subparsers.add_parser("average").set_defaults(func=proteins_average_lenght)
    subparsers.add_parser("bar_average-by-taxa").set_defaults(func=bar_plot_average_by_taxa)

    args = parser.parse_args()

    args.func(args)
