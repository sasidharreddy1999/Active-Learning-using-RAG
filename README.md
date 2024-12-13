# Active-Learning-using-RAG

# Install from git 
git clone https://github.com/sasidharreddy1999/Active-Learning-using-RAG 
cd ActiveRAG-main

# Install the necessary packages 
pip install -r requirements.txt

# Set your own api (in path - ActiveRAG-main/scripts/agent.py) 
MODEL = "gpt-3.5-turbo-1106" 
openai_api_key = "" 
openai_api_base = "https://api.openai.com/v1"

# Execute the code 
python app.py --dataset nq --topk 5
