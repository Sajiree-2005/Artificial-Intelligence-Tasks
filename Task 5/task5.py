import tkinter as tk
from tkinter import scrolledtext
# Chatbot Logic (Rule-Based)
def chatbot_response(user_input):
    user_input = user_input.lower()
    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! 😊 How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! 😄"
    elif "your name" in user_input:
        return "I am your friendly rule-based chatbot."
    # FAQs
    elif "python" in user_input:
        return "Python is widely used for AI, web development, and data science."
    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence — machines that mimic human intelligence."
    elif "course" in user_input:
        return "You can explore courses on platforms like Coursera, Udemy, and edX."
    elif "help" in user_input:
        return "You can ask me about AI, Python, or general questions!"
    # Exit
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    # Default
    else:
        return "Sorry, I didn't understand that. Please try again."

# Send Message Function
def send_message(event=None):
    user_input = entry.get().strip()
    if user_input == "":
        return
    # Display user message
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    # Get bot response
    response = chatbot_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    # Clear input field
    entry.delete(0, tk.END)
    # Auto-scroll
    chat_area.yview(tk.END)
    # Exit if user says bye
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        root.after(1000, root.destroy)
# GUI Setup
root = tk.Tk()
root.title("Rule-Based Chatbot")
root.geometry("500x550")
root.resizable(False, False)
# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# Input field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)
# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)
# Bind Enter key
root.bind('<Return>', send_message)
# Initial message
chat_area.insert(tk.END, "Bot: Hello! Type 'bye' to exit.\n\n")
# Run app
root.mainloop()