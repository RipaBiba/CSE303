# Sum of Series 1²+2²+3²+….+n²

def sumofsquareseries(numb):
    if(numb == 0):
        return 0
    else:
        ## (number * (number + 1) * (2 * number + 1)) / 6
        return (numb * numb) + sumofsquareseries(numb - 1)


numb = int(input("Please Enter any Positive Number  : "))
total = sumofsquareseries(numb)

print(f'The Sum of Series upto {numb}  = {total}')
