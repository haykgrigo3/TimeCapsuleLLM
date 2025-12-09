<div align="right">
  <details>
    <summary >🌐 Language</summary>
    <div>
      <div align="center">
        <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=en">English</a>
        | <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=zh-CN">简体中文</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=zh-TW">繁體中文</a> 
        | <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=ja">日本語</a>
        | <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=ko">한국어</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=as">हिन्दी</a> 
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=th">ไทย</a> 
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=fr">Français</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=de">Deutsch</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=es">Español</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=it">Italiano</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=ru">Русский</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=pt">Português</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=nl">Nederlands</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=pl">Polski</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=ar">العربية</a>
        | <a href="#" title="Coming soon">فارسی (coming soon)</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=tr">Türkçe</a>
        | <a href="https://openaitx.github.io/#/view?user=haykgrigo3&project=TimeCapsuleLLM&lang=vi">Tiếng Việt</a>
        | <a href="#" title="Coming soon">Bahasa Indonesia (coming soon)</a>

      </div>
    </div>
  </details>
</div>


# TimeCapsule LLM

*A language model trained **from scratch** exclusively on data from certain places and time periods to reduce modern bias and emulate the voice, vocabulary, and worldview of the era.*

Imagine if an AI model didnt just pretend to be historical but actually was.

v0 and v0.5 built on [nanoGPT by Andrej Karpathy](https://github.com/karpathy/nanoGPT) Core training scripts and model architecture are his work. 

v1 built on [Phi 1.5 by Microsoft](https://huggingface.co/microsoft/phi-1_5)

[Hugging Face Link](https://huggingface.co/haykgrigorian/TimeCapsuleLLM)


##  Model Behavior & Limitations

### **v0**  

Early prompts show the model responding with 1800's language and behavior. 
Example: Prompt: "Who art Henry?" and it replied "I know that man, I have did not a black, the storm." 

![TimeLockLLM Sample Output](https://github.com/haykgrigo3/TimeCapsuleLLM/blob/main/london_1800_1850_v0/timelockllm_sample_output.png?raw=true)

- No mention of modern concepts  
- Mostly era-accurate vocabulary  
- Sentences are mostly incoherent (expected for ~187MB training data)

### **v0.5** 

A significant improvement over v0.  
- Victorian writing style, proper punctuation, mostly grammatical sentences  
- Still high factual hallucination rate  
- OCR noise (“Digitized by Google”) still present in outputs

![TimeLockLLM Sample Output](https://github.com/haykgrigo3/TimeCapsuleLLM/blob/main/london_1800_1875_v0.5/fellowcitizens.png?raw=true)

### **v1**

First model to recall and connect a real historical event with an actual figure from the dataset.

Example: Prompt: "It was the year of our Lord 1834" 

The output: "It was the year of our Lord 1834 and the streets of London were filled with protest and petition. The cause, as many re counted, was not bound in the way of private, but having taken up the same day in the day of Lord Palmerston, the public will receive a short statement of the difficulties under which the day of law has reached us. It is a matter of deep regret, that the present events in the history of the world are clear, and consequently will be'known. It is not true that the very men who first settled in the Gospel at Jerusalem should have so extensive and so interesting a record of the prosperity and prosperity" 

At first I assumed that a protest might have coincidentally taken place the same year but take a look at this: ![1834protest](1834protest.png)

### Why this matters:

This is the first example of one of my models connecting a year to both a real historical event and a real person tied to that event (Lord Palmerston). Earlier models (v0 and v0.5) could mimic writing styles of the 19th century but would always hallucinate events, people and facts. This shows the model is beggining to remember things from the dataset 

## Upcoming Plans 

- There are nearly 175,000 texts published in London from 1800-1875 on Internet Archive 
- I plan on expanding the corpus and cleaning it more for better reasoning abilities
- Expanding to different regions and time periods for more historical models


## How to Use

This project focuses mostly on curating historical data, preparing it for training and building a tokenizer. I am not going to cover the full LLM training process, for that refer to nanoGPT by Andrej Karpathy.

### Step 1: Gather and Prepare Historical Texts 

- Collect .txt files of public domain books, documents, etc from your chosen time period (e.g., London 1800-1850) 
- Keep them within your chosen time/place window  
- Clean the text files using a script or manually remove headers/footer from Project Gutenberg, Modern annotations or things like OCR errors.

### Step 2: Build a Custom Tokenizer

- Run train_tokenizer.py or train_tokenizer_hf.py on the cleaned data.
- This will give you vocab.json and merges.txt
- Thes files define vocab and merge rules for your model

### Step 3: Train Your Model 

- Refer to [nanoGPT by Andrej Karpathy](https://github.com/karpathy/nanoGPT) for the training process or your chosen architecture’s docs.

# FAQ

## What is Selective Temporal Training ?

Selective Temporal Training (STT) is a machine learning methodology where all training data is specifically curated to fall within a specific historical time period. It's done in order to model the language and knowledge of that era without influence from modern concepts. For example, the current model I have now (v0.5) is trained on data exclusively from 1800-1875, it's not fine tuned but trained from scratch resulting in output that reflects the linguistic style and historical context of that time period.

## Why not just use fine-tuning or LoRA?

For this project I'm trying to create a language model that is unclouded from modern bias. If I fine-tune something like GPT-2, it's already pre-trained and that information won't go away. If I train from scratch the language model won't pretend to be old, it just will be. The Goal for this project right now is to create something can reason exclusively using knowledge from London books published between 1800 and 1875.

## What kind of data did you use for training?

I'm using books, legal documents, newspapers, and other writings from 1800–1875 London. The list I linked (for v0) has like 200 but for the first training I just used 50 files about ~187 MB. You can view a list of the documents:
https://github.com/haykgrigo3/TimeCapsuleLLM/blob/main/Copy%20of%20London%20Documents%20for%20Time%20Capsule%20LLM.txt

Dataset sizes:
- v0: ~187MB
- v0.5: ~435MB 
- v1: ~6.25GB 
- v2mini-eval1: 15GB

## How large are the models ?

v0: 16M Parameters

v0.5 123M Parameters

v1: 700M Parameters

v2mini-eval1: 300M Parameters

# Training Specs ? 

# v0/v0.5
GPU: Geforce rtx 4060
CPU: i5-13400F 
Ram: 16GB DDR5.

# v1
GPU: A100 SXM rented

# v2mini-eval1

GPU: A100 SXM rented





















