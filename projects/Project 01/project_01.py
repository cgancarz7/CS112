"""
Project 01 Template File

CS/BIOS 112 - Project 01

   Describe
   Project 01 
   Here
   

@author:    <your name here>
UIC NetID:  <your NetID here>
Due Date:   <due date here>
"""


# The following function should NOT be modified!!
def read_one_seq_fasta(fasta_file):
    """Read a FASTA file that contains one sequence."""
    seq = ''
    with open(fasta_file, 'r') as f:
        f.readline()  # by pass description in first line of data file
        for line in f.readlines():
            seq = seq + line[:-1]
    return seq
# The above function should NOT be modified!!!

def gc_content(seq):
    ''' describe function here '''
    pass


# Tests for gc_content function. Should print True in all cases.
print('\ngc_content Tests')
print(gc_content('ATGTGAA') == 0.2857142857142857)
print(gc_content('ATGAGATAAG') == 0.3)


def get_orf(seq):
    ''' describe function here '''
    stop_codons = ['TAG', 'TAA', 'TGA']
    pass


# Tests for get_orf function. Should print True in all cases.
print('\nget_orf Tests')
print(get_orf('ATGTGAA') == 'ATG')
print(get_orf('ATGAGATAAG') == 'ATGAGA')
print(get_orf('ATGAGATAGG') == 'ATGAGA')
print(get_orf('ATGAGATGAGGGTAA') == 'ATGAGA')
print(get_orf('ATGAAATT') == 'ATGAAATT')


def one_frame(seq):
    ''' describe function here '''
    start_codon = 'ATG'
    pass


# Tests for one_frame function. Should print True in all cases.
print('\none_frame')
print(one_frame('ATGTGAA') == ['ATG'])
print(one_frame('ATGAGATAAG') == ['ATGAGA'])
print(one_frame('ATGAGATAGG') == ['ATGAGA'])
print(one_frame('ATGAGATGAGGGTAA') == ['ATGAGA'])
print(one_frame('ATGAAATT') == ['ATGAAATT'])
print(one_frame('ATGAGATGAACCATGGGGTAA') == ['ATGAGA', 'ATGGGG'])


def forward_frames(seq):
    ''' describe function here '''
    pass


# Tests for forward_frames function. Should print True in all cases.
print('\nforward_frames')
print(forward_frames('ATGAGATAAG') == ['ATGAGA'])
print(forward_frames('ATGAGATGAGGGTAA') == ['ATGAGA', 'ATGAGGGTAA'])
print(forward_frames('ATGAAATT') == ['ATGAAATT'])
print(forward_frames('ATGAGATGACACCATGGGGTAA') == ['ATGAGA', 'ATGGGG', 'ATGACACCATGGGGTAA'])


def gene_finder(fasta_file, min_len, min_gc):
    ''' describe function here '''
    pass


# Tests for gene_finder function. Should print True.
print('\ngene_finder')
calculated_result = gene_finder('gene_finder_test.fasta', 6, 0.45)
desired_result = [[6, 0.6666666666666666, 'ATGCCC'], [9, 0.7777777777777778, 'ATGCCCCGG']]
print( calculated_result == desired_result)

orf_list = gene_finder('human_chr9_segment.fasta', 550, 0.45)
print (len(orf_list) == 5)

# viewing the results of the gene_finder( ) calculations
orf_list = gene_finder('gene_finder_test.fasta', 6, 0.45)
print (orf_list)


"""
Identify ORFs in the provided X73525.fasta file

< In this comment, replace this paragraph with the information you learn from the 
  top BLAST hits when using data produced by the results of gene_finder( ) when using 
  the data in the X73525.fasta file on the GenBank website at:
       http://www.ncbi.nlm.nih.gov/blast/Blast.cgi
  Include the parameter values used when you called gene_finder( ).  
  Briefly describe the likely function of your gene and paste your gene information 
  and sequence (length, %GC, and DNA sequence) that you used in the BLAST search. >
"""