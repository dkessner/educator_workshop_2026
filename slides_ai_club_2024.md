
.center[
<br/> <br/> <br/> <br/>

## A Deeper Dive Into AI

<br/> <br/> <br/> <br/>

Dr. Darren Kessner  
Marlborough School   
Pushing Perspectives / AI Club  
November 12, 2024  

<br/> <br/>

[dkessner.github.io/ai_club_2024](http://dkessner.github.io/ai_club_2024)  
]

---

### Who Am I?

.split-50[
.column[
.center[
<img src="pix/DarrenKessner_25.jpg" width="50%"/>
<img src="pix/marlborough_school_cover.jpeg" width="70%"/>
<img src="pix/ei_building.jpg" width="70%"/>
]
]

.column[
]
.center[
__Dr. Kessner__
]

- BS, MA in Mathematics

- PhD in Bioinformatics

- software developer for over 25 years


.center[
__Marlborough School__
]

- Program Head of Computer Science and Software Innovation

- 11th year

- AP Computer Science and Honors Computer Science Projects

.center[
__Ellison Institute of Technology__  
]

- Software Engineer in AI and Advanced Molecular Medicine group

]




---

### Linear regression


.split-60[

.column[
<img src="pix/linear_regression_0.jpg" width="90%"/>
]
.column[
__Data__  
x: input  
y: output  
]

]



---

### Linear regression

.split-60[

.column[
<img src="pix/linear_regression_1.jpg" width="90%"/>
]

.column[
__Data__  
x: input  
y: output  
  
__Model__  
line     
y = mx + b
  
__Parameters__   
m (slope)  
b (intercept)  

__Training / Learning__ 
finding the best parameters - 
minimizing a loss function

]
]


---

### Linear regression


.split-60[

.column[
<img src="pix/linear_regression_2.jpg" width="90%"/>
]

.column[
__Data__  
x: input  
y: output  
  
__Model__  
line     
y = mx + b
  
__Parameters__   
m (slope)  
b (intercept)  

__Training / Learning__ 
finding the best parameters - 
minimizing a loss function

__Overfitting__  
using too many parameters

]
]

---

### Training the model

.split-50[

.column[
<img src="pix/gradient_descent.png" width="90%"/>
]

.column[
__Train the model__  

&nbsp; = learn from data

&nbsp; = find best parameters  

&nbsp; = minimize loss function  

<br/>

__Gradient Descent__  

- give training data to model as input

- calculate gradient of loss function

- adjust parameters in the direction of the gradient

]
]


---

### Neural networks

.split-60[

.column[
<img src="pix/neuron.png" width="80%"/>
<br/>
<br/>
<img src="pix/artificial_neuron.png" width="80%"/>

<br/>
<br/>
<br/>
<small>
Image credits:
[1](https://commons.wikimedia.org/wiki/File:Neuron3.svg)
[2](https://commons.wikimedia.org/wiki/File:Artificial_neuron_structure.svg)
[3](https://commons.wikimedia.org/wiki/File:Colored_neural_network.svg)
</small>

]

.column[
<br/>
<img src="pix/neural_network.png" width="100%"/>

.center[
weights == parameters

training == adjusting weights to decrease loss
]

]

]

<br/>

---

### Neural networks 


.center[

<img src="pix/neural_network_composition.ppm" width="70%"/>

<br/>

__Neural network__   
composition of functions   
(linear transformations / matrix multiplication)

<br/>

__Backpropagation algorithm__  
calculation of gradient   
(chain rule)  

]

<small>
[Image credit](https://www.researchgate.net/figure/Example-of-simple-neural-network-architecture-with-linear-transformation-dense-layer-and_fig2_347965848)
</small>



---

### Computer vision

.split-50[

.column[
<img src="pix/cv_training.png" width="95%"/>
.center[__Training__]

<br/>
<br/>
<small>
Image credits:
[1](https://commons.wikimedia.org/wiki/File:Simplified_neural_network_training_example.svg)
[2](https://commons.wikimedia.org/wiki/File:Simplified_neural_network_training_example.svg)
</small>
]

.column[
<img src="pix/cv_prediction.png" width="95%"/>
.center[__Prediction__]
]

]

---

### Cosine similarity

.center[
<img src="pix/cosine.png" width="60%"/>
]

$$
\cos \theta = \dfrac{u \cdot v}{|u||v|}
$$



---

### Semantic embedding

.split-60[

.column[
<img src="pix/word_vectors.jpg" width="90%"/>

<br/>
<br/>
<small>
[Image credit](https://commons.wikimedia.org/wiki/File:Word_vector_illustration.jpg)
</small>

]

.column[
__Embedding__  

mapping of words to vectors in a high-dimensional vector space

__Semantic similarity__   

words with the same meaning have a higher
cosine similarity (shorter distance)


__Contextual embedding__

mapping of words depends on its context within a sentence:  

_"Time __flies__ like an arrow, fruit __flies__ like a banana"_


]

]


---

### Transformer architecture

<br/>

2017 (Google) "Attention is All you Need" introduces the transformer
architecture

<br/>
<br/>


- model trained for text translation

- contextualization of embeddings

- parallelization / scaling to handle a large amount of training data

- foundation model pre-training + downstream fine-tuning



---

### Transformers history

- 2017 (Google) "Attention is All you Need": introduces the transformer
  architecture

- 2018 (Google) Bidirectional encoder representations from transformers
  (BERT): large language model using transformers

- 2018 (OpenAI) "Improving Language Understanding by Generative
  Pre-Training": GPT-1 released, using transformer architecture,
  unsupervised pre-training, fine-tuning for downstream tasks

- 2019 (OpenAI) GPT-2 released (closed, no source code)

- 2020 (OpenAI) GPT-3 released

- 2022 (OpenAI) ChatGPT released

- 2023 (OpenAI) GPT-4 released

- 2022-2024 Google Gemini, Anthropic Claude, Meta Llama, BLOOM, lots of others


---

### Large Language Models (LLMs)

- contextualization of embeddings
- pre-trained on large body of text
- trained to predict hidden (BERT) or next (GPT) word

<br/>

GPT: Generative Pre-trained Transformer

.split-50[

.column[

Parameter counts

- GPT-1: 117 million
- BERT: 340 million
- GPT-2: 1.5 billion
- GPT-3: 175 billion
- BLOOM: 175 billion
- Llama 3.1: 405 billion
- Claude: 52 billion
- Claude 2-3: ?
- Gemini: ?
- GPT-4: ?

[<a href="https://en.wikipedia.org/wiki/Large_language_model#List_of_Large_Language_Models" target="_blank">Wikipedia List of LLMs</a>]

]

.column[
<img src="pix/ai_cost.png" width="80%"/>

<small>
Image: Economist Sep 19, 2024
</small>
]

]

---

### Applications

.split-50[

.column[

<br/>

Traditional
- audio analysis
- image analysis
- natural language  
  processing

<br/>

Generative
- text generation
- image generation
- drug discovery
]

.column[

<img src="pix/breast_cancer_ai_prediction.png" width="60%"/>  
Breast cancer AI prediction

<img src="pix/alphafold3.webp" width="60%"/>  
AlphaFold 3 protein prediction

<small>
Image credits:
[1](https://www.nature.com/articles/srep46450)
[2](https://www.nature.com/articles/d41586-024-03708-4)
</small>

] 

]

---

### Math & Science Concepts

<br/>

- Linear regression

<br/>

- Linear algebra
    - vectors
    - dot product
    - matrix multiplication
    - linear transformations

<br/>

- Calculus 
    - derivatives
    - minimization / maximization of functions
        - Newton's method
    - multivariable functions
        - gradients
    - chain rule


---

### Thank you!

.center[

<br/>
dkessner.github.io/ai_club_2024  
<br/>

<img src="pix/qr.png" width="30%"/>

<br/>

Join AI Club or Code Violet,   
or sign up for a coding class!

]







