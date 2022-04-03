def mix( nums, n):
    ans=[]
    for i in range(n):
        ans.append(nums[i])   
        ans.append(nums[n+i])
    print(ans)


mix([2,5,1,3,4,7], 3)