must read:
https://git-scm.com/book/zh/v2

如何把这个仓库的内容更新到自己fork的远程仓库？
'''
D:\git\weloveinterns>git remote -v
nepha   https://github.com/nephashi/weloveinterns (fetch)
nepha   https://github.com/nephashi/weloveinterns (push)
origin  https://github.com/lazyparser/weloveinterns (fetch)
origin  https://github.com/lazyparser/weloveinterns (push)
#这里nepha是我自己的fork远程仓库 origin是项目仓库

D:\git\weloveinterns>git fetch origin
remote: Counting objects: 127, done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 127 (delta 41), reused 53 (delta 37), pack-reused 69
Receiving objects: 100% (127/127), 607.81 KiB | 208.00 KiB/s, done.

Resolving deltas: 100% (57/57), completed with 8 local objects.
From https://github.com/lazyparser/weloveinterns
   11bd56c..8ba0376  master     -> origin/master
   
D:\git\weloveinterns>git branch -a
`*` master
  remotes/nepha/master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
  
D:\git\weloveinterns>git merge origin/master
Updating 4db8407..8ba0376
Fast-forward
 ...220\210\346\210\220\346\234\215\345\212\241.md" |  236 +++++
 Reports/Report-of-CNNdroid.md                      |    2 +-
 Reports/Report-of-ScanNet.md                       |   29 +
 ....
 
D:\git\weloveinterns>git push nepha
Counting objects: 127, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (64/64), done.
Writing objects: 100% (127/127), 606.93 KiB | 0 bytes/s, done.
Total 127 (delta 60), reused 122 (delta 56)
remote: Resolving deltas: 100% (60/60), completed with 8 local objects.
To https://github.com/nephashi/weloveinterns
   4db8407..8ba0376  master -> master
'''

