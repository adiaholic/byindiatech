from dotenv import load_dotenv
import os

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

import os
from supabase import create_client, Client

load_dotenv()

app = Flask(__name__)
csrf = CSRFProtect(app)

supabase_client = None

def create_supabase_client():
    url = os.environ.get("SUPABASE_PROJECT_URL")
    key = os.environ.get("SUPABASE_API_KEY")
    supabase_client = create_client(url, key)

create_supabase_client()

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", default=True))
