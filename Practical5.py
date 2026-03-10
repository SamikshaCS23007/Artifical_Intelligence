alphabets = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

found = False

for S in range(1,10):  # S cannot be 0
    for E in range(10):
        for N in range(10):
            for D in range(10):
                for M in range(1,10):  # M cannot be 0
                    for O in range(10):
                        for R in range(10):
                            for Y in range(10):

                                numbers = [S,E,N,D,M,O,R,Y]

                                if len(set(numbers)) != 8:
                                    continue

                                send = S*1000 + E*100 + N*10 + D
                                more = M*1000 + O*100 + R*10 + E
                                money = M*10000 + O*1000 + N*100 + E*10 + Y

                                if send + more == money:

                                    print("Solution Found!\n")

                                    print(f"S = {S}")
                                    print(f"E = {E}")
                                    print(f"N = {N}")
                                    print(f"D = {D}")
                                    print(f"M = {M}")
                                    print(f"O = {O}")
                                    print(f"R = {R}")
                                    print(f"Y = {Y}")

                                    print("\nValues:")
                                    print(f"SEND = {send}")
                                    print(f"MORE = {more}")
                                    print(f"MONEY = {money}")

                                    print(f"\n{send} + {more} = {money}")

                                    found = True
                                    break
                            if found: break
                        if found: break
                    if found: break
                if found: break
            if found: break
        if found: break
    if found: break

if not found:
    print("No solution found")