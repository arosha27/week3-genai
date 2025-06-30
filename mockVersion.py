# summary_generator.py (Mock version)

def get_summary(user_notes, instructions=None):
    """Mock summary generator based on input notes."""
    mock_response = f"""
  

                  ----------- ✅ WEEK 1: Learnings from the 5-Day GenAI Intensive Course with Google --------------
📌 Overview:
  - Completed an intensive 5-day course focused on Generative AI concepts and tools.
  - Explored key terminologies and real-world applications of LLMs and GenAI systems.

📅 Daily Breakdown:
  🔹 Day 1 – Foundational Models & Prompt Engineering:
     • Understood how LLMs evolved (Transformers → Fine-tuning → Reasoning models).
     • Learned the basics of prompt engineering for better LLM output.

  🔹 Day 2 – Embeddings and Vector Stores:
     • Grasped how embeddings work to convert text into vector format.
     • Learned about vector databases and their role in similarity search.

  🔹 Day 3 – Generative AI Agents:
     • Learned how to build autonomous agents using LLMs.
     • Understood the architecture and iteration process of agents.

  🔹 Day 4 – Domain-Specific LLMs:
     • Explored task-specific models like Med-PaLM and SecLM.
     • Learned how fine-tuned models can be used in healthcare and security.

  🔹 Day 5 – MLOps for Generative AI:
     • Understood how MLOps practices are applied to GenAI workflows.
     • Explored tools like Vertex AI to manage GenAI pipelines.

🎯 Key Concepts Learned:
  • Large Language Models (LLMs) and their evolution
  • Prompt Engineering techniques
  • Embeddings and Vector Representations
  • Vector Search and Vector Databases
  • Agentic AI and Autonomous Systems
  • Retrieval-Augmented Generation (RAG)
  • Model Fine-tuning vs. Instruction Tuning
  • Inference Acceleration and Optimization

🧠 Realization:
  → AI has revolutionized automation — we can now solve real-world problems by using pre-trained base models and fine-tuning them, instead of building everything from scratch.

🧪 Kaggle Exploration:
  • Explored the Kaggle platform and participated in a competition.
  • Understood the structure of AI challenges and various solution approaches.
  • Studied the "LLM - Detect AI Generated Text" competition to learn how GenAI is applied in classification problems.


                     -------------✅ WEEK 2: Learnings from Short Courses and Kaggle Competition Presentation----------------

📘 Completed Courses from DeepLearning.ai:

  1️⃣  ChatGPT Prompt Engineering for Developers:
     • Learned how to design effective prompts using few-shot and zero-shot methods.
     • Understood how system messages guide LLM behavior.
  
  2️⃣  Building Applications Using ChatGPT:
     • Built multi-step LLM workflows using the OpenAI API.
     • Learned techniques to structure and format LLM outputs.
  
  3️⃣  LangChain for LLM Application Development:
     • Explored LangChain’s use in building LLM-powered applications.
     • Learned how to use chains, agents, and vector stores to enhance application design.

🎤 Kaggle Competition Presentation: "LLM - Detect AI Generated Text"

  • Delivered a presentation on a real-world Kaggle competition problem.
  • Gained hands-on exposure to text classification using GenAI techniques.
  • Learned about the use of the 🧠 DistilBERT model — a lighter version of BERT.
  • Explored the full ML pipeline: preprocessing, feature engineering, model training.
  • Studied common libraries used such as: 
      - Scikit-learn
      - NumPy
      - Pandas
      - Matplotlib
  • Understood key evaluation metrics like:
      - Accuracy
      - F1-score
      - ROC-AUC

🔍 Key Takeaways:
  • Strengthened foundational skills in prompt design and LLM behavior control.
  • Gained practical exposure to GenAI tools used in production-level applications.
  • Understood how to analyze, evaluate, and present a classification problem using a pre-trained model.


"""

    if instructions:
        mock_response += f"\n(Note: Summary was adjusted based on instruction: {instructions})"

    return mock_response


# 🚀 Main program
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
            instruction = input("✏️ Enter the instruction (e.g., 'Make it more concise' or 'Add emojis'):\n")
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
