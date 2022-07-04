def solutions(S,T):
    if(S == T):
        return "NOTHING"
        
    try:
        St = S + T[len(T)-1] 
        if(T == St):
            return f"ADD {T[len(T)-1]}"
    except:
        pass

    try:
        i = 0
        for c in S:
            if(S[i] == S[i+1]):
                mergedS = S[0 : i : ] + S[i + 1 : :]
                if(mergedS == T):
                    return f"JOIN {S[i]}"
            i+=1
    except:
        pass

    try:
        i = 0
        for c in range(len(S)):
            for c2 in range(len(S)):
                if (S[c] != S[c2]):
                    swapedS = S[:c] + S[c2] + S[c + 1:]
                    swapedS = swapedS[:c2] + S[c] + swapedS[c2 + 1:]
                    if swapedS == T:
                        return f"SWAP {S[c]} {S[c2]}"
    except:
        pass


    return "IMPOSSIBLE"

if __name__ == '__main__':
    print(solutions("nice","nicer"))
    print(solutions("meet","met"))
    print(solutions("late","tale"))
    print(solutions("o","odd"))