#!/usr/bin/python3
# --- 001 > U5W1P1_Task1_w1

def solution(s):
    # print( ''.join(reversed(s))  )
    if( s==''.join(reversed(s))):
        return  bool(True)
    return bool(False)

if __name__ == "__main__":
    print('----------start------------')
    s = "zork"
    print(solution( s ))
    print('------------end------------')
