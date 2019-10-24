# reference: http://wakabame.hatenablog.com/entry/2017/09/06/221400 

"""
ベルマンフォード法
Params:
    edges: エッジに関する情報
    num_v: ノードの数
    source: スタート地点のノード番号
Return:
    d: distanceリスト全部
"""

def bellman_ford(edges:list, num_v:int, source:int):
    INF = float("inf")
    d = [INF for i in range(num_v)]
    d[source] = 0

    for i in range(num_v):
        for e in edges:
            if e[0] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                if i==num_v-1: return -1
    return d