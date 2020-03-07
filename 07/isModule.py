# モジュールのインポート
import encoder # モジュールのインポート

# 変数encoderはmoduleクラスのインスタンス
print( type(encoder) )


# encoderモジュールのトップレベルのオブジェクトが確認できる
dir(encoder)
print( dir(encoder) )


# モジュール内で定義された関数の呼び出し
encoder.str_to_base64('python')
print( encoder.str_to_base64('python') )
