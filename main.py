from sub_solver import SubstitutionSolver
from quadgrams import quad_count

# uncomment this line to generate a frequency file that
# can be feed to the SubstitutionSolver
# quad_count('big.txt', 'quadgrams.txt')

solver = SubstitutionSolver('quadgrams.txt')

cipher_txt = raw_input("Enter text to be deciphered: \n")

inp = ""
while inp != "n":
    
    highest = [0, -10000]
    attempts = 0

    while attempts < 100:
        solution = solver.solve(cipher_txt)

        if highest[1] < solution[1]:
            print(solution[0] + " -> " + str(solution[1]))
            highest = solution
            attempts = 0

        else: 
            attempts += 1

    inp = raw_input("Should I try again? (y/n): ")

