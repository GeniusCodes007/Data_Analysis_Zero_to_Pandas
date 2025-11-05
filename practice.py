import pandas as pnd

t_e = []
for x in range(0, 398):
    #print(x+1)
    t_e.append(x+1)

#print(tup_le)
bn = pnd.read_csv('Bitcoin_Prices_List.csv')
bn.index = t_e
print(bn)
#print(bn.index)

"""
with open('Bitcoin_Prices_List.csv', 'r') as prices:
    for index, lines in prices:
        print(index + 1, lines.read_lines())"""