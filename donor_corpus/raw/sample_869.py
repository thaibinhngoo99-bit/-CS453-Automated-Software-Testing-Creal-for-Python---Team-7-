import sys

if len(sys.argv) != 2:
    print("Usage: python3 orgmybmarks.py bookmarks.html")
    quit()
file = open(sys.argv[1])
# file = open("in.html")
fileout = open("out.html", "w")
hreflist = []
# 读到第一个链接
numm = 1
while True:
    line = file.readline()
    if not line:
        break
    if line.find("HREF") == -1:
        continue
    num = line.find("HREF")
    href = line[num + 6:]
    num = href.find("\"")
    href = href[:num]
    hreflist.append(href)
    print("%d now %s" % (numm, href))
    numm += 1
numbef = len(hreflist)
hreflist = list(set(hreflist))  # 去重
numaft = len(hreflist)
fir = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 ADD_DATE="1530070116" LAST_MODIFIED="1532090715" PERSONAL_TOOLBAR_FOLDER="true">书签栏</H3>
    <DL><p>
'''
fileout.write(fir)
for i in range(len(hreflist)):
    sec = "        <DT><A HREF=\"%s\">%d</A>\n" % (hreflist[i], i)
    fileout.write(sec)
end = '''    </DL><p>
</DL><p>'''
fileout.write(end)
file.close()
fileout.close()
print("finished! now you have %d bookmarks, %d duplicated bookmarks deleted!" % (numaft, numbef - numaft))
