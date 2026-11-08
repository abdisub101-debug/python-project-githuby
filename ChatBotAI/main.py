
import tkinter as tk
from urllib import response

from cffi import model
from google import genai
client = genai.Client(api_key="NotToday")
def sent_text():
    user_text = text_box.get('1.0', tk.END)
    text_area.insert(tk.END, 'You:' + user_text)
    text_box.delete('1.0', tk.END)

def computer_response(message):
    response = client.models.generate_content(
        model = "gemini-3.8-flash",
        contents = message,
    )
    text_area.insert(tk.END, 'Computer:' + response.text)

wd = tk.Tk()
wd.title("ChatBot")

text_area = tk.Text(width=40, height=20, wrap="word")
text_box = tk.Text(width=40, height=2, wrap="word")
button_clear = tk.Button(width=10, height=2, text="Clear All")
button_sent = tk.Button(width=10, height=2, text="Sent")

text_area.grid(row=0, column=0, padx=(15, 5), pady=5)
text_box.grid(row=1, column=0, padx=(15, 5), pady=5)
button_clear.grid(row=0, column=1, sticky='N' ,padx=5, pady=5)
button_sent.grid(row=1, column=1, padx=5, pady=5)

tk.mainloop()
