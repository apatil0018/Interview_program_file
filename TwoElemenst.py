#Write a program or algorithm for Two Elements whose sum is closest to zero

def SumPair(arr,arr_size):
    inv_count=0
    if arr_size<2:
        print("Invalid input")
        return

    min_l=0
    min_r=1

    min_sum=arr[0]+arr[1]
    for l in range(0,arr_size-1):
        for r in range(l+1,arr_size):
            sum=arr[l]+arr[r]
            if abs(min_sum)>abs(sum):
                min_sum=sum
                min_l=l
                min_r=r

    print("Two elements which is closets to zero",arr[min_l],"and",arr[min_r])

arr = [-23,12,-35,45,20,36]

SumPair(arr,6)
