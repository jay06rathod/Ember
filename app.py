from flask import Flask, request, redirect
from flask import send_from_directory
from db import init_db, get_conn

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.','index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    with get_conn() as conn:
        cursor = conn.cursor()
        og_url = request.json['og_url']
        entropy = request.json.get('entropy', 0)
        
        insert_data = "INSERT INTO URLS (original_url) VALUES (%s) RETURNING id"
        cursor.execute(insert_data, (og_url,))
        row_id = cursor.fetchone()[0]
        
        short_code = base62_encoder(row_id + entropy)
        
        update = "UPDATE URLS SET short_code = %s WHERE id = %s"
        cursor.execute(update, (short_code, row_id))
        conn.commit()
        
    return f"https://ember-ages.onrender.com/r/{short_code}"

def base62_encoder(n):
    strings = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    while n>0:
        curr = n%62
        code+=strings[curr]
        n=n//62

    return code[::-1]

@app.route('/r/<short_code>', methods=['GET'])
def redirect_url(short_code):
    with get_conn() as conn:
        cursor = conn.cursor()
        redirect_query = """
            SELECT original_url FROM URLS WHERE short_code = %s
        """
        cursor.execute(redirect_query, (short_code,))
        result = cursor.fetchone()
        if result is None:
            return "Link not found", 404
    return redirect(result[0])
    
init_db()

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))