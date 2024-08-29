# findBlockers.py
# HJ v0.2 - 29/08/24
# Generate and test putative blocking oligos for use in target enrichment

# Changelog
# 0.2:
# - arguments added for command line use
# - accept xlsx input for sequence list rather than hardcoded dict
# - remove rough heterodimer calculation, to be redone at some point!

# Imports
#import primer3 # Only used for heterodimer calculation
import argparse
import random as rand
import pandas as pd
from Bio.SeqUtils import MeltingTemp

# Variables
count = 0

# Functions

# generate a string of random bases. Maybe naive but works
def randomSeqs(nbases):
    
    seq = rand.choices(('A', 'T', 'C', 'G'), k = nbases)
    seq = ''.join(seq)
    global count 
    count += 1
    
    return(seq)

# finds a putative blocker for each input sequence. Loops until an option is found within the melting temp range
def findBlockers(nbases, name, seq, minMelt, maxMelt):
    
    randomBases = randomSeqs(nbases)
    temp = MeltingTemp.Tm_GC(f'{randomBases}{seq}')
    
    while temp <= minMelt or temp >= maxMelt:
        
        randomBases = randomSeqs(nbases)
        temp = MeltingTemp.Tm_GC(f'{randomBases}{seq}')
    
    return(f'{randomBases}{seq}', temp)
        
# Main loop #
if __name__ == '__main__': 
    
    # setup argument handling
    parser = argparse.ArgumentParser(
        prog = 'findBlockers.py',
        description = 'Generate putative blocking oligos for use in target enrichment')
    
    parser.add_argument('-m', '--minMelt', default = 63.4,
                        help = 'minimum oligo melting temperature. Default is 63.4')
    parser.add_argument('-M', '--maxMelt', default = 65.6,
                        help = 'maximum oligo melting temperature. Default is 65.6')
    
    parser.add_argument('-n', '--nbases', default = 8,
                        help = 'number of bases to prepend. Default is 8')
    
    parser.add_argument('-b', '--barcodes',  required = True,
                        help = 'excel file containing two columns: [barcode_names] [barcodes_sequences]')
    
    parser.add_argument('-o', '--output',  default = 'output',
                        help = 'directory and name for writing output. Default is output.xlsx')
    args = parser.parse_args()
    
    # testing stuff (REMOVE THIS)
    #seqList = pd.read_excel('ont_pcr_barcodes.xlsx')
    
    # convert out input xlsx into a dataframe, and then generate an empty one to take output
    seqList = pd.read_excel(args.barcodes)
    blockerList = pd.DataFrame(columns = ['Name', 'Sequence', 'meltingTemp'], index = seqList.index.copy())
    
    # loop over each sequence and run findBlockers on it, saving output to dataframe
    for i in range(0, len(seqList)):
        
        name, seq = seqList['barcode_name'][i], seqList['barcode_sequence'][i]
        
        temp = findBlockers(args.nbases, name, seq, args.minMelt, args.maxMelt)
        
        blockerList.loc[i, 'Name'] = f'{name}_block'
        blockerList.loc[i, 'Sequence'] = temp[0]
        blockerList.loc[i, 'meltingTemp'] = temp[1]
        
    blockerList.to_excel(f'{args.output}.xlsx', index = False)
 
print(f'##############################\nfound {len(seqList)} blockers in {count} tries\noutput written to {args.output}.xlsx\n##############################')