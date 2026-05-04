import streamlit as st

st.title(" şifrem güvenlimi.com")

# Kullanıcının şifresini yazacağı alan
kullanici_sifresi = st.text_input("Kontrol etmek istediğiniz şifreyi yazın:", type="password")

if kullanici_sifresi:
    uzunluk = len(kullanici_sifresi)
    st.write(f"Şifre Uzunluğu: {uzunluk}")

    # Güvenlik Kontrol Mantığı
    if uzunluk < 8:
        st.error(f"'{kullanici_sifresi}' güvenli değil!")
        st.subheader("Seviye: Charmander")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png", width=200)
        st.info("İpucu: Şifren çok kısa, en az 8 karakter yapmalısın.")

    elif 8 <= uzunluk < 16:
        st.warning(f"'{kullanici_sifresi}' orta derecede güvenli.")
        st.subheader("Seviye: Charizard")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png", width=250)
        st.info("İpucu: Biraz daha uzun veya karmaşık yaparsan daha iyi olur.")

    else:
        st.success(f"'{kullanici_sifresi}' çok güvenli!")
        st.subheader("Seviye: Mega Charizard X")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/10059.png", width=300)
        st.balloons() # Tebrik efekti
