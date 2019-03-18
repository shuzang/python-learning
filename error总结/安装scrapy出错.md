## 问题
win10,python3.7，64位
使用`pip install scrapy`安装scrapy出错
```
building 'twisted.test.raiser' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
```

## 解决办法
从[此处](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)下载twisted对应版本的whl文件，如我下载`Twisted-18.7.0-cp37-cp37m-win_amd64.whl`文件,cp后面是python版本，amd64代表64位，运行命令：

    pip install C:\Users\lylw1\Desktop\Twisted-18.7.0-cp37-cp37m-win_amd64.whl

其中`install`后面为下载的whl文件完整路径名

安装完成后，再次运行`pip install scrapy`即可成功