n = int(input()) # キーボード からnの値を読み取り
prime_list = [2] # 素数をいれるリストを作成
for i in range(3, n+1): # ３からnまで繰り返し
    isprime = True # 素数かどうかの真偽値の変数
    for prime in prime_list: # 今までにでできた素数のぶん繰り返し
        if i%prime == 0: # もし割り切れたら
            isprime = False # 判定をfalseに変える
            break # 繰り返しを抜けて次の値に移る
    if isprime: # 判定がTrueなら
        prime_list.append(i) # リストに値を追加

with open('primes_at_most_n.txt', 'w') as f: # txtファイルを作成して開く
    for prime in prime_list: # リストの素数一つずつ繰り返し
        f.write(str(prime) + '\n') # 値の後に改行を追加して書き込み