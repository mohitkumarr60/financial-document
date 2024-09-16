import json
from llama_index.core import VectorStoreIndex, StorageContext
from initialization import initialize_cache_store, initialize_llm

# Initialize Redis client
vector_store = initialize_cache_store()

# Initialize LLM
initialize_llm()    

def get_cached_response(user_query):
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    # Create the index
    query_engine = index.as_query_engine()
    response = query_engine.query(user_query)
    cached_response = str(response)
    # print("cache response:")
    # print(cached_response)
    # print("type:")
    # print(type(cached_response))

    if cached_response and cached_response != "Empty Response" :
        return cached_response
    else:
        return None
    
def cache_response(user_query, response):
    """Store the query and response in the Redis cache."""
    documents = [{
        "id": str(hash(user_query)),
        "doc_id": "cache_" + str(hash(user_query)),
        "text": {"query":user_query, "response":response},
    }]

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index=VectorStoreIndex.from_documents(documents, storage_context=storage_context,show_progress=True)
    print("cache stored successfully")
    print(index)