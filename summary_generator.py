# summary_generator.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# ✅ Load the API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("SUMMARY_GENERATOR"))


def get_summary(user_notes, instructions=None):
    """Generate a summary based on user notes and optional instructions"""
    base_prompt = f"""
You are an AI assistant. A user is sharing their raw learning notes.
Generate a clean, structured summary with headings such as:

- Concepts Learned
- Tools & Libraries Explored
- Projects & Applications
- Key Takeaways

Use bullet points and clear formatting. Here are the notes:

{user_notes}
"""

    if instructions:
        base_prompt += f"\n\nPlease follow these additional instructions:\n{instructions}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes learning notes."},
            {"role": "user", "content": base_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# 🚀 Main Program
if __name__ == "__main__":
    print("📝 Enter your weekly learning notes (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    user_notes = "\n".join(lines)

    summary = get_summary(user_notes)
    print("\n📘 Generated Summary:\n")
    print(summary)

    while True:
        improve = input("\n🔁 Do you want to improve the summary? (yes/no): ").strip().lower()
        if improve == "yes":
            instruction = input("✏️ Enter the instruction (e.g., 'Make it more concise', 'Add emojis'):\n")
            summary = get_summary(user_notes, instruction)
            print("\n📘 Updated Summary:\n")
            print(summary)
        elif improve == "no":
            break
        else:
            print("Please type 'yes' or 'no'.")

    # 💾 Save final summary to file
    with open("Output.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("\n✅ Summary saved to 'Output.txt'")
