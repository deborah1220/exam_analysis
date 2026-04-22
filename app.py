import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.title("📊 정기고사 문항분석 결과 자동 생성기")
st.subheader("신일비즈니스고 교과협의록 지원 도구")

# 데이터 입력 섹션
st.info("교과협의록의 표 데이터를 아래에 입력해주세요.")
col1, col2 = st.columns(2)

with col1:
    class_name = st.text_input("강의실/학급명", placeholder="예: 1강의실, 2학년 1반")
    student_count = st.number_input("응시 인원", min_value=0)

with col2:
    average_score = st.number_input("평균 점수", min_value=0.0, format="%.1f")
    total_avg = st.number_input("전체 평균", min_value=0.0, format="%.1f")

# 분석 실행 버튼
if st.button("분석 결과 생성하기"):
    prompt = f"""
    학교 정기고사 문항분석 교과협의록을 작성해야 해. 
    다음 데이터를 바탕으로 '결과 분석' 내용을 전문적인 교육 용어를 사용하여 개괄식(-체)으로 작성해줘.
    
    [데이터]
    - 대상: {class_name}
    - 응시인원: {student_count}명
    - 해당 학급 평균: {average_score}점
    - 전체 평균: {total_avg}점
    
    [작성 가이드]
    1. 전체적인 성취 수준 언급
    2. 전체 평균 대비 해당 학급의 특징 분석
    3. 향후 지도 방안(기초학력 보충 등) 포함
    """
    
    response = model.generate_content(prompt)
    
    st.divider()
    st.success("✅ 생성된 분석 내용")
    st.write(response.text)