from bottle import run
import server
import os

if __name__ == "__main__":
    run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
