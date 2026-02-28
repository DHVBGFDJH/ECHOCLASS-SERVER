from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_video():
    if "video" not in request.files:
        return jsonify({"error": "No video provided"}), 400

    file = request.files["video"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({
        "message": "Video uploaded successfully",
        "url": f"/videos/{file.filename}"
    })

@app.route("/videos/<filename>", methods=["GET"])
def get_video(filename):
    return app.send_static_file(os.path.join("uploads", filename))

if __name__ == "__main__":
    app.run()