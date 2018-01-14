from random import shuffle, choice

from math import log10
from quadgrams import FitnessCalculator

THRESHOLD = 1000

# === SUBSTITUTION SOLVER =========================================================
#
#   this class uses a simple algorithm involving the fitness calculator to 
#   solve substitution encrypted strings of text.
# 
#   like most NLP problems the answer isn't always definite and due to the random
#   nature of the algorithm the solver may have to run many times to determine the
#   correct answer. 
#
#   outline of the algorithm:
#       1) generate a random key by shuffling the alphabet
#       2) convert the cipher text, and calculate the fitness
#       3) make one random swap in the parent key, this is the child key
#       4) calculate the fitness of the child key
#       5) if the child is more fit, we call it the parent and go to 2
#       6) if the child is less fit, we undo the swap and try again
#       7) if the child is equally fit we don't undo (seems to work better)
#       8) if we reach 1000 iterations without increasing we call it good
#
#   it is possible to increase the 1000 try threshold but it obviously it causes
#   the algo to run for a very long time, I would rather just try again if the 
#   message wasn't correct that way the user sees some improvement each time
# ================================================================================

class SubstitutionSolver():
    def __init__(self, fn):
        self.freqs = {}
        self.alphabet = map(chr, range(97, 123))
        self.swap = []

        self.fcalc = FitnessCalculator()
        self.fcalc.loadFreqs(fn)
        
    def getFitness(self, txt):
        return self.fcalc.calculateFitness(txt)

    def convertChar(self, c, key):
        if c == ' ':
            return ' '
        elif c.isalpha():
            return key[self.alphabet.index(c)]
        else:
            return ''

    def convertString(self, txt, key):
        txt_arr = list(txt) 

        for i in range(0, len(txt_arr)):
            txt_arr[i] = self.convertChar(txt_arr[i], key) 

        return ''.join(txt_arr)
    
    def randomSwap(self, key):
        a = choice(range(0, len(key)))
        b = choice(range(0, len(key)))

        self.swap = [a, b]
        key[a], key[b] = key[b], key[a]
        return key

    def undoSwap(self, key):
        a = self.swap[0]
        b = self.swap[1]

        key[a], key[b] = key[b], key[a]

    def solve(self, cipher):
        cipher = cipher.lower()

        running = 1
        no_increase = 0

        p_key = self.alphabet[:]
        shuffle(p_key)

        converted = self.convertString(cipher, p_key)
        p_fit = self.getFitness(converted)

        while no_increase < THRESHOLD:
            c_key = self.randomSwap(p_key)
            converted = self.convertString(cipher, c_key)
            c_fit = self.getFitness(converted)

            if (c_fit > p_fit):
                p_fit = c_fit
                p_key = c_key
                no_change = 0

            elif (c_fit < p_fit):
                self.undoSwap(p_key)

            else:
                no_increase += 1


        return [converted, c_fit]
