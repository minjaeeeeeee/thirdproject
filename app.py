import streamlit as st

st.title("조합화학 - 기본 조각 포함 화합물 찾기 (비구조화 버전)")

fragment_smiles = st.text_input("기본 화학 조각 SMILES를 입력하세요 (예: 'CO')")

compound_data = {
    "에탄올": "CCO",
    "아세트산": "CC(=O)O",
    "메탄올": "CO",
    "프로판올": "CCCO",
    "부탄올": "CCCCO",
    "아세톤": "CC(=O)C",
    "벤젠": "c1ccccc1",
    "톨루엔": "Cc1ccccc1",
    "페놀": "c1ccc(cc1)O"
}

def is_substring(fragment, compound):
    # 아주 단순한 포함 여부 체크 (SMILES 문자열 기준)
    return fragment in compound

if fragment_smiles:
    matched = []
    for name, smi in compound_data.items():
        if is_substring(fragment_smiles, smi):
            matched.append((name, smi))

    if not matched:
        st.warning("입력한 조각이 포함된 화합물이 없습니다.")
    else:
        st.subheader(f"'{fragment_smiles}' 조각이 포함된 대표 화합물 3개")

        for name, smi in matched[:3]:
            st.write(f"**{name}** - SMILES: {smi}")
            # 구글 이미지 검색 링크
            query = name + " molecule"
            url = f"https://www.google.com/search?tbm=isch&q={query.replace(' ', '+')}"
            st.markdown(f"[{name} 구조 이미지 검색]({url})")
