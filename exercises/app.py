from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    games=["skyrim","dark souls","the witcher","The legend of zelda","call of duty","life is strange","injustice","tekken","goat simulator","binding of isac","forza","mario bros","assassians creed","overwatch","portal","god of war","halo","cuphead","fallout","anime games","rocket league","guitar hero","far cry","mortal kombat","watch_dogs"]
    return render_template(
        "index.html",
        games=games,
        no_games=False)
        
if __name__ == '__main__':
   app.run(debug = True)