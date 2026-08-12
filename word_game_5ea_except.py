# 시작
from pygame import mixer
import time
import random
import os

def scorePrint(words):
    result=0
    for i in range(1,6):
        print(f"Question #{i}")
        result += gameRun(words)
        time.sleep(0.5)
    if result>=3: print("합격했습니다.")
    else: print("불합격했습니다.")
    return result

def gameRun(words):
    mixer.init()
    question = random.choice(words)
    print(question)
    answer = input()
    if question==answer:
        print("맞춰서~\n")
        try:
            mixer.music.load("./word_game_problem/assets/good.wav")
            mixer.music.play()
        except Exception as e:
            print(f"예외 발생 {e}")
        return 1
    else:
        print("못맞춰서~\n")
        try:
            mixer.music.load("./word_game_problem/assets/bad.wav")
            mixer.music.play()
        except Exception as e:
            print(f"예외 발생 {e}")
        return 0

def wordLoad():
    word=[]
    try:
        with open("./word_game_problem/data/word.txt","r", encoding='utf-8') as f:
            word=list(f)
            word = [w.strip() for w in word]
    except Exception as err:
        print(f"예외 발생 {err}")
    return word

#################main#################
if __name__ == "__main__":
    print(__name__)
    words = wordLoad()
    print(words)
    input_s = input("준비? 엔터를 입력하세요. 종료하려면 q를 입력하세요.")
    if input_s.strip()=='q':
        exit()

    starttime = time.time()
    total_corr = scorePrint(words)
    endtime = time.time()
    total_time = endtime-starttime
    print("게임 걸린시간 : %.2f초, 맞춘 개수: %d"%(total_time, total_corr))
    ###### 기록 ######
    if not os.path.exists("./output"):
        os.makedirs("output")
    if not os.path.exists("./output/result.csv"):
        with open("./output/result.csv","w",encoding='utf-8') as record:
            record.write("맞춘개수,걸린시간\n")

    with open("./output/result.csv","a",encoding='utf-8') as record:
        record.write(f"{total_time:.2f},{total_corr}\n")