from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

#setting calculating parameters
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
mypipeline = pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)


app = FastAPI()

#Welcome page
@app.get("/")
def read_root():
    return {"Welcome": "page"}

#calculating method
@app.post("/calculate/")
async def transform(sentence: str = Form(...)):
    result = mypipeline(sentence)
    return result


#html page that takes the input
@app.get("/input/")
async def read_input():
    html_content = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Carbon Consulting</title>
    </head>
    <body>
    <h1>Enter your sentence</h1>
    <form action="/calculate" method="post" enctype="multipart/form-data">
        <input type="text" name="sentence">
        <input type="submit">
    </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
