import csv
import pandas as pd

# df = pd.read_csv('soc-sign-bitcoinotc.csv')
# print(df.to_string())

edgeDict = {}
revEdgeDict = {}
nodeDict = {}


def load_graph(path):
    i = 0
    maxWeight = 1
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

    print(maxWeight)
    print(len(edgeDict.keys()))

    return '1'


def calculate_page_rank(beta, epcil, maxIterations):
    return '1'


def get_PageRank(node_name):
    return '1'


def get_top_PageRank(n):
    return '1'


def get_all_PageRank():
    return 1


load_graph("soc-sign-bitcoinotc.csv")
print(len(revEdgeDict.keys()))
