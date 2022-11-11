import csv
import pandas as pd

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
        if int(line[0]) in edgeDict.keys():
            edgeDict[int(line[0])].append(line[1])
        else:
            edgeDict[int(line[0])] = [line[1]]

print(edgeDict)


def load_graph(path):
    return '1'


def calculate_page_rank(beta, epcil, maxIterations):
    return '1'


def get_PageRank(node_name):
    return '1'


def get_top_PageRank(n):
    return '1'


def get_all_PageRank():
    return 1
