from flask import Flask, render_template, request
from anime_recommender_package.recommender_system import anime_recommender

app = Flask(__name__)
recommender = anime_recommender('anime_recommender_package/assets/anime.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    anime_name = request.form['anime_name']
    recommendations = recommender.recommend(anime_name)
    return render_template('recommendations.html', anime_name=anime_name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)