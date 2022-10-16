my_dict = {'Peter': 21, 'George': 18, 'John': 45}
sorted_dict = sorted(my_dict.items(), key=lambda x: x[0][-2])
# [('George', 18), ('John', 45), ('Peter', 21)]
print(sorted_dict)
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
# [('George', 18), ('John', 45), ('Peter', 21)]
print(sorted_dict)
reversed_dict = sorted(my_dict.items(),
                       key=lambda x: x[0],
                       reverse=True)
# [('Peter', 21), ('John', 45), ('George', 18)]
print(reversed_dict)