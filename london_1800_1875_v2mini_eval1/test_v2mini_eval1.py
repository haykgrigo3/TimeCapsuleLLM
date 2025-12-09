import torch
from transformers import LlamaForCausalLM, AutoTokenizer


# config
MODEL_DIR = r"C:\Projects\TimeCapsuleLLM_RunPod\checkpoint-10000"

# setup
if torch.cuda.is_available():
    device = torch.device("cuda")
    dtype = torch.float16
    
    print(f"[Device] Using GPU: {torch.cuda.get_device_name(0)}")

else:
    device = torch.device("cpu")
    
    dtype = torch.float32
    print("[Device] CUDA not available — using CPU.")

    # optional for cpu only (commented out)
    # device = torch.device("cpu")
    # dtype = torch.float32
    # print("[Device] Forcing CPU mode.")
    # If your CPU runs out of RAM, enable low-memory loading:
    # model = LlamaForCausalLM.from_pretrained(
    #     MODEL_DIR,
    #     torch_dtype=torch.float32,
    #     low_cpu_mem_usage=True,
    #     device_map=None,     # CPU only
    #     local_files_only=True
    # )
    #
    # slower but safer if you have <32GB RAM.


# load tokenizer and model
print(f"[Tokenizer] Loading from local folder: {MODEL_DIR}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
print(f"[Model] Loading model from local folder: {MODEL_DIR}")

model = LlamaForCausalLM.from_pretrained(
    MODEL_DIR,
   
    torch_dtype=dtype,
   
    device_map={"": device},
   
    local_files_only=True

)
model.to(device)

model.eval()


# generation
def infer(prompt):
    print("\n==============================")
    print("PROMPT:")
    print(prompt)
    print("==============================")

    # tokenize
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    inputs.pop("token_type_ids", None)

    # generate
    with torch.no_grad():
        output = model.generate(
            **inputs,
            
            max_length=200,
            
            temperature=0.7,
            
            top_p=0.9,
            do_sample=True
        )

    text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(text)
    
    print("==============================\n")

# test prompts
infer("add your prompt here")
infer("you can use all of these for different prompts")
infer("comment them out or delete if you dont need them")
