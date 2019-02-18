from src.utils import *
from src.sentiment_utils import *
from src.trend_utils import *
from src.plot import *

# Path to data sets.
sentiment_path = ""
trend_path = ""

sentiment_df = read_csv(sentiment_path)
trend_df = read_csv(trend_path)

sentiment_scores = sentiment_sequences(sentiment_df,
                                        company_row_name="company",
                                        date_row_name="published",
                                        sentiment_row_name="sentiment")

sentiment_scores_description = get_sentiment_scores_with_description(sentiment_df,
                                                                     company_row_name="company",
                                                                     date_row_name="published",
                                                                     sentiment_row_name="sentiment",
                                                                     description_row_name="summary",
                                                                     url_row_name="url")

trend_scores = get_trend_scores(trend_df,
                                company_row_name="entity",
                                date_row_name="date",
                                trend_row_name="normalizedMentionScore")


plot_bars_with_descriptions(sentiment_scores_description, "Sentiments")
