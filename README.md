# TimeCapsuleLLM
An LLM trained only on data from certain time periods to reduce modern bias.

Imagine if an AI model didnt just pretend to be historical but actually was.

Built on nanoGPT by Andrej Karpathy. Core training scripts and model architecture are his work. 

# Project Goals 

TimeCapsule LLM is an expirimental project that will only be trained on texts written during certain time periods. The goal is to simulate the worldview and language of specific historical eras.

# Why fine tuning isn't enough 

If you just fine tune a pre-trained model, your LLM is still gonna know modern concepts. Of course achieving zero modern bias is difficult but I want to get as close as possible to this. Getting no modern bias requires training a model from scratch.

# Expected outcomes 

Hopefully when finished, this model will not know modern concepts and will not be able to reason beyond what it's been trained on. It shouldnt recognize modern concepts/vocab and I hope it doesn't hallucinate modern knowledge.

# Progress Updates

July 9th, 2025

I've set my time period for 1800-1850 and region: London 

I've gathered a list of texts, books, documents 

So far I've gotten 50 as txt files and will begin training NanoGPT soon 

Will update this as long as progress is made

July 13th, 2025

Trained nanoGPT with 187MB of historial text data. 

# Current Model Behavior & Limitations 

Early prompts show the model responding with 1800's language and behavior. For example, I prompted it with "Who art Henry?" and it replied "I know that man, I have did not a black, the storm." and yeah that sentences makes no sense but the LLM is recognizing I'm asking about a person.

There is no mention of modern concetps, outputs contain mostly words and phrasing from the 1800's.

It still needs alot of work, training off of 187MB will not give you a model that produces text with complex reasoning. 

Right now it produces sentences that lack full sentence structure and overall just make no sense but this is normal for the training size. 

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

# Training Specs

GPU: Geforce rtx 4060
CPU: i5-13400F 
Ram: 16GB DDR5.

