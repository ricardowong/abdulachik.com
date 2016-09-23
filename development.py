# from app import create_app
from app import app
from livereload import Server, shell
# Start development web server
if __name__ == "__main__":
    # app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(debug=True)
