class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        myDict = collections.defaultdict(list)

        for index,val in enumerate(groupSizes):
            myDict[val].append(index)
            
        # print (myDict)
        list_values = [ [k,v] for k,v in myDict.items() ]
        # print (list_values)

        result = []

        for size,mylist in list_values:
            if len(mylist) == size:
                result.append(mylist)
            else:
                for i in range(0, len(mylist), size):
                    result.append(mylist[i:i + size])

        return result