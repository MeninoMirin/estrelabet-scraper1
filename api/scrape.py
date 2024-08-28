from flask import Flask, jsonify
from scraper import scrape_estrelabet

app = Flask(__name__)

@app.route('/api/scrape', methods=['GET'])
def scrape():
    result = scrape_estrelabet()
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
