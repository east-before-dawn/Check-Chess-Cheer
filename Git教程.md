# Git教程

- 克隆版本库
`git clone https://github.com/three-C-team/Check-Chess-Cheer.git`
&nbsp;

    ```none
    正克隆到 'Check-Chess-Cheer'...
    remote: Enumerating objects: 22, done.
    remote: Counting objects: 100% (22/22), done.
    remote: Compressing objects: 100% (15/15), done.
    remote: Total 22 (delta 1), reused 0 (delta 0), pack-reused 0
    接收对象中: 100% (22/22), 5.14 KiB | 2.57 MiB/s, 完成.
    处理 delta 中: 100% (1/1), 完成.
    ```

- 查看版本库状态
`git status`
&nbsp;

    ```none
    位于分支 main
    您的分支与上游分支 'origin/main' 一致。

    尚未暂存以备提交的变更：
    （使用 "git add <文件>..." 更新要提交的内容）
    （使用 "git restore <文件>..." 丢弃工作区的改动）
        修改：     README.md

    未跟踪的文件:
    （使用 "git add <文件>..." 以包含要提交的内容）
        "Git\346\225\231\347\250\213.md"

    修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
    ```

- 添加要提交修改的文件
`git add README.md`
&nbsp;
- 提交修改至本地版本库
`git commit --message "在README中添加了中文标题"`
&nbsp;

    ```none
    [main 3aa02a6] 在README中添加了中文标题
     1 file changed, 1 insertion(+)
    ```

- 上传修改至远程版本库（GitHub）
`git push`
&nbsp;

    ```none
    枚举对象中: 5, 完成.
    对象计数中: 100% (5/5), 完成.
    使用 8 个线程进行压缩
    压缩对象中: 100% (2/2), 完成.
    写入对象中: 100% (3/3), 353 字节 | 353.00 KiB/s, 完成.
    总共 3（差异 0），复用 0（差异 0），包复用 0
    To https://github.com/three-C-team/Check-Chess-Cheer.git
    7a764a6..3aa02a6  main -> main
    ```
