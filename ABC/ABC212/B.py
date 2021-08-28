S = input()
if S[0]==S[1] and S[1]==S[2] and S[2]==S[3]:
    print("Weak")
elif S == "0123" \
    or S == "1234" \
    or S == "2345" \
    or S == "3456" \
    or S == "4567" \
    or S == "5678" \
    or S == "6789" \
    or S == "7890" \
    or S == "8901" \
    or S == "9012":
    print("Weak")

else:
    print("Strong")