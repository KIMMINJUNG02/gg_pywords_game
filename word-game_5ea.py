# 시작
from pygame import mixer
import time
import random

def scorePrint():
    result=0
    for i in range(1,6):
        print(f"Question #{i}")
        result += gameRun()
    if result>=3: print("합격했습니다.")
    else: print("불합격했습니다.")
    return result

def gameRun():
    question = random.choice(words)
    print(question)
    answer = input()
    if question==answer:
        print("맞춰서~\n")
        mixer.music.load("./word_game_problem/assets/good.wav")
        mixer.music.play()
        return 1
    else:
        print("못맞춰서~\n")
        mixer.music.load("./word_game_problem/assets/bad.wav")
        mixer.music.play()
        return 0

#################main#################
mixer.init()
with open("./word_game_problem/data/word.txt","r", encoding='utf-8') as f:
    words=list(f)
    words = [word.strip() for word in words]
    print(words)
input("준비? 엔터를 입력하세요.")
starttime = time.time()
total_corr = scorePrint()
endtime = time.time()
total_time = endtime-starttime
print("게임 걸린시간 : %.2f초, 맞춘 개수: %d"%(total_time, total_corr))