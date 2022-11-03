#python program to find all triplets with zero sum

def findTriplets(arr,n):
    f=False
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                    f=True

    if(f==False):
        print("not exist")


arr=[-1,0,1,2,-1,-4]

n=len(arr)
findTriplets(arr,n)

