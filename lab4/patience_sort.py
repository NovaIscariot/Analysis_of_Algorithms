import bisect, heapq

def patience_sort(seq):
    piles = []
    for x in seq:
        new_pile = [x]
        i = bisect.bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].insert(0, x)
        else:
            piles.append(new_pile)
    # priority queue allows us to retrieve least pile efficiently
    for i in range(len(seq)):
        small_pile = piles[0]
        seq[i] = small_pile.pop(0)
        if small_pile:
            heapq.heapreplace(piles, small_pile)
        else:
            heapq.heappop(piles)
    assert not piles

    return seq

#https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Patience_sort
