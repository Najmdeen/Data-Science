z = ["Ade", "ale", "Ola", "Baayo"]
x = [1, 2, 3, 4]

def list_dict(x:list,y:list):
    zipped_list = list(zip(x,y))
    x_dict = {key: value for key, value in zipped_list}
    print(x_dict)

p = ["lagos", 44, "oyo", 80, "Abuja", 92, "osun", 30]
def list_to_dic(p):
    p_dict = {p[i]: p[i + 1] for i in range(0, len(p), 2)}
    print(p_dict)

a = [1,2,3,4,5,6,7,8,9,10]


def convert_dict(a):
    it = iter(a)
    dict_a = dict(zip(it, it))
    print(dict_a)


convert_dict(a)
list_to_dic(p)
list_dict(x, z)
