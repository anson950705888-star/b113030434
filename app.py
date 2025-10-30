from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬資料庫 (實際上你可以改用 SQLite)
posts = [
    {
        "id": 1,
        "title": "第一篇文章",
        "author": "柏諺",
        "content": "這是我的第一篇 Flask 部落格文章！"
    },
    {
        "id": 2,
        "title": "學習 Flask 的心得",
        "author": "小明",
        "content": "Flask 的模板系統真的很方便，Jinja2 可以讓我們輕鬆地插入變數。"
    }
]

@app.route('/')
def index():
    # 顯示所有文章
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 根據 id 顯示單篇文章
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "找不到該文章", 404
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        new_id = len(posts) + 1
        posts.append({
            "id": new_id,
            "title": title,
            "author": author,
            "content": content
        })
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
