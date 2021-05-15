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

- 进入目录
`cd Check-Chess-Cheer`
&nbsp;
- 修改或添加文件
`略`
&nbsp;
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

- 如果有人在你push之前push过，那么你的push会被拒绝，此时应先从远程版本库（GitHub）拉取更改
`git pull`
&nbsp;

    ```none
    已经是最新的。
    ```

- 查看Git日志
`git log --graph`
&nbsp;

    ```none
    * commit c83f0bb11e46789553515d462669f1d835c69b1b (HEAD -> main, origin/main, origin/HEAD)
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 14:00:04 2021 +0800
    | 
    |     修改了README
    | 
    * commit 28590ec71e8d8932d9553f9f2611c846d5c966fc
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:58:59 2021 +0800
    | 
    |     修改了Git教程
    | 
    * commit 4b57799cf7438b28a812fe36c5617c0b11e1d3cc
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:58:31 2021 +0800
    | 
    |     修改了Git教程
    | 
    * commit 0bc9f5cf347a54cabdc9c9ea2d61edc1d93e1c0c
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:44:54 2021 +0800
    | 
    |     修改了Markdown教程
    | 
    * commit 4876c7bc618b722eded49b629176cfeb74d4cc85
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:43:18 2021 +0800
    | 
    |     修改了Markdown教程
    | 
    * commit 24cbe45e39262bb1ecdff47f4b83a983dc810232
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:41:54 2021 +0800
    | 
    |     修改了Markdown教程
    | 
    * commit a658ecc6c8c69c1918db6dd6e6716ce61f9147a9
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:31:20 2021 +0800
    | 
    |     添加了Markdown教程
    | 
    * commit 30ec36b50b4eab4673356c83957e582918b2f7c7
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:15:38 2021 +0800
    | 
    |     修改了Git教程
    | 
    * commit 7b5f695777fe12acf10c67a90ad36237dab91137
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:13:25 2021 +0800
    | 
    |     修改了Git教程
    | 
    * commit 9a162b1c56a3ce773cebca9a2681d5387c5db7c1
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:12:10 2021 +0800
    | 
    |     添加了Git教程
    | 
    * commit 99255dd61250e831b1c7fc6c4c6042f51745c2a3
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:08:41 2021 +0800
    | 
    |     添加了Git教程
    | 
    * commit 2bb691d2381e1ffa7f6b5292b428c4fb80d6e063
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 13:06:20 2021 +0800
    | 
    |     添加了Git教程
    | 
    * commit 3aa02a6914219ee706537bf4d4a0a3638b0fbeef
    | Author: hcp <389041637@qq.com>
    | Date:   Sat May 15 12:39:20 2021 +0800
    | 
    |     在README中添加了中文标题
    | 
    * commit 7a764a64a4300ca7d2fb695e27417a6e0a77d742
    | Author: 0x66CCFF <389041637@qq.com>
    | Date:   Tue Mar 16 00:27:13 2021 +0800
    | 
    |     Update README.md
    | 
    * commit b8f33986b6be8f1d480a05f2ea49307f3bdf421a
    | Author: 0x66CCFF <389041637@qq.com>
    | Date:   Tue Mar 16 00:20:48 2021 +0800
    | 
    |     Update README.md
    | 
    * commit 4843309abde773157b2dcb2f9827deb70e3fc995
    Author: 0x66CCFF <389041637@qq.com>
    Date:   Mon Mar 15 22:15:35 2021 +0800
    
        Initial commit
    (END)
    ```

- 查看差异
`git diff`
&nbsp;

    ```none
    diff --git "a/Git\346\225\231\347\250\213.md" "b/Git\346\225\231\347\250\213.md"
    index 90c97b9..e8f754b 100644
    --- "a/Git\346\225\231\347\250\213.md"
    +++ "b/Git\346\225\231\347\250\213.md"
    @@ -177,3 +177,11 @@
            Initial commit
        (END)
        ```
    +
    +- 查看差异
    +`git diff`
    +&nbsp;
    +
    +    ```none
    +    ;
    +    ```
    (END)
    ```
