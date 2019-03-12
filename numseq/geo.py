#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Geometric numbers
"""
__author__ = "jayaimzzz"



def square(n):
    '''returns the squre of a number'''
    return n ** 2

def triangle(n):
    '''returns the triangle of a number'''
    # result = 0
    # while n:
    #     result += n
    #     n -= 1
    # return result
    return (n * (n+1) / 2)

def cube(n):
    '''returns the cube of a number'''
    return n ** 3

