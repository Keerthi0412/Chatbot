import ssl
import wolframalpha
import asyncio

# Bypass SSL verification (if necessary)
ssl._create_default_https_context = ssl._create_unverified_context

# WolframAlpha API Key
APP_ID = "KWGUR2-LVT685YGHT"

# Initialize the WolframAlpha client
client = wolframalpha.Client(APP_ID)

# Get user query
question = input("Question: ")

async def get_wolfram_answer(query):
    """Handles the asynchronous call to WolframAlpha API."""
    try:
        res = await client.aquery(query)  # Ensure using async version
        
        # Check if results exist
        if hasattr(res, 'results') and res.results:
            answer = next(res.results).text
            print(f"Answer: {answer}")
        else:
            print("WolframAlpha could not interpret the query. Try rewording your question.")
    except Exception as e:
        print(f"Error: {e}")

# Run the async function in Jupyter Notebook without causing event loop issues
if asyncio.get_event_loop().is_running():
    task = asyncio.create_task(get_wolfram_answer(question))  # Use create_task instead of asyncio.run()
else:
    asyncio.run(get_wolfram_answer(question))  # Normal script execution
