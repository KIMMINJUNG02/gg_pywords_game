#######절차지향(함수)
'''
from word_game_5ea_except import wordLoad, gameRun, scorePrint
import time

words = wordLoad()
print(words)
input_s = input("준비? 엔터를 입력하세요. 종료하려면 q를 입력하세요.")
if input_s=='q':
    exit()

starttime = time.time()
total_corr = scorePrint(words)
endtime = time.time()
total_time = endtime-starttime
print("게임 걸린시간 : %.2f초, 맞춘 개수: %d"%(total_time, total_corr))
'''

########절차지향(class)
from word_game_5ea_class import WordGame

new_game = WordGame()
new_game.run()