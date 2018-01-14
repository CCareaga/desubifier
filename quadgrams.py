import itertools
from math import log10

def quad_count(inf, outf):
    qdata = {}

    for i in itertools.product(' abcdefghijklmnopqrstuvwxyz', repeat=4):
        qdata[''.join(i)] = 0

    with open(inf, "r") as f:
        for line in f:
            for i in range(0, len(line) - 3):
                quad = line[i : (i + 4)].lower()

                if checkWord(quad):
                    qdata[quad] += 1

    with open(outf, "w") as f:
        for key, value in sorted(qdata.iteritems(), key = lambda (k,v): (v,k)):
            f.write(key + '-' + str(value) + '\n')

            
def checkWord(word):
    new_word = ''.join(e for e in word if (e.isalpha() or e == ' '))
    return len(new_word) == 4

# === FITNESS CALCULATOR =========================================================
#
#    this class is used to determine the fitness of a peice of text.
#    in order to calculate a fitness the object must first be loaded with quadgram
#    data by calling 'loadFreqs' this function takes the name of a file that was
#    created using the 'train' function above. after loading the quadgram data
#    the 'calculateFitness' method can be used.
#
#    fitness is determined by quadgram frequency. each quadgram is assigned its
#    own fitness using the following equation
#
#    fitness = log10( freq. of quadgram / 27 ^ 4)
#   
#    once values for each quadgram are calculated, to determine the fitness of 
#    a peice of text I simply add up the individual quadgram fitnesses
#
#    NOTE: quadgrams with 0 occurences in the training data are given a fitness
#          using the same data except they I divide by the total number of quad
#          grams in the training text
#
#    fitness scores depend on the length of a string but this is irrelevent 
#    when comparing two fitness scores, the strings are always the same size
# ================================================================================

class FitnessCalculator():
    def __init__(self):
        self.qdata = {}

        res = itertools.product(' abcdefghijklmnopqrstuvwxyz', repeat=4)
        for i in res:
            self.qdata[''.join(i)] = 0.0

    def loadFreqs(self, fn): 
        total = 0
        quads = 0

        with open(fn, "r") as f:
            for line in f:
                parts = line.lower().strip().split('-')
                self.qdata[parts[0]] = int(parts[1])

                total += int(parts[1])
                quads += 1

        for key in self.qdata.keys():
            if self.qdata[key] == 0:
                self.qdata[key] = log10(float(1) / total)
            else:
                self.qdata[key] = log10(float(self.qdata[key]) / quads)

    def calculateFitness(self, txt):
        fit = 0

        for i in range(0, len(txt) - 3):
            word = txt[i : (i + 4)]
            fit += self.qdata.get(word)

        return fit

