#!/usr/bin/env python

"""Nori starter"""

import sys
from nori import Nori

def main():
    """Main"""
    try:
        nori = Nori()
        sys.exit(nori.run())
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()
