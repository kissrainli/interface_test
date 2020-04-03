# kangaroo_class

## 使用须知
### 目录介绍
- achives：存放从charles中导出的har包
- testcase：存放api的测试用例yml文件
### 使用步骤
- 使用charles抓包：
  - 检查手机和电脑的网路是否处于一个局域网内
  - 手机证书是否安装，是否授权
  - 首次抓包，电脑上会弹出是否允许代理的确认弹窗，请选择Allow
  - 过滤api：filter -> api-test.100daishu.com -> focus
- 导出har包：
  - 右键选择export导出，文件类型选择http achive（har）
  - 存放到项目工程下的achives目录下（可以自己决定，不是必要的）
- 生成用例：
  - 进入终端，切换到achives目录下
  - 执行命令：``har2case xxx.har -2y``(导出的har包) -> xxx.yml(生成的测试用例)
- 修改用例：
  - 打开"xxx.yml(生成的测试用例)"
  - 在request标签下方添加需要动态引用的参数
  ```
  extract:
        token: content.data.token
        user_id: content.data.userId
  ```
  - 在后续的api中使用进行引用变量
  ```
  $token
  $user_id
  ```
- 执行用例
  - 关闭charles对电脑的代理，否则会报错ssl证书问题（切记，切记，切记！！！）
  - 不关闭charles的情况下，测试用例中``config``下增加``verify: False``即可；
  - 进入终端执行命令：``hrun xxx.yml``(注意用例所在文件路径)
  - 查看reports目录下的测试报告

## 测试用例分层
### 接口管理
- api目录下为单个接口的用例
- testcases目录下根据api目录下的单个接口组装符合测试场景的测试用例
- .env文件为测试数据的临时环境变量管理，shell关闭后会自动重置，加载测试用例时会自动设置
```shell
# 执行测试用例命令，在interface_test工程下
直接执行   ./run.sh test    (.env-test)   OR   ./run.sh  具体看参数方式


舍弃
$ hrun testcases/test_teacher.yml --dot-env-path .env --log-level debug
```