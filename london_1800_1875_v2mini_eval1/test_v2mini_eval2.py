# run script for TimeCapsuleLLM 1800-1875 London v2mini-eval2
import torch
from transformers import LlamaForCausalLM, AutoTokenizer

# config
MODEL_DIR = "put your folder path here"
TOKENIZER_DIR = "put your path to tokenizer"  


# device setup
if torch.cuda.is_available():
    
    device = "cuda"
    dtype = torch.float16
    print(f"[Device] Using GPU: {torch.cuda.get_device_name(0)}")
else:
    device = "cpu"
    dtype = torch.float32
   
    print("[Device] CUDA not available — using CPU")


# load tokenizer
print(f"[Tokenizer] Loading tokenizer from: {TOKENIZER_DIR}")
tokenizer = AutoTokenizer.from_pretrained(
    
    TOKENIZER_DIR,
    
    local_files_only=True
)


# load model
print(f"[Model] Loading model from: {MODEL_DIR}")

model = LlamaForCausalLM.from_pretrained(
    MODEL_DIR,
    dtype=dtype,
    device_map="auto",
)
model.eval()

# generation function
def infer(prompt, max_new_tokens=200):
    print("\n==============================")
    print("PROMPT:")
    
    print(prompt)
    print("==============================")

    inputs = tokenizer(
        prompt,
        
        return_tensors="pt"
   
   
    )

    
    inputs.pop("token_type_ids", None)
    inputs = inputs.to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            
            temperature=0.7,
            top_p=0.9,
            
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id,
        )

    text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(text)
    
    print("==============================\n")


#  test prompts
infer("Put your prompt here")
infer("Theres no QA training, so questions dont work")
