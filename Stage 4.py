input = [441, 484, 529, 576, 625]
output = [12, 22, 32, 42, 52]

def overwrite_sequence(input):
    u0 = 0
    u1 = 1

    liste = [u0, u1]
    i = 2
    while  2*liste[-1] - liste[-2] + 2 != input[0] :
        liste.append(2*liste[-1] - liste[-2] + 2)
        i+=1

    res = [i]
    for i in range(1, len(input)) :
        res.append(res[-1] + 1)

    for i in range(len(input)) :
        res[i] = int(str(res[i])[::-1])
    
    return res