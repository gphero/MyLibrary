#체스판 Knight 이동 가능한 칸 구하기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 아스키코드로 알파벳 빼고 남은 수 + 1로 컬럼 알 수 있음

#나이트가 이동할 수 있는 8가지 방향을 2차원 배열로 정의 한닷 : 이렇게 하면 이중 루프를 안돌려도 되네..
#steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, -2), (-1, -2), (-1, 2), (1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print( result )
