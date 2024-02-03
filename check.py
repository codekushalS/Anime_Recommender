from anime_recommender_package.recommender_system import anime_recommender
import pandas as pd


def testrec():
    datasetpath = 'anime_recommender_package/assets/anime.csv'
    # df = pd.read_csv(datasetpath)
    # print(df.shape)

    recommender = anime_recommender(datasetpath)
    
    animetitle = 'Tokyo Ghoul'

    recs = recommender.recommend(animetitle)

    for x in recs:
        print(x)


if __name__ == '__main__':
    testrec()