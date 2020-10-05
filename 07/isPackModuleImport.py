from b64 import encoder, decoder

# 文字列のbase64形式表現
encoder.str_to_base64('python')
print( encoder.str_to_base64('python') )

# base64形式表現のもとの文字列
# 引数はbytes型なので頭にbを付ける
decoder.base64_to_str(b'cHl0aG9u')
print( decoder.base64_to_str(b'cHl0aG9u') )
