#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name": "Fraudulent Web Identifier",
    "description": "Offers a comprehensive solution for obtaining detailed domain registration data, including registrant contact information, domain availability status, registration and expiration dates, and nameserver details.",
    "author": "Padmanabh Raje",
    "html_title": "Fraudulent Web Identifier",
    "project_name": "Fraudulent Web Identifier",
}


@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)


@app.route("/about")
def about():
    return render_template("about.html", app_data=app_data)


@app.route("/service")
def service():
    return render_template("service.html", app_data=app_data)


@app.route("/contact")
def contact():
    return render_template("contact.html", app_data=app_data)


if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)
