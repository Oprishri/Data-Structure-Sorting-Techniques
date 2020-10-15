# Data Structure (Sorting-Techniques)-Bubble Sort

arr = [64, 25, 12, 22, 11]

def bubble_sort(arr):
  n=len(arr)
  for j in range(n):
    flag=False
    for i in range(len(arr)-1):
      if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
        flag=True
    if flag==False:
      break
  return arr
bubble_sort(arr)
