def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    # Write your code here
    
    jeanShoesMap = dict()
    res = 0
    
    for jprice in priceOfJeans:
        for shprice in priceOfShoes:
            cur_sum = jprice + shprice
            jeanShoesMap[cur_sum] = jeanShoesMap.get(cur_sum, 0) + 1
    # print(jeanShoesMap)       
    for skprice in priceOfSkirts:
        for tprice in priceOfTops:
            cur_sum = dollars - (skprice + tprice)
            affordable_k = [k for k in jeanShoesMap if k <= cur_sum]
            affordable_v = [jeanShoesMap.get(k) for k in affordable_k]
            res += sum(affordable_v)
            
    
    return res