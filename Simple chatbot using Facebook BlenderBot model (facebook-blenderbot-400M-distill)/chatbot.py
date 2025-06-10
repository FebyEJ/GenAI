from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def chat_with_bot():
    while True:
        input_text = input("You: ")
        if input_text.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        inputs = tokenizer.encode(input_text, return_tensors="pt")
        outputs = model.generate(inputs, max_new_tokens=150) 
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        print("Chatbot:", response)

chat_with_bot()