#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for u in range(len(name)):
        if name[u][0] != "_" and name[u][1] != "_":
            print(name[u])
