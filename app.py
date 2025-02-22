from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)


# # Configure SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Define the YcStartup model
# class YcStartup(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     yc_batch = db.Column(db.String(50), nullable=False)
#     funding = db.Column(db.String(50))
#     team_size = db.Column(db.String(50))
#     linkedin = db.Column(db.String(200))

#     def __repr__(self):
#         return f'<YcStartup {self.name}>'

# # Initialize the database
# with app.app_context():
#     db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/add", methods=["GET", "POST"])
# @csrf.exempt
# def add_startup():
#     if request.method == "POST":
#         data = request.get_json()
#         name = data["name"]
#         yc_batch = data["yc_batch"]
#         funding = data["funding"]
#         team_size = data["team_size"]
#         linkedin = data["linkedin"]

#         new_startup = YcStartup(
#             name=name,
#             yc_batch=yc_batch,
#             funding=funding,
#             team_size=team_size,
#             linkedin=linkedin
#         )

#         db.session.add(new_startup)
#         db.session.commit()

#     return jsonify({"message": "Startup added successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
