﻿#### ForShop
a shop
运行：
该代码在编译器中编写，最后实时编译后在微信开发工具上看效果
* 使用了wepy
* 先全局安装wepy    npm install wepy-cli -g
* 安装依赖    npm install
* 开启实时编译  wepy build --watch
* 在微信开发者工具上打开dist文件，即可实时看效果

样式：
 建议使用less，建议定义全局使用的主色调变量，方便之后修改全局色调风格
 公用样式放在styles文件里
 
 目录
    src
      api
         api.js //接口地址
      components
         common  //公用组件
      images 
         //整个项目需要使用的图片
      pages//页面
      utils//公共函数
        tip.js//弹出框
        util.js//数的处理
        wxRequest.js//请求封装
      app.wpy

图标库
http://www.iconfont.cn/collections/detail?spm=a313x.7781069.0.da5a778a4&cid=1312
http://www.iconfont.cn/collections/detail?spm=a313x.7781069.0.da5a778a4&cid=4513
