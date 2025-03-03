def rank_list(lst):
    sorted_lst = sorted(lst)
    rank = [sorted_lst.index(x) + 1 for x in lst]
    print(rank)

lst = [100, 2, 2, 11]
rank_list(lst)