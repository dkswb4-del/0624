"""
def process_numbers():
    # 1. 반드시 리스트 형 변수를 먼저 선언합니다.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 2. for문 실행
    for num in numbers:
        # [짝수 판별] 2로 나누어 떨어지면 짝수입니다.
        if num % 2 == 0:
            print(num, "-> 짝수이므로 continue (건너뜁니다).")
            continue  # 아래 코드를 실행하지 않고 다음 숫자로 바로 넘어갑니다.
            
        # 홀수인 경우에만 아래 코드가 실행됩니다.
        total_sum += num
        print(num, f"-> 홀수 발견! 현재 합계: {total_sum}")
        
        # [종료 조건] 합계가 10을 넘으면 함수를 끝냅니다.
        if total_sum > 10:
            print("=> 합계가 10을 초과했습니다. return으로 함수를 종료합니다.")
            return total_sum  # 값을 가지고 함수를 즉시 빠져나갑니다.

    # 만약 리스트를 다 돌 때까지 합이 10을 넘지 않으면 여기서 return 합니다.
    return total_sum
"""

def process_numbers():
    numbers = ["회사소개", "제품소개", "게시판"]
    최종글 = ""

    for num in numbers:
     if num == "제품소개" : 
          최종글 = ""
          continue
     최종글 += num


    return 최종글

# 함수 호출 및 결과 출력
result = process_numbers()
print("최종 반환된 값:", result)

