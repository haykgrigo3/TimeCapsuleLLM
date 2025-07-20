
<div align="right">
  <details>
    <summary >🌐 Language</summary>
    <div>
      <div align="center">
        <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=en">English</a>
        | <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=zh-CN">简体中文</a>
        | <a href="#" title="Coming soon">繁體中文 (coming soon)</a> |
        | <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=ja">日本語</a>
        | <a href="https://openaitx.github.io/view.html?user=haykgrigo3&project=TimeCapsuleLLM&lang=ko">한국어</a>
        | <a href="#" title="Coming soon">हिन्दी (coming soon)</a> |
        | <a href="#" title="Coming soon">ไทย (coming soon)</a> |
        | <a href="#" title="Coming soon">Français (coming soon)</a>
        | <a href="#" title="Coming soon">Deutsch (coming soon)</a>
        | <a href="#" title="Coming soon">Español (coming soon)</a>
        | <a href="#" title="Coming soon">Italiano (coming soon)</a>
        | <a href="#" title="Coming soon">Русский (coming soon)</a>
        | <a href="#" title="Coming soon">Português (coming soon)</a>
        | <a href="#" title="Coming soon">Nederlands (coming soon)</a>
        | <a href="#" title="Coming soon">Polski (coming soon)</a>
        | <a href="#" title="Coming soon">العربية (coming soon)</a>
        | <a href="#" title="Coming soon">فارسی (coming soon)</a>
        | <a href="#" title="Coming soon">Türkçe (coming soon)</a>
        | <a href="#" title="Coming soon">Tiếng Việt (coming soon)</a>
        | <a href="#" title="Coming soon">Bahasa Indonesia (coming soon)</a>

      </div>
    </div>
  </details>
</div>

# TimeCapsule LLM
An LLM trained only on data from certain time periods to reduce modern bias.

Imagine if an AI model didnt just pretend to be historical but actually was.

