import requests

# 项目列表（完整未省略）
projects = [
    # 全栈框架集成（16项）
    "strapi/strapi",
    "TryGhost/Ghost",
    "directus/directus",
    "payloadcms/payload",
    "odoo/odoo",
    "wagtail/wagtail",
    "netlify/netlify-cms",
    "django-cms/django-cms",
    "keystonejs/keystone",
    "VulcanJS/Vulcan",
    "refinery/refinerycms",
    "tinacms/tinacms",
    "apostrophecms/apostrophe",
    "silverstripe/silverstripe-cms",
    "sulu/sulu",
    "plone/Products.CMFPlone",
    
    # 静态站点生成器（36项）修正路径
    "vercel/next.js",
    "gatsbyjs/gatsby",
    "gohugoio/hugo",
    "facebook/docusaurus",  # 修正路径
    "nuxt/nuxt.js",
    "vuejs/vuepress",
    "hexojs/hexo",
    "jekyll/jekyll",
    "GitbookIO/gitbook",
    "slatedocs/slate",
    "sveltejs/kit",
    "11ty/eleventy",
    "redwoodjs/redwood",
    "gridsome/gridsome",
    "withastro/astro",
    "getpelican/pelican",
    "blitz-js/blitz",
    "middleman/middleman",
    "getgrav/grav",
    "getzola/zola",
    "mkdocs/mkdocs",
    "brunch/brunch",
    "metalsmith/metalsmith",
    "lektor/lektor",
    "saberland/saber",
    "jnordberg/wintersmith",
    "assemble/assemble",
    "jaspervdj/hakyll",
    "getnikola/nikola",
    "MoOx/phenomic",
    "eudicots/Cactus",
    "GetPublii/Publii",
    "cobalt-org/cobalt.rs",
    "google/docsy",        # 修正路径
    "mbutterick/pollen",
    "scullyio/scully",
    
    # 无头电商平台（3项）
    "saleor/saleor",
    "spree/spree",
    "reactioncommerce/reaction",
    
    # 内容协作平台（4项）
    "pocketbase/pocketbase",
    "decaporg/decap-cms",
    "sanity-io/sanity",
    "payloadcms/cloud",
    
    # Kubernetes集成方案（5项）
    "webiny/webiny-js",
    "ponzu-cms/ponzu",
    "qor/qor",
    "stephenmcd/mezzanine",
    "getzola/zola-operator",
    
    # Python生态扩展（3项）
    "getpelican/pelican",
    "rochacbruno/quokka",
    "feincms/feincms",
    
    # 其他技术栈（9项）
    "appwrite/appwrite",
    "supabase/supabase",
    "craftcms/cms",
    "locomotivecms/engine",
    "amplication/amplication",
    "nhost/nhost",
    "owen2345/camaleon-cms",
    "bolt/core",
    "AlchemyCMS/alchemy_cms",
    
    # 新兴技术方案（12项）
    "tinacms/tinacms",
    "fiction-com/factor",
    "nocobase/nocobase",
    "flextype/flextype",
    "redaxscript/redaxscript",
    "worona/worona",
    "plentico/plenti",
    "strapi/cloud",
    "overhangio/still",
    "cabal-club/cabal",
    "payloadcms/templates",
    "Kotti/Kotti",
    
    # 扩展方案（15项）
    "forestryio/forestry",
    "agentejo/cockpit",
    "strapi/strapi-starter",
    "GraphCMS/graphcms",
    "ButterCMS/buttercms",
    "contentful/contentful-cli",
    "Kentico/kontent",
    "prismicio/prismic",
    "cosmicjs/cosmic",
    "datocms/js-datocms",
    "storyblok/storyblok",
    "contentstack/contentstack",
    "agility/agilitycms",
    "prepr/prepr",
    "magnolia-cms/magnolia"
]

# GitHub API URL
api_url = "https://api.github.com/repos/"

# 获取项目数据（新增url字段）
def get_project_data(project):
    response = requests.get(api_url + project)
    data = response.json()
    return {
        "name": data.get("name", project.split("/")[-1]),  # 获取仓库显示名称
        "url": data.get("html_url", f"https://github.com/{project}"),  # GitHub地址
        "forks": data.get("forks_count", 0),
        "stars": data.get("stargazers_count", 0)
    }

# 获取并处理数据
project_data = [get_project_data(project) for project in projects]

# 按stars和forks排序
sorted_projects = sorted(
    project_data,
    key=lambda x: (-x["stars"], -x["forks"])
)

# 生成Markdown格式报告
with open("output.md", "w", encoding="utf-8") as f:
    f.write("# GitHub CMS 项目统计（103项）\n\n")
    
    # 项目列表（完整输出）
    for idx, project in enumerate(sorted_projects, 1):
        stars = project['stars']
        stars_str = f"{stars/1000:.1f}k".replace(".0k", "k") if stars >= 1000 else str(stars)
        
        f.write(
            f"{idx}. **{project['name']}**  \n"
            f"   GitHub: [{project['url']}]({project['url']})  \n"
            f"   ⭐{stars_str} | 🍴{project['forks']}\n\n"
        )
    
    # 技术栈分布表（完整保留）
    f.write("""## 技术栈分布
| 分类                | 项目数 | 技术特性概要                  |
|---------------------|--------|-----------------------------|
| 全栈框架集成        | 16     | 企业级/框架深度集成           |
| 静态站点生成器      | 36     | 文档/博客/高性能生成          |
| 无头电商平台        | 3      | 电商API/订单管理             |
| 内容协作平台        | 4      | 团队协作/版本控制            |
| Kubernetes集成方案  | 5      | 云原生部署优化               |
| Python生态扩展      | 3      | Django生态扩展              |
| 其他技术栈          | 9      | 多语言支持                  |
| 新兴技术方案        | 12     | 低代码/可视化               |
| 扩展方案            | 15     | 企业扩展/工作流优化          |
| **总计**            | 103    | -                          |""")
