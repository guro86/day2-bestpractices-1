#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:22:17 2022

@author: robertgc
"""

class Fish:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Shark', 'Aborre', 'Mört']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
