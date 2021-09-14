"""
hogwarts 
yejq
"""
import yaml


def get_cacldate():
    with open("./dates/calcudates.yaml")as f:
        totals = yaml.safe_load(f)
        # print(totals)
        return [totals["dates"], totals["ids"]]


print(get_cacldate())



# l = [1]
# for i in range(5):
#     print(l)
#     l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1]
#
# x = 1
# a = [x * x for x in range(1,100)]