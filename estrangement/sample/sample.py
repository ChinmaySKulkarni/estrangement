#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sample script demonstrating the use of the Estrangement library to plot temporal communities. 
"""

__author__ = """\n""".join(['Vikas Kawadia (vkawadia@bbn.com)',
                            'Sameet Sreenivasan <sreens@rpi.edu>',
                            'Stephen Dabideen <dabideen@bbn.com>'])

#   Copyright (C) 2012 by 
#   Vikas Kawadia <vkawadia@bbn.com>
#   Sameet Sreenivasan <sreens@rpi.edu>
#   Stephen Dabideen <dabideen@bbn.com>
#   All rights reserved. 
#   BSD license. 


import sys
import os
sys.path.append(os.getcwd() + "/..")
sys.path.append(os.getcwd() + "../..")
import options_parser
import plots
import estrangement
import multiprocessing

# use argparse to parse command-line arguments using optionsadder.py
opt = options_parser.parse_args()

# set the values of delta for which to create plots
deltas = [0.01,0.025,0.05,1.0]

# check if there are results for these deltas
for d in deltas:
    if(os.path.isfile(opt.exp_name + "/task_delta_" + str(d) + "/matched_labels.log")):
        print("WARNING: Using existing results for delta=" +str(d) + ".\n \tIf you wish to repeat the simulation, please delete the directory: \"%s\" !! "%(d,opt.exp_name))


# dictionary to pass the simulation output to the plot function
matched_labels_dict = {}

# A folder is created, specified by the --exp_name argument in 
# the current working directory and all the files from the experiment will
# be placed in this file. 
if(not os.path.exists(opt.exp_name)):
    os.mkdir(opt.exp_name)
os.chdir(opt.exp_name)

q = multiprocessing.Queue()

for d in deltas:
    # check if the matched_labels.log file file exists, and prompt the user if it does 
    label_file = "task_delta_" + str(d) + "/matched_labels.log"
    if(os.path.isfile(label_file) and os.path.getsize(label_file) > 0 ):
	print(d)
        with open("task_delta_" + str(d) + "/matched_labels.log", 'r') as ml:
            matched_labels = ml.read()
            matched_labels_dict[str(d)] = eval(matched_labels)

    # run the simulation if the matched_labels.log file does not exist
    # run multiple processes in parallel, each for a different value of delta
    else:
	print("Running simulations for delta=%d"%d)
        p = multiprocessing.Process(target=estrangement.ERA,args=(opt.dataset_dir,opt.precedence_tiebreaking,opt.tolerance,opt.convergence_tolerance,d,opt.minrepeats,opt.increpeats,500,False,q))
        p.start()

# combine the results stored in the queue into a single dictionary
for d in deltas:
        entry = q.get()
        for k in entry.keys():
                matched_labels_dict[k] = entry[k]
        matched_label_file = open("task_delta_" + k +"/matched_labels.log", 'w')
        matched_label_file.write(str(matched_labels_dict[k]))
        matched_label_file.close()

# plot the temporal communities 
plots.plot_temporal_communities(matched_labels_dict)
os.chdir("..")


# to plot other parameters, set write_stats=True in estrangement.ERA() 
# and use plots.plot_function(). For example,
# plots.plot_function(['Estrangement'])
# plots.plot_function(['ierr','feasible'])

