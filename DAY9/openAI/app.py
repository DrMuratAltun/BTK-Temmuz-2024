import gradio as gr
import time
import openai
import os
from dotenv import load_dotenv
from openai import OpenAI
client = OpenAI()

# Ortam değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Duygu analizi fonksiyonu
def sentiment_analysis(text):
    try:
        my_assistant = client.beta.assistants.create(
        instructions="Sen duygu analizi asistanısın. Sana verilen metinleri kendi dillerinde duygu durumuna göre  analiz et ve değerlendir. Cümleler farklı duygu durumlarını yansıtabilir. Metnin ana duygusunu ağır basan duyguyu ele al. Duygu durumu pozitif ise: 1, Negatif ise: -1 veya Nötr ise: 0 değerlerinden birini döndür. Senin yanıtın 1, 0 veya -1 sayılarından yalnızca birisi olmalıdır. Yanıtta başka bir şey yer almamalıdır.",
        name="SenAssist",
        #model="gpt-4-turbo",
        model='gpt-3.5-turbo',
)
        my_thread = client.beta.threads.create()
        my_message = client.beta.threads.messages.create(
            thread_id=my_thread.id,
            role="user",
            content=text)
        my_run = client.beta.threads.runs.create(
            thread_id=my_thread.id,
            assistant_id=my_assistant.id
)
        my_run = client.beta.threads.runs.retrieve(
              thread_id=my_thread.id,
              run_id=my_run.id
  )
        while my_run.status in ['queued', 'in_progress', 'cancelling']:
            time.sleep(1) # Wait for 1 second
            my_run = client.beta.threads.runs.retrieve(
                thread_id=my_thread.id,
                run_id=my_run.id
  )
        if my_run.status == 'completed':
            # list messages for my_thread
            new_messages = client.beta.threads.messages.list(thread_id=my_thread.id)
            # determine response from new_messages
            response = new_messages.data[0].content[0].text.value
            return response
            #print(f"Assistant response: {response}")
        else:
            return my_run.status     
    except Exception as e:
        return str(e)
    
# Gradio arayüzü
iface = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(lines=2, placeholder="Metni buraya giriniz..."),
    outputs="text",
    title="Duygu Analizi",
    description="Girilen metnin duygu durumunu değerlendiren bir araç."
)

if __name__ == "__main__":
    iface.launch()