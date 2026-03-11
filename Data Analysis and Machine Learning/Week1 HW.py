ss = []
out = []
for i in range(6):
    for j in range(6):
        out.append([i+1, j+1])

try:
    for a in range(len(out)):
        for b in range(len(out)):
            for c in range(len(out)):
                for d in range(len(out)):
                    for e in range(len(out)):
                        for f in range(len(out)):
                            ss.append([out[a], out[b], out[c], out[d], out[e], out[f]])
    print(len(ss))
except Exception as e:
    print(e)