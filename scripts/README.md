
# 指南

## 需要自己做的

### virtualenv + pip 需要怎么做

本地开发完后，再把代码给别人之前，需要

``` bash
pip freeze > requirements.txt
```

## 需要别人做的事情

### 安装 virtualenv, virtualenvwrapper, pip
在 .bashrc 中加入

``` bash
source path/to/virtualenvwrapper.sh
export VENVS=path/to/virtualenv_home
```


### 开发前，需要执行下面代码

mkvirtualenv env
workon env
pip install -r requirements.txt

