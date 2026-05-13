# GitHub Pages 部署方式

这个页面可以用 GitHub Pages 部署，但数据接口要换成 Google Apps Script。

## 1. 创建 Apps Script 接口

1. 打开 `script.google.com`，新建项目。
2. 把 `google-apps-script.js` 里的代码复制进去。
3. 保存后点击“部署” -> “新建部署”。
4. 类型选择“Web 应用”。
5. 执行身份选择“我”。
6. 访问权限选择“任何人”或“知道链接的任何人”。
7. 部署后复制 Web App URL。

## 2. 填入前端接口地址

打开 `index.html`，找到：

```js
const APPS_SCRIPT_URL = "";
```

把空字符串替换成你的 Web App URL，例如：

```js
const APPS_SCRIPT_URL = "https://script.google.com/macros/s/xxxxx/exec";
```

## 3. 上传到 GitHub

把 `sheet_monitor` 目录里的这些文件上传到仓库：

- `index.html`
- `vendor/three.module.min.js`
- `google-apps-script.js`
- `README_DEPLOY_GITHUB_PAGES.md`

`server.py` 只用于本地测试，GitHub Pages 不需要它。

## 4. 开启 GitHub Pages

1. 进入 GitHub 仓库 Settings。
2. 找到 Pages。
3. Source 选择 `Deploy from a branch`。
4. 选择你的分支和目录。
5. 等待 GitHub 给出 Pages 地址。
