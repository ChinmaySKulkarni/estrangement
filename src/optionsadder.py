import os
import argparse

""" OptionsAdder: Helper function for parsing arguments from the command line or a config file"""

__all__ = ['parse_args','add_options']
__author__ = """\n""".join(['Vikas Kawadia (vkawadia@bbn.com)',
                            'Sameet Sreenivasan <sreens@rpi.edu>'])

#   Copyright (C) 2012 by 
#   Vikas Kawadia <vkawadia@bbn.com>
#   Sameet Sreenivasan <sreens@rpi.edu>
#   All rights reserved. 
#   BSD license. 

 


def parse_args():
    """@brief parse cmd line and conf file options 
    @returns opt  as returned by argsparse.parse_args"""
    # read in options from cmdline and conffile
    usage="""usage: %prog [options] (--help for help)\n"""

    parser = argparse.ArgumentParser(description="Estrangement Confinement Algorithm",
         fromfile_prefix_chars='@')

    add_options(parser)
    opt = parser.parse_args()
    return opt

def add_options(parser):
    """define all the program options here"""
    parser.add_argument("--dataset_dir",
            dest="dataset_dir", 
            help="dir where all the datasets are stored [default: %default]",
            type=str,
            default=os.path.join(os.path.expanduser("~"), "datasets")
    )


    parser.add_argument("-e", "--precedence_tiebreaking",
            dest="precedence_tiebreaking", 
            help="turn on precedence tiebreaking which keeps a node's current label if it is one of the dominant lables. [default: %default]",
            action="store_true",
            default=False
    )

    parser.add_argument("--maxfun",
            dest="maxfun", 
            help="max number of iterations allowed for scipy optimize [default: %default]",
            type=int,
            default=200
    )

 
    parser.add_argument("--tolerance",
            dest="tolerance", 
            help="tolerance as a fraction of the max when picking dominant labels [default: %default]",
            type=float,
            default=0.00001
    )
    
    parser.add_argument("--convergence_tolerance",
            dest="convergence_tolerance", 
            help="lambda (X) tolerance for scipy optimize [default: %default]",
            type=float,
            default=0.01
    )

    parser.add_argument("--delta",
            dest="delta", 
            help="constraint on estrangement [default: %default]",
            type=float,
            default=0.05
    )
    
    
    parser.add_argument("--minrepeats",
            dest="minrepeats", 
            help="min number of repeats for each snapshot [default: %default]",
            type=int,
            default=10
    )

    parser.add_argument("--increpeats",
            dest="increpeats", 
            help="number of repeats in increased by this amount for every call to g_of_lambda [default: %default]",
            type=int,
            default=10
    )


    parser.add_argument("--savefor_layouts",
            dest="savefor_layouts",
            type=bool,
            help="Save gexf for layouts [default: %default]",
            default=False
    )

    parser.add_argument("-x", "--xfigsize",
            dest="xfigsize",
            help="fig width in inches [default: %default]",
            type=float,
            default=16.0
    )

    parser.add_argument("-y", "--yfigsize",
            dest="yfigsize",
            help="fig height in inches [default: %default]",
            type=float,
            default=12.0
    )

    parser.add_argument("--tiled_figsize",
            dest="tiled_figsize",
            help="tuple of figsize for the tiled plots [default: %default]",
            type=str,
            default='(36,16)'
    )


    parser.add_argument("-m", "--markersize",
            dest="markersize",
            help="marker size in points [default: %default]",
            type=float,
            default=15
    )
    parser.add_argument("--markerheight",
            dest="markerheight",
            help="marker height as a fraction of markersize [default: %default]",
            type=float,
            default=0.2
    )

    parser.add_argument("--xtick_separation",
            dest="xtick_separation",
            help="separation of labels on the x axis [default: %default]",
            type=int,
            default=5
    )


    parser.add_argument("--linewidth",
            dest="linewidth",
            help="linewidth in pts [default: %default]",
            type=float,
            default=2.0
    )


    parser.add_argument("--seed",
            dest="seed",
            help="seed for randomizing label indices [default: %default]",
            type=int,
            default=1378389
    )

    parser.add_argument("--label_sorting_keyfunc",
            dest="label_sorting_keyfunc",
            help="keyfunc for sorting label indices so that patches dont get nearby colors in the the colormap [default: %default]. Identity implies sorting by label values. Also see the seed option above.",
            type=str,
            default="random"
    )

    parser.add_argument("--fontsize",
            dest="fontsize",
            help="fontsize for figure text [default: %default]",
            type=float,
            default=28
    )
    parser.add_argument("--label_fontsize",
            dest="label_fontsize",
            help="fontsize for axis labels [default: %default]",
            type=float,
            default=20
    )


    parser.add_argument("--alpha",
            dest="alpha",
            help="figure transparency [default: %default]",
            type=float,
            default=1.0
    )


    parser.add_argument("--dpi",
            dest="dpi",
            help="dpi for savefig [default: %default]",
            type=int,
            default=200
    )

    parser.add_argument("--wspace",
            dest="wspace",
            help="whitespace between subplots [default: %default]",
            type=float,
            default=0.2
    )

    parser.add_argument("--bottom",
            dest="bottom",
            help="whitesapce below subplots [default: %default]",
            type=float,
            default=0.1
    )

    parser.add_argument("--frameon",
            dest="frameon",
            help="set frameon on each axis True or False [default: %default]",
            type=bool,
            default=True
    )
    parser.add_argument("--delta_to_use_for_node_ordering",
            dest="delta_to_use_for_node_ordering",
            help="delta value to use for node ordering on the tiles plots [default: %default]",
            type=float,
            default=1.0
    )

    parser.add_argument("--deltas_to_plot",
            dest="deltas_to_plot",
            help="deltas_to_plot in the dynconsuper plot [default: %default]",
            type=list,
            default=[]
    )

    parser.add_argument("--manual_colormap",
            dest="manual_colormap",
            help="dict of label_indices to colors to use for the patches in the dynconsuper plot [default: %default]",
            type=str,
            default=None
    )


    parser.add_argument("--title",
            dest="title",
            help="title text [default: %default]",
            type=str,
            default="Dynamic communities"
    )

    parser.add_argument("--xlabel",
            dest="xlabel",
            help="xlabel [default: %default]",
            type=str,
            default="Time"
    )

    parser.add_argument("--ylabel",
            dest="ylabel",
            help="ylabel [default: %default]",
            type=str,
            default="Node id"
    )
    parser.add_argument("--label_cmap",
            dest="label_cmap",
            help="color map for communities [default: %default]",
            type=str,
            default='Paired'
    )


    parser.add_argument("--display_on",
            dest="display_on",
            help="display label plot after each task is done [default: %default]",
            type=bool,
            default=False
    )


    parser.add_argument("--show_title",
            dest="show_title",
            help="show title on plots [default: %default]",
            type=bool,
            default=True
    )


    parser.add_argument("--use_separate_label_indices",
            dest="use_separate_label_indices",
            help="set to true if labels are not from the space of nodenames [default: %default]",
            type=bool,
            default=True
    )

    parser.add_argument("--colorbar",
            dest="colorbar",
            help="display colorbar if true [default: %default]",
            type=bool,
            default=True
    )

    parser.add_argument("--show_yticklabels",
            dest="show_yticklabels",
            help="display yticklabels if true [default: %default]",
            type=bool,
            default=False
    )

    parser.add_argument("--loglevel",
            dest="loglevel",
            choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
            help="Set console logging level to LEVEL [default: %default]",
            metavar="LEVEL",
            default="INFO"
    )

    parser.add_argument("--node_indexing",
            dest="node_indexing",
            help="node indexing scheme [default: %default]",
            type=str,
            default='fancy'
    )

    parser.add_argument("--nodeorder",
            dest="nodeorder",
            help="psecify node order for tiled plots [default: %default]",
            type=str,
            default=None
    )



    parser.add_argument("--nodelabel_func",
            dest="nodelabel_func",
            help="func which provides node names to display, it should return a dict from nodes in the graph to node name strs to display[default: %default]",
            type=str,
            default=None
    )

    parser.add_argument("--nodes_of_interest",
            dest="nodes_of_interest",
            help="only show labels ever taken by the node in this list, can be specified multiple times[default: %default]",
            type=list,
            action="append"
    )


    parser.add_argument("--snaphotlabel_func",
            dest="snapshotlabel_func",
            help="func which provides snapshot names to display, it should return a dict from nodes in the graph to snapshot name strs to display[default: %default]",
            type=str,
            default=None
    )

    parser.add_argument("--image_extension",
            dest="image_extension",
            help="image_extension [default: %default]",
            type=str,
            default="svg"
    )

    parser.add_argument("--partition_file",
            dest="partition_file",
            help="name of the file from which to read matched partitions (simplified_matched_labels.log is max weight matching and matched_labels.log is max mutual overlap) [default: %default]",
            type=str,
            default="matched_labels.log"
    )

    parser.add_argument("--profiler_on",
        dest="profiler_on",
        help="turn profiling using cProfile on [default: %default], saves output to profile_output_filename",
        type=bool,
        default=True
    )


