def twoSum(nums, target):
        keys = []
        for index, value in enumerate(nums):
            if loopThruList(nums, index, target - value) == True:
                keys.append(index)
        return keys

def loopThruList(dataList, index, search):
    cacheList = dataList.copy()
    cacheList.pop(index)
    founded = False
    for element in cacheList:
        if element == search:
            founded = True
    return founded        

print( twoSum([0,4,3,0], 0))