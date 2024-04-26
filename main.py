# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:33:53 2024

@author: Zhaojx
"""

import os
import subprocess

root_path = r'D:\\works\\学工\\数据挖掘\\第二次互评作业\\data\\'

def main(root_path):
    files_and_dirs = os.listdir(root_path)
    data_files = [f for f in files_and_dirs if f.endswith('.data')]
    
    for data in data_files:
        file_path = root_path + data
        command = ['python', '-m', 'gspan_mining', '-s', '1', '-p', 'True', file_path]
        with open(root_path + 'result_' + data,'wb') as file:
            subprocess.run(command, stdout = file,  text=True)
        
if __name__ == '__main__':
    main(root_path)
        