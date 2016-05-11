from util import pcd_path
from matplotlib import pyplot as plt
from lingpy import *


converter = dict(
        lexstat = "LexStat",
        sca = "SCA",
        infomap = "Infomap",
        mcl = "Markov",
        strict = "Strict",
        loose = "Loose",
        p = "Partial",
        f = "Normal",
        upgma = "UPGMA",
        )



def get_method(datastring):
    tmp = datastring.split('_')[:-1]
    return '-'.join([converter[x] for x in tmp])

def box_plot_average(methods, markers, colors, data, bcube=-3, labels=[]):
    plt.figure()
    if not labels:
        labels = [m for m in methods]
    scaler = -0.2
    for j, method in enumerate(methods):
        max_val = 0
        max_idx = 0
        best_vals = []
        for i in range(1,20):
            t = i * 0.05
            tmp = [x[-3:] for x in data if get_method(x[0]) == method and x[2] == t]
            
            all_vals = [sum([x[0] for x in tmp]) / len(tmp),
                    sum([x[1] for x in tmp]) / len(tmp),
                    sum([x[2] for x in tmp]) / len(tmp)]
            this_val = all_vals[bcube] 
            bp = plt.boxplot([x[-1] for x in tmp], widths=[0.3], 
                    positions=[i+scaler], patch_artist=True)
            plt.setp(bp['boxes'], color='black')
            plt.setp(bp['boxes'], facecolor=colors[j])
            plt.setp(bp['whiskers'], color='black')
            plt.setp(bp['medians'], color='0', linewidth=0.1,
                linestyle='dashed') #colors[j])
            plt.setp(bp['caps'], color=colors[j])
            plt.setp(bp['fliers'], marker='None')            
            plt.plot(i+scaler, this_val, 'o', color='black', markersize=2)
            if this_val > max_val:
                max_idx = i
                max_val = this_val
                best_vals = all_vals
        plt.plot(max_idx+scaler, max_val, 'v',color='black', markersize=5,
                )
        plt.plot(0, 10, 's', color=colors[j], markersize=10,
                label=labels[j])
        scaler += 0.4

def best_vals(methods, data, bcube=-3):
    for j, method in enumerate(methods):
        max_val = 0
        max_idx = 0
        best_vals = []
        for i in range(1,20):
            t = i * 0.05
            tmp = [x[-3:] for x in data if get_method(x[0]) == method and x[2] == t]
            
            all_vals = [sum([x[0] for x in tmp]) / len(tmp),
                    sum([x[1] for x in tmp]) / len(tmp),
                    sum([x[2] for x in tmp]) / len(tmp)]
            this_val = all_vals[bcube] 
            if this_val > max_val:
                max_idx = i
                max_val = this_val
                best_vals = all_vals
        print('{0:25}\t{1:.4f}\t{2[0]:.4f}\t{2[1]:.4f}\t{2[2]:.4f}'.format(
            method,
            max_idx * 0.05,
            best_vals
            ))
def plot_line_of_dataset(filename, methods, markers, colors, data, bcube=-1, labels=[]):
    plt.clf()
    if not labels:
        labels = [m for m in methods]

    for i, method in enumerate(methods):
        for j,k in zip(range(1,19), range(2,20)):
            t1, t2 = j*0.05, k*0.05
            tmp = [x[-3:] for x in data if get_method(x[0]) == method \
                    and (x[2] == t1 or x[2] == t2) and filename == x[1]]
            tmp1, tmp2 = tmp[0][bcube], tmp[1][bcube] 
            plt.plot([t1, t2], [tmp1, tmp2], markers[i], color=colors[i],
                    linewidth=2)
        plt.plot(0, 10, markers[i], color=colors[i], markersize=10,
                label=labels[i])

infiles = ['Chinese-180-18', 'Bai-110-9', 'Tujia-109-5']
# load data from results file
data = csv2list('results.tsv', dtype=[str, str, float, str, float, float,
    float])


for ds in infiles:
    plot_line_of_dataset(ds, 
            [
                'Partial-LexStat-UPGMA-Strict', 
                'Partial-LexStat-Markov-Strict',
                'Partial-LexStat-Infomap-Strict',
                'Normal-LexStat-UPGMA-Strict',
                'Normal-LexStat-Markov-Strict',
                'Normal-LexStat-Infomap-Strict',
            ],  
            ['-','-','-','--','--','--'],
            ['red', 'lime', 'blue', 'red', 'lime', 'blue'],
                #'#2c7bb6', 'green', 'lightgreen'],
            data,
            bcube=-1,
            labels = [
                'Partial-LexStat-UPGMA', 
                'Partial-LexStat-Markov',
                'Partial-LexStat-Infomap',
                'LexStat-UPGMA',
                'LexStat-Markov',
                'LexStat-Infomap',
                ]
            )
    plt.ylim(0.5,1)
    plt.title(ds)
    plt.legend(loc=(0.4,0.1), numpoints=1)
    plt.savefig(pcd_path('plots', ds+'-fp-upgma.pdf'))



# plot comparison of Normal-Lexstat with Normal-SCA
box_plot_average(['Normal-LexStat-UPGMA-Strict', 'Partial-LexStat-UPGMA-Strict'], 
        ['v', 'o', 'v', 'o'], 
        ['#d7191c','#fdae61', '#abd9e9','#2c7bb6'],
        [x for x in data if x[1] in infiles], 
        bcube=-1,
        labels = ['LexStat-strict', 'LexStat-IM-strict']
        )
plt.xticks(list(range(0,21)), ['{0:.2}'.format(x * 0.05) if not x % 2 else ''
    for x in range(0,21)])

plt.legend(loc=(0.5,0.1), numpoints=1)
plt.savefig(pcd_path('plots', 'lexstat-vs-infomap.pdf'))

# plot comparison of Normal-Lexstat with Normal-SCA
box_plot_average(['Partial-SCA-Infomap', 'Partial-LexStat-Infomap'], 
        ['v', 'o', 'v', 'o'], 
        ['#d7191c','#fdae61', '#abd9e9','#2c7bb6'],
        [x for x in data if x[1] in infiles], 
        bcube=-1,
        labels = ['SCA-IM', 'LexStat-IM']
        )
plt.xticks(list(range(0,21)), ['{0:.2}'.format(x * 0.05) if not x % 2 else ''
    for x in range(0,21)])
plt.ylim(0.5,1)
plt.legend(loc=(0.5,0.1), numpoints=1)
plt.savefig(pcd_path('plots', 'sca-vs-lexstat-infomap.pdf'))

best_vals([
    'Normal-LexStat-UPGMA-Strict',
    'Normal-LexStat-Markov-Strict',
    'Normal-LexStat-Infomap-Strict',
    'Normal-SCA-UPGMA-Strict',
    'Normal-SCA-Markov-Strict',
    'Normal-SCA-Infomap-Strict',
    'Partial-LexStat-UPGMA-Strict',
    'Partial-LexStat-Markov-Strict',
    'Partial-LexStat-Infomap-Strict',
    'Partial-SCA-UPGMA-Strict',
    'Partial-SCA-Markov-Strict',
    'Partial-SCA-Infomap-Strict',
    'Partial-LexStat-UPGMA',
    'Partial-LexStat-Markov',
    'Partial-LexStat-Infomap',
    'Partial-SCA-UPGMA',
    'Partial-SCA-Markov',
    'Partial-SCA-Infomap',
    ], data, bcube=-1)
