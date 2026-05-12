def dem_so_lxh(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_str = input("Nhập danh sách các từ(cách nhau bằng dấu phẩy):")
word_list = input_str.split(',')

so_lan_xh = dem_so_lxh(word_list)
print("Số lần xuất hiện của các phần từ:", so_lan_xh)