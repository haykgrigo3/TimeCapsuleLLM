# for TimeCapsuleLLM v2 1800-1875 London
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# config
MODEL_PATH = "./final"  # or "./final" ./checkpoint-182000

PROMPTS = [
    "Put prompt here,",
    "Put prompt here",
]

MAX_NEW_TOKENS = 200

TEMPERATURE = 0.7

TOP_P = 0.9
REPETITION_PENALTY = 1.1


# device
assert torch.cuda.is_available(), "CUDA not available"

device = "cuda"
dtype = torch.float16

print(f"✅ Using GPU: {torch.cuda.get_device_name(0)}")


# tokenizer
print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    use_fast=True
)


# model
print("Loading model...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    
    dtype=dtype,
    low_cpu_mem_usage=True,
    device_map="auto"
)

model.eval()
torch.cuda.empty_cache()


# generation
def generate(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    inputs.pop("token_type_ids", None)
    inputs = inputs.to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
           
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=True,
            
            temperature=TEMPERATURE,
            top_p=TOP_P,
            repetition_penalty=REPETITION_PENALTY,
           
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id,
       
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)

print("\n GENERATIONS\n" + "=" * 50)
for p in PROMPTS:
    print(f"\nPROMPT:\n{p}\n")
    
    print(generate(p))
    print("-" * 50)
