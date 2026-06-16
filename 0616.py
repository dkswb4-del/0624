import pandas as pd

# CSV 파일 경로 지정
file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv'  # 파일명을 여기에 적어주세요.

# CSV 파일을 읽어서 데이터프레임으로 변환
df = pd.read_csv(file_path)

# 상위 5개 데이터 확인
print(df.head())