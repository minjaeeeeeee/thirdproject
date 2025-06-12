import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

st.title("조합화학 - 기본 화학 조각 포함 화합물 찾기")

# 1. 기본 조각 SMILES 입력 받기
fragment_smiles = st.text_input("기본 화학 조각 SMILES를 입력하세요 (예: 'CO')")

# 2. 예시 화합물 데이터 (이름과 SMILES)
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

if fragment_smiles:
    fragment_mol = Chem.MolFromSmiles(fragment_smiles)
    if fragment_mol is None:
        st.error("유효하지 않은 SMILES 형식입니다. 다시 입력해주세요.")
    else:
        # 3. 조각이 포함된 화합물 찾기
        matched = []
        for name, smi in compound_data.items():
            mol = Chem.MolFromSmiles(smi)
            if mol.HasSubstructMatch(fragment_mol):
                matched.append((name, mol))

        if len(matched) == 0:
            st.warning("입력한 조각이 포함된 화합물이 없습니다.")
        else:
            st.subheader(f"'{fragment_smiles}' 조각이 포함된 대표 화합물 3개")

            # 최대 3개까지 보여주기
            for name, mol in matched[:3]:
                st.write(f"**{name}**")
                st.image(Draw.MolToImage(mol), width=300)
