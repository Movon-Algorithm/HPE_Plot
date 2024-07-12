
l1 = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = list(range(1,11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = list(range(10,30,2))
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

list_all = [l1, l2, l3]

with open("test.csv", "w") as f:
    for l in list_all:
        s = ",".join([str(i) for i in l])
        f.write(f"{s}\n")

