#!/usr/bin/env python
#coding:utf-8

import getopt
import sys
from json import load

verbose = False


def heract():
    pass


def preparation_config(config_file, config_section, extra=[]):
    v("Load config %s" % config_file)
    config = load(file(config_file))[config_section]


def v(text):
    """
    Verbose
    """
    global verbose
    if verbose:
        print text


def usage():
    print('''Heractor v.1.0
 Description:
    Static site generator

 Help:
    --help          display help
    --config=       select config file (default: config.json)
    --section=      config file section (default: main)
    --verbose       verbose mode
    ''')


def main():
    global verbose
    config_file = "config.json"
    config_section = "main"

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:vs:', ["help", "config=", "verbose", "section="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit()

    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
        elif o in ("-c", "--config"):
            config_file = a
        elif o in ("-s", "--section"):
            config_section = a
        else:
            usage()
            sys.exit()

    preparation_config(config_file, config_section)

if __name__ == "__main__":
    main()