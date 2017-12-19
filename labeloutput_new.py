import metapy
import sys
import os
import PyPDF2
import shutil

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def training_algo(path):

    os.chdir(path)

    inv_idx = metapy.index.make_inverted_index('training-config.toml')
    fwd_idx = metapy.index.make_forward_index('training-config.toml')
    dset = metapy.classify.MulticlassDataset(fwd_idx)
    #nb = metapy.classify.NaiveBayes(dset)
    ova = metapy.classify.OneVsAll(dset, metapy.classify.SGD, loss_id='hinge')
    f_inv_idx = metapy.index.make_inverted_index('regulations-config.toml')
    f_fwd_idx = metapy.index.make_forward_index('regulations-config.toml')
    f_dset = metapy.classify.MulticlassDataset(f_fwd_idx)

    os.chdir('.\\regulations')

    filecounter = 0
    icount = 0
    icount1 = 0
    # icount2 = 1
    labellist = []
    iterator = 0
    iterator1 = 0

    with open('regulations.dat', 'r') as f:
        lines = f.readlines()
        # numlines = len(lines)

        for contents in lines:
            doc = metapy.index.Document()
            doc.content(str(contents))
            labels = ova.classify(fwd_idx.tokenize(doc))
            # print(labels)
            # print(contents)

            labellist.append(labels)

            with open('labels.txt', 'a+') as f11:
                f11.write(str(labels) + '\n')
                f11.close()

            #make_sure_path_exists(path + "\\regulations" + "\\DataClumps")
            try:
                os.makedirs(path + "\\regulations" + "\\DataClumps")
            except:
                pass

            os.chdir('.\\DataClumps')

            if labels == 'keyrule':
                icount = icount + 1
                filecounter = filecounter + 1
                iterator = 0
                with open('%s%s.txt' %(filecounter,icount), 'a+') as newfile:
                    newfile.write(str(contents) + '\n')

            if icount >= 1:

                if labels in ('operatingrequirements', 'reportingrequirement'):
                    iterator1 = iterator1 + 1
                    if iterator1 < 8:
                        with open('%s%s.txt' % (filecounter,icount), 'a+') as newfile12:
                            newfile12.write(str(contents) + '\n')
                    else:
                        iterator1 = 0
                        labellist = [x for x in labellist if x != "keyrule"]


            if "keyrule" not in set(labellist):
                if labels in ('operatingrequirements', 'reportingrequirement'):
                    # print(iterator)
                    iterator = iterator + 1
                    # print(iterator)

                    if iterator >= 8:
                        filecounter = filecounter + 1
                        #icount1 = icount1 + 1
                        #filecounter = filecounter + 1
                        iterator = 0

                    if iterator < 8:
                            with open('%s%s.txt' % (filecounter,filecounter +1 ), 'a+') as newfile1:
                                newfile1.write(str(contents) + '\n')


           # if labels == 'keyruleamendment':
            #    with open('keyruleamendment.txt', 'a+') as f1:
              #      f1.write(str(contents) + '\n')
                    # f1.write('\n')
               #     f1.close()
            os.chdir('..')

            #make_sure_path_exists(path + "\\regulations" + "\\Labelledcontent")
            try:
                os.makedirs(path + "\\regulations" + "\\Labelledcontent")
            except:
                pass


            os.chdir('.\\Labelledcontent')

            if labels == 'observations':
                with open('observations.txt', 'a+') as f2:
                    f2.write(str(contents) + '\n')
                    # f2.write('\n')
                    f2.close()
            elif labels == 'definitions':
                with open('definitions.txt', 'a+') as f3:
                    f3.write(str(contents) + '\n')
                    # f3.write('\n')
                    f3.close()
            elif labels == 'operatingrequirements':
                with open('operatingrequirements.txt', 'a+') as f4:
                    f4.write(str(contents) + '\n')
                    # f4.write('\n')
                    f4.close()
            elif labels == 'keyrule':
                with open('keyrule.txt', 'a+') as f5:
                    f5.write(str(contents) + '\n')
                    # f5.write('\n')
                    f5.close()
            elif labels == 'reportingrequirement':
                with open('reportingrequirement.txt', 'a+') as f6:
                    f6.write(str(contents) + '\n')
                    # f6.write('\n')
                    f6.close()
            elif labels == 'toc':
                with open('toc.txt', 'a+') as f7:
                    f7.write(str(contents) + '\n')
                    # f7.write('\n')
                    f7.close()
            elif labels == 'tradingrestrictions':
                with open('tradingrestrictions.txt', 'a+') as f8:
                    f8.write(str(contents) + '\n')
                    # f8.write('\n')
                    f8.close()

            os.chdir('..')

                    # print (labellist)

                #print(str(labels))
    #with open('outputlabels.txt','w',encoding='ascii',errors='ignore') as f1:
        #for icount in range(0,f_fwd_idx.num_docs()):
           # try:
              #  print ('%s;%s'%(ova.classify(f_dset[icount].weights),f_fwd_idx.metadata(icount).get('content')),file = f1)
            #except:
             #   continue