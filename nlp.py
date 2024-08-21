from transformers import pipeline

# Load a pre-trained model for question answering
nlp_model = pipeline("question-answering")

def answer_question(question, context):
    answer = nlp_model(question=question, context=context)
    return answer['answer']
