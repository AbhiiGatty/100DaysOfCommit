# Problem Statememt: https://projecteuler.net/problem=100

''' '''
def arranged_probability(total):
    blue_discs = 85
    known_total = 120
    while known_total < total:
        # Diophantine Quadratic Equation Solution
       blue_discs, known_total = 3 * blue_discs + 2 * known_total - 2, 4 * blue_discs + 3 * known_total - 3
    return blue_discs

if __name__ == "__main__":
    total = 10 ** 12
    blue_discs = arranged_probability(total)
    print("Blue Discs:{} \nRed Discs:{}  has a probability of 0.5 of taking 2 Blue Discs at Random".format(blue_discs, total - blue_discs))
