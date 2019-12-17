


def divisibleSumPairs(n, k, ar):

    counter = 0
    
    for i in range(len(ar)):
        # i < j
        # ar[i] < ar[j]
        
        # find first pair
        # print(ar[i])

        # check next one that the sum will be equal to % == 0 
        for j in range(i+1, len(ar)):
            #print(ar[i] + ar[j])
            if (ar[i] + ar[j]) % k == 0:
                counter += 1
    
    print(counter)
    return counter

ar = [1,2,3,4,5,6]
k = 5
n = len(ar)

divisibleSumPairs(n, k, ar)