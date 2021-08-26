from graphviz import Digraph
import json
import numpy as np
from copy import deepcopy
from collections import OrderedDict
import sys

from cx_network import cxReader
from cx_network import FDNPlotter


if __name__ == "__main__":
    import argparse
    if True:
        parser = argparse.ArgumentParser()
        parser.add_argument("--show_workflow",
                            help="show workflows", action="store_true")
        parser.add_argument(
            "--show_is_a", help="show is-a relation", action="store_true")
        parser.add_argument("--output_filename", help="output name",
                            default="output.cx")
        parser.add_argument("--name", help="Network name",
                            default="fd_network")
        parser.add_argument("file", nargs="+")
        args = parser.parse_args()

        filename_list = args.file

    cxreader_list = []
    for filename in filename_list:
        if "is-a" in filename:
            type_ = "is-a"
        else:
            type_ = "workflow"
        cxreader = cxReader(filename)
        cxreader.make_network(type_)
        if type_ == "workflow" and args.show_workflow:
            cxreader.graphviz_workflow(filename+".png")
        if type_ == "is-a" and args.show_is_a:
            cxreader.graphviz_workflow(filename+".png", rankdir="TB")

        cxreader_list.append(cxreader)

    plotter = FDNPlotter(cxreader_list)

    # plotter.graphviz_fd_network("df_network")
    plotter.cx_fd_network(args.name, args.output_filename)
