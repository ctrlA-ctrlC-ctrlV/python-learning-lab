# Q10 — echo until quit (while True + break) 
msg = str(input("Say something (or 'quit'): "))

while msg.lower().strip() != "quit":
    print(f"You said: {msg}")
    msg = str(input("Say something (or 'quit'): "))

print("Goodbye!")