def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        list_to_remove_elements.pop(0)
        list_to_remove_elements.pop(3)
        list_to_remove_elements.pop(3)
    elif len(list_to_remove_elements) == 5:
        list_to_remove_elements.pop(0)
        list_to_remove_elements.pop()
    elif list_to_remove_elements and len(list_to_remove_elements) < 5:
        list_to_remove_elements.pop(0)
    return list_to_remove_elements


def add_elements(list_to_add_elements):
    color1, color2 = 'Pink', 'Yellow'
    list_to_add_elements.insert(0, color1)
    list_to_add_elements.append(color2)
    return list_to_add_elements


def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else: 
            return False
    else:
        False


def list_of_lists(list_of_lists_to_modify):
    if list_of_lists_to_modify[0]:
        item1 = list_of_lists_to_modify[0][0]
        if len(list_of_lists_to_modify[0]) >= 2:
            item2 = list_of_lists_to_modify[0][1]
            new_lst1 = [item1, item2]
        else:
            new_lst1 = [item1]
        list_of_lists_to_modify[0] = new_lst1

    if len(list_of_lists_to_modify[1]) >= 2:
        items_lst2 = list_of_lists_to_modify[1][1:4]
        list_of_lists_to_modify[1] = items_lst2
    else:
        list_of_lists_to_modify[1] = []

    if len(list_of_lists_to_modify[1]) >= 2:
        list_of_lists_to_modify[2].reverse()
        items_list3 = list_of_lists_to_modify[2][0:2]
        list_of_lists_to_modify[2] = items_list3
        items_list3.reverse()

    return list_of_lists_to_modify
