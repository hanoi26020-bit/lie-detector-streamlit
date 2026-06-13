import streamlit as st
import random

st.set_page_config(
    page_title="AI 거짓말 탐지기",
    page_icon="🤥",
)

st.title("🤥 AI 거짓말 탐지기")
st.write("문장을 입력하면 AI가 장난스럽게 거짓말 지수를 분석합니다.")

suspicious_words = [
    "진짜",
    "절대",
    "무조건",
    "100%",
    "확실",
    "맹세",
    "한번도",
    "솔직히",
    "사실"
]

text = st.text_area(
    "문장을 입력하세요",
    placeholder="예) 저는 숙제를 정말 다 했어요."
)

if st.button("🔍 분석하기"):

    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:

        score = random.randint(0, 40)
        found_words = []

        for word in suspicious_words:
            if word in text:
                score += random.randint(10, 20)
                found_words.append(word)

        score = min(score, 100)

        st.subheader("📊 분석 결과")

        st.progress(score)

        st.metric(
            label="거짓말 지수",
            value=f"{score}%"
        )

        if score < 30:
            st.success("😇 매우 진실해 보입니다.")
        elif score < 60:
            st.info("🤔 약간 수상합니다.")
        elif score < 80:
            st.warning("😏 의심스러운 부분이 있습니다.")
        else:
            st.error("🚨 거짓말 가능성이 높아 보입니다!")

        if found_words:
            st.subheader("🔍 의심 키워드")

            for word in found_words:
                st.write(f"• {word}")

        reasons = [
            "너무 강조하는 표현이 많습니다.",
            "설명이 지나치게 완벽합니다.",
            "AI의 촉이 뭔가 이상하다고 말합니다.",
            "과도한 자신감이 감지되었습니다.",
            "조금 수상한 느낌이 있습니다.",
            "특별한 근거는 없지만 의심됩니다."
        ]

        st.subheader("🤖 AI 의견")
        st.write(random.choice(reasons))

st.caption("※ 이 서비스는 재미를 위한 프로그램이며 실제 거짓말을 판별하지 않습니다.")
