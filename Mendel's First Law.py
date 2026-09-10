# Mendel's First Law


"""
                            |    offspring possibilites given X and Y choice
-------------------------------------------------------------------------
X Y |  P(X,Y)               |   d(dominant)     h(hetero)   r(recessive)
-------------------------------------------------------------------------
d d     k/a*(k-1)/(a-1)     |    1               0           0
d h     k/a*(m)/(a-1)       |    1/2            1/2          0
d r     k/a*(n)/(a-1)       |    0               1           0
                            |
h d     m/a*(k)/(a-1)       |    1/2            1/2          0
h h     m/a*(m-1)/(a-1)     |    1/4            1/2         1/4
h r     m/a*(n)/(a-1)       |    0              1/2         1/2
                            |
r d     n/a*(k)/(a-1)       |    0               0           0
r h     n/a*(m)/(a-1)       |    0               1/2        1/2
r r     n/a*(n-1)/(a-1)     |    0               0           1


"""

# k=2  #AA
# m=2 #Aa
# n=2 #aa
with open(r"C:\Users\Viki\Downloads\rosalind_iprb (4).txt", "r") as file:
    input_text = file.read().strip()

k, m, n = map(int, input_text.split(' '))

# Calculate total number of organisms in the population:
total = k + m + n
# print(f'{k}-{m}-{n} - {a}')

# p_recessive = (1/4*m*(m-1) + 1/2*m*n + 1/2*m*n + n*(n-1))/(a*(a-1))
# p_wanted = 1 - p_recessive
# p_wanted = round(p_wanted, 5)

ordered_pairs = total * (total - 1)
dominant_numerator = (k * (k - 1) + 2 * k * (m + n) + 0.75 * m * (m - 1) + m * n)
final = dominant_numerator / ordered_pairs
print(f"{final:.5f}")


