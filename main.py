import csv

# import pandas as pd

# df = pd.read_csv('soc-sign-bitcoinotc.csv')
# print(df.to_string())

edgeDict = {}
revEdgeDict = {}
nodeDict = {}
maxWeight = 50  # maybe sum of weights?
prevPRiter = {}
currPRiter = {}


def load_graph(path):
    i = 0
    maxWeight = 1
    with open(path, 'r') as data:
        for line in csv.reader(data):
            if i == 0:
                i += 1
                continue
            nodeDict[line[0]] = 0  # init a set of all the nods
            nodeDict[line[1]] = 0
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

    # print(maxWeight)
    # print(len(nodeDict.keys()), "&&&&&&&&&&&")

    return '1'


def calculate_page_rank(beta=0.85, epcil=0.001, maxIterations=20):
    n = len(edgeDict.keys())

    # first iteration - each node gets r=1/n * weight normalized
    n = len(nodeDict.keys())
    for node in nodeDict.keys():
        prevPRiter[node] = 1 / n

    # running the algorithm
    delta = epcil + 1  # init delta for a value that assures the first running

    while maxIterations > 0 and delta > epcil:  # stop if delta is smaller than epcil or we reached maxIterations
        for node in nodeDict.keys():
            currPRiter[node] = float(beta * calc_rank(node) + 1 - beta)  # PageRank formula

        # updating
        delta = calc_delta()
        maxIterations -= 1
        for node in prevPRiter.keys():
            prevPRiter[node] = currPRiter[node]

    return '1'


def calc_rank(node):
    rank = 0
    if node in revEdgeDict.keys():
        for nei in revEdgeDict[node].keys():
            weight = revEdgeDict[node][nei]
            weight = weight / maxWeight  # normlizing to get to sum of 1
            rank += weight * prevPRiter[nei]
    return rank


def calc_delta():
    delta = sum([abs(prevPRiter[node] - currPRiter[node]) for node in nodeDict.keys()])
    delta = 0
    for node in nodeDict.keys():
        res = abs(prevPRiter[node] - currPRiter[node])
        delta += res
    return delta


def get_PageRank(node_name):
    calculate_page_rank()  # todo: maybe do once globally in main?
    if node_name in (currPRiter.keys()):
        return currPRiter[node_name]
    return '-1'


def get_top_PageRank(n):
    calculate_page_rank()  # todo: maybe do once globally in main?
    # print([tup for tup in currPRiter.items()])
    tups = [tup for tup in currPRiter.items()]
    tups.sort(key = lambda x: x[1])
    return tups[:n]


def get_all_PageRank():
    calculate_page_rank()  # todo: maybe do once globally in main?
    return [tup for tup in currPRiter.items()]


# load_graph("soc-sign-bitcoinotc.csv")
load_graph("test.csv")

print(get_all_PageRank())
