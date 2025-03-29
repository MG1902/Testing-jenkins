with open('test.txt','r') as infile:
    fids = infile.readlines()

with open('test1.txt','w') as outfile:
    for fid in fids:
        outfile.write(fid)