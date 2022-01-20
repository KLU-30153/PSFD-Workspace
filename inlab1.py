def srt(x):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if(x[i][0]>x[j][0]):
                temp = x[j]
                x[j] = x[i]
                x[i] = temp
            elif(x[i][0] == x[j][0]):
                if(x[i][1]<x[j][1]):
                    temp = x[j]
                    x[j] = x[i]
                    x[i] = temp
                     
 
# Function to sort the array of strings
# by its frequency in the array
def printArraystring(str,n):
    m = {str[i]:0 for i in range(n)}
 
    # Loop to store the frequency
    # of a string in a hash-map
    for i in range(n):
        m[str[i]] += 1
 
    # Iterator for the map
    vec = []
 
    # Loop to store the frequency and
    # string in a vector
    for key,value in m.items():
        vec.append([value,key])
 
    # Sort the string
    # using custom comparator
    srt(vec)
 
    # Loop to print the sorted vector
    for i in range(len(vec)):
        if i==len(vec)-1:
            print(vec[i][1])
        else:
            print(vec[i][1],end = ",")
         
 
# Driver Code
if __name__ == '__main__':
    arr = ["Ramesh", "Mahesh", "Mahesh", "Ramesh"]
    n = len(arr)
 
    # Function to perform sorting
    printArraystring(arr, n)