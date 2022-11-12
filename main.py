import csv
#import pandas as pd

# df = pd.read_csv('soc-sign-bitcoinotc.csv')
# print(df.to_string())

edgeDict = {}
revEdgeDict = {}
# edgeDict["1"]=5
# print(edgeDict["1"])
i = 0
with open("soc-sign-bitcoinotc.csv", 'r') as data:
    for line in csv.reader(data):
        if i == 0:
            i += 1
            continue
        if line[0] in edgeDict.keys():
            edgeDict[line[0]][line[1]] = line[2]
        else:  # if value not exist,create a new dic as value {node:{node:weight}}
            valueWightDic = {line[1]: line[2]}
            edgeDict[line[0]] = valueWightDic

print(edgeDict["6"])


def load_graph(path):
    return '1'

maxWight=10 #todo: delete afte merge

def calculate_page_rank(beta=0.85, epcil=0.001, maxIterations=20):
    n = len(edgeDict.keys())

    #first iteration - each node gets r=1/n
    prevPRiter = {node:calc_W_Rank(node, 1/n) for k in edgeDict.keys()}
    currPRiter = {}

    delta = 1 #todo:update with function

    while maxIterations > 0 and delta > epcil: #stop if delta is smaller than epcil or we reached maxIterations
        currPRiter =


    print(currPRiter)

def calc_W_Rank(node, rank):
    weight = #todo
    return rank*weight/maxWight

calculate_page_rank()

def get_PageRank(node_name):
    return '1'


def get_top_PageRank(n):
    return '1'


def get_all_PageRank():
    return 1
