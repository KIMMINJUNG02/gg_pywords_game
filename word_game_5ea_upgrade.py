# 시작
from pygame import mixer
import time
import random

def scorePrint():
    result=0
    starttime = time.time()
    num=0
    while time.time()-starttime<20:
        num+=1
        print(f"Question #{num}")
        result += gameRun()
    return result, num

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
with open("./best_score.txt","r",encoding='utf-8') as score:
    best = list(score)
    best = int(best[0])

print("현재 best score :", best)
input("준비? 엔터를 입력하세요.")
total_corr, total_pro = scorePrint()
print("맞춘 개수: %d / %d"%(total_corr, total_pro))


#################기록 저장##############
with open("./word_game_record.txt","a",encoding='utf-8') as record:
    record.write("맞춘 개수: %d / %d"%(total_corr, total_pro))
if total_corr>best:
    print("신기록 달성!!")
    with open("./best_score.txt","w",encoding='utf-8') as score:
        score.write(f"{total_corr}")


