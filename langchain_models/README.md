#### **Language Models**

Language Models works as:
Text Input `-->` Text Output

Language Models have two types

1. LLM's: General Purpose Models, Can be used for any kind of task such as text generation, summarization, etc. These are kind of old and there support from langchain will be depriciated from future versions.

2. Chat Models: They are specialized for conversational task. They can take sequence of message as input and return a chat as output rather than the LLMs which works for single string I/O.

---

#### **Embedding Models**

These are the models which does not return output as string they return a vector instead of string. They are mostly used for semantic search of the input.

Text Input `-->` Vectors Output

---

#### **Close Source Models**

Since we dont have access to close source model we are just testing using random apis from website.

- Open ai
- Anthropic Claude
- Google Gemini

---

#### **Open Source Models**

- can be fine tune
- can be customize
- can be easily deployed

- some famous open source model
  - Llama
  - Mixtral
  - Mistral
  - Falcon
  - Deepseek
  - Gwen

We can find these open source models from `HuggingFace` which is a larget repository for open source models

---

#### **Two methods to Use Open Source Models**

1. Run locally by downloading(solid hardware needed)
2. Use Free Hugging Face Api

#### **Drawbacks**

- Some open source models dont have fine tuning with human feedback
- Limited Multimodel Capability

---

#### **Document Similarity**

- Why we didn't use `np.max()` to fetch the maximum value of the vector array

> Because when we fetch the maximum value we only know what the value is and if we want to show the corresponding text to it we cannot do that, thus first we have enumerate on that to provide index to each and then sorted and extracted the value and index. and with that index we can show the coresponding text of embedding.

- Here we are not storing any embedding so everytime we run we are again converting embedding for all the documents which is costly operations, so later we will see how we are going to store those vector embedding to a database which is known as **vector databases**
