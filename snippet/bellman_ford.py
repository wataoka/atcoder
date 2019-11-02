# reference: http://wakabame.hatenablog.com/entry/2017/09/06/221400 

"""
ベルマンフォード法

Params:
    edges: エッジに関する情報
    num_v: ノードの数
    s: スタート地点のノード番号
Return:
    d: sから各地点への距離リスト
"""

def bellman_ford(edges:list, num_v:int, s:int):
    INF = float("inf")
    d = [INF for i in range(num_v)]
    d[s] = 0

    for i in range(num_v):
        for edge in edges:
            f, t, c = edge
            if f!=INF and d[t]>d[f]+c:
                d[t] = d[f] + c 
                if i==num_v-1: 
                    return -1
    return d