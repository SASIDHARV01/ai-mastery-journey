# AI mastery roadmap — ordered curriculum checklist

Source: **Complete_AI_Mastery_Roadmap.pdf**, 12 pages, supplied by the learner. Page numbers below refer to PDF pages. Curriculum groups, named subitems, repeated concepts, and phase Build requirements follow their source order. Resource recommendations are omitted until they can be verified when needed. Source statements and dated labels are transcribed as source context, not independently verified claims.

## How to use this checklist

- Follow phases, topic groups, and named subitems in the order shown. Every checkbox starts unchecked.
- A compressed topic-group entry is an inventory, **not a single combined lesson**. Teach and assess its named subitems separately, from left to right. Record the active subitem in `PROGRESS.md`; do not check its parent group until every listed subitem has passed its completion gate.
- The first group has explicit lesson IDs. For later groups, retain the group ID and record the exact active subitem; assign sequential lesson IDs as each group is opened without changing the source order.
- Every taught subtopic requires its own small project. Source phase **Build milestones are additional requirements** and do not replace those projects.
- Completion requires demonstrated understanding, a reviewed and passed quiz, and a project pushed to GitHub. Scaffolding, reading, or a local commit alone does not establish completion.
- Repeated concepts remain on this checklist in each listed context. All Phase 8 items remain required under the learner's instructions, even though the source suggests choosing a subset for deeper research.
- Minimal repository setup supports the learning log; the formal Git/GitHub topic remains in its source position.

## Phase 0 — Foundations (Math + Programming)

Source: pp. 1–2.

### Math

- [ ] **P0-01 — Linear Algebra: vectors, matrices, eigenvalues/eigenvectors, SVD** (p. 2)
  - [ ] **P0-01-01 — Vectors**
  - [ ] **P0-01-02 — Matrices**
  - [ ] **P0-01-03 — Eigenvalues**
  - [ ] **P0-01-04 — Eigenvectors**
  - [ ] **P0-01-05 — SVD**
- [ ] **P0-02 — Calculus:** derivatives, partial derivatives, chain rule, gradients (p. 2)
- [ ] **P0-03 — Probability & Statistics:** distributions, Bayes' theorem, expectation, variance (p. 2)
- [ ] **P0-04 — Optimization:** convex optimization basics, gradient descent variants (p. 2)

### Programming

- [ ] **P0-05 — Python (core language)** (p. 2)
- [ ] **P0-06 — NumPy, Pandas, Matplotlib** (p. 2)
- [ ] **P0-07 — Git/GitHub** (p. 2)
- [ ] **P0-08 — SQL basics** (p. 2)

The source does not specify a separate Phase 0 Build milestone. Per-subtopic projects are still required.

## Phase 1 — Classical Machine Learning

Source: pp. 2–3.

- [ ] **P1-01 — Supervised Learning:** Linear/Logistic Regression, Decision Trees, Random Forest, SVM, k-NN (p. 2)
- [ ] **P1-02 — Unsupervised Learning:** K-Means, Hierarchical Clustering, PCA, t-SNE, UMAP (p. 2)
- [ ] **P1-03 — Ensemble Methods:** Bagging, Boosting (AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost) (p. 3)
- [ ] **P1-04 — Model Evaluation:** cross-validation, precision/recall/F1, ROC-AUC, bias-variance tradeoff (p. 3)
- [ ] **P1-05 — Feature Engineering & Feature Selection** (p. 3)
- [ ] **P1-06 — Regularization:** L1/L2, Ridge, Lasso, Elastic Net (p. 3)

### Source phase Build milestones

- [ ] **P1-B01 — Kaggle Titanic/House Prices** (p. 3)
- [ ] **P1-B02 — A spam classifier** (p. 3)
- [ ] **P1-B03 — A recommendation system with collaborative filtering** (p. 3)

## Phase 2 — Deep Learning Foundations

Source: pp. 3–4.

- [ ] **P2-01 — Perceptron → Multi-Layer Perceptrons (MLP)** (p. 3)
- [ ] **P2-02 — Activation functions:** Sigmoid, Tanh, ReLU, Leaky ReLU, GELU, Swish (p. 3)
- [ ] **P2-03 — Forward/Backpropagation, Chain Rule in networks** (p. 3)
- [ ] **P2-04 — Loss functions:** MSE, Cross-Entropy, Hinge Loss (p. 3)
- [ ] **P2-05 — Optimizers:** SGD, Momentum, RMSprop, Adam, AdamW (p. 3)
- [ ] **P2-06 — Regularization:** Dropout, Batch Normalization, Layer Normalization, Early Stopping (p. 3)
- [ ] **P2-07 — Weight Initialization:** Xavier, He initialization (p. 4)
- [ ] **P2-08 — Frameworks:** TensorFlow/Keras, PyTorch (learn PyTorch deeply — used in ~90% of research) (p. 4; percentage is an unverified source claim)

