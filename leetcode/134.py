#贪心算法，如果能环绕一圈，那么所有的汽油加起来应该够所有的消耗
def canCompleteCircuit(gas, cost) -> int:
    # 暴力遍历会超时
    # lu = len(gas)
    # for i in range(len(gas)):
    #     index = i
    #     pre_cost = 0
    #     pre_get = 0
    #     while True:
    #         print(pre_get,pre_cost)
    #         last = pre_get - pre_cost
    #         if last < 0: break
    #         pre_get = last + gas[index % lu]
    #         pre_cost = cost[index % lu]
    #         index += 1
    #         if index > i + lu:
    #             return i
    # return -1

    n = len(gas)

    total_tank, curr_tank = 0, 0
    starting_station = 0
    for i in range(n):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        if curr_tank < 0:
            starting_station = i + 1
            curr_tank = 0
    #如果所有汽油加起来都不够消耗的，那肯定不能环绕一圈
    return starting_station if total_tank >= 0 else -1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))