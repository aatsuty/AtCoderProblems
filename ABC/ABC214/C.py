import copy

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

firstGivenTime = copy.deepcopy(T) #T秒後には必ずもらえるので

for k in range(100):
    for i in range(N): #i番目のすぬけ君が渡す事象について
        index = S[i]%N #i番目のすぬけ君が渡す相手の番号
        giveTime = S[i] #i番目のすぬけ君が前回もらってから渡すまでの時間
        defaultTime = firstGivenTime[index] #i番目のすぬけ君から受け取るすぬけ君が現状受け取る時間
        giveTime_ = firstGivenTime[i]+giveTime #i番目のすぬけ君から受け取る時刻
        firstGivenTime[index]=min([defaultTime,giveTime_])
    print(firstGivenTime)