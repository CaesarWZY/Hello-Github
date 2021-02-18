## 怎么这么奇怪那这个文件

还行并不是很奇怪



### Run
```
python hello.py

```

## 正规合作开发时候需要注意的地方

### 不能上传配置文件到github

那怎么办那

使用git 上传的时候可以进行选择

### step1 建立.gitignore 文件

在根目录下创建.gitignore文件，首先，在该目录下git bash然后命令行中输入

```Linux C
touch .gitignore ##创建.gitignore 文件该文件是txt文件
```

## step2 在文件中写入需要在上传过程中被忽略的文件

编辑文本文件如：

```
#Default ignored files
/.idea  ## 忽略该目录下的素有文件
/venv
/.gitignore.txt ##忽略某个文件，一定要加文件名但是这样是不行的

```

### step3 git中进行清除所需要的忽略文件的缓存

很多次的实验都是基于上次的但是不能成功，最大的原因是使用git的过程中，git记住了诸如.idea文件的位置以及内容所以保证失败。但是如果在git中进行如下操作那么就可以成功

```
git rm -r --cached .idea ##清除.idea在git当中的缓存

```

但是只有这一步是不可以的因为我试过，结果是.idea里面的内容确实消失了但是文件夹依旧存在，所以step2和3结合才能成功.

### step4 进行git更改、保存并上传

```
git add .
git commit -m 'add .gitignore'
git push

git remote add origin git@github仓库地址 ##将本地的仓库与远端仓库进行连接
git push --set-upstream origin dev  //dev为创建分支的名字 建立本地到远端仓库的链接 --这样代码才能提交上去

```

```cpp
更新远程分支列表
git remote update origin --prune

查看所有分支
git branch -a

删除远程分支Chapater6
git push origin --delete Chapater6

删除本地分支 Chapater6
git branch -d  Chapater6
```

### 把新建的分支push到远程，相当于创建一个远程分支

```
git push origin 名称:名称
```