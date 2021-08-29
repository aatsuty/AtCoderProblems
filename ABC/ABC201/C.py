S = input()

maruCount = len([1 for s in S if s == "o"])
batuCount = len([1 for s in S if s == "x"])
hateCount = len([1 for s in S if s == "?"])
kanoCount = len([1 for s in S if s == "o" or s == "?"])

if maruCount + batuCount + hateCount != 10:
    print("error")
    exit()
    
if kanoCount != maruCount + hateCount:
    print("error")
    exit()

# 使用必須な数字が過多なケース
if maruCount > 4:
    print(0)
    exit()
    
# 使用可能な数字が過少なケース
if kanoCount == 0:
    print(0)
    exit()
    
if maruCount == 4:
    answer = 4*3*2*1
    print(answer)
    exit()
    
if maruCount == 1:
    answer = kanoCount**4 - hateCount**4
    print(answer)
    exit()
    
if maruCount == 2:
    answer = kanoCount**4 - hateCount**4
    # この時点で、〇が1つは入ってるが、２つともは入っていない可能性がある
    answer = answer - ((hateCount+1)**4-hateCount**4)*2
    print(answer)
    exit()
    
if maruCount == 3:
    answer = 3*2*1*4*hateCount
    answer = answer + 3 * 3 * 2*1
    print(answer)
    exit()