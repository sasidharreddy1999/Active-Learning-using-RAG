from flask import Flask, render_template, request
from transformers import pipeline
from scripts import run, build, evaluate, execute_sample

app = Flask(__name__)

# Function to chunk the passage into smaller parts
def chunk_text(text, chunk_size):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form.get("question")
        print('question',question)

        if question != "when was beowulf most likely composed when did it 's events probably take place":
            return render_template("index.html", error="Please enter a VALID question. Eg: when was beowulf most likely composed when did it 's events probably take place")
       
        if not question:
            return render_template("index.html", error="Please enter a question")
        else:
            #output = run.code_to_run()
            #print(output)
            #build.code_to_build()
            #evaluate.code_to_evaluate()
            output = execute_sample.execute()
            
        return render_template("index.html", cot=output['cot'], cot_correctness=output['cot_correctness'], anchoring_output=output['anchoring_output'], anchoring_correctness=output['anchoring_correctness'],
                               associate_output=output['associate_output'], associate_correctness=output['associate_correctness'],
                               logician_output=output['logician_output'], logician_correctness=output['logician_correctness'],
                               cognition_output=output['cognition_output'], cognition_correctness=output['cognition_correctness'])

    return render_template("index.html")

if __name__ == "__main__":
    app.run()

