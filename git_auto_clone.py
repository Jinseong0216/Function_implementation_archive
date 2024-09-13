import os           #
import subprocess

current_folder = os.getcwd()
print('path', current_folder)
''' URL 예시
https://lab.ssafy.com/pnum2378/django_hw_1_2
'''

USER_NAME = 'pnum2378'
SUBJECT = input('과목을 입력해 주세요. ex) django, db, js, vue : ')
DAY = input('날짜를 입력해 주세요. : ')
STAGE_dic = {'hw': [2, 4], 'ws': [1, 2, 3, 4, 5, 'a', 'b', 'c']}

for SEPERATOR in ['hw', 'ws']:
    for STAGE in STAGE_dic[SEPERATOR]:
        BASE_URL = f'https://lab.ssafy.com/{USER_NAME}/{SUBJECT}_{SEPERATOR}_{DAY}_{STAGE}'
        subprocess.run(['git', 'clone', BASE_URL])