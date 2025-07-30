import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from datetime import datetime
import pyttsx3
from groq import Groq

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def handle_input():
    user_input = entry.get()
    entry.delete(0, END)

    user_input_lower = user_input.lower()

    if user_input_lower in ["exit", "quit", "stop"]:
        root.destroy()
        return

    if "hello" in user_input_lower or "hi" in user_input_lower:
        reply = "Welcome to Text Assistant. How can I help you?"
    elif "date" in user_input_lower:
        now = datetime.now().strftime("%Y-%m-%d")
        reply = f"Today's date is {now}"
    elif "time" in user_input_lower:
        time_now = datetime.now().strftime("%H:%M")
        reply = f"Current time is {time_now}"
    elif "open youtube" in user_input_lower:
        webbrowser.open("https://www.youtube.com/")
        reply = "Opening YouTube"
    elif "open facebook" in user_input_lower:
        webbrowser.open("https://www.facebook.com/")
        reply = "Opening Facebook"
    elif "open whatsapp" in user_input_lower:
        webbrowser.open("https://www.whatsapp.com/")
        reply = "Opening WhatsApp"
    elif "play" in user_input_lower:
        song = user_input_lower.replace("play", "").strip()
        if song:
            query = song.replace(" ", "+")
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            reply = f"Searching '{song}' on YouTube..."
        else:
            reply = "Please specify a song name after 'play'"
    elif "open" in user_input_lower:
        term = user_input_lower.replace("open", "").strip()
        if term:
            query = term.replace(" ", "+")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            reply = f"Redirecting to search for '{term}'"
        else:
            reply = "Please specify what to open"
    else:
        try:
            client = Groq(api_key="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")
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "Reply with short, clear, and concise answers."},
                    {"role": "user", "content": user_input}
                ],
            )
            reply = completion.choices[0].message.content
        except Exception as e:
            reply = "Sorry, I couldn't get a response. Check your internet or Groq API."

    output_label.config(text=reply)
    speak(reply)

def handle_radio():
    selected = choice.get()
    if selected == "A":
        webbrowser.open("https://www.youtube.com/")
        speak("Opening YouTube")
    elif selected == "B":
        webbrowser.open("https://www.facebook.com/")
        speak("Opening Facebook")
    elif selected == "C":
        webbrowser.open("https://www.whatsapp.com/")
        speak("Opening WhatsApp")

root = tk.Tk()
root.title("TEXT ASSISTANT (by Sanket De)")  
root.geometry("600x600")
root.configure(bg="black")

#this is the title of the app
label = tk.Label(root, text="Text Assistant", fg="white", bg="black", font=("Gloucester MT Extra Condensed", 40))
label.pack(pady=10)

#this is to type your questions......
entry = tk.Entry(root, fg="white", bg="black", font=("Helvetica", 14), width=40)
entry.place(x=25,y=99)

#last line comments
label = tk.Label(root, text='''                            #Give your feedback so we can make it convinient for you...                 
                 #use "play" as prefix to search any song on youtube...               
# use "open" as prefix to search anything on google...
                                # Made by: Sanket De''', fg="white", bg="black", font=("Eras Bold ITC", 12))
label.place(x=-110,y=470)

#this is the output box
output_label = tk.Label(root, text="", fg="black", bg="lightgrey", font=("Helvetica", 13),width=49,height=7)
output_label.place(x=25, y=140)

#this is the enter button
button=Button(root,text="ENTER",fg="black",bg="lightgrey",width=8, command=handle_input)
button.place(x=500,y=99)

#from here options and their images are set...........................
choice = tk.StringVar()

# --- YouTube Button + Image ---
yt_image = Image.open("ty.png")
yt_image = yt_image.resize((60, 30))
yt_photo = ImageTk.PhotoImage(yt_image)
yt_label = tk.Label(root, image=yt_photo, bg="black")
yt_label.place(x=0, y=300)

r1 = tk.Radiobutton(root, text="Open YouTube", variable=choice, value="A", bg="black", fg="white", command=handle_radio)
r1.place(x=70, y=305)

# --- Facebook Button + Image ---
fb_image = Image.open("fb.png")
fb_image = fb_image.resize((60, 30))
fb_photo = ImageTk.PhotoImage(fb_image)
fb_label = tk.Label(root, image=fb_photo, bg="black")
fb_label.place(x=0, y=350)

r2 = tk.Radiobutton(root, text="Open Facebook", variable=choice, value="B", bg="black", fg="white", command=handle_radio)
r2.place(x=70, y=355)

# --- WhatsApp Button + Image ---
wp_image = Image.open("wp.png")
wp_image = wp_image.resize((60, 30))
wp_photo = ImageTk.PhotoImage(wp_image)
wp_label = tk.Label(root, image=wp_photo, bg="black")
wp_label.place(x=0, y=400)

r3 = tk.Radiobutton(root, text="Open WhatsApp", variable=choice, value="C", bg="black", fg="white", command=handle_radio)
r3.place(x=70, y=405)

root.mainloop()
