#!/usr/bin/env python

import argparse
import os
import sys
import re


def mkbbl(infile=None, outfile=None):

    if outfile is None:
        outfile = os.path.extsep.join([os.path.splitext(infile)[0], 'bbl'])

    data = None

    with open(infile, 'r') as f:
        data = ''.join([_ for _ in f])


    match = re.search(r'.*(\\begin\{thebibliography\}.*\\end\{thebibliography\}).*', 
                        data, 
                        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
    output = ''

    if match:
        output = match.groups()[0]

    with open(outfile, 'w') as f:
        f.write(output)


def parse_args(args):

    parser = argparse.ArgumentParser(description='Construct a .bbl file if none exists')

    parser.add_argument('infile', action='store', type=str, help='input .tex file')
    parser.add_argument('outfile', action='store', type=str, help='output .bbl file', nargs='?', default=None)


    return vars(parser.parse_args(args))

if __name__ == '__main__':
    kwargs = parse_args(sys.argv[1:])

    mkbbl(**kwargs)
