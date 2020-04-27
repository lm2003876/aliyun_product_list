# aliyun_product_list
## 背景介绍
因需要关注阿里云上新产品的动态。因此爬取了控制台上产品列表里的产品。工具使用python3+selenium。

## 功能
1. 爬取阿里云主账号控制台上的产品，将其写入csv文件，通过get_products_with_rootuser.py实现。
2. 对比两个csv文件的差异，找出新上产品或者原产品名字变动，通过diff_files.py实现。

## 用法
1. 因阿里系的反爬机制，浏览器驱动需要使用**此处**上传的chromedriver.exe, 适用于Chrome 76。
2. Chrome文件夹中是可以正常使用的Chrome 76.0.3809.132浏览器，使用时可通过76.0.3809.132_chrome64_stable_windows_installer.exe安装；若无法安装成功，可以直接使用Chrome/Chrome-bin文件夹中的chrome.exe（推荐此种做法），如：在脚本中设置options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"。
3. 本脚本是爬取的主账号里的产品列表，在使用前请准备**阿里云主账号**。(请注意保管主账号信息，一旦泄漏可能造成严重损失)

## 其它
欢迎来探讨指教，WeiXin: liman_yi