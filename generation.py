from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM
from langchain.schema.runnable import RunnableSequence
import time
class Generation:
    def __init__(self,document):
        self.document = document
        self.llm_model = OllamaLLM(model="llama3.2", temperature=0.4,streaming=True)

        # Initialize memory (this will store the conversation history)
        self.memory = ConversationBufferMemory(return_messages=True)

        # Define your custom prompt
        self.prompt_template = PromptTemplate(
            input_variables=["topic", "document", "questions", "history"],
            template=(
                "You are an expert in answering the user question in Arabic.\n\n"
                "Question: {topic}\nAnswer:\n\n"
                "Please only answer in Arabic and from the data I provided you. The question will be in Arabic too.\n\n"
                "please be specific in your answer in arabic \n\n"
                "understand the question well and avoide short answers\n\n"
                #"dont confuse english with arabic with numbers too\n\n"
                "You can answer general questions from your base knowledge,but any thing about \n\n"
                "you will find te write answer in this data search it will and generate the answer : ({document})\n\n"
                "you will answer as presented in the data that i provided you \n\n"
                "Conversation History: {history}\n\n"
            )
        )

        # The data and list of general questions
        #self.document = "مبادرة مصر الرقميه تسعي الي انشاء جيل متعلم و سليم و عنده وعي و يعرف كيف يعمل علي منصات العمل الحر"
        self.questions = [
            "مرحبًا، كيف حالك؟",
            "من أنت؟",
            "ماذا تفعل؟",
            "كيف يمكنني مساعدتك؟",
            "ما هو عملك؟",
            "هل يمكنك مساعدتي؟",
            "ما هي قدراتك؟",
            "كيف يعمل هذا النظام؟",
            "ماذا تعرف عني؟",
            "ما هي اللغة التي تفهمها؟",
            "كيف أبدأ؟",
            "هل يمكنك شرح هذا لي؟",
            "ماذا يمكنني أن أسألك؟",
            "ما هو دورك؟",
            "كيف يمكنني تحسين مهاراتي؟",
            "هل تستطيع الإجابة على أي سؤال؟",
            "ما هي حدود معرفتك؟",
            "كيف تم تدريبك؟",
            "هل يمكنك إعطائي نصيحة؟",
            "كيف يمكنني استخدامك بشكل أفضل؟"
        ]

        # Create the conversation chain using the prompt template and memory
        self.conversation_chain = RunnableSequence(self.prompt_template|self.llm_model)
        
    def interact_with_conversation(self,topic):
        self.topic=topic
        history=self.memory.load_memory_variables({}).get("history", "")
        inputs = {
            "topic": self.topic,
            "document": self.document,
            "questions": ", ".join(self.questions),
            "history": history
        }

        # Use the apply method to handle multiple input variables
        response_stream = self.conversation_chain.invoke(inputs)

        #print(f"User: {topic}")
        print("AI: ", end="", flush=True)

        # Iterate over streamed response and print it progressively
        for chunk in response_stream: 
            print(chunk, end="", flush=True)
            time.sleep(0.05)

        # Save the current conversation into memory
        self.memory.save_context({"input": topic}, {"output": ''.join(response_stream)})
        

        
        