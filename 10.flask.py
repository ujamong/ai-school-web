# Flask 기본형
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# app.run()


from flask import Flask
import random

app = Flask(__name__)

topics = [
  {"id": 1, "title": "html", "body":"html is ..."},
  {"id": 2, "title": "css", "body" : "css is ..."},
  {"id": 3, "title" : "js", "body" : "js is..."}
]

# @app.route("/")
# def hello_world():
#   return "<strong>random</strong> : " + str(random.random())

def template(content):
  #인덱스 함수에 있는 부분 가져옴
  liTags = ''
  for topic in topics:
    liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
  return f"""
  <html>
    <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        {liTags}  
      </ol>
      {content}
      <ul>
        <li><a href="/create/">create</a></li>
      </ul>
    </body>
  </html>
  """

@app.route("/")
def index():
  # liTags = ''
  # for topic in topics:
  #   liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</li>'
  # return f"""
  # <html>
  #   <body>
  #     <h1><a href="/">WEB</a></h1>
  #     <ol>
  #       {liTags}  
  #     </ol>
  #     <h2>Welcome</h2>
  #     Hello, WEB!
  #   </body>
  # </html>
  # """
  return template('<h2>Welcome</h2>Hello, WEB!')

# @app.route("/")
# def index():
#   liTags = ''
#   for topic in topics:
#     liTags = liTags + f'<li>{topic["title"]}</li>'
#   return f'''
#   <html>
#     <body>
#       <h1><a href="/">WEB</a></h1>
#       <ol>
#         {liTags}
#       </ol>
#       <h2>Welcome</h2>
#       Hello, WEB!
#     </body>
#   </html>
#   '''

#route계속 생성하는 것은 비효율적
@app.route("/read/<int:id>/")
def read(id):
  #print(id)
  title = ''
  body = ''
  for topic in topics:
    if topic['id'] == id:
      title = topic['title']
      body = topic['body']
      break;
      
#   return f"""
#   <html>
#     <body>
#       <h1><a href="/">WEB</a></h1>
#       <ol>
#         <li><a href = "/read/1">html</a></li>
#         <li><a href = "/read/2">css</a></li>
#         <li><a href = "/read/3">js</a></li>
#       </ol>
#       <h2>{title}</h2>
#       {body}
#     </body>
#   </html>
  
#   """
  return template(f'<h2>{title}</h2>{body}')







@app.route("/create/")
def create():
  # return "Create"
  content = '''    
    <form action="/create/"> # https://www.google.com/search
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea name="body" placeholder = "body"></textarea></p>
      <p><input type="submit" value = "create"></p>
    </form>
  '''
  return template(content)



@app.route("/update/")
def update():
  return "Update"

app.run()

