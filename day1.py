# data setup
with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n")
data = [int(x) for x in data if x.isdigit()]


# part 1
def get_2020_sum_multiple(data_dict):
    for d in data_dict:
        if data_dict[d] in data_dict:
            return d * data_dict[d]
    return None


data_set = {x: 2020-x for x in data}
answer_1 = get_2020_sum_multiple(data_set)


# part 2
def get_2020_sum_multiple_3(data_list, data_set):
    for x in data_set:
        d = data_list
        d.remove(x)
        possible_sums = list(filter(lambda y: y <= data_set[x], d))
        triset = {p: data_set[x]-p for p in possible_sums}
        result = get_2020_sum_multiple(triset)
        if result is not None:
            return result * x

print(get_2020_sum_multiple_3(data, data_set))
