# Anime Recommender Web App

This web application uses a Flask backend to recommend animes based on a dataset. It incorporates a simple user interface for users to input an anime title and receive recommendations.

## Project Structure

```text
/Anime_Recommender
<<<<<<< HEAD
    │
    ├── app.py
    ├── check.py
    ├── anime_recommender_package
    │     ├── __init__.py
    │     ├── recommender_system.py
    │     └── assets
    │           └── anime.csv
    ├── templates
    │     ├── index.html
    │     └── recommendations.html
    ├── static
    │     └── styles.css
    └── notebooks
        └── m1.ipynb
=======
│
├── app.py
├── check.py
├── anime_recommender_package
│     ├── __init__.py
│     ├── recommender_system.py
│     └── assets
│           └── anime.csv
├── templates
│     ├── index.html
│     └── recommendations.html
├── static
│     └── styles.css
└── notebooks
      └── m1.ipynb
>>>>>>> 9a7e4340bc58d08033d75a1d18b30fc0f8c23fea
```

- **app.py**: Main Flask application file.
- **anime_recommender_package**: Python package containing the recommender system logic.
- **templates**: HTML templates for the web application.
- **static**: CSS file for styling.
- **notebooks**: Folder for Jupyter notebooks or analysis files.


## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo.git

# Navigate to the project folder
cd your_project_folder

# Install the required Python packages
pip install -r requirements.txt

# Run the Flask application
python app.py
```

Open the application in your web browser at http://localhost:5000.

## Usage
1. Enter the title of an anime in the input field.
2. Click the **Recommend** button to get a list of recommended animes.

## Additional Notes
1. Modify the recommender_system.py file to customize the recommendation logic.
2. Explore and analyze the dataset using Jupyter notebooks in the notebooks folder.
