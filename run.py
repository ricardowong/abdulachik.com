from app import app

# Start development web server
if __name__ == "__main__":
    app.run(debug=True, extra_files=[app.config["WEBPACK_MANIFEST_PATH"]])
