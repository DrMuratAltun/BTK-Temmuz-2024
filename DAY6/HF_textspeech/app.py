from gtts import gTTS
import streamlit as st
import os
import translator
from translate import Translator

st.title('Text To Speech')

lang_options = {
    'Turkish': 'tr',
    'English': 'en',
    'German': 'de',
    'French': 'fr',
    'Spanish': 'es'
}

input_language=st.selectbox("Your txt language:", list(lang_options.keys()))
lang_input=lang_options[input_language]
selected_lang = st.selectbox("Language to be vocalized:", list(lang_options.keys()))
lang = lang_options[selected_lang]

uploaded_file = st.file_uploader("Upload.txt file:", type=["txt"])


#translator = Translator(from_lang=lang_input, to_lang=lang)
#translated_text = translator.translate(text, src=lang_input, dest=lang_out).text
#translated_text = translator.translate(text)
#st.write(f"Çevrilen metin ({text}):\n{translated_text}")


if uploaded_file is not None:
    text = uploaded_file.read().decode('utf-8')
    st.write(f"Text:\n{text}")
    translator = Translator(from_lang=lang_input, to_lang=lang)
    #translated_text = translator.translate(text, src=lang_input, dest=lang_out).text
    translated_text = translator.translate(text)
    st.write(f"Translated Text:\n{translated_text}")

    if st.button("Create"):
        try:
            save_it = gTTS(text=translated_text, lang=lang, slow=False)
            output_filename = str(text[:5]) + '.mp3'
            save_it.save(output_filename)
            st.success(f"Here is your file: {output_filename}")

            
            with open(output_filename, "rb") as file:
                st.download_button(
                    label="Download",
                    data=file,
                    file_name=output_filename,
                    mime="audio/mpeg",
                )
            
            
                    
                
        except Exception as e:
            st.error("Error.")
            print("Hata:", e)
        
        
    
       