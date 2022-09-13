cook_book =  {}

with open('recepes.txt','r', encoding='utf8') as file:
    for line in file:
        c_name =  line.strip()
        cook_temp = {c_name: []}
        c_count = file.readline()
        for i in range(int(c_count)):
            temp = file.readline()
            i_name, i_qty, i_measure = temp.split(' | ')
            temp_ingr = {"ingredient_name": i_name,'quantity':i_qty, 'measure':i_measure.strip()}  
            cook_temp[c_name].append(temp_ingr)
        file.readline()  
        cook_book.update(cook_temp)



def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for search_dishes in dishes:
        for search_ingredient in (cook_book[search_dishes]):
            qty = (int(search_ingredient['quantity']))*person_count
            meas = str(search_ingredient['measure'])
            ing_name = search_ingredient['ingredient_name']
            if ing_name in result:
                qty += result[ing_name]['quantity']
            result[ing_name]={'measure':meas, 'quantity':qty}
    return result
        

dish_list = ['Фахитос', 'Омлет']
p_c = 3

dish_list =  get_shop_list_by_dishes(dish_list, p_c)
print(dish_list)