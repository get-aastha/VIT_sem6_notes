from flask import Flask, render_template, request
from urllib.parse import quote  # Sanitize user input (for potential future use)

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("search.html")

@app.route("/results", methods=["GET"])
def search_results():
    keyword = request.args.get("keyword", "").lower()  # Get and lowercase keyword
    sanitized_keyword = quote(keyword)  # Sanitize for potential future use (doesn't affect logic here)

    # Implement your image retrieval logic here (replace with actual image source)
    images = []
    if keyword == "madhuri":
        images = ["1.jpeg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]


    if keyword == "1=1 --)":
        images = ["1.jpeg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    return render_template("results.html", keyword=keyword, images=images)

if __name__ == "__main__":
    app.run(debug=True)
