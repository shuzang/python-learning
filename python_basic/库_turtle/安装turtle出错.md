## 问题
python3.7安装turtle，提示错误
```
Collecting turtle
  Using cached https://files.pythonhosted.org/packages/ff/f0/21a42e9e424d24bdd0e509d5ed3c7dfb8f47d962d9c044dba903b0b4a26f/turtle-0.0.2.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-hpqxw6_s/turtle/setup.py", line 40
        except ValueError, ve:
                         ^
    SyntaxError: invalid syntax

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-hpqxw6_s/turtle/
```
## 解决办法
按照给点的链接把turtle包下载到本地，手动解压，修改setup.py文件再安装
- 1 打开`setup.py`文件，第`40`行修改为
    `except (ValueError, ve):`
    原来的写法没加括号，是Python2的写法，加了括号python3才能用
- 2 用pip安装
    `pip install -e [文件路径]`
    `-e` 后的文件路径是修改过的`setup.py`文件所在路径
- 3 搞定