from flaskr import create_app
app = create_app()

if __name__ == "__main__":
    # When you change stuff other than a python file, set debug to True. It allows you to get the right away.
    # When you do it with a python file, it can crash the program.
    app.run("127.0.0.1", 5000, debug=True)