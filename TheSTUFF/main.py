from website import create_app
import os

app = create_app()

if __name__ == '__main__':
#    os.system("start chrome http://127.0.0.1:5000/")
    website_url = 'stuff.webapp:5000'
    app.config['SERVER_NAME'] = website_url
    app.run(debug=True) # Deving shit
#    app.run() # Proding shit