# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:29:34 2024

@author: Zhaojx
"""

import pandas as pd
import os

def csv2graph(root_path, file_name):
    csv_file_path = root_path + file_name + '.csv'
    csv_file = pd.read_csv(csv_file_path, sep=',', header=0)
    graph_file_path = root_path + file_name + '.data'
    node1 = []
    node2 = []
    weight = []
    
    with open(graph_file_path,'w') as file:
        file.write('t # 0\n')
        for i in range(len(csv_file)):
            node1.append(csv_file.iloc[i, 0])
            node2.append(csv_file.iloc[i, 1])
            weight.append(csv_file.iloc[i, 2])
        node_num = max(set(node1) | set(node2)) + 1
        
        for i in range(node_num):
            file.write('v ' + str(i) + ' ' + str(i) + '\n')
        for i in range(len(csv_file)):
            file.write('e ' + str(node1[i]) + ' ' +  str(node2[i]) + ' ' + str(weight[i]+11) + '\n')
        
        file.write('t # -1\n')

root_path = r'D:\\works\\学工\\数据挖掘\\第二次互评作业\\data\\'
name_list = []
for name in os.listdir(root_path):
    if(name.split('.')[1] == 'csv'):
        name_list.append(name.split('.')[0])

for name in name_list:
    csv2graph(root_path, name)

        