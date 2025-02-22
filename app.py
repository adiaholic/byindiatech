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

def create_supabase_client():
    url = os.environ.get("SUPABASE_PROJECT_URL")
    key = os.environ.get("SUPABASE_API_KEY")
    supabase_client = create_client(url, key)
    return supabase_client

create_supabase_client()


@app.route('/api/startups', methods=['GET'])
def get_startups():
    supabase_client = create_supabase_client()
    result = supabase_client.table("yc-startups").select("*").execute()
    if result:
        startups = result.data
        startups = [
            {
                "name": startup["name"],
                "yc_batch": startup["yc_batch"],
                "team_size": startup["teamsize"],
                "website": startup["website"]
            }
            for startup in startups
        ]
    else:
        startups = []
    return jsonify(startups)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", default=True))
