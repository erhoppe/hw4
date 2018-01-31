import csv
import numpy as np

#### Import files #####
score_fn = "/home/erhoppe/PycharmProjects/hw4_multiD_arrays/blossum.tsv"
protein_fn= "/home/erhoppe/PycharmProjects/hw4_multiD_arrays/insulin.fasta"


#### Functions ####
def print_dict(d):
    for key in sorted(d):
        print("%s --> %s" % (key, d[key]))

def print_list(l):
    for item in l:
        print(item)

def read_scores(filename):
    try:
        f = open(filename, 'r')
    except IOError:
        print("The file %s does not exist" % filename)
        return
    else:
        aas = [aa for aa in f.readline().strip().split() if aa];
        lines = [line.strip() for line in f]
        score_d = {  # build a 2d dictionary of scores
            line[0]: {aa_top: score for aa_top, score in zip(aas, line[1:].split())}
            for line in lines
            }
        f.close()
        return(aas,score_d)

def read_fasta(filename):
    try:
        f = open(filename,'r')
        print("opened %s" % filename)
    except IOError:
        print("The file %s does not exist" % filename)
        return
    else:
        seq_list = [line.strip() for line in f if line[0] is not '>' and line.strip()] #add if not a header line or blank, assumes one line per sequence
        return seq_list

def make_3D_array(seq_list):
    i_len, j_len, k_len = (len(element) for element in seq_list)
    arr = np.zeros((i_len+1,j_len+1,k_len+1)) #default data type is float64, which should be enough
    return arr #dimensions are seq1 x seq2 x seq3 lengths





#### Program ####

#Read in files
aa_list, score_dict = read_scores(score_fn)
protein_list = read_fasta(protein_fn)

node_max_arr = make_3D_array(protein_list)
node_ptr_arr = make_3D_array(protein_list)

