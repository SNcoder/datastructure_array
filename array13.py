# # # # # # # # rotate cyclic array by one
# # # # # # # def rotate(arr,n):
# # # # # # #     x=arr[n-1]
# # # # # # #     for i in range(n-1,0,-1):
# # # # # # #         arr[i]=arr[i-1]
# # # # # # #     arr[0]=x
# # # # # # #     # return arr
# # # # # # # arr=[12,3,4,5,6,1]
# # # # # # # n=len(arr)
# # # # # # # for i in range(n):
# # # # # # #     print(arr[i],end=" ")
# # # # # # # rotate(arr,n)
# # # # # # # print(end='\n')
# # # # # # # for i in range(n):
# # # # # # #     print(arr[i],end=" ")

# # # # # # import math
# # # # # # def max_array(arr,n):
# # # # # #     m=-100000000-1
# # # # # #     em=0
# # # # # #     start=0
# # # # # #     sum=0
# # # # # #     ar=[0]*n
# # # # # #     e=0
# # # # # #     s=0
# # # # # #     for i in range(0,n):
# # # # # #         em+=arr[i]
# # # # # #         if arr[i]>0:
# # # # # #             s+=arr[i]
# # # # # #         if m<em:
# # # # # #             m=em
# # # # # #             start=s
# # # # # #             e=i
# # # # # #         if em<0:
# # # # # #             em=0
# # # # # #             s=i+1
# # # # # #         if s>0:
# # # # # #             ar.append(arr[i])
        
# # # # # #     print("max_sum array is ",m)
# # # # # #     print("start index is ",s)
# # # # # #     print("end index is e",e)
# # # # # #     for i in ar:
# # # # # #        print(i)
# # # # # # arr=[-2,-3,4,-1,-2,1,5,-3]
# # # # # # n=len(arr)
# # # # # # max_array(arr,n)
# # # # # def func1(arr,n,k):
# # # # #     arr.sort()
# # # # #     tempmx=arr[n-1]
# # # # #     tempmi=arr[0]
# # # # #     ans=arr[n-1]-arr[0]
# # # # #     for i in range(1,n):
# # # # #         if arr[i]<k:
# # # # #             continue
# # # # #         tempmi=min(arr[0]+k,arr[i]-k)
# # # # #         tempmx=max(arr[i-1]+k,arr[n-1]-k)
# # # # #         ans=min(ans,tempmx-tempmi)
# # # # #     return ans
# # # # # arr = [7, 4, 8, 8, 8, 9]
# # # # # n=len(arr)
# # # # # k=6
# # # # # print(func1(arr,n,k))

# # # # # def jump(arr,N):
# # # # #     s=0
# # # # #     e=0
# # # # #     j=0
# # # # #     for i in range(N-1):
# # # # #         e=max(e,arr[i]+1)
# # # # #         if(s==i):
# # # # #             s=e
# # # # #             j+=1
# # # # #     if (s<N-1):
# # # # #         return -1
# # # # #     return j
# # # # # N = 11 
# # # # # arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] 
# # # # # # print(jump(arr,N))
# # # # # # class Solution:
# # # # # #     def overlappedInterval(self, Intervals):
# # # # # #         #Code here
# # # # # #         Intervals.sort()
        
# # # # # #         stack = []
# # # # # #         stack.append(Intervals[0])
        
# # # # # #         for i in Intervals[1:]:
# # # # # #             if stack[-1][0]<=i[0]<=stack[-1][1]:
# # # # # #                 stack[-1][1]=max(stack[-1][1],i[1])
# # # # # #             else:
# # # # # #                 stack.append(i)
# # # # # #         return stack
            
# # # # # class Solution:
# # # # #     def overlappedInterval(self, Intervals):
# # # # #         #Code here
# # # # #         Intervals.sort()
        
# # # # #         stack = []
# # # # #         stack.append(Intervals[0])
        
# # # # #         for i in Intervals[1:]:
# # # # #             if stack[-1][0]<=i[0]<=stack[-1][1]:
# # # # #                 stack[-1][1]=max(stack[-1][1],i[1])
# # # # #             else:
# # # # #                 stack.append(i)
# # # # #         return stack
            
# # # # # def overlappedInterval(arr):
# # # # #         arr.sort()
# # # # #         i=0
# # # # #         while(i<len(arr)-1):
# # # # #             a=i+1
# # # # #             if arr[i][1]<arr[a][0]:
# # # # #                 i+=1
# # # # #             else:
# # # # #                 if arr[i][1]>=arr[a][1]:
# # # # #                     arr.pop(a)
# # # # #                 else:
# # # # #                     arr[i][1]=arr[a][1]
# # # # #                     arr.pop(a)
# # # # #         return arr
# # # # # arr=[[1,3],[2,4],[6,7]]
# # # # # # print(overlappedInterval(arr))
# # # # # # arr.pop(1)
# # # # # print(arr[0])
# # # # # # print(arr[1][0])
# # # # # for i in arr[1:]:
# # # # #     print(i)
# # # # arr = [1, 2, 3, 6, 5, 4]
# # # # # n=len(arr)
# # # # # # s=0
# # # # # # e=len(arr)
# # # # # # arr[s:e]=arr[s:e][::-1]
# # # # # # print(arr[s:e])
# # # # # i=2
# # # # # for j in range(n-1, i, -1):
# # # # #             if (arr[j] > arr[i]):
# # # # # #                 break
# # # # # print(j)
# # # # for i in range(5,-1,-1):
# # # #         print(arr[i])

