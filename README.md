NAO Robot Audio Chatbot
Welcome to the NAO Robot Audio Chatbot project! This is an exciting robotics project where a NAO robot in Webots, a free simulator, interacts with you through text-based chat. You type a message, and NAO responds using AI, speaks the response aloud, and nods its head for a lifelike interaction. Built with Python, Webots, LangChain, and Mistral AI, this project is perfect for exploring human-robot interaction and AI integration.
Check out the demo video below to see NAO in action!

Features

Text Input: Type messages (e.g., “Hi, NAO!”) in Webots’ 3D view.
AI Responses: Powered by Mistral AI via LangChain for natural replies.
Text-to-Speech: NAO speaks responses using pyttsx3.
Head Nodding: NAO nods its head during speech for engaging interaction.
Console Feedback: Real-time typing and responses shown in Webots Console.

Tech Stack

Webots R2025a: Open-source robot simulator.
Python 3.10: Run in a Conda environment (py310).
LangChain & Ollama: For Mistral AI model integration.
pyttsx3: Text-to-speech library.
Platform: Developed on Windows 10 (compatible with Mac/Linux).

Prerequisites
Before running the project, ensure you have:

A computer with at least 8GB RAM.
Internet connection for downloading tools and Mistral model.
Basic familiarity with Python and terminal commands.

Installation
1. Install Webots

Download and install Webots R2025a from cyberbotics.com.
Open Webots and create a project directory (e.g., D:\Projects\NaoChatbot).

2. Set Up Python Environment

Install Miniconda.
Open Anaconda Prompt and create a Conda environment:conda create -n py310 python=3.10
conda activate py310


Install required Python packages:pip install langchain langchain-ollama pyttsx3 pywin32 comtypes



3. Install Ollama

Download Ollama from ollama.ai and install it.
Start the Ollama server in a terminal:ollama serve


Pull the Mistral model:ollama pull mistral:latest



4. Configure Webots

In Webots, go to Tools > Preferences > General.
Set “Python command” to your Conda Python path (e.g., C:\Users\YourUsername\.conda\envs\py310\python.exe).
Restart Webots to apply changes.

5. Clone the Repository

Clone this repository to your local machine:git clone https://github.com/your-username/nao-chatbot-project


Copy chat_world.wbt to your Webots project’s worlds folder.
Copy controllers/audio_chat_controller/audio_chat_controller.py to your controllers/audio_chat_controller folder.

Usage

Start Ollama:
Run ollama serve in a terminal.


Launch Webots:
Open chat_world.wbt from your Webots project folder.
Click the Run button in Webots.


Interact with NAO:
Click the 3D view to focus on NAO.
Type a message (e.g., “Hi”) and press Enter.
Watch the Webots Console for:Key pressed: 72  # H
Typing: H
Key pressed: 105  # i
Typing: Hi
Key pressed: 4  # Enter
Enter pressed, input_text: 'Hi'
User: Hi
Processing response...
Robot: Hello! I'm NAO, how can I help?
HeadPitch device found, starting nod animation...
Nod animation completed.


NAO nods its head and speaks the response.



Project Structure

chat_world.wbt: Webots world file containing the NAO robot.
controllers/audio_chat_controller/audio_chat_controller.py: Python controller for the chatbot logic.
README.md: This documentation.

Troubleshooting

Enter Key Not Working:
If Enter registers as a different key (not 4 or 13), test key codes:from controller import Robot, Keyboard
import sys
robot = Robot()
timestep = int(robot.getBasicTimeStep())
keyboard = robot.getKeyboard()
keyboard.enable(timestep)
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    if key != -1:
        print(f"Key: {key}")
        sys.stdout.flush()


Update audio_chat_controller.py to include your key code in if key in [13, 4]:.


No AI Response:
Ensure ollama serve is running.
Test Ollama:conda activate py310
python -c "from langchain_ollama import OllamaLLM; print(OllamaLLM(model='mistral:latest')('Hi'))"


If it fails, restart Ollama or re-pull: ollama pull mistral:latest.


No Audio Output:
Test pyttsx3:python -c "import pyttsx3; pyttsx3.init().say('Test').runAndWait()"


Reinstall dependencies:pip install pywin32 comtypes




No Head Nodding:
Check Console for “HeadPitch device found...” or “Error: HeadPitch device not found.”
In audio_chat_controller.py, increase nod angle (0.5) or timing (timestep * 15) in nod_head_while_speaking().



