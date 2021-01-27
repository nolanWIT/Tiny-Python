import argparse
import os
import sys


def get_args():
    parser = argparse.ArgumentParser(description = 'to upper', formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('str', help = 'string to uppercase', metavar='str')
    parser.add_argument('-o', '--outfile', help= 'file name to write to', metavar='file')

    return parser.parse_args()

def main():
    args = get_args()
    arg = args.str
    outfile = args.outfile
    word_upper = ''
    if os.path.isfile(arg):
        word_upper = open(arg, 'rt').read().upper().strip()
        #print(word_upper)
    else:
        word_upper = arg.upper()
    
    if args.outfile:
        open(outfile, 'wt').write(word_upper)
        #print(word_upper, outfile)
    else: 
        print(word_upper)


if __name__ == '__main__':
    main()