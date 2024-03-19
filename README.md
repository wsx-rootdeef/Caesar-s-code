主要用于处理buuctf的变异凯撒密码，如果普通的可以去网站上处理
前提是有顺序比如n+1
这样我们可以将key的值给n-1
这样就能解体
如果没有特殊符号我们可以将第五行改成
 plaintext += chr((ord(ciphertext[i]) - ord('a') + key) %26 + ord('a')) 
