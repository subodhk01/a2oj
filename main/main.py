

a = '''
http://codeforces.com/problemset/problem/4/A
http://codeforces.com/problemset/problem/71/A
http://codeforces.com/problemset/problem/118/A
http://codeforces.com/problemset/problem/112/A
http://codeforces.com/problemset/problem/339/A
http://codeforces.com/problemset/problem/160/A
http://codeforces.com/problemset/problem/58/A
http://codeforces.com/problemset/problem/122/A
http://codeforces.com/problemset/problem/136/A
http://codeforces.com/problemset/problem/263/A
http://codeforces.com/problemset/problem/144/A
http://codeforces.com/problemset/problem/451/A
http://codeforces.com/problemset/problem/268/A
http://codeforces.com/problemset/problem/208/A
http://codeforces.com/problemset/problem/69/A
http://codeforces.com/problemset/problem/337/A
http://codeforces.com/problemset/problem/479/A
http://codeforces.com/problemset/problem/443/A
http://codeforces.com/problemset/problem/469/A
http://codeforces.com/problemset/problem/318/A
http://codeforces.com/problemset/problem/466/A
http://codeforces.com/problemset/problem/313/A
http://codeforces.com/problemset/problem/459/A
http://codeforces.com/problemset/problem/230/A
http://codeforces.com/problemset/problem/476/A
http://codeforces.com/problemset/problem/490/A
http://codeforces.com/problemset/problem/439/A
http://codeforces.com/problemset/problem/510/A
http://codeforces.com/problemset/problem/25/A
http://codeforces.com/problemset/problem/432/A
http://codeforces.com/problemset/problem/330/A
http://codeforces.com/problemset/problem/441/A
http://codeforces.com/problemset/problem/462/A
http://codeforces.com/problemset/problem/385/A
http://codeforces.com/problemset/problem/276/A
http://codeforces.com/problemset/problem/456/A
http://codeforces.com/problemset/problem/151/A
http://codeforces.com/problemset/problem/378/A
http://codeforces.com/problemset/problem/496/A
http://codeforces.com/problemset/problem/255/A
http://codeforces.com/problemset/problem/483/A
http://codeforces.com/problemset/problem/404/A
http://codeforces.com/problemset/problem/233/A
http://codeforces.com/problemset/problem/499/A
http://codeforces.com/problemset/problem/165/A
http://codeforces.com/problemset/problem/262/A
http://codeforces.com/problemset/problem/501/A
http://codeforces.com/problemset/problem/189/A
http://codeforces.com/problemset/problem/350/A
http://codeforces.com/problemset/problem/152/A
http://codeforces.com/problemset/problem/265/A
http://codeforces.com/problemset/problem/353/A
http://codeforces.com/problemset/problem/114/A
http://codeforces.com/problemset/problem/300/A
http://codeforces.com/problemset/problem/389/A
http://codeforces.com/problemset/problem/488/A
http://codeforces.com/problemset/problem/224/A
http://codeforces.com/problemset/problem/445/A
http://codeforces.com/problemset/problem/43/A
http://codeforces.com/problemset/problem/75/A
http://codeforces.com/problemset/problem/296/A
http://codeforces.com/problemset/problem/373/A
http://codeforces.com/problemset/problem/361/A
http://codeforces.com/problemset/problem/355/A
http://codeforces.com/problemset/problem/239/A
http://codeforces.com/problemset/problem/437/A
http://codeforces.com/problemset/problem/363/A
http://codeforces.com/problemset/problem/408/A
http://codeforces.com/problemset/problem/376/A
http://codeforces.com/problemset/problem/359/A
http://codeforces.com/problemset/problem/302/A
http://codeforces.com/problemset/problem/358/A
http://codeforces.com/problemset/problem/34/A
http://codeforces.com/problemset/problem/143/A
http://codeforces.com/problemset/problem/186/A
http://codeforces.com/problemset/problem/108/A
http://codeforces.com/problemset/problem/416/A
http://codeforces.com/problemset/problem/194/A
http://codeforces.com/problemset/problem/106/A
http://codeforces.com/problemset/problem/257/A
http://codeforces.com/problemset/problem/298/A
http://codeforces.com/problemset/problem/279/A
http://codeforces.com/problemset/problem/27/A
http://codeforces.com/problemset/problem/370/A
http://codeforces.com/problemset/problem/49/A
http://codeforces.com/problemset/problem/284/A
http://codeforces.com/problemset/problem/192/A
http://codeforces.com/problemset/problem/56/A
http://codeforces.com/problemset/problem/234/A
http://codeforces.com/problemset/problem/31/A
http://codeforces.com/problemset/problem/305/A
http://codeforces.com/problemset/problem/197/A
http://codeforces.com/problemset/problem/35/A
http://codeforces.com/problemset/problem/88/A
http://codeforces.com/problemset/problem/18/A
http://codeforces.com/problemset/problem/374/A
http://codeforces.com/problemset/problem/393/A
http://codeforces.com/problemset/problem/390/A
http://codeforces.com/problemset/problem/397/A
http://codeforces.com/problemset/problem/200/A
'''

b = a.split("\n")
c = []
for link in b:
    link = link[41:]
    c.append(link.split('/'))
for x in c:
    print(x, ",")
