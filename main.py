from Chroma_Database import chromadatabase
from generation import Generation
if __name__=="__main__":
    query = input("\nكيف اساعدك اليوم ؟ \n")
    flag=False
    while True:
        if flag == True: 
            query=input("")
        query_result=chromadatabase(query)
        generation=Generation(query_result)
        flag=True
        if query.lower() in ['exit', 'quit']:
            print("Exiting the conversation.")
            break
        generation.interact_with_conversation(query)