Demo Video
See the chatbot in action: YouTube Demo (replace with your video link).
Medium Tutorial
Learn how I built this project in my Medium article: Building a Talking NAO Robot Chatbot (replace with your article link).
Future Enhancements

Chat Logging:with open('chat_log.txt', 'a') as f:
    f.write(f"User: {input_text}\nRobot: {response}\n")


Conversation Memory:from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
chain = RunnableSequence(prompt_template | llm | memory)


More Animations:head_yaw = robot.getDevice('HeadYaw')
head_yaw.setPosition(0.2)  # Tilt left
robot.step(timestep * 10)
head_yaw.setPosition(-0.2)  # Tilt right



Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Ideas for new features or bug fixes are welcome!
Acknowledgments
Thanks to Webots, LangChain, Ollama, and pyttsx3 for making this project possible. This was my first robotics adventure, and it’s been a blast!
License
This project is licensed under the MIT License. See LICENSE for details.
Created on June 15, 2025

---

### Instructions for Using the `README.md`
1. **Create the GitHub Repository**:
   - On GitHub, create a new repository named `nao-chatbot-project`.
   - Initialize it without a README (you’ll add this one).

2. **Add the `README.md`**:
   - Create a `README.md` file in your repo’s root directory.
   - Copy and paste the above markdown content.
   - Replace placeholders:
     - `https://github.com/your-username/nao-chatbot-project` with your repo URL.
     - `VIDEO_ID` with your YouTube video ID (e.g., `dQw4w9WgXcQ` for `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
     - Medium article link (`[Building a Talking NAO Robot Chatbot](#)`) with your published Medium URL.
   - If you don’t have a `LICENSE` file, either create one (MIT License text [here](https://opensource.org/licenses/MIT)) or remove the “License” section.

3. **Upload Project Files**:
   - Create the folder structure:
     - `worlds/chat_world.wbt`
     - `controllers/audio_chat_controller/audio_chat_controller.py`
   - Add files:
     - `chat_world.wbt` (your Webots world file with NAO and `controller` set to `audio_chat_controller`).
     - `audio_chat_controller.py` (use the code from your working version, as shared in the Medium article).
   - Push to GitHub:
     ```bash
     git add .
     git commit -m "Add NAO chatbot project files and README"
     git push origin main
     ```

4. **Upload Video to YouTube** (Recommended Hosting):
   - Sign into YouTube, upload your screen recording, and set visibility to “Public” or “Unlisted” (Unlisted is private but accessible via link).
   - Copy the video ID from the URL (e.g., `VIDEO_ID` from `https://www.youtube.com/watch?v=VIDEO_ID`).
   - Update the `README.md` with the correct `VIDEO_ID` for the thumbnail and link.
   - Example:
     ```markdown
     [![NAO Chatbot Demo](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
     ```

5. **Verify the `README.md`**:
   - View your repo on GitHub to confirm the YouTube thumbnail displays and links correctly.
   - Test setup instructions by cloning the repo on another machine.
   - Ensure file paths in “Project Structure” match your repo’s layout.

---

### Notes
- **Video Hosting**: As advised previously, YouTube is the best choice for hosting your demo video due to its embedding support, unlimited storage, and compatibility with GitHub and Medium. Update the `README.md` with your YouTube link once uploaded.
- **README Structure**: The file is professional yet approachable, with clear sections for setup, usage, and troubleshooting. It mirrors your Medium article’s tone and includes code snippets for enhancements, aligning with your interest in NLP and robotics.
- **Repo Best Practices**:
  - Keep the repo organized with `worlds` and `controllers` folders to match Webots’ structure.
  - Add a `.gitignore` file to exclude Conda environments or temporary files (example [here](https://github.com/github/gitignore/blob/main/Python.gitignore)).
  - Consider adding a `requirements.txt` for Python dependencies:
    ```text
    langchain
    langchain-ollama
    pyttsx3
    pywin32
    comtypes
    ```
- **Resume Integration**: Include this repo in your resume:

  NAO Robot Audio Chatbot (June 2025)

Created an interactive chatbot in Webots using LangChain (Mistral AI) and pyttsx3.
Implemented speech synthesis and head-nodding for human-robot interaction.
Published a Medium tutorial and shared code on GitHub: [repo link].
Skills: Python, Robotics, NLP, AI Integration, Simulation


Let me know if you need help with:
- Uploading the video to YouTube.
- Setting up the GitHub repo.
- Tweaking the `README.md` (e.g., adding your name or specific credits).
- Anything else for your Medium article or resume.

Share your YouTube link, Medium URL, and GitHub repo URL when ready, and I can refine further. Awesome work on this project!

