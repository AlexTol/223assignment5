import requests
import json
import os
import sys

def completeMatchCount(mGRNA, Genome):
    Genome = ''.join(Genome.strip().split('\n'))
    
    forward = Genome
    backwards = Genome[::-1]

    score = 0
    for i in range(0, len(Genome)-19):
        string1 = ''
        string2 = ''
        for j in range(0,20):
            try:
                string1 += forward[i+j]
                string2 += backwards[i+j]
                print(str(j) + backwards[i+j])
            except IndexError:
                print('out of range')
        
        string1 = string1.splitlines()
        string1 = ''.join(string1)
        string2 = string2.splitlines()
        string2 = ''.join(string2)
        print(string1)
        print(string2)
        score += completeMatch(mGRNA,string1) + completeMatch(mGRNA,string2)


    return score


def completeMatch(g, s):
    comp_dict = {'A':'T','T':'A','C':'G','G':'C','Y':'R','R':'Y','W':'W','S':'S','K':'M','M':'K','N':'N'}
    for i in range(0,20):
        if(g[i] != comp_dict[s[i]]):
            return 0

    return 1

site = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
params = {}
params['db'] = 'nucleotide'
params['id'] = 'NC_014426.2'
params['from'] = '1078419'
params['to'] = '1079394'
params['rettype'] = 'fasta'

r = requests.get(site, params = params)
genome = r.text[130:]
grna = 'AATGAAGGTGGTTCCGACTT'

print(genome)
print(completeMatchCount(grna,genome))