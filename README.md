# xie 使用文档
## 理念
实践性语言，没有多余的语法，专为项目而生
## 基本语法
### print 输出文字
```xie
print>>我是字符
```
多次输出
```xie
print>>我是字符>>1
```
我是字符:需要输出的文字
1:输出次数
### input 输入
```xie  
input>>我是字符
```
我是字符:输出内容提示语
## requests 网络模块
### requests.get 获取
```xie
request.get>>www.example.com>>type
```
www.example.com:需要获取的网址
text:获取的内容类型
```text
text 文字
cookie 用户cookie
code 链接状态码
```
# 2.0beta 更新
## time 语法
```xie
time>>number
```
number:停止时间
## audio模块
### audio.play 启动服务
