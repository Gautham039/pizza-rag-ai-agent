# 🍽️ Restaurant Review AI — My First RAG Project

Hi! I'm a beginner in **AI Engineering**, currently learning how to build practical AI applications through hands-on projects.

This is my **first AI project**, built while learning about Retrieval-Augmented Generation (RAG).

## 🚀 About the Project

This project is a simple AI-powered restaurant review assistant. It uses RAG to retrieve relevant restaurant reviews from a dataset and generate answers based on the retrieved information.

Instead of relying only on the language model's existing knowledge, the application searches the review database and uses relevant results as context when answering questions.

## 🧠 How I Built It

This project was inspired by a tutorial, but I wanted to understand what I was building rather than simply copy and paste the code.

My learning process:

1. First, I watched the tutorial to understand the overall workflow.
2. Then, I tried to recreate the project on my own.
3. I referred back to the tutorial when I got stuck.
4. I explored how the different components work together.

I'm still learning, and this project is part of my journey toward becoming an AI Engineer.

## 🛠️ Technologies Used

- **Python** — Main programming language
- **Ollama** — Running language models locally
- **Qwen3:4B** — Language model for generating responses
- **LangChain** — Connecting the different components
- **ChromaDB** — Storing and retrieving vector embeddings
- **mxbai-embed-large** — Generating text embeddings
- **Pandas** — Reading and processing the review dataset

## ⚙️ How It Works

1. Restaurant reviews are loaded from a CSV dataset.
2. The reviews are converted into vector embeddings.
3. The embeddings are stored in ChromaDB.
4. When a user asks a question, the retriever searches for relevant reviews.
5. The retrieved reviews are passed to the language model.
6. The model generates an answer using the retrieved context.

## 🎯 What I Learned

While building this project, I explored:

- What RAG is and why it is useful.
- How text embeddings work.
- How vector databases store information.
- How similarity search retrieves relevant documents.
- How LangChain connects models, prompts, and retrievers.
- How to run an AI application locally using Ollama.

## 🔮 What's Next?

This is just the beginning of my AI Engineering journey.

I'm planning to improve my Python skills, learn database integration, understand tool calling, and eventually build AI agents that can interact with real-world data and perform useful tasks.

## 💬 Feedback & Suggestions

I'm still a beginner, so **constructive feedback, suggestions, and guidance are always welcome!**

If you have any suggestions on how I can improve this project or what I should learn next, feel free to reach out.

- **Discord:** `gauthm007`
- **Email:** [gauthamkrishna039@gmail.com](mailto:gauthamkrishna039@gmail.com)

Thanks for checking out my first project! ⭐