### Source phase Build milestones

- [ ] **P2-B01 — MNIST digit classifier from scratch (no framework, pure NumPy)** (p. 4)
- [ ] **P2-B02 — Then rebuild in PyTorch** (p. 4; follows P2-B01)

## Phase 3 — Computer Vision

Source: pp. 4–5.

- [ ] **P3-01 — Convolutional Neural Networks (CNNs):** convolution, pooling, stride, padding (p. 4)
- [ ] **P3-02 — Classic architectures:** LeNet, AlexNet, VGG, GoogLeNet/Inception, ResNet, DenseNet, EfficientNet (p. 4)
- [ ] **P3-03 — Object Detection:** R-CNN family, YOLO, SSD, DETR (p. 4)
- [ ] **P3-04 — Image Segmentation:** U-Net, Mask R-CNN, semantic vs instance segmentation (p. 4)
- [ ] **P3-05 — Vision Transformers (ViT), Swin Transformer** (p. 4)
- [ ] **P3-06 — Self-supervised vision:** SimCLR, MoCo, DINO, MAE (Masked Autoencoders) (p. 4)
- [ ] **P3-07 — Generative vision:** GANs (DCGAN, StyleGAN, CycleGAN), VAEs, Diffusion Models (DDPM, Stable Diffusion, latent diffusion) (p. 4)

### Source phase Build milestones

- [ ] **P3-B01 — Custom image classifier** (p. 5)
- [ ] **P3-B02 — An object detector on a real dataset** (p. 5)
- [ ] **P3-B03 — A mini Stable-Diffusion-style image generator** (p. 5)

## Phase 4 — Natural Language Processing

Source: p. 5.

- [ ] **P4-01 — Text preprocessing:** tokenization, stemming/lemmatization, embeddings (p. 5)
- [ ] **P4-02 — Classical NLP:** Bag of Words, TF-IDF, word2vec, GloVe, FastText (p. 5)
- [ ] **P4-03 — Sequence models:** RNN, LSTM, GRU, Seq2Seq, Attention mechanism (p. 5)
- [ ] **P4-04 — The Transformer architecture (Attention Is All You Need)** — study this deeply, it's the backbone of everything modern (p. 5; source wording)
- [ ] **P4-05 — BERT and encoder-only models:** BERT, RoBERTa, ALBERT, ELECTRA (p. 5)
- [ ] **P4-06 — GPT and decoder-only models:** GPT-1/2/3/4, LLaMA, Mistral, Gemma, Qwen (p. 5)
- [ ] **P4-07 — Encoder-Decoder models:** T5, BART (p. 5)
- [ ] **P4-08 — Tokenization deep-dive:** BPE, WordPiece, SentencePiece (p. 5)

### Source phase Build milestones

- [ ] **P4-B01 — Sentiment analyzer** (p. 5)
- [ ] **P4-B02 — A chatbot with a transformer** (p. 5)
- [ ] **P4-B03 — Fine-tune a small BERT model** (p. 5)

## Phase 5 — Large Language Models & Generative AI

Source: pp. 6–7. The source adds the label “Hottest Current Field.”

- [ ] **P5-01 — Pretraining vs Fine-tuning vs Instruction-tuning** (p. 6)
- [ ] **P5-02 — Scaling Laws:** Chinchilla, Kaplan et al. (p. 6)
- [ ] **P5-03 — RLHF (Reinforcement Learning from Human Feedback), DPO, RLAIF** (p. 6)
- [ ] **P5-04 — Parameter-Efficient Fine-Tuning:** LoRA, QLoRA, Adapters, Prefix-tuning (p. 6)
- [ ] **P5-05 — Prompt Engineering & Prompt Optimization** (p. 6)
- [ ] **P5-06 — Retrieval-Augmented Generation (RAG)** — vector databases (FAISS, Pinecone, Chroma), embeddings, hybrid search (p. 6)
- [ ] **P5-07 — AI Agents & Agentic Workflows** — tool use, function calling, ReAct, planning, multi-agent systems (p. 6)
- [ ] **P5-08 — Mixture of Experts (MoE) architectures:** Mixtral, Switch Transformer (p. 6)
- [ ] **P5-09 — State Space Models:** Mamba, S4 (Transformer alternatives, big 2024-25 research direction) (p. 6; dated source description)
- [ ] **P5-10 — Long-context techniques:** RoPE, ALiBi, sliding window attention, context extension (p. 6)
- [ ] **P5-11 — Multimodal LLMs:** vision-language models (CLIP, LLaVA, GPT-4V/4o-style, Gemini) (p. 6)
- [ ] **P5-12 — Quantization & efficient inference:** GGUF, GPTQ, AWQ, speculative decoding (p. 7)
- [ ] **P5-13 — Model evaluation:** benchmarks (MMLU, HumanEval, GSM8K), hallucination measurement (p. 7)
- [ ] **P5-14 — AI Alignment & Interpretability:** mechanistic interpretability, RLHF limitations, constitutional AI, red-teaming (p. 7)

