from controller import Robot, Keyboard, Display
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
import pyttsx3
import sys
import time

# Initialize Webots robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())
keyboard = robot.getKeyboard()
keyboard.enable(timestep)

# Initialize display
display = robot.getDevice('chat_display')
if display:
    print("Display initialized")
    display.setColor(0xFFFFFF)  # White text
    display.setFont('Arial', 16, True)  # Larger font
    display.fillRectangle(0, 0, display.getWidth(), display.getHeight())  # Clear display
else:
    print("Display not found")

# Initialize pyttsx3 for TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# Initialize LangChain with Ollama
llm = OllamaLLM(model='mistral:latest')
prompt_template = PromptTemplate(
    input_variables=['input'],
    template='You are a friendly NAO robot. Respond to: {input}'
)
chain = RunnableSequence(prompt_template | llm)

# Chat state
input_text = ''
response = ''
new_input = False
last_key = -1  # Track last processed key for debouncing

def display_text(text, y_offset):
    if display:
        display.setColor(0x000000)  # Black background
        display.fillRectangle(0, y_offset, display.getWidth(), 20)
        display.setColor(0xFFFFFF)  # White text
        display.drawText(text[:50], 5, y_offset)  # Limit to 50 chars

def nod_head_while_speaking():
    """Animate NAO's head nodding during speech."""
    head_pitch = robot.getDevice('HeadPitch')
    if head_pitch:
        print("HeadPitch device found, starting nod animation...")
        sys.stdout.flush()
        # Perform 3 nod cycles (down and up)
        for _ in range(3):
            head_pitch.setPosition(0.4)  # Nod down (increased for visibility)
            robot.step(timestep * 10)  # Wait longer for smooth motion
            head_pitch.setPosition(0.0)  # Return to neutral
            robot.step(timestep * 10)
        print("Nod animation completed.")
        sys.stdout.flush()
    else:
        print("Error: HeadPitch device not found.")
        sys.stdout.flush()

print("Chatbot ready! Type your message and press Enter.")
sys.stdout.flush()

# Main loop
while robot.step(timestep) != -1:
    # Get keyboard input
    key = keyboard.getKey()
    if key != -1 and key != last_key:  # Process only new keypresses
        print(f"Key pressed: {key}")  # Debug
        sys.stdout.flush()
        if key in [13, 4]:  # Handle Enter as 13 or 4
            print(f"Enter pressed, input_text: '{input_text}'")  # Debug
            if input_text.strip():  # Non-empty input
                new_input = True
                print(f"User: {input_text}")
                sys.stdout.flush()
        elif key == 8:  # Backspace
            input_text = input_text[:-1]
            print(f"Typing: {input_text}")
            sys.stdout.flush()
            display_text(f"Typing: {input_text}", 10)
        elif 32 <= key <= 126:  # Printable ASCII
            input_text += chr(key)
            print(f"Typing: {input_text}")
            sys.stdout.flush()
            display_text(f"Typing: {input_text}", 10)
        last_key = key  # Update last processed key
    elif key == -1:  # Reset when no key is pressed
        last_key = -1

    # Process input and get LLM response
    if new_input:
        print("Processing response...")  # Debug
        sys.stdout.flush()
        try:
            response = chain.invoke({'input': input_text})
            print(f"Robot: {response}")
            sys.stdout.flush()
            if display:
                display_text(f"User: {input_text}", 30)
                display_text(f"Robot: {response}", 50)
            # Start nodding animation in parallel with speech
            nod_head_while_speaking()
            # Speak the response
            engine.say(response)
            engine.runAndWait()
            display_text("Typing: ", 10)  # Reset typing line
        except Exception as e:
            print(f"Error generating response: {e}")
            sys.stdout.flush()
        input_text = ''
        new_input = False