import sys

def create_dict():
    file = open(sys.argv[1], "r")
    content = file.readlines()

    s1 = content[0].strip()
    s2 = content[1].strip()
    
    for i in range(0, len(content)):
        content[i] = content[i].rstrip('\n')
        content[i] = content[i].split(" ")

    scores = {}
    col = content[2]
    for i in range(3, len(content)):
        row = content[i]
        for j in range(1, len(row)):
            if(row[j] != " "):
                scores[row[0] + col[j]] = int(row[j])
    return s1, s2, scores

def hsa(s1, s2, dictionary):
    len_s1 = len(s1)  
    len_s2 = len(s2)

    scoring = []
    for i in range(len_s2 + 1):
        scoring.append([])
        for j in range(len_s1 + 1):
            scoring[-1].append(0)

    for i in range(len_s2 + 1):
        scoring[i][0] = dictionary["-" + s2[i - 1]] * i
        
    for j in range(len_s1 + 1):
        scoring[0][j] = dictionary[s1[j - 1] + "-"] * j
    
    for i in range(1, len_s2 + 1):
        for j in range(1, len_s1 + 1):
            match = scoring[i - 1][j - 1] + dictionary[s1[j - 1] + s2[i - 1]]
            delete = scoring[i - 1][j] + dictionary["-" + s2[i - 1]]
            insert = scoring[i][j - 1] + dictionary[s1[j - 1] + "-"]
            scoring[i][j] = max(match, delete, insert)
    
    a1 = ""
    a2 = ""
    x_max = len_s2
    y_max = len_s1

    while len_s2 > 0 and len_s1 > 0:
        diag = scoring[len_s2 - 1][len_s1 - 1]
        curr = scoring[len_s2][len_s1]
        above = scoring[len_s2][len_s1 - 1]
        left = scoring[len_s2 - 1][len_s1]
    
        if curr == diag + dictionary[s1[len_s1 - 1] + s2[len_s2 - 1]]:
            a1 += s1[len_s1 - 1]
            a2 += s2[len_s2 - 1]
            len_s1 -= 1
            len_s2 -= 1
        elif curr == above + dictionary[s1[len_s1 - 1] + '-']:
            a1 += s1[len_s1 - 1]
            a2 += '-'
            len_s1 -= 1
        elif curr == left + dictionary['-' + s2[len_s2 - 1]]:
            a1 += '-'
            a2 += s2[len_s2 - 1]
            len_s2 -= 1
            
    while len_s1 > 0:
        a1 += s1[len_s1 - 1]
        a2 += '-'
        len_s1 -= 1

    while len_s2 > 0:
        a1 += '-'
        a2 += s2[len_s2 - 1]
        len_s2 -= 1

    a1 = a1[::-1]
    a2 = a2[::-1]

    return a1, a2, str(scoring[x_max][y_max])

seqs = create_dict()
x, y, final_score = hsa(seqs[0], seqs[1], seqs[2])
print("x:", " ".join(x))
print("y:", " ".join(y))
print("Score:", final_score)
