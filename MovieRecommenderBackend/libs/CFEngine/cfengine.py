import pandas as pd
import numpy as np
import pickle
from scipy.sparse.linalg import svds
from pathlib import Path


def get_recommendations_list(user_id, movies, ratings, num_recommendations=10):
    # Prepare dataframes
    ratings_df = pd.DataFrame.from_records(ratings)
    movies_df = pd.DataFrame.from_records(movies)

    user_data = ratings_df[ratings_df.user_id == user_id]
    if user_data.empty:
        return None

    preds_file = Path('preds_df.pkl')
    if not preds_file.exists():
        train_model(ratings)
    preds_df = pd.read_pickle('preds_df.pkl')

    # Get and sort the user's predictions
    user_row_number = user_id - 1  # UserID starts at 1, not 0
    sorted_user_predictions = preds_df.iloc[user_row_number].sort_values(ascending=False)

    # Get the user's data and merge in the movie information.
    user_data = ratings_df[ratings_df.user_id == user_id]
    user_full = (user_data.merge(movies_df, how='left', left_on='movie_id', right_on='movie_id').
                 sort_values(['rating'], ascending=False)
                 )

    print
    'User {0} has already rated {1} movies.'.format(user_id, user_full.shape[0])
    print
    'Recommending the highest {0} predicted ratings movies not already rated.'.format(num_recommendations)

    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    recommendations = (movies_df[~movies_df['movie_id'].isin(user_full['movie_id'])].
                       merge(pd.DataFrame(sorted_user_predictions).reset_index(), how='left',
                             left_on='movie_id',
                             right_on='movie_id').
                       rename(columns={user_row_number: 'Predictions'}).
                       sort_values('Predictions', ascending=False).
                       iloc[:num_recommendations, :-1]
                       )

    return recommendations


def train_model(ratings):
    ratings_list = pd.DataFrame.from_records(ratings)
    ratings_df = ratings_list.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
    ratings = ratings_df.as_matrix()
    user_ratings_mean = np.mean(ratings, axis=1)
    ratings_demeaned = ratings - user_ratings_mean.reshape(-1, 1)
    U, sigma, Vt = svds(ratings_demeaned, k=50)
    sigma = np.diag(sigma)
    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    preds_df = pd.DataFrame(all_user_predicted_ratings, columns=ratings_df.columns)
    preds_df.to_pickle('prefs_df.pkl')