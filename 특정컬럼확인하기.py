import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = './원본/한국언론진흥재단_뉴스빅데이터_메타데이터_노인_20011231.csv' 
df = pd.read_csv(file_path, encoding='cp949')
# 판다스가 csv 파일을 데이터 프레임화 시킨다.

region_mask = df["통합 분류1"].notna() & df["통합 분류1"].str.contains("지역")
# 통합 분류1 컬럼이 비어있지 않고, '지역'이 포함된 데이터만 추출 (=지역기사만 추출)

df_region = df[region_mask].copy() 

df_region['상세지역'] = df_region['통합 분류1'].apply(
    lambda x: x.split('-')[-1].strip() if '-' in str(x) else x.strip()
)
# 상세지역이라는 컬럼을 추가할게.

# 1회용 함수 람다
# lambda x: [조건이 참일 때 매수] if [조건식] else [조건이 거짓일 때 매수]

print("=== [콘솔 확인] 1. 추출된 상세지역 상위 빈도수 ===")
print(df_region['상세지역'].value_counts(),
      f"\n 상세지역은 총 {len(df_region['상세지역'].value_counts())}개")
print("====================================================\n")


df_region['키워드'] = df_region['키워드'].fillna('')
# 빈문자열이라도 삽입 


from collections import Counter
# 어떤 요소가 몇 개씩 들어있는지 계산하여 딕셔너리 형태로 반환
# 키워드컬럼에서 키워드 순위 10

def get_top_10_keywords(series):

    all_text = " ".join(series.astype(str))

    # 단어 통합
    all_text = all_text.replace('노인들', '노인')

    words = [word.strip() for word in all_text.replace(',', ' ').split() if word.strip()]

    # 불용어 제거
    words = [word for word in words if word not in stopwords]

    top_10 = [item[0] for item in Counter(words).most_common(10)]

    return top_10

stopwords = {
    '노인', '노인들',
    '지역', '주민',
    '사회', 
    '사업', '행사',
    '전달', 
    '지원', '추진',
    '시설', '운영',
    '회장', '참석',
    '활동',
    '사랑'
}

# 지역명도 제거
regions = set(df_region['상세지역'].unique())
stopwords.update(regions)

print(stopwords)


# 지역명도 제거

regions = set(df_region['상세지역'].unique())
stopwords.update(regions)
df_region['상세지역'].unique()

summary_df = df_region.groupby('상세지역').agg(
    뉴스빈도수=('상세지역', 'count'),
    키워드순=('키워드', get_top_10_keywords)
).sort_values(by='뉴스빈도수', ascending=False)



print("=== [콘솔 확인] 4. 상세지역별 통합 키워드 순위  ===")
print(summary_df)
print("\n----------------------------------------------------")
print("데이터프레임 정보 및 타입 확인:")
print(summary_df.info())
print("====================================================\n")

def get_clean_keywords(text) :
    if not text : return []
    words = [word.strip() for word in str(text).replace(',', ' ').split() if word.strip()]

    #word.strip() 
    #for word in str(text).replace(',', ' ').split() 
    #if word.strip()
    #> for 구문에 구동이 끝나면 word, 나머지는 if 식 
    
    clean_keywords = []
    for word in words :
        if word in base_stop_words : continue
        if any(region in word for region in all_region_names): continue
        clean_words.append(word)
    return clean_words



keyword_series = summary_df['키워드순']
print("=== [콘솔 확인] 5. '키워드순' 컬럼 (시리즈 구조) ===")
print(keyword_series.head(10))
print(f"데이터 타입: {type(keyword_series)}")
print("====================================================\n")


# 분석에 무의미한 불용어(Stopwords)를 걸러내는 작업

# 제외 키워드(불용어) 리스트 정의
# --------------------------------------------------
# 기본적으로 제외할 단어들을 세트(Set) 구조로 등록합니다. (검색 속도 최적화)
base_stop_words = {'노인', '참석', '일동', '주민', 
                   "지역", "마을", "노인들", "노인분들", "주민들","주민일동",
                   "이날" }
all_region_names = list(df_region['상세지역'].dropna().unique())

def get_clean_keywords(text):
    if not text: return []
    words = [word.strip() for word in str(text).replace(',', ' ').split() if word.strip()]
    
    clean_words = []
    for word in words:
        if word in base_stop_words: continue
        if any(region in word for region in all_region_names): continue
        clean_words.append(word)
    return clean_words

# --------------------------------------------------
# 3. 상세지역별 키워드 통합 및 상위 5개 추출 (키워드순 컬럼 생성)
# --------------------------------------------------
df_region['정제된_리스트'] = df_region['키워드'].apply(get_clean_keywords)

def merge_and_rank(series):
    merged_list = [word for sublist in series for word in sublist]
    return [item[0] for item in Counter(merged_list).most_common(10)]

summary_df = df_region.groupby('상세지역').agg(
    키워드순=('정제된_리스트', merge_and_rank)
)

# 최종 출력용 시리즈 구조 생성
category_counts = summary_df['키워드순']

# --------------------------------------------------
# [콘솔 확인] 기존 출력 포맷 유지
# --------------------------------------------------
print("=== [콘솔 확인] 통합 분류1 카테고리 시리즈 ===")
print(category_counts)
print("데이터 타입:", type(category_counts))
print("====================================================\n") 