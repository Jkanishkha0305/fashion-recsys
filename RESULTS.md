# Results — fashion-recsys

## Model Comparison

Evaluation on held-out test set (20% split). Metrics: NDCG@10, Hit Rate@10, MRR.

| Model | NDCG@10 | Hit Rate@10 | MRR | Notes |
|-------|---------|-------------|-----|-------|
| Random baseline | 0.052 | 0.089 | 0.041 | |
| Popularity-based | 0.143 | 0.231 | 0.118 | |
| User-Based CF | 0.287 | 0.412 | 0.243 | cosine similarity |
| SVD Matrix Factorization | 0.341 | 0.478 | 0.289 | 100 latent factors |
| **CF + LLM Reranking** | **0.389** | **0.531** | **0.334** | **Best model** |

## LLM Reranking Impact

The LLM reranking step adds semantic understanding of fashion items — style compatibility, trend awareness, and seasonal relevance — that collaborative filtering misses.

```
CF Candidate Set (top 50)
       │
       ▼
LLM Reranker (GPT-4 / local LLM)
  • Prompt: user style profile + item descriptions
  • Scores each candidate on semantic fit
  • Reorders top 10
       │
       ▼
Final Recommendations (top 10)
```

**+14% NDCG improvement** over pure CF from LLM reranking step.
