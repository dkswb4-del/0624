import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.


df = pd.read_csv(file_path, encoding='cp949')



# 🛠️ 통합 분류 집계 시각화


plt.rcParams["font.family"] = "Malgun Gothic"  
plt.rcParams["axes.unicode_minus"] = False  


##### 여기서 부터 커스터마이징 #####

'''
LLM 프롬프트 명령어

1. 주제 : **주요 언론사별 뉴스 발행량 비교**
    주력컬럼 : 언론사, 일자
    시각화 메서드 : 막대 차트 (Bar Chart)
    X축 : 언론사
    Y축 : 뉴스 발행 건수

    이거 주제로 df가 전체 데이터프레임이야
    시각화를 위한 시리즈를 생성해줘
    반드시 시리즈를 콘솔에 확인시켜줘야해 그 다음에 시각화진행 

'''

# 1. 언론사별 뉴스 발행량 시리즈 생성
media_counts = df["언론사"].value_counts()

# 2. 반드시 콘솔에 시리즈 구조와 데이터 확인
print("=== [콘솔 확인] 언론사별 뉴스 발행량 시리즈 ===")
print(media_counts)
print("Type:", type(media_counts))
print("============================================\n")

# 3. 시리즈를 활용한 막대 차트 시각화
# 그래프 크기 설정 (가로 10인치, 세로 6인치)
plt.figure(figsize=(10, 6))

# Seaborn을 활용한 막대 차트 생성
# 시리즈의 index(언론사명)를 X축으로, values(발행 건수)를 Y축으로 지정합니다.
sns.barplot(x=media_counts.index, y=media_counts.values, palette="muted")

# 차트 제목 및 축 레이블 설정
plt.title("주요 언론사별 뉴스 발행량 비교", fontsize=16, fontweight="bold", pad=15)
plt.xlabel("언론사", fontsize=12, labelpad=10)
plt.ylabel("뉴스 발행 건수 (건)", fontsize=12, labelpad=10)

# 막대 위에 구체적인 숫자 표시 (가독성 향상)
for i, value in enumerate(media_counts.values):
    plt.text(i, value + 0.1, str(value), ha="center", va="bottom", fontsize=11)

# 그래프 출력
plt.tight_layout()
plt.show()

