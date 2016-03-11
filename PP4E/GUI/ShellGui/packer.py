# e.g. 10-7

import sys, glob
marker = ':' * 20 + 'textpak=>'


def pack(ofile, ifiles):
    outfile = open(ofile, 'w')
    for ifile in ifiles:
        infile = open(ifile, 'r')
        outfile.write(marker+ifile+'\n')
        for data in infile.readlines():
            outfile.write(data)
            if data[-1] != '\n':
                outfile.write('\n')


if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:
        ifiles += glob.glob(patt)
    print(ifiles)
    pack(sys.argv[1], ifiles)