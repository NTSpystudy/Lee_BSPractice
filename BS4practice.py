from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8" />
    <title>제목</title>
</head>
<body>
<h1>제목1</h1>
<p>
    내용1...
</p>
<h1>제목2</h1>
<p>
    내용2...
</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())