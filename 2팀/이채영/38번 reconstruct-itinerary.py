import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        # input_list = input().split(',')
        # area_list = []

        # for elem in input_list:
        #     chr_list = []
        #     for chr in elem:
        #         if chr not in '[ ]"':
        #             chr_list.append(chr)
        #     area = "".join(chr_list)
        #     area_list.append(area)

        # tickets = []
        # for i in range(len(area_list)):
        #     if i % 2 == 1:
        #         l1 = [area_list[i-1], area_list[i]]
        #         tickets.append(l1)

        
        ###sol1 - 시간초과 

        ticket_dict = {}  
        for elem in tickets:
            fr, to = elem[0], elem[1]
            if fr not in ticket_dict.keys():
                ticket_dict[fr] = [to]
            else:
                ticket_dict[fr].append(to)
                ticket_dict[fr].sort()

        # {"MUC":["LHR"], "JFK:["MUC"], "SF0":["SJC"], "LHR":["SF0"]}
    

        travel = ["JFK"]
        satisfied = False

        for i in range(len(tickets)):
            fr = travel[-1]
        
            to = ticket_dict[fr][0] #KUL
            ticket_dict[fr].pop(0)

            if to not in ticket_dict.keys() and i < len(tickets)-1: #마지막 도착 역
                arriving_area = to
                satisfied = True
                continue

            travel.append(to)
        
        if satisfied is True:
            travel.append(arriving_area)

        return travel
        
        #####sol2

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets): #key끼리& value list 내에서 모두 정렬됨
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]: #value값이 존재하는 동안
                dfs(graph[a].pop[0])
            route.append(a)

        dfs['JFK']
        return route[::-1]
