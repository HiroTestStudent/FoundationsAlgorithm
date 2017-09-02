def all_combinations(the_list):
   results = [] #req
   for item in the_list:
       for inner_item in the_list:
           results.append((item, inner_item))
   return results

list = [1,2,3,4,5]

print(all_combinations(list))