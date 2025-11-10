def merge_lists_dict(keys, values):
    merged_dict = {}
    
    for i in range(len(keys)):
        merged_dict[keys[i]] = values[i]
    return merged_dict   
                 
print(merge_lists_dict(['a','b','c'],[1,2,3]))