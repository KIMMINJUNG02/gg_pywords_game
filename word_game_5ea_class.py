# 시작
from pygame import mixer
import time
import random
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent


# 클래스 정의
class WordGame: # 상속없을땐 괄호X
    #속성 : words
    def __init__(self):
        self.words = []
        self.result = 0
        self.total_time = 0
    
    #메서드
    def scorePrint(self):
        for i in range(1,6):
            print(f"Question #{i}")
            self.result += self.gameRun()
            time.sleep(0.5)
        if self.result>=3: print("합격했습니다.")
        else: print("불합격했습니다.")

    def gameRun(self):
        mixer.init()
        question = random.choice(self.words)
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

    def wordLoad(self):
        try:
            word_path = BASE_DIR /"word_game_problem"/"data"/"word.txt"
            with open(word_path,"r", encoding='utf-8') as f:
                word=list(f)
                self.words = [w.strip() for w in word] # 공백문자 제거
        except Exception as err:
            print(f"예외 발생 {err}")

    def record(self):
            if not os.path.exists("./output"):
                os.makedirs("output")
            if not os.path.exists("./output/result.csv"):
                with open("./output/result.csv","w",encoding='utf-8') as record:
                    record.write("맞춘개수,걸린시간\n")

            with open("./output/result.csv","a",encoding='utf-8') as record:
                record.write(f"{self.total_time:.2f},{self.result}\n")

    def run(self):
        self.wordLoad()
        print(self.words)
        input_s = input("준비? 엔터를 입력하세요. 종료하려면 q를 입력하세요.")
        if input_s.strip()=='q':
            exit()
        starttime = time.time()
        self.scorePrint()
        endtime = time.time()
        self.total_time = endtime-starttime
        print("게임 걸린시간 : %.2f초, 맞춘 개수: %d"%(self.total_time, self.result))
        self.record()

#################main#################
if __name__ == "__main__":
    game = WordGame()
    game.run()