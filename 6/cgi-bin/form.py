import cgi

form = cgi.FieldStorage()
a = float(form.getfirst("a", "Missing a argument."))
b = float(form.getfirst("b", "Missing b argument."))
c = float(form.getfirst("c", "Missing c argument."))

print("Content-type: text/html")
print('')
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>""")

mn= min([a,b,c])
mx=max([a,b,c])
if mn==0:
    print("Zero division error")
else:
    print("Your result is ")
    print(mx/mn)


print("""</body>
        </html>""")
