#입력받을때
n = int(intput()) # 숫자 하나
a,b,c = map(int, input().split()) # 1 2 3 처럼 공백으로 나뉜 입력을 순서대로 a, b, c에 넣음

inputs = list(map(int, input().split())) # list 형태로 받음

# 입력받을 때 입력 양이 크면 입력받다 제한시간 끝나므로.
  sys.stdin.readline().rstrip() 메서드를 사용 . 이진탐색, 정렬, 그래프

# 람다 : 이름없는 함수. 함수를 입력으로 받는 함수의 매개변수로 사용(sorted 같은)
 (lambda a, b: a+b)(3,7)
 ,
 array = [('홍길동', 50), ('이순신',32), ('아무개',74)]
 def my_key(x):
     return x[1]
 sorted(array, key=my_key))
 #my_key를 key로 넣는것과, 아래 람다함수로 구현과 겨로가 같음
 sorted(array, key=lambda x: x[1])
 ,
 #여러 리스트에 적용, 아래 처럼 하면 list1과 list2의 각원소별 합을 가진 result list를 얻음
 list1 = [1,2,3]
 list2 = [4,5,6]
 result = map(lambda a, b: a+b, list1, list2)
 print(list(result))

 #  방향벡터(왼쪽위부터 0,0 이고. 오른쪽으로가면 y증가, 아래로가면 x 증가)
# 동R 북U 서L 남D
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

 x, y = 2, 2 일때
 for i in range(4):
  nx = x + dx[i]
  ny = y + dy[i]

