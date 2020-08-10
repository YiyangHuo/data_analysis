

* 文件名 一般用小写+下划线命名，而不适用大驼峰 https://google.github.io/styleguide/pyguide.html#316-naming
* 空行问题 https://google.github.io/styleguide/pyguide.html#35-blank-lines
* 空格问题 https://google.github.io/styleguide/pyguide.html#36-whitespace
* line 2 & 4: Unused imports
* line12: python3 类定义似乎已经不需要再写 `(object)` 了
* line14: label 范围 1~7，_sequences 作为 list 需要转换：index = label - 1，这语义很乱，容易在之后使用中出错。建议改用 dict。
* line20: 不要 print。如果确实需要 log 信息的话，打印中增加一些 context 信息便于追溯
* line21: 如果 row_size == 0，这里会不会有 exception
* line23: 这种遍历写法不太 pythonic，直接 `for row in file_data` 就好，如果需要下标则 `for index, row in enumberate(file_data)`
* line26: 这个条件分支似乎可以写到 for 之外，也就是 for 完之后必进行 append 操作
    * line 19: 于是 row_size 这个变量就没有用了
* line27: 用 `current_sequences` 逐一 append 数据看起来也可以记录一下起始的 start_index，在append的时候直接取 [start_index:end_index]。我猜测后一种的效率会更高一些但不确定，可以写个脚本测试一下
* line 33 & 34: could be inline like this:  `current_sequences = [file_data[index]]`
* line35: test print 删掉
* line37: 测试代码单写，如果只是写在同一个文件里简单测功能用 `if __name__ == '__main__':` 包起来

* line38: 感觉构造函数可以加参数直接进行 addData 方便调用。当然这是接口设计习惯问题 没有对错
    
* 感觉 np 在这里没有什么用处啊...如果只是单纯为了读文件手写就好了或者用官方的 csv 包，没必要上 np


