# s= 'GATATATGCATATACTT'
# t = 'ATAT'

with open(r"C:\Users\Viki\Downloads\rosalind_subs.txt", "r") as file:
    input_string = file.read().strip()
s,t = map(str, input_string.split())
occurances= []
for i in range(len(s)):
    if s[i] == t[0]:
        if s[i:i+len(t)] == t:
            occurances.append(str(i+1))

print(' '.join(occurances))