### Source phase Build milestones

- [ ] **P5-B01 — Fine-tune an open-source LLM (LLaMA/Mistral) with LoRA** (p. 7; source model description)
- [ ] **P5-B02 — Build a RAG pipeline over your own docs** (p. 7)
- [ ] **P5-B03 — Build a tool-using AI agent** (p. 7)

## Phase 6 — Reinforcement Learning

Source: pp. 7–8.

- [ ] **P6-01 — MDPs, Bellman equations, Value Iteration, Policy Iteration** (p. 7)
- [ ] **P6-02 — Q-Learning, Deep Q-Networks (DQN)** (p. 7)
- [ ] **P6-03 — Policy Gradient methods:** REINFORCE, Actor-Critic, A2C/A3C (p. 7)
- [ ] **P6-04 — PPO (Proximal Policy Optimization)** — used in RLHF for LLMs (p. 7)
- [ ] **P6-05 — Model-based RL, AlphaZero/MuZero-style planning** (p. 8)
- [ ] **P6-06 — Multi-agent RL** (p. 8)

### Source phase Build milestones

- [ ] **P6-B01 — Train an agent on OpenAI Gym environments (CartPole → Atari)** (p. 8; preserve this progression)
- [ ] **P6-B02 — Implement PPO from scratch** (p. 8)

## Phase 7 — MLOps & Production AI

Source: p. 8.

- [ ] **P7-01 — Model deployment:** Docker, FastAPI/Flask, ONNX (p. 8)
- [ ] **P7-02 — Model serving:** TorchServe, TensorFlow Serving, vLLM (for LLM serving) (p. 8)
- [ ] **P7-03 — Experiment tracking:** MLflow, Weights & Biases (p. 8)
- [ ] **P7-04 — Data/Model versioning:** DVC (p. 8)
- [ ] **P7-05 — CI/CD for ML pipelines** (p. 8)
- [ ] **P7-06 — Monitoring:** model drift, data drift detection (p. 8)
- [ ] **P7-07 — Cloud platforms:** AWS SageMaker, GCP Vertex AI, Azure ML (p. 8)
- [ ] **P7-08 — Distributed training:** data parallelism, model parallelism, DeepSpeed, FSDP (p. 8)

### Source phase Build milestones

- [ ] **P7-B01 — Deploy one of your trained models as a live API with monitoring** (p. 8)

## Phase 8 — Frontier Research Topics

Source: pp. 9–10. The source adds the label “Currently Active Research Areas.” Every item below remains in scope.

- [ ] **P8-01 — World Models** — models that simulate environments for planning (Sora-style video generation, JEPA) (p. 9)
- [ ] **P8-02 — Agentic AI / Autonomous Agents** — long-horizon planning, memory systems, multi-agent collaboration (p. 9)
- [ ] **P8-03 — Neurosymbolic AI** — combining neural networks with symbolic reasoning (p. 9)
- [ ] **P8-04 — AI Safety & Alignment research** — scalable oversight, weak-to-strong generalization, deceptive alignment (p. 9)
- [ ] **P8-05 — Mechanistic Interpretability** — reverse-engineering what neural networks actually learn (Anthropic's core research area) (p. 9; source description)
- [ ] **P8-06 — Efficient AI / Green AI** — model compression, distillation, sparse models, edge AI (p. 9)
- [ ] **P8-07 — Federated Learning** — training across decentralized data without centralizing it (p. 9)
- [ ] **P8-08 — Causal Inference in ML** — moving beyond correlation to causal reasoning (p. 9)
- [ ] **P8-09 — Neuromorphic Computing** — brain-inspired hardware/algorithms (p. 9)
- [ ] **P8-10 — Graph Neural Networks (GNNs)** — for molecules, social networks, recommendation systems (p. 9)
- [ ] **P8-11 — AI for Science** — protein folding (AlphaFold), materials discovery, drug design (p. 10)
- [ ] **P8-12 — Robotics + AI** — embodied AI, sim-to-real transfer, vision-language-action models (p. 10)
- [ ] **P8-13 — Test-time compute / reasoning models** — models that “think longer” (o1/o3-style reasoning, chain-of-thought scaling) (p. 10)
- [ ] **P8-14 — Synthetic data generation for training** (p. 10)

The source does not specify a separate Phase 8 Build milestone. Per-subtopic projects are still required.

## Timing boundary

The PDF's suggested timeline appears on pp. 10–11. It describes months of study for each phase at approximately 10–15 hours per week, with research ongoing; it does not support a promise of mastering every item in 1–2 months. Set the lesson pace from the learner's available hours and demonstrated progress. Time elapsed never substitutes for a completion gate.
