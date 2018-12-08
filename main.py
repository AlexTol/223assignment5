def completeMatchCount(GRNA, Genome):
    forward = Genome
    backwards = Genome[::-1]

    score = 0
    for i in range(0, len(Genome)-19):
        string1 = ''
        string2 = ''
        for j in range(0,20):
            string1 = forward[i+j]
            string2 = backwards[i+j]
        
        score += completeMatch(GRNA,string1) + completeMatch(GRNA,string2)

    return score


def completeMatch(g, s):
    for i in range(0,20):
        if(g[i] != s[i]):
            return 0

    return 1