🧠 GenAI Weekly Summary Generator
--------------------------------

A Python-based command-line app that uses OpenAI’s GPT-3.5 to convert weekly learning notes into structured summaries.

🎯 Purpose
----------
This project automates the summarization of raw notes using LLMs — showcasing real-world use of prompt engineering, API integration, and text organization.

📁 File Descriptions
--------------------

• summary_generator.py – Main script that takes user input, generates/refines summaries via OpenAI API.

• output.txt – Stores generated summaries.

• mockVersion.py – Mock script to simulate output when API limit is exceeded.

• summary.txt – Contains learnings from Week 1 and Week 2 of the GenAI program.

• prompt_examples.md – Includes 3 clear prompts used to guide LLM behavior.

• .env – Stores API key securely (not pushed to GitHub).

• .gitignore – Ensures .env and other sensitive files aren’t tracked.

🚀 How to Run
-------------

1. Install dependencies:
   pip install openai python-dotenv

2. Create .env file:
   echo OPEN_API_KEY=your-key > .env

3. Run the script:
   python summary_generator.py
