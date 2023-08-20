def majorityElement(self, A, N):
        #Your code her
        res = {}
        for i in A:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        max_count = max(res.values())
        if max_count > (N // 2):
            for i in res:
                if res[i] == max_count:
                    return i
        
        return -1
  
