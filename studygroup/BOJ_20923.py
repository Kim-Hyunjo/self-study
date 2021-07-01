import sys

# do_grnd + su_grnd = 5 ==> su(양쪽다 0이 아님)
# do_grnd or su_grnd = 5 ==> do

N,M = map(int, sys.stdin.readline().split())
do_cards = []
su_cards = []
for _ in range(N):
    do,su = map(int, sys.stdin.readline().split())
    do_cards.append(do)
    su_cards.append(su)

do_grnd = []
su_grnd = []
print(id(do_grnd))
win = None
for i in range(M):  # i짝수: do, i홀수: su
    if not do_cards:
        win = 'su'
        break
    elif not su_cards:
        win = 'do'
        break
    else:
        if i % 2 == 0:
            do_grnd.append(do_cards.pop())
            if do_grnd[0] == 5:
                do_cards = sorted(do_grnd,reverse=True) + sorted(su_grnd.sort,reverse=True) + do_cards
                do_grnd = []; su_grnd = []
                print(id(do_grnd))
        else:
            su_grnd.append(su_cards.pop())
            if su_grnd[0] == 5:
                do_cards = sorted(do_grnd,reverse=True) + sorted(su_grnd,reverse=True) + do_cards
                do_grnd = []; su_grnd = []

        if do_grnd and su_grnd:
            if do_grnd[0] + su_grnd[0] == 5:
                su_cards = sorted(su_grnd,reverse=True) + sorted(do_grnd,reverse=True) + su_cards
                do_grnd = []; su_grnd = []

if win is None:
    if len(do_cards) > len(su_cards):
        win = 'do'
    elif len(do_cards) < len(su_cards):
        win = 'su'
    else:
        win = 'dosu'

print(win)

