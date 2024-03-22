import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_code(task_description):
    model_name = "Salesforce/codet5p-770m-py"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    input_tokens = tokenizer.encode(task_description, return_tensors="pt")
    output_tokens = model.generate(input_tokens, max_length=512)
    generated_code = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return generated_code

iface = gr.Interface(
    fn=generate_code,
    inputs="text",
    outputs="text",
    title="Code Generator",
    description="Generates Python code from a natural language description."
)

iface.launch(server_name="0.0.0.0",share=True)
