import os
import subprocess

current_folder = os.getcwd()
print(current_folder)
# 현재 폴더의 모든 하위 폴더를 반복
for foldername, subfolder, filenames in os.walk(current_folder):
    print(foldername, subfolder, filenames)
    # root 디렉토리는 제외
    if foldername == current_folder: continue
    folder_path = os.path.join(foldername, '.git')
#     subfolder.run('rm', '-rf', folder_path)
    print(f'{folder_path} 폴더가 삭제 되었습니다.')
