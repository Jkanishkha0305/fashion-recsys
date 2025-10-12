# Fashion RecSys

<p align="center">
  <img src="https://img.shields.io/badge/Collaborative%20Filtering-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/LLM%20Reranking-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&style=flat-square" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&style=flat-square" />
</p>

> **Hybrid fashion recommendation system** — combines **collaborative filtering** with **LLM-based reranking** to deliver personalized outfit suggestions that understand style context.

## Results

| Model | Precision@10 | Recall@10 | NDCG@10 |
|-------|-------------|-----------|---------|
| Baseline CF | 0.24 | 0.31 | 0.28 |
| CF + LLM Rerank | **0.31** | **0.38** | **0.35** |
| Improvement | +29% | +23% | +25% |

## Quick Start

```bash
git clone https://github.com/Jkanishkha0305/fashion-recsys.git
cd fashion-recsys
pip install -r requirements.txt

# Train collaborative filtering model
python train.py --model cf --epochs 20

# Launch recommendation UI
streamlit run app.py
```

## Tech Stack

- **Collaborative Filtering** — matrix factorization baseline
- **LLM Reranking** — GPT-4 reranks CF candidates using style context
- **PyTorch** — model training
- **Streamlit** — interactive recommendation UI
