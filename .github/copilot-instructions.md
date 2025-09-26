## Quick orientation

This repository implements an end-to-end fashion recommender system (retrieval + ranking).
Key folders:
- `recsys/` - core library: config, feature engineering, embedding and hopsworks integration.
- `recsys/features/` - data transformations (Polars + pandas). See `articles.py`, `embedding.py`.
- `recsys/hopsworks_integration/` - code that creates feature groups and feature views in Hopsworks (`feature_store.py`, `constants.py`).
- `notebooks/` - exploratory pipelines and training steps (use these as runnable examples).

## Big-picture architecture notes for code edits
- Retrieval model pipeline: transactions feature group joins `customers` and `articles` feature groups to produce the retrieval training view (see `create_retrieval_feature_view` in `recsys/hopsworks_integration/feature_store.py`).
- Articles use an `article_description` text field and an `embeddings` vector stored in the feature store. Embedding size is controlled by `settings.TWO_TOWER_MODEL_EMBEDDING_SIZE` in `recsys/config.py`.
- Feature groups are created/updated via the `hopsworks` and `hsfs` SDKs. Modifying FG shapes or names must be reflected in `constants.py` and in any code that reads those groups (notebooks and training scripts).

## Project-specific conventions & patterns
- Settings: central config lives in `recsys/config.py` using `pydantic-settings`. Prefer reading `settings` rather than environment variables directly.
- Dataframes: feature code uses Polars heavily (`recsys/features/articles.py`). Be mindful of Polars types and `pl.Series` operations.
- Embeddings: two styles exist: sentence-transformers in `features/articles.py` (generates `embeddings` column with lists) and TensorFlow-based candidate embedding in `features/embedding.py`. Keep outputs compatible with Hopsworks `EmbeddingIndex` (see `create_candidate_embeddings_feature_group`).

## Developer workflows (how to run, build, test)
- Python runtime: project targets Python 3.11 (see `pyproject.toml`).
- Install: repository includes a minimal `makefile`; it expects a helper `uv` task runner. If `uv` is not present, create a venv and install dependencies from `pyproject.toml` manually:

```bash
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -e .[all]
```

- Notebooks: run the notebooks under `notebooks/` to reproduce ETL and training steps; they are the canonical runnable examples.

## CI / lint / tests
- There is no CI configuration in the repo. A minimal dev dependency group exists in `pyproject.toml` (ruff). Follow existing style when editing.

## Integration points & external dependencies
- Hopsworks: uses `hopsworks` and `hsfs` SDKs. Real runs expect a HOPSWORKS API key or cached login. See `recsys/hopsworks_integration/feature_store.py` for login logic.
- Sentence-transformers and TensorFlow are used for embeddings and models. Large models may require GPU; be conservative in CI/dev runs.

## When editing code, check these files (examples)
- `recsys/config.py` — global knobs (embedding size, model ids, keys)
- `recsys/hopsworks_integration/feature_store.py` — feature group/view creation and naming
- `recsys/features/articles.py` — Polars feature transformations and embedding generation
- `recsys/features/embedding.py` — candidate embedding TensorFlow pipeline
- `notebooks/` — runnable examples (ETL → feature store → training)

## Safety for automated edits
- Don't change feature-group names or primary keys without updating `constants.py`, downstream notebooks and feature view queries.
- Avoid checking in API keys. `recsys/config.py` expects secrets via `.env` or `SecretStr`.

If anything is unclear or you'd like more detail (CI commands, tests, or expanding examples into scripts), tell me which area to expand and I will iterate.
