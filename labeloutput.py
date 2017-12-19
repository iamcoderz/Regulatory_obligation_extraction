import metapy
import sys
import os

def trainingalgo():
    os.chdir('C:\\Users\\Pradeep\\Anaconda3_1\\Lib\\site-packages\\metapy')
    inv_idx = metapy.index.make_inverted_index('training-config.toml')
    fwd_idx = metapy.index.make_forward_index('training-config.toml')
    dset = metapy.classify.MulticlassDataset(fwd_idx)
    #nb = metapy.classify.NaiveBayes(dset)
    ova = metapy.classify.OneVsAll(dset, metapy.classify.SGD, loss_id='hinge')
    f_inv_idx = metapy.index.make_inverted_index('regulations-config.toml')
    f_fwd_idx = metapy.index.make_forward_index('regulations-config.toml')
    f_dset = metapy.classify.MulticlassDataset(f_fwd_idx)
    with open('outputlabels.txt','w',encoding='ascii',errors='ignore') as f1:
        for icount in range(0,f_fwd_idx.num_docs()):
            try:
                print ('%s;%s'%(ova.classify(f_dset[icount].weights),f_fwd_idx.metadata(icount).get('content')),file = f1)
            except:
                continue