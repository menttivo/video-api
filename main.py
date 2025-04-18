from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api/download", methods=["GET"])
def download():
    video_url = request.args.get("url")
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        response = requests.get(f"https://api.vevioz.com/api/button/videos/{video_url}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Failed to fetch"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
