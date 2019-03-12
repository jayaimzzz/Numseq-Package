#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Returns the nth Fibonacci number
"""
__author__ = "jayaimzzz"

import sys
import argparse

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return "error"
    

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='nth Fibonacci number')
    return parser

def main():
    """Main function is declared as standalone, for testability"""
    parser = create_parser()
    args = parser.parse_args()
    n = int(args.number)
    return fib(n)

if __name__ == '__main__':
    """Docstring goes here"""
    main()
