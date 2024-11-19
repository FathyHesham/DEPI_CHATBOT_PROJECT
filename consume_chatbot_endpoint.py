import os
from openai import AzureOpenAI

endpoint = os.getenv(
    "ENDPOINT_URL", "https://aistudiohubfor9916303168.openai.azure.com/"
)
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo-16k")
search_endpoint = os.getenv(
    "SEARCH_ENDPOINT", "https://ai-search-for-depi.search.windows.net/"
)
search_key = os.getenv("SEARCH_KEY", "put your Azure AI Search admin key here")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

# Prepare the chat prompt
chat_prompt = [
    {
        "role": "system",
        "content": "You are an expert in answering questions in Arabic about DEPI scholarship.\nonly answer in Arabic and from the data I provided, The questions could be in Arabic or English.\npolitely refuse to answer to any question not related to DEPI scholarship.",
    },
    {"role": "user", "content": "من انت"},
]

# Include speech result if speech is enabled
speech_result = chat_prompt

# Generate the completion
completion = (
    client.chat.completions.create(
        model=deployment,
        messages=speech_result,
        past_messages=5,
        max_tokens=500,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False,
    ),
)
extra_body = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "filter": None,
                "endpoint": f"{search_endpoint}",
                "index_name": "chatbot-depi-index",
                "semantic_configuration": "azureml-default",
                "authentication": {"type": "api_key", "key": f"{search_key}"},
                "embedding_dependency": {
                    "type": "endpoint",
                    "endpoint": "https://aistudiohubfor9916303168.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-07-01-preview",
                    "authentication": {
                        "type": "api_key",
                        "key": "981b619e94c44d29b739e48224f022b5",
                    },
                },
                "query_type": "vector_simple_hybrid",
                "in_scope": True,
                "role_information": "You are an expert in answering questions in Arabic about DEPI scholarship.\nonly answer in Arabic and from the data I provided, The questions could be in Arabic or English.\npolitely refuse to answer to any question not related to DEPI scholarship.",
                "strictness": 3,
                "top_n_documents": 5,
            },
        }
    ]
}
print(completion.to_json())
