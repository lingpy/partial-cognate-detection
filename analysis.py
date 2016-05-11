"""
Code computes the partial cognate detection analysis in various flavors.
"""
from __future__ import division, print_function
from util import pcd_path
from lingpy.evaluate.acd import bcubes, partial_bcubes
from lingpy.compare.partial import Partial
from lingpy.compare.lexstat import LexStat
from sys import argv

infiles = ['Chinese-180-18', 'Bai-110-9', 'Tujia-109-5']

if len(argv) > 1:
    if 'file' in argv:
        infiles = [argv[argv.index('file')+1]]

ccubes = []

def pprint_result(f, mode, t, p, r, fs):
    print('{0:15}   {1:30}   {2}   {3:.2f}   {4:.2f}   {5:.2f}'.format(
        f, mode, ts, p, r, fs))

methods = ['sca', 'lexstat']
cluster_methods = ['infomap', 'mcl', 'upgma']
measures = ['partial', 'strict', 'loose']

for f in infiles:
    try:
        lex = Partial(pcd_path('data', 'BIN_'+f+'.tsv'))
    except IOError:
        lex = Partial(pcd_path('data', f+'.tsv'))
        lex.get_scorer(
                preprocessing=False, 
                runs=10000,
                )
        lex.output('tsv', filename=pcd_path('data', 'BIN_'+f[2:]))

    # create new reference ids for cogantes from partial cognates
    if not 'strict_cogid' in lex.header:
        lex.add_cognate_ids('partialids', 'strict_cogid', 'strict')
    if not 'loose_cogid' in lex.header:
        lex.add_cognate_ids('partialids', 'loose_cogid', 'loose')

    for i in range(1,20):
        print("Analyzing {0} with t={1}...".format(f, i))
        t = 0.05 * i
        ts = '{0:.2f}'.format(t).replace('0.','')

        for m in methods:
            msf = 'f_'+m
            for cm in cluster_methods:
                ms = '{0}_{1}_{2}'.format('p', m, cm)
                msf = '{0}_{1}_{2}'.format('f', m, cm)
                msp = ms +'_'+ts

                lex.partial_cluster(method=m, cluster_method=cm, threshold=t, ref=msp)

                # get loose and strict cognate ids for this method
                lex.add_cognate_ids(msp, ms+'_strict'+'_'+ts, 'strict')
                lex.add_cognate_ids(msp, ms+'_loose'+'_'+ts, 'loose')

                # get the bcubes
                for mode in ['strict', 'loose']:
                    msm = ms+'_'+mode+'_'+ts
                    p, r, fs = bcubes(lex, mode+'_cogid', msm,
                            pprint=False)
                    pprint_result(f, msm, ts, p, r, fs)
                    ccubes += [[msm, f, t, ts, p, r, fs]]
                p, r, fs = partial_bcubes(lex, 'partialids', msp, pprint=False)
                pprint_result(f, msp, ts, p, r, fs)
                ccubes += [[msp, f, t, ts, p, r, fs]]
                
                lex.cluster(method=m, cluster_method=cm, threshold=t,
                        ref=msf+'_'+ts)
                for mode in ['strict', 'loose']:
                    p, r, fs = bcubes(lex, mode+'_cogid', msf+'_'+ts,
                            pprint=False)
                    pprint_result(f,msf+'_'+mode+'_'+ts, ts, p, r, fs)
                    ccubes += [[msf+'_'+mode+'_'+ts, f, t, ts, p, r, fs]]
       
with open('results.tsv', 'w') as f:
    for line in ccubes:
        f.write('\t'.join([str(x) for x in line])+'\n')

