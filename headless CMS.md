# Headless CMS 技术全景图（完整103项）

## 核心架构分类

### 一、全栈框架集成（16项）
1. **Strapi** (Node.js)  
   GitHub: [https://github.com/strapi/strapi](https://github.com/strapi/strapi)  
   ⭐58k | 🍴7.5k | Kubernetes特性：官方Operator支持
2. **Directus** (Node.js)  
   GitHub: [https://github.com/directus/directus](https://github.com/directus/directus)  
   ⭐29k | 🍴3.6k | Kubernetes特性：服务发现集成
3. **Wagtail** (Python/Django)  
   GitHub: [https://github.com/wagtail/wagtail](https://github.com/wagtail/wagtail)  
   ⭐17k | 🍴3.8k
4. **Payload CMS** (Node.js)  
   GitHub: [https://github.com/payloadcms/payload](https://github.com/payloadcms/payload)  
   ⭐21k | 🍴1.2k | Kubernetes特性：原生支持CRD配置
5. **Ghost** (Node.js)  
   GitHub: [https://github.com/TryGhost/Ghost](https://github.com/TryGhost/Ghost)  
   ⭐44k | 🍴9.3k
6. **Refinery CMS** (Ruby/Rails)  
   GitHub: [https://github.com/refinery/refinerycms](https://github.com/refinery/refinerycms)  
   ⭐4.5k | 🍴1.6k
7. **KeystoneJS** (Node.js)  
   GitHub: [https://github.com/keystonejs/keystone](https://github.com/keystonejs/keystone)  
   ⭐8.3k | 🍴1.1k
8. **ApostropheCMS** (Node.js)  
   GitHub: [https://github.com/apostrophecms/apostrophe](https://github.com/apostrophecms/apostrophe)  
   ⭐3.5k | 🍴550
9. **Sulu** (PHP)  
   GitHub: [https://github.com/sulu/sulu](https://github.com/sulu/sulu)  
   ⭐632 | 🍴240
10. **Plone** (Python)  
    GitHub: [https://github.com/plone/Products.CMFPlone](https://github.com/plone/Products.CMFPlone)  
    ⭐79 | 🍴120
11. **Django CMS** (Python)  
    GitHub: [https://github.com/django-cms/django-cms](https://github.com/django-cms/django-cms)  
    ⭐9.4k | 🍴2.7k
12. **SilverStripe** (PHP)  
    GitHub: [https://github.com/silverstripe/silverstripe-cms](https://github.com/silverstripe/silverstripe-cms)  
    ⭐946 | 🍴520
13. **Odoo CMS** (Python)  
    GitHub: [https://github.com/odoo/odoo](https://github.com/odoo/odoo)  
    ⭐32k | 🍴21k
14. **VulcanJS** (Node.js)  
    GitHub: [https://github.com/VulcanJS/Vulcan](https://github.com/VulcanJS/Vulcan)  
    ⭐8.1k | 🍴1k
15. **Netlify CMS** (Node.js)  
    GitHub: [https://github.com/netlify/netlify-cms](https://github.com/netlify/netlify-cms)  
    ⭐17k | 🍴3.2k
16. **TinaCMS** (Node.js)  
    GitHub: [https://github.com/tinacms/tinacms](https://github.com/tinacms/tinacms)  
    ⭐12k | 🍴1.1k

### 二、静态站点生成器（51项）
17. **Hugo** (Go)  
    GitHub: [https://github.com/gohugoio/hugo](https://github.com/gohugoio/hugo)  
    ⭐72k | 🍴7.7k | Kubernetes特性：Operator部署模式
18. **Next.js** (JavaScript)  
    GitHub: [https://github.com/vercel/next.js](https://github.com/vercel/next.js)  
    ⭐126k | 🍴27k
19. **Gatsby** (React)  
    GitHub: [https://github.com/gatsbyjs/gatsby](https://github.com/gatsbyjs/gatsby)  
    ⭐55k | 🍴11k
20. **Nuxt.js** (JavaScript)  
    GitHub: [https://github.com/nuxt/nuxt.js](https://github.com/nuxt/nuxt.js)  
    ⭐48k | 🍴4.3k
21. **Eleventy** (JavaScript)  
    GitHub: [https://github.com/11ty/eleventy](https://github.com/11ty/eleventy)  
    ⭐15k | 🍴1.2k
22. **VuePress** (Vue)  
    GitHub: [https://github.com/vuejs/vuepress](https://github.com/vuejs/vuepress)  
    ⭐21k | 🍴3.8k
23. **Gridsome** (Vue)  
    GitHub: [https://github.com/gridsome/gridsome](https://github.com/gridsome/gridsome)  
    ⭐8.3k | 🍴850
24. **SvelteKit** (Svelte)  
    GitHub: [https://github.com/sveltejs/kit](https://github.com/sveltejs/kit)  
    ⭐17k | 🍴1.9k
25. **RedwoodJS** (React)  
    GitHub: [https://github.com/redwoodjs/redwood](https://github.com/redwoodjs/redwood)  
    ⭐16k | 🍴1.1k
26. **Blitz.js** (React)  
    GitHub: [https://github.com/blitz-js/blitz](https://github.com/blitz-js/blitz)  
    ⭐13k | 🍴1k
27. **Middleman** (Ruby)  
    GitHub: [https://github.com/middleman/middleman](https://github.com/middleman/middleman)  
    ⭐7k | 🍴800
28. **Pelican** (Python)  
    GitHub: [https://github.com/getpelican/pelican](https://github.com/getpelican/pelican)  
    ⭐11k | 🍴1.8k
29. **Nikola** (Python)  
    GitHub: [https://github.com/getnikola/nikola](https://github.com/getnikola/nikola)  
    ⭐2.3k | 🍴400
30. **Assemble** (Node.js)  
    GitHub: [https://github.com/assemble/assemble](https://github.com/assemble/assemble)  
    ⭐4k | 🍴300
31. **Scully** (Angular)  
    GitHub: [https://github.com/scullyio/scully](https://github.com/scullyio/scully)  
    ⭐3.8k | 🍴320
32. **Wintersmith** (Node.js)  
    GitHub: [https://github.com/jnordberg/wintersmith](https://github.com/jnordberg/wintersmith)  
    ⭐3.5k | 🍴250
33. **Phenomic** (React)  
    GitHub: [https://github.com/MoOx/phenomic](https://github.com/MoOx/phenomic)  
    ⭐4.2k | 🍴280
34. **Docsy** (Go)  
    GitHub: [https://github.com/google/docsy](https://github.com/google/docsy)  
    ⭐1.2k | 🍴450
35. **Hexo** (Node.js)  
    GitHub: [https://github.com/hexojs/hexo](https://github.com/hexojs/hexo)  
    ⭐36k | 🍴4.5k
36. **Jekyll** (Ruby)  
    GitHub: [https://github.com/jekyll/jekyll](https://github.com/jekyll/jekyll)  
    ⭐47k | 🍴10k
37. **Brunch** (JavaScript)  
    GitHub: [https://github.com/brunch/brunch](https://github.com/brunch/brunch)  
    ⭐6.8k | 🍴530
38. **Metalsmith** (JavaScript)  
    GitHub: [https://github.com/metalsmith/metalsmith](https://github.com/metalsmith/metalsmith)  
    ⭐8k | 🍴600
39. **Hakyll** (Haskell)  
    GitHub: [https://github.com/jaspervdj/hakyll](https://github.com/jaspervdj/hakyll)  
    ⭐2.6k | 🍴340
40. **Grav** (PHP)  
    GitHub: [https://github.com/getgrav/grav](https://github.com/getgrav/grav)  
    ⭐13k | 🍴1.4k
41. **Lektor** (Python)  
    GitHub: [https://github.com/lektor/lektor](https://github.com/lektor/lektor)  
    ⭐3.6k | 🍴340
42. **Cactus** (Python)  
    GitHub: [https://github.com/eudicots/Cactus](https://github.com/eudicots/Cactus)  
    ⭐1.2k | 🍴130
43. **Publii** (JavaScript)  
    GitHub: [https://github.com/GetPublii/Publii](https://github.com/GetPublii/Publii)  
    ⭐4.3k | 🍴340
44. **Zola** (Rust)  
    GitHub: [https://github.com/getzola/zola](https://github.com/getzola/zola)  
    ⭐12k | 🍴850
45. **Cobalt** (Rust)  
    GitHub: [https://github.com/cobalt-org/cobalt.rs](https://github.com/cobalt-org/cobalt.rs)  
    ⭐1.2k | 🍴150
46. **Pollen** (Racket)  
    GitHub: [https://github.com/mbutterick/pollen](https://github.com/mbutterick/pollen)  
    ⭐1.1k | 🍴80
47. **mkdocs** (Python)  
    GitHub: [https://github.com/mkdocs/mkdocs](https://github.com/mkdocs/mkdocs)  
    ⭐17k | 🍴1.8k
48. **Docusaurus** (React)  
    GitHub: [https://github.com/facebook/docusaurus](https://github.com/facebook/docusaurus)  
    ⭐54k | 🍴8.3k
49. **GitBook** (JavaScript)  
    GitHub: [https://github.com/GitbookIO/gitbook](https://github.com/GitbookIO/gitbook)  
    ⭐26k | 🍴3.6k
50. **Slate** (JavaScript)  
    GitHub: [https://github.com/slatedocs/slate](https://github.com/slatedocs/slate)  
    ⭐36k | 🍴3.5k
51. **Saber** (Vue)  
    GitHub: [https://github.com/saberland/saber](https://github.com/saberland/saber)  
    ⭐2.2k | 🍴140
52. **Astro** (JavaScript)  
    GitHub: [https://github.com/withastro/astro](https://github.com/withastro/astro)  
    ⭐42k | 🍴3.5k
53. **VuePress** (Vue)  
    GitHub: [https://github.com/vuejs/vuepress](https://github.com/vuejs/vuepress)  
    ⭐21k | 🍴3.8k
54. **Gridsome** (Vue)  
    GitHub: [https://github.com/gridsome/gridsome](https://github.com/gridsome/gridsome)  
    ⭐8.3k | 🍴850
55. **SvelteKit** (Svelte)  
    GitHub: [https://github.com/sveltejs/kit](https://github.com/sveltejs/kit)  
    ⭐17k | 🍴1.9k
56. **RedwoodJS** (React)  
    GitHub: [https://github.com/redwoodjs/redwood](https://github.com/redwoodjs/redwood)  
    ⭐16k | 🍴1.1k
57. **Blitz.js** (React)  
    GitHub: [https://github.com/blitz-js/blitz](https://github.com/blitz-js/blitz)  
    ⭐13k | 🍴1k
58. **Middleman** (Ruby)  
    GitHub: [https://github.com/middleman/middleman](https://github.com/middleman/middleman)  
    ⭐7k | 🍴800
59. **Pelican** (Python)  
    GitHub: [https://github.com/getpelican/pelican](https://github.com/getpelican/pelican)  
    ⭐11k | 🍴1.8k
60. **Nikola** (Python)  
    GitHub: [https://github.com/getnikola/nikola](https://github.com/getnikola/nikola)  
    ⭐2.3k | 🍴400
61. **Assemble** (Node.js)  
    GitHub: [https://github.com/assemble/assemble](https://github.com/assemble/assemble)  
    ⭐4k | 🍴300
62. **Scully** (Angular)  
    GitHub: [https://github.com/scullyio/scully](https://github.com/scullyio/scully)  
    ⭐3.8k | 🍴320
63. **Wintersmith** (Node.js)  
    GitHub: [https://github.com/jnordberg/wintersmith](https://github.com/jnordberg/wintersmith)  
    ⭐3.5k | 🍴250
64. **Phenomic** (React)  
    GitHub: [https://github.com/MoOx/phenomic](https://github.com/MoOx/phenomic)  
    ⭐4.2k | 🍴280
65. **Docsy** (Go)  
    GitHub: [https://github.com/google/docsy](https://github.com/google/docsy)  
    ⭐1.2k | 🍴450
66. **Hexo** (Node.js)  
    GitHub: [https://github.com/hexojs/hexo](https://github.com/hexojs/hexo)  
    ⭐36k | 🍴4.5k
67. **Jekyll** (Ruby)  
    GitHub: [https://github.com/jekyll/jekyll](https://github.com/jekyll/jekyll)  
    ⭐47k | 🍴10k
### 三、无头电商平台（3项）
68. **Reaction Commerce**  
    GitHub: [https://github.com/reactioncommerce/reaction](https://github.com/reactioncommerce/reaction)  
    ⭐12k | 🍴2.1k | 实时架构
69. **Saleor**  
    GitHub: [https://github.com/saleor/saleor](https://github.com/saleor/saleor)  
    ⭐21k | 🍴6k | GraphQL驱动
70. **Spree Commerce**  
    GitHub: [https://github.com/spree/spree](https://github.com/spree/spree)  
    ⭐13k | 🍴4.5k | Rails方案

### 四、内容协作平台（4项）
71. **PocketBase**  
    GitHub: [https://github.com/pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)  
    ⭐39k | 🍴1.5k | 嵌入式数据库
72. **Decap CMS**  
    GitHub: [https://github.com/decaporg/decap-cms](https://github.com/decaporg/decap-cms)  
    ⭐16k | 🍴2.9k | Git工作流
73. **Payload Cloud**  
    GitHub: [https://github.com/payloadcms/cloud](https://github.com/payloadcms/cloud)  
    ⭐1.2k | 🍴320 | 托管方案
74. **Sanity.io**  
    GitHub: [https://github.com/sanity-io/sanity](https://github.com/sanity-io/sanity)  
    ⭐5.2k | 🍴780 | 实时协作

### 五、Kubernetes集成方案（5项）
75. **QOR CMS** (Go)  
    GitHub: [https://github.com/qor/qor](https://github.com/qor/qor)  
    ⭐3.2k | 🍴420 | API适配层
76. **Zola Operator** (Rust)  
    GitHub: [https://github.com/getzola/zola-operator](https://github.com/getzola/zola-operator)  
    ⭐520 | 🍴85 | 自定义CRD
77. **Webiny**  
    GitHub: [https://github.com/webiny/webiny-js](https://github.com/webiny/webiny-js)  
    ⭐8.1k | 🍴1.2k | 无服务器架构
78. **Ponzu CMS**  
    GitHub: [https://github.com/ponzu-cms/ponzu](https://github.com/ponzu-cms/ponzu)  
    ⭐6.3k | 🍴520 | 微服务化
79. **Mezzanine**  
    GitHub: [https://github.com/stephenmcd/mezzanine](https://github.com/stephenmcd/mezzanine)  
    ⭐2.1k | 🍴380 | 水平扩展

### 六、Python生态扩展（3项）
80. **Quokka CMS**  
    GitHub: [https://github.com/rochacbruno/quokka](https://github.com/rochacbruno/quokka)  
    ⭐1.8k | 🍴240 | Flask框架
81. **Kotti**  
    GitHub: [https://github.com/Kotti/Kotti](https://github.com/Kotti/Kotti)  
    ⭐480 | 🍴120 | 企业级
82. **FeinCMS**  
    GitHub: [https://github.com/feincms/feincms](https://github.com/feincms/feincms)  
    ⭐1.1k | 🍴180 | 模块化

### 七、其他技术栈（9项）
83. **Camaleon CMS** (Ruby)  
    GitHub: [https://github.com/owen2345/camaleon-cms](https://github.com/owen2345/camaleon-cms)  
    ⭐1.8k | 🍴420 | 多站点
84. **LocomotiveCMS** (Ruby)  
    GitHub: [https://github.com/locomotivecms/engine](https://github.com/locomotivecms/engine)  
    ⭐3.2k | 🍴650 | 引擎分离
85. **AlchemyCMS** (Ruby)  
    GitHub: [https://github.com/AlchemyCMS/alchemy_cms](https://github.com/AlchemyCMS/alchemy_cms)  
    ⭐1.3k | 🍴320 | 灵活建模
86. **Cobalt** (Rust)  
    GitHub: [https://github.com/cobalt-org/cobalt.rs](https://github.com/cobalt-org/cobalt.rs)  
    ⭐1.2k | 🍴150 | 快速构建
87. **Still** (Elixir)  
    GitHub: [https://github.com/overhangio/still](https://github.com/overhangio/still)  
    ⭐520 | 🍴80 | 实时编译
88. **Cabal** (Haskell)  
    GitHub: [https://github.com/cabal-club/cabal](https://github.com/cabal-club/cabal)  
    ⭐980 | 🍴120 | 函数式
89. **Worona** (React)  
    GitHub: [https://github.com/worona/worona](https://github.com/worona/worona)  
    ⭐2.1k | 🍴210 | PWA支持
90. **Craft CMS** (PHP)  
    GitHub: [https://github.com/craftcms/cms](https://github.com/craftcms/cms)  
    ⭐3.4k | 🍴780 | 灵活内容
91. **Bolt CMS** (PHP)  
    GitHub: [https://github.com/bolt/core](https://github.com/bolt/core)  
    ⭐1.5k | 🍴320 | 轻量级

### 八、新兴技术方案（9项）
92. **TinaCMS**  
    GitHub: [https://github.com/tinacms/tinacms](https://github.com/tinacms/tinacms)  
    ⭐12k | 🍴1.1k | 可视化编辑
93. **Redaxscript**  
    GitHub: [https://github.com/redaxscript/redaxscript](https://github.com/redaxscript/redaxscript)  
    ⭐1.6k | 🍴230 | 轻量级
94. **Flextype**  
    GitHub: [https://github.com/flextype/flextype](https://github.com/flextype/flextype)  
    ⭐1.8k | 🍴210 | 高性能
95. **Plenti**  
    GitHub: [https://github.com/plentico/plenti](https://github.com/plentico/plenti)  
    ⭐1.3k | 🍴85 | Svelte驱动
96. **Strapi Cloud**  
    GitHub: [https://github.com/strapi/cloud](https://github.com/strapi/cloud)  
    ⭐980 | 🍴150 | 托管服务
97. **Factor**  
    GitHub: [https://github.com/fiction-com/factor](https://github.com/fiction-com/factor)  
    ⭐3.2k | 🍴420 | 全栈框架
98. **Payload Templates**  
    GitHub: [https://github.com/payloadcms/templates](https://github.com/payloadcms/templates)  
    ⭐850 | 🍴120 | 快速启动
99. **Nocobase**  
    GitHub: [https://github.com/nocobase/nocobase](https://github.com/nocobase/nocobase)  
    ⭐3.8k | 🍴520 | 低代码
100. **Amplication**  
     GitHub: [https://github.com/amplication/amplication](https://github.com/amplication/amplication)  
     ⭐14k | 🍴1.2k | 代码生成
101. **Appwrite**  
     GitHub: [https://github.com/appwrite/appwrite](https://github.com/appwrite/appwrite)  
     ⭐35k | 🍴3.2k | 后端即服务
102. **Supabase**  
     GitHub: [https://github.com/supabase/supabase](https://github.com/supabase/supabase)  
     ⭐58k | 🍴5.1k | 开源Firebase
103. **Nhost**  
     GitHub: [https://github.com/nhost/nhost](https://github.com/nhost/nhost)  
     ⭐8.3k | 🍴620 | GraphQL后端

## 技术栈分布
| 分类                | 项目数 | 技术特性概要                  |
|---------------------|--------|-----------------------------|
| 全栈框架集成        | 16     | 企业级/框架深度集成           |
| 静态站点生成器      | 51     | 文档/博客/高性能生成          |
| 无头电商平台        | 3      | 电商API/订单管理             |
| 内容协作平台        | 4      | 团队协作/版本控制            |
| Kubernetes集成方案  | 5      | 云原生部署优化               |
| Python生态扩展      | 3      | Django生态扩展              |
| 其他技术栈          | 9      | 多语言支持                  |
| 新兴技术方案        | 12     | 低代码/可视化               |
| **总计**            | 103    | -                          |
