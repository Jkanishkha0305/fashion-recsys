import polars as pl


def extract_articles_df() -> pl.DataFrame:
    return pl.read_csv("https://repo.hops.works/dev/jdowling/h-and-m/articles.csv", try_parse_dates=True)


def extract_customers_df() -> pl.DataFrame:
    return pl.read_csv("https://repo.hops.works/dev/jdowling/h-and-m/customers.csv", try_parse_dates=True)


def extract_transactions_df() -> pl.DataFrame:
    return pl.read_csv(
        "https://repo.hops.works/dev/jdowling/h-and-m/transactions_train.csv", try_parse_dates=True
    )