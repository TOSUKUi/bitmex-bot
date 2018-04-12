def rci3lines(bin):

    return long, mid, short


def williams_vix_fix(bin):
    return


def ord(seq, idx, itv):
    p = seq[idx]
    o = 1
    for i = 0 in itv - 1:
        if p < seq[i]:
            o = o + 1
    return o

def d(itv):
    sum = 0.0
    for i = 0 in itv - 1:
        sum := sum + pow((i + 1) - ord(src, i, itv), 2)
    sum

rci(itv) => (1.0 - 6.0 * d(itv) / (itv * (itv * itv - 1.0))) * 100.0 + 100
