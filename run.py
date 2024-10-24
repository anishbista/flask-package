from dotenv import load_dotenv
from calculator import app

load_dotenv()

if __name__ == "__main__":
    app.run(debug=True)
