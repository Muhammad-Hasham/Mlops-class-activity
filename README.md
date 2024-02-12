# Mlops-class-activity

# i200752 Muhammad Hasham Ul Haq
hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity
$ git init
Initialized empty Git repository in C:/Users/hasha/Desktop/Mlops-class-activity/.git/

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (master)
$ git remote add origin https://github.com/Muhammad-Hasham/Mlops-class-activity.git

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (master)
$ git branch -M main

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (main)
$ git add .

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (main)
$ git commit -m "scaffolding python-project"
[main (root-commit) 0fde07e] scaffolding python-project
 4 files changed, 39 insertions(+)
 create mode 100644 README.md
 create mode 100644 src/main.py
 create mode 100644 src/my_module.py
 create mode 100644 tests/test_main.py

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (main)
$ git push -u origin main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 947 bytes | 947.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Muhammad-Hasham/Mlops-class-activity.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (main)
$ git checkout -b dev
Switched to a new branch 'dev'

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git add .

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git commit -m "scaffolding python-project from dev branch"
On branch dev
nothing to commit, working tree clean

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git push -u origin dev
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/Muhammad-Hasham/Mlops-class-activity/pull/new/dev
remote:
To https://github.com/Muhammad-Hasham/Mlops-class-activity.git
 * [new branch]      dev -> dev
branch 'dev' set up to track 'origin/dev'.

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git checkout -b test
Switched to a new branch 'test'

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (test)
$ git add .

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (test)
$ git commit -m "scaffolding python-project from test branch"
On branch test
nothing to commit, working tree clean

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (test)
$ git push -u origin test
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'test' on GitHub by visiting:
remote:      https://github.com/Muhammad-Hasham/Mlops-class-activity/pull/new/test
remote:
To https://github.com/Muhammad-Hasham/Mlops-class-activity.git
 * [new branch]      test -> test
branch 'test' set up to track 'origin/test'.

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (test)
$ git checkout -b i200752
Switched to a new branch 'i200752'

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (i200752)
$ git checkout dev
Switched to branch 'dev'
M       src/my_module.py
Your branch is up to date with 'origin/dev'.

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git merge i200752
Already up to date.

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git add .

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git commit -m "i200752 branch merged to dev branch"
[dev db3d274] i200752 branch merged to dev branch
 1 file changed, 2 insertions(+), 1 deletion(-)

hasha@Sebastian MINGW64 ~/Desktop/Mlops-class-activity (dev)
$ git push -u origin dev
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 483 bytes | 483.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Muhammad-Hasham/Mlops-class-activity.git
   0fde07e..db3d274  dev -> dev
branch 'dev' set up to track 'origin/dev'.

# Zaryab i202487

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (main)
$ git checkout dev
Switched to a new branch 'dev'
branch 'dev' set up to track 'origin/dev'.

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (dev)
$ git checkout -b i202487
Switched to a new branch 'i202487'

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (i202487)
$ git checkout dev
Switched to branch 'dev'
M       src/my_module.py
Your branch is up to date with 'origin/dev'.

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (dev)
$ git merge i202487
Already up to date.

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (dev)
$ git add .

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (dev)
$ git commit -m "i202487 branch merged to dev"
[dev 941ce31] i202487 branch merged to dev
 1 file changed, 3 insertions(+), 1 deletion(-)

Waleed@DESKTOP-3MA3LP1 MINGW64 /d/Final Sem/MLOPS/Mlops-class-activity (dev)
$ git push -u origin dev
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 444 bytes | 444.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Muhammad-Hasham/Mlops-class-activity.git
   db3d274..941ce31  dev -> dev
branch 'dev' set up to track 'origin/dev'.

