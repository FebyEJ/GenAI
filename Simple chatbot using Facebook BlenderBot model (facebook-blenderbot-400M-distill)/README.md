As one of my initial experiments in GenAI, I created a simple chatbot using Facebook BlenderBot model (facebook-blenderbot-400M-distill) from Hugging Face. 

## Output
This is a simple conversation I had with the chatbot. But the chats don't make sense!
![Chatbot_output](https://github.com/user-attachments/assets/c78def36-689d-4206-acc9-ff3b5851eda8)

## Observations: Why BlenderBot 400M's Answers Do Not Make Sense:

BlenderBot 400M is a lightweight, older conversational AI model, and its limitations explain why its responses can sometimes be inaccurate or inconsistent. Key reasons include:

### 1. Small and Outdated Architecture  
BlenderBot 400M is a distilled model with only 400 million parameters—tiny compared to modern models like ChatGPT or LLaMA 3 (7–70B+).
- Lacks training on diverse tasks or strong factual grounding  
- Prone to shallow, inconsistent, or inaccurate replies (e.g., claiming to use tools it doesn’t actually access)

### 2. Not Built for Fact-Based Q&A  
The model is optimized for casual, open-domain conversation—not for:
- Answering factual or self-referential questions accurately  
- Understanding technical terms (e.g., "language model")  
- Handling structured Q&A scenarios

### 3. No Conversation Memory  
Each message is processed in isolation, leading to:
- Contradictory or contextually unaware responses  
- No recollection of earlier parts of the conversation

> In short, BlenderBot 400M is best seen as a creative chatbot, not a reliable source of truth or memory-aware assistant.
