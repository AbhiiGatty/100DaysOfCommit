# Problem Statement: https://projecteuler.net/problem=22 

def name_score():
    total_value = 0
    for index, name in enumerate(sorted(open('p022_names.txt').read().split(",")), 1):
        value_of_name  = sum([ ord(char) - 64 for char in name.replace('''"''',"")]) # Using 64 since all names are in upper case
        total_value += index * value_of_name
    return total_value

if __name__ == "__main__":
    print("Total Name Score: {}".format(name_score()))