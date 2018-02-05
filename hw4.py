#import csv
import numpy as np
import time

#### Import files #####
score_fn = "blossum.tsv"
protein_fn = "insulin.fasta"#"test_prots.fasta"


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
            line[0]: {aa_top: float(score) for aa_top, score in zip(aas, line[1:].split())}
            for line in lines
            }
        f.close()
        return(aas,score_d)

def read_fasta(filename):
    try:
        f = open(filename,'r')
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

def get_aa(seq_num,aa,aai):
    if aa == aai:
        return "-"
    else:
        return protein_list[seq_num][aa]

def combinations(str): #list comp to get the three combos
    return [ [ci,str[j]]
            for i,ci in enumerate(str)
            for j in range(i+1,len(str))]


def get_trio_score(str):
    comb_list = combinations(str)
    if str.count('-') == 2:
        return float(gap_score*2) #if you have two gaps, just assign double the gap penalty
    else:
        return sum([score_dict[pair[0]][pair[1]] if "-" not in pair else gap_score for pair in comb_list])


def edge_score(x,y,z, xi,yi,zi):
        #lookup in dictionary
    trio = get_aa(0,x,xi) + get_aa(1,y,yi) + get_aa(2,z,zi)
    if trio in trio_score_dict:
        edge_hist[trio] += 1
        return trio_score_dict[trio]
    else:
        #calculate score
        score = get_trio_score(trio)
        #add to dictionary
        trio_score_dict[trio] = score
        edge_hist[trio] = 1
        return score

def bequeath_scores(x,y,z,val):
    parent_coords = np.array([x,y,z])
    child_coords = parent_coords + np.array([[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
    parent_score = node_max_arr[x][y][z]
    for (xi,yi,zi) in child_coords:
        try:
            child_score = node_max_arr[xi][yi][zi]
            new_score = edge_score(x,y,z, xi,yi,zi) + parent_score
            if new_score >= child_score: #used greater or equals so I can still get the start, which might be zero
                node_max_arr[xi][yi][zi] = new_score
                max_par_dict[(xi,yi,zi)] = (x,y,z)
        except IndexError:
            pass #hacky...but should work for cases when the child doesn't exist

def traceback(child_ind): #traces back from max(as determined by the numpy array), printing out alignments
    ind = child_ind
    reverse_alignment = []
    while ind in max_par_dict:
        #print(ind)
        par_ind = max_par_dict[ind] #retrieve parent index
        align_coords = list(zip(par_ind,ind))
        aligned_trio = ''.join([get_aa(i,align_coords[i][0],align_coords[i][1]) for i in range(3)])
        reverse_alignment.append(aligned_trio)
        ind = par_ind
    return reversed(reverse_alignment) #right side up return, all but the last which wasn't part of it since it doesn't have a parent in dict


#### Program ####

t = time.clock()

#Read in files
aa_list, score_dict = read_scores(score_fn)
gap_score = float(-6)
protein_list = read_fasta(protein_fn)

node_max_arr = make_3D_array(protein_list) #numpy array to hold things; should be one of the fastest ways
trio_score_dict = {}
max_par_dict = {}
edge_hist = {}

a_len, b_len, c_len = node_max_arr.shape

#File header print stuff
print("Assignment: GS540 HW4")
print("Name: Emma Hoppe")
print("Email: erhoppe@uw.edu")
print("Language: Python3 ( >>> C++)")
print("Runtime: 36 seconds")
print("")

for (a,b,c), value in np.ndenumerate(node_max_arr): #yay fast numpy iteration
    bequeath_scores(a,b,c,value)

#for key,value in sorted(trio_score_dict.items()):
#    print(key,": ", int(value))

max_ind = np.unravel_index(np.argmax(node_max_arr,axis=None), node_max_arr.shape)
print("Score: ", node_max_arr[max_ind])
print("")
print("Edge weights:")
for key,value in sorted(trio_score_dict.items()):
    print(key," = ", int(value))

print("")
print("Edge counts:")
for key,value in sorted(edge_hist.items()):
    print (key, " = ", int(value))

max_alignment = traceback(max_ind)
print("")
print("Local alignment:")
for row in max_alignment:
    print(row)



print(time.clock() - t, " seconds")