Built on [nanoGPT by Andrej Karpathy](https://github.com/karpathy/nanoGPT) Core training scripts and model architecture are his work. 

# Project Goals 

TimeCapsule LLM is an expirimental project that will only be trained on texts written during certain time periods. The goal is to simulate the worldview and language of specific historical eras.

# Why fine tuning isn't enough 

If you just fine tune a pre-trained model, your LLM is still gonna know modern concepts. Of course achieving zero modern bias is difficult but I want to get as close as possible to this. Getting no modern bias requires training a model from scratch.

# Expected outcomes 

Hopefully when finished, this model will not know modern concepts and will not be able to reason beyond what it's been trained on. It shouldnt recognize modern concepts/vocab and I hope it doesn't hallucinate modern knowledge.

# Progress Updates

## July 9th, 2025

I've set my time period for 1800-1850 and region: London 

I've gathered a list of texts, books, documents 

So far I've gotten 50 as txt files and will begin training NanoGPT soon 

Will update this as long as progress is made

## July 13th, 2025

Trained nanoGPT with 187MB of historial text data. 

## July 15th, 2025

I started downloading texts for the second training run. I'm getting everything from Internet Archive and I've expanded the time period to 1800-1875. To get a diverse range of texts, you can use subject and search filters for publication location, time period and subjects on Internet Archive. 

![Search Filters](searchfilter.jpg)

## July 16th, 2025

I downloaded around 500 txt files from Internet Archive and after cleaning them (just deleting whitespaces, Gutenberg headers, etc) I have around 500MB of data. It's a tiny dataset but last time I trained off of 187MB so there should be at least some kind of noticable difference in the output after I train the second model. I'm hoping this model can at least produce more coherent sentences that kind of make sense. It's not a guarantee of course since this is still a tiny tiny dataset, but it's more than what I used last time. 

This should be doable on my own hardware, it's good too because I can hopefully see some kind of improvements before I jump to a bigger dataset which would require me to rent a GPU. But don't worry I still plan on renting a GPU soon, but before I do that I wanna make sure my dataset is as curated and clean as possible. One of the issues I have is cleaning, a lot of these txt files have gibberish mixed in. The scripts I've used for cleaning do work but they're not 100% effective. 

I will train this dataset today and it should take around 4-5 hours. Once it's done and I test it, I will give updates. Thank you again to everyone whos checking out my project, I've even had some people even giving me links to OCR resources so Thank you! I hope more people try this out and expirement with they're own datasets. 

### Training Update 

I started training on a 435MB (108 M tokens) corpus, it's going pretty smooth right now. Train loss dropped from 10.9 to 4.9 in the first 2800 iterations. I expect it'll take around 8 or 9 hours to complete. I'll post another update once it's done.

## July 17th, 2025 2:13AM

The training is done for the second model, it took my 4060 around 8 hours and 40 minutes (3,900 iters/hr) for 33,000 iters (5 epochs). Final train loss was 3.73. The outputs were suprisingly good it genuinely generates coherent 19th century style sentences now. 

# V0 Model Behavior & Limitations 

Early prompts show the model responding with 1800's language and behavior. For example, I prompted it with "Who art Henry?" and it replied "I know that man, I have did not a black, the storm." and yeah that sentence makes no sense but the LLM is recognizing I'm asking about a person. 

![TimeLockLLM Sample Output](https://github.com/haykgrigo3/TimeCapsuleLLM/blob/main/london_1800_1850_v0/timelockllm_sample_output.png?raw=true)

There is no mention of modern concetps, outputs contain mostly words and phrasing from the 1800's.

It still needs alot of work, training off of 187MB will not give you a model that produces text with complex reasoning. 

Right now it produces sentences that lack full sentence structure and overall just make no sense but this is normal for the training size. 

# V0.5 Model Behavior & Limitations

This is a nice improvement compared to the last model. The writing style and vocab is Victorian and almost every sentence is grammatically correct with proper punctuation. And again this is trained from scratch so it sticks to 1800's subjects. 

![TimeLockLLM Sample Output](https://github.com/haykgrigo3/TimeCapsuleLLM/blob/main/london_1800_1875_v0.5/fellowcitizens.png?raw=true)

There are a lot of factual hallucinations. A lot (like 100%) of the details (dates, events, historical figures)  are made up. Also the sentences don't really have connections to each other, sometimes maybe 2 sentences will relate to each other but beyond that they dont. Another issue is sometimes a stray “Digitized by Google” footer shows up, so the next time I train I really have to make sure the texts are cleaned well. Overall I'm very happy with the results, it's nowhere near an LLM yet but definitely a sentence generator. 

I'm learning a lot and will start figuring out what I need to do better in the coming weeks. I will upload files soon! 

# Upcoming Plans 

I'm going to start work on version 1, instead of training using 50 books, I'll train using ideally 500-600. Right now I'm training nanoGPT using books from 1800-1850 and specifically from London. There is some challeneges like making sure the books I find are not updated or have modern interpretations but untouched books published withtin my chosen time period.

# How to Use This Project 

This project focuses mostly on curating historical data, preparing it for training and building a tokenizer. I am not going to cover the full LLM training process, for that refer to nanoGPT by Andrej Karpathy.

# Step 1: Gather and Prepare Historical Texts 

Collect .txt files of public domain books, documents, etc from your chosen time period (e.g., London 1800-1850)

You can use download_texts_improved.py to download books for you if you need to.

Clean the text files using a script or manually remove headers/footer from Project Gutenberg, Modern annotations or things like OCR errors.

prepare_dataset.py should work fine.

# Step 2: Build a Custom Tokenizer

Run train_tokenizer.py or train_tokenizer_hf.py on the cleaned data.
This will give you vocab.json and merges.txt

Thes files define vocab and merge rules for your model

# Step 3: Train Your Model (nanoGPT) 

Refer to [nanoGPT by Andrej Karpathy](https://github.com/karpathy/nanoGPT) for the training process.

You can train a different LLM if you want, but I used nanoGPT 

# FAQ

## Why not just use fine-tuning or LoRA?

For this project I'm trying to create a language model that is unclouded from modern bias. If I fine-tune something like GPT-2, it's already pre-trained and that information won't go away. If I train from scratch the language model won't pretend to be old, it just will be. The Goal for this project right now is to create something can reason exclusively using knowledge from London books published between 1800 and 1850.

## What kind of data did you use for training?

I'm using books, legal documents, newspapers, and other writings from 1800–1850 London. The list I linked has like 200 but for the first training I just used 50 files about ~187 MB. You can view a list of the documents:
https://github.com/haykgrigo3/TimeCapsuleLLM/blob/main/Copy%20of%20London%20Documents%20for%20Time%20Capsule%20LLM.txt

## How large is the Version 0 model ?

This model is very small right now, I'm just doing this for fun and following a strict training rule of no modern sources. It has almost 16 million parameters but I'm gonna start gathering more old texts to begin another model training. Will give updates as I go.

## Training Specs ? 

GPU: Geforce rtx 4060
CPU: i5-13400F 
Ram: 16GB DDR5.
