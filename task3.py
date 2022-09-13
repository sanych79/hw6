result={}
temp_files_data = []
count_dict = {}

def loadfiles_and_len(name, data_dict, c_dict):
    temp = []
    with open(name, 'r', encoding='utf8') as files1:
        for line in files1:
            temp.append(line.strip())
        data_dict[name] = temp
        c_dict[name] = len(temp)

for i in range(3):
    fm = f'{i+1}.txt'
    loadfiles_and_len(fm, result, count_dict)


sorted_values = sorted(count_dict.values()) 
sorted_dict = {}

for i in sorted_values:
    for k in count_dict.keys():
        if count_dict[k] == i:
            sorted_dict[k] = count_dict[k]
            break


for x,y in sorted_dict.items():
    print(x)
    print(y)  
    for z in result[x]:
        print(z)