# # # def mergesort(arr):
# # #     if(len(arr)>1):
# # #         mid=len(arr)//2
# # #         l=arr[:mid]
# # #         r=arr[mid:]
# # #         mergesort(l)
# # #         mergesort(r)
# # #         i=0
# # #         j=0
# # #         k=0
# # #         while(i<len(l) and j<len(r)):
# # #             if l[i]<=r[j]:
# # #                 arr[k]=l[i]
# # #                 i=i+1
# # #             else:
# # #                 arr[k]=r[j]
# # #                 j=j+1
# # #             k=k+1
# # #         while(i<len(l)):
# # #             arr[k]=l[i]
# # #             k=k+1
# # #             i=i+1
# # #         while(j<len(r)):
# # #             arr[k]=r[j]
# # #             k=k+1
# # #             j=j+1
# # # arr=[3,11,56,33,2,12]
# # # mergesort(arr)
# # # print(arr)            
# # # def sell_buy(arr,n):
# # #     buy=arr[0]
# # #     max_profit=0
# # #     for i in range(1,n):
# # #         if buy>arr[i]:
# # #             buy=arr[i]
# # #         elif(arr[i]-buy>max_profit):
# # #             max_profit=arr[i]-buy
# # #     return max_profit
# # # arr=[7,1,5,6,4]
# # # n=len(arr)
# # # maxs_profit=sell_buy(arr,n)
# # # print(maxs_profit)

# # #  sum is equal to count pair
# # # def count_pair(arr,n,sum):
# # #     m=[n]*1000
# # #     for i in range(0,n):
# # #         m[arr[i]]+=1
# # #     tw=0
# # #     for i in range(0,n):
# # #         tw+=m[sum-arr[i]]
# # #         if(sum-arr[i]==arr[i]):
# # #             tw-=1
# # #     return(int(tw//2))
# # # arr=[6,3,4,7,2]
# # # n=len(arr)
# # # sum=5
# # # print(count_pair(arr,n,sum))

# # def sum_count(arr,k):
# #     d={}
# #     c=0
# #     for i in arr:
# #         if k-i in d:
# #             c+=d[k-i]
# #         if i in d:
# #             d[i]+=1
# #         else:
# #             d[i]=1
# #     return c
# # arr=[1,2,4,3,6]
# # print(sum_count(arr,5))

# #print common element in three sorted array in array

# # def c_e(a1,a2,a3,n1,n2,n3):
# #     i,j,k=0,0,0
# #     while(i<n1 and j<n2 and k<n3):
# #         if(a1[i]==a2[j] and a2[j]==a3[k]):
# #             print(i)
# #             i=i+1
# #             j=j+1
# #             k=k+1
# #         elif(a1[i]<a2[j]):
# #             i=i+1
# #         elif(a2[j]<a3[k]):
# #             j=j+1
# #         else:
# #             k=k+1
# # a1 = [1, 5, 10, 20, 40, 80]
# # a2 = [6, 7, 20, 80, 100]
# # a3 = [3, 4, 15, 20, 30, 70, 80, 120]
# # n1=len(a1)
# # n2=len(a2)
# # n3=len(a3)
# # c_e(a1,a2,a3,n1,n2,n3)
# def b_search(a1,n1,ele):
#     l=0
#     h=n1-1
#     mid=(l+h)//2
#     while(l<=h):
#         if(a1[mid]==ele):
#             return True
#         elif(a1[mid]<ele):
#             l=mid+1
#         else:
#             h=mid-1
#     return False



# def c_e(a1,a2,a3,n1,n2,n3):
#     for i in a1:
#         if(i!=0 and a1[i]==a1[i-1]):
#             continue
        
#         if(b_search(a2,n2,a1[i]) and b_search(a3,n3,a1[i]) ):
#             print(a1[i],end=" ")
# a1 = [1, 5, 10, 20, 40, 80]
# a2 = [6, 7, 20, 80, 100]
# a3 = [3, 4, 15, 20, 30, 70, 80, 120]
# n1=len(a1)
# n2=len(a2)
# n3=len(a3)
# c_e(a1,a2,a3,n1,n2,n3)
# print(1%2)
# print(-5%2)
def rearrange(arr,n):
    i=0
    j=n-1
    while(i<j):
        while(i<n-1 and arr[i]>0):
            i+=1
        while(j>=0 and arr[j]<0):
            j-=1
        if(i<j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    
    if(i==0 and i==n):
        return 0

    k=0
    while(k<n and i<n):
        temp=arr[k]
        arr[k]=arr[i]
        arr[i]=temp
        i=i+1
        k+=2
def parr(arr,n):
    for i in range(0,n):
        print(arr[i])        
arr=[1, 2, 3, -4, -1, 4]
n=len(arr)
parr(arr,n)
rearrange(arr,n)
print("\n")
parr(arr,n)
