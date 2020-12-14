#How long time I need?
import time


n = int(input())
data = list(map(int, input().split()))
start_time = time.time() # start of time
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

#Program Sourcecode
end_time = time.time() # end of time
print("time : ", end_time - start_time)

