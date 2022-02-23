def hackerCard(collections, d):
    ##This res list is for storing the result
    res = []
    ##This dictionary is for keep track which id number is already in collection
    dictionary = {}
    for element in collections:
        ##First mark those Id numbers which are already in collections
        dictionary[element] = 1

        ##Store d+1 in a temporary variable temp
    temp = d + 1
    ##Start traversing for every value from 1 to temp(temp excluded) (means from 1 to d, cause maximum value/Id number can be added is d)
    for i in range(1, temp):
        ##If current value is more than budget then come out from the loop(Cause checking values in ascending order)
        if (i > d):
            break
        ##This flag to check if current value is already in collection or not
        flag = False
        ##If it in collection then make flag true
        if i in dictionary:
            flag = True
        ##If current value is less than or equal to budget and that value is not in collection then,
        if (i <= d and flag == False):
            ##Subtract that current value from budget
            d = d - i
            ##Append that value in result list
            res.append(i)
            ##For every iteration increment i by 1
        i = i + 1
    ##At the end return that result list
    return res


##This is just for a sample run of above function
if __name__ == "__main__":
    ##Collections list
    collections = [4,6,12,8]
    ##Budget
    d = 14
    ##Call that function
    List = hackerCard(collections, d)
    ##Print the result
    for element in List:
        print(element)