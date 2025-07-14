# TimeCapsuleLLM
An LLM trained only on data from certain time periods to reduce modern bias.

Imagine if an AI model didnt just pretend to be historical but actually was.

Built on nanoGPT by Andrej Karpathy.

# Project Goals 

TimeCapsule LLM is an expirimental project that will only be trained on texts written during certain time periods. The goal is to simulate the worldview and language of specific historical eras.

# Why fine tuning isn't enough 

If you just fine tune a pre-trained model, your LLM is still gonna know modern concepts. Of course achieving zero modern bias is difficult but I want to get as close as possible to this. That's why training a model from scratch is the only way to achieve this goal.

# Expected outcomes 

So my goal is to train a model from scratch using only text from a certain time period, these texts will be free of modern interpretaion, translation, modern annotations, etc.

Hopefully when finished, this model will not know modern concepts and will not be able to reason beyond what it's been trained on.

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

I'm going to start creating a list of books, ideally 500-600. Right now I'm training nanoGPT using books from 1800-1850 and specifically from London. There is some challeneges like making sure the books I find are not updated or have modern interpretations but untouched books published withtin my chosen time period.

