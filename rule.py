import random

# Lookup tables for Hensel notation stuff

trans = ['B0', 'B1c', 'B1e', 'B2c', 'B2e', 'B2k', 'B2a', 'B2i', 'B2n', 'B3c', 'B3e', 'B3k', 'B3a', 'B3i', 'B3n', 'B3y', 'B3q', 'B3j', 'B3r', 'B4c', 'B4e', 'B4k', 'B4a', 'B4i', 'B4n', 'B4y', 'B4q', 'B4j', 'B4r', 'B4t', 'B4w', 'B4z', 'B5c', 'B5e', 'B5k', 'B5a', 'B5i', 'B5n', 'B5y', 'B5q', 'B5j', 'B5r', 'B6c', 'B6e', 'B6k', 'B6a', 'B6i', 'B6n', 'B7c', 'B7e', 'B8', 'S0', 'S1c', 'S1e', 'S2c', 'S2e', 'S2k', 'S2a', 'S2i', 'S2n', 'S3c', 'S3e', 'S3k', 'S3a', 'S3i', 'S3n', 'S3y', 'S3q', 'S3j', 'S3r', 'S4c', 'S4e', 'S4k', 'S4a', 'S4i', 'S4n', 'S4y', 'S4q', 'S4j', 'S4r', 'S4t', 'S4w', 'S4z', 'S5c', 'S5e', 'S5k', 'S5a', 'S5i', 'S5n', 'S5y', 'S5q', 'S5j', 'S5r', 'S6c', 'S6e', 'S6k', 'S6a', 'S6i', 'S6n', 'S7c', 'S7e', 'S8']
trans_idx = {trans[i]: i for i in range(len(trans))}

# An INT rule.

class Rule:
    def __init__(self, *args):
        self.translist = {} # A dict mapping transition -> present or not (bool)

        if len(args) == 0: # A default Rule() represents B3/S23. 
            for tran in trans:
                self.translist[tran] = (tran[:2] in ['B3', 'S2', 'S3'])
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                for tran in trans:
                   self.translist[tran] = False
                bs = None
                digit = None
                for c in arg:
                    if c in 'BS':
                        bs = c
                    elif c in '0123456789':
                        digit = c
                        if digit in '08':
                            self.translist[bs + c] = True
                    else:
                        assert c in 'cekainjqrytwz/', "Illegal character in rule: %s" % c
                        if c != '/':
                            self.translist[bs + digit + c] = True
            else: raise ValueError
        else: raise ValueError

    def __str__(self): # Returns the rule in Hensel format
        s = ''

        # Birth transitions
        s += 'B'
        if self.translist['B0']: s += '0'
        for i in range(1, 8):
            t = ''
            for letter in 'cekainjqrytwz':
                tran = 'B%i%c' % (i, letter)
                if tran in trans and self.translist[tran]:
                    t += letter
            if t:
                s += '%i%s' % (i, t)
        if self.translist['B8']: s += '8'

        # Survival transitions
        s += '/S'
        if self.translist['S0']: s += '0'
        for i in range(1, 8):
            t = ''
            for letter in 'cekainjqrytwz':
                tran = 'S%i%c' % (i, letter)
                if tran in trans and self.translist[tran]:
                    t += letter
            if t:
                s += '%i%s' % (i, t)
        if self.translist['S8']: s += '8'
        return s

    def __repr__(self):
        return "<Rule %s>" % self.__str__()

    def toggle(self, tran):
        self.translist[tran] = not self.translist[tran]
