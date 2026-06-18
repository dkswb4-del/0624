"""
=========================================
[시각화 관점] 통합 분류1(카테고리) 뉴스 비중 분석
- 상위 10개 카테고리 추출 및 데이터 검증
=========================================
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.


df = pd.read_csv(file_path, encoding='cp949')

# 1. '통합 분류1' 컬럼의 빈도수를 계산하여 시리즈 생성
category_counts = df["통합 분류1"].value_counts().head(10)  # 상위 10개 카테고리만 추출

# 2. ★반드시 콘솔에 시리즈 구조와 데이터 확인
print("=== [콘솔 확인] 통합 분류1  카테고리 시리즈 ===")
print(category_counts)
print("데이터 타입:", type(category_counts))
print("====================================================\n")

# 한글 폰트 설정 (환경에 맞게 선택)
plt.rcParams["font.family"] = "Malgun Gothic"  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'   # Mac
plt.rcParams["axes.unicode_minus"] = False

# 그래프 크기 설정 (가로 10인치, 세로 7인치)
plt.figure(figsize=(10, 7))

# 가로 막대 차트 생성 (y축에 카테고리 index, x축에 발행 건수 values를 지정)
# hue에 카테고리를 지정하여 각각 고유한 색상을 부여합니다.
ax = sns.barplot(
    x=category_counts.values,
    y=category_counts.index,
    hue=category_counts.index,
    palette="Set3",
    legend=True,
)

# Y축 레이블(글자)을 지우고 우측 범례로 상징화하여 시인성 확보
ax.set_yticklabels([])
plt.ylabel("뉴스 카테고리 고유 색상 (우측 범례 참조)", fontsize=12, labelpad=10)
plt.xlabel("뉴스 발행 건수 (건)", fontsize=12, labelpad=10)

# 차트 제목 설정
plt.title(
    "뉴스 통합 분류1 카테고리별 발행 비중 TOP 10",
    fontsize=16,
    fontweight="bold",
    pad=20,
)

# 가로 막대 우측 끝에 구체적인 숫자(발행 건수) 표시
for i, value in enumerate(category_counts.values):
    plt.text(value + 0.1, i, f" {value}건", va="center", ha="left", fontsize=11)

# 범례(Legend) 스타일 및 위치 커스텀
plt.legend(
    title="통합 분류 카테고리",
    loc="upper right",
    bbox_to_anchor=(1.35, 1),  # 범례가 그래프 오른쪽에 깔끔하게 배치되도록 조정
    frameon=True,
    shadow=True,
)

# 그래프 출력
plt.tight_layout()
plt.show()