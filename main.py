import csv
#import pandas as pd

# df = pd.read_csv('soc-sign-bitcoinotc.csv')
# print(df.to_string())

edgeDict = {}
revEdgeDict = {}
nodeDict = {}
maxWeight = 1


def load_graph(path):
    i = 0
    with open(path, 'r') as data:
        for line in csv.reader(data):
            nodeDict[line[0]] = 0  # init a set of all the nods
            nodeDict[line[1]] = 0
            if i == 0:
                i += 1
                continue
            if line[0] in edgeDict.keys():
                edgeDict[line[0]][line[1]] = int(line[2])
                if maxWeight < int(line[2]):
                    maxWeight = int(line[2])
            else:  # if value not exist,create a new dic as value {node:{node:weight}}
                valueWightDic = {line[1]: int(line[2])}
                edgeDict[line[0]] = valueWightDic
                if maxWeight < int(line[2]):
                    maxWeight = int(line[2])

            if line[1] in revEdgeDict.keys():
                revEdgeDict[line[1]][line[0]] = int(line[2])
                if maxWeight < int(line[2]):
                    maxWeight = int(line[2])
            else:  # if value not exist,create a new dic as value {node:{node:weight}}
                valueWightDic = {line[0]: int(line[2])}
                revEdgeDict[line[1]] = valueWightDic
                if maxWeight < int(line[2]):
                    maxWeight = int(line[2])

def load_graph(path):
    return '1'

def calculate_page_rank(beta=0.85, epcil=0.001, maxIterations=20):
    n = len(edgeDict.keys())

    # first iteration - each node gets r=1/n
    prevPRiter = {node: calc_W_Rank(k, 1 / n) for k in edgeDict.keys()}
    currPRiter = {}

    calc_rank("1")
    delta = 1  # todo:update with function

    # while maxIterations > 0 and delta > epcil: #stop if delta is smaller than epcil or we reached maxIterations
    #     currPRiter =

    print(edgeDict)


def calc_rank(node):
    rank = 0
    for nei in edgeDict[node]:
        weight = revEdgeDict[node][nei] / maxWight
        num_of_neis = len(edgeDict[nei].keys)
        rank += weight * prevPRiter[nei] / num_of_neis
    print(rank)
    return rank


#calculate_page_rank()


def get_PageRank(node_name):
    return '1'


def get_top_PageRank(n):
    return '1'


def get_all_PageRank():
    return 1



load_graph("test.csv")
print(len(revEdgeDict.keys()))

print(maxWeight)
print(len(edgeDict.keys()))
print(edgeDict)
print(revEdgeDict)
print(nodeDict)
