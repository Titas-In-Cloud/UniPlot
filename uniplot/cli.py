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

def pie_plot_average_by_taxa(args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_pie_show(av)

def cli():
    parser = argparse.ArgumentParser(prog = "uniplot", usage = '%(prog)s [options]')

    subparsers = parser.add_subparsers(help = "Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=name_list)
    subparsers.add_parser("average").set_defaults(func=proteins_average_lenght)
    subparsers.add_parser("bar_average-by-taxa").set_defaults(func=bar_plot_average_by_taxa)
    subparsers.add_parser("pie_average-by-taxa").set_defaults(func=pie_plot_average_by_taxa)

    parser.add_argument('--dump', help = 'gives a list with all the information about proteins '
                                         '- protein sequence, ID, name, lenght, description and other '
                                         'related data')
    parser.add_argument('--list', help = 'gives a list with only the lenghts of proteins')
    parser.add_argument('--average', help = 'gives average lenght of all proteins')
    parser.add_argument('--bar_average-by-taxa', help = 'gives average lenght of proteins categorized '
                                                        'by type in a form of a bar chart')
    parser.add_argument('--pie_average-by-taxa', help = 'gives average lenght of proteins categorized '
                                                        'by type in a form of a pie chart')

    args = parser.parse_args()

    args.func(args)
