text = input()
nums_list = text.split(" ")
rev_list=[]
while len(nums_list)>0:
    rev_list.append(nums_list.pop())
print(" ".join(rev_list))