import requests

# 项目列表
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
    
    # 静态站点生成器（36项）
    "vercel/next.js",
    "gatsbyjs/gatsby",
    "gohugoio/hugo",
    "facebook/docusaurus",
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
    "google/docsy",
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

# 获取项目的fork和star数
def get_project_data(project):
    response = requests.get(api_url + project)
    data = response.json()
    return {
        "name": project,
        "forks": data.get("forks_count", 0),
        "stars": data.get("stargazers_count", 0)
    }

# 获取所有项目的数据
project_data = [get_project_data(project) for project in projects]

# 按照fork和star数排序
sorted_projects = sorted(project_data, key=lambda x: (x["forks"], x["stars"]), reverse=True)

# 保存结果到文件
with open("output.txt", "w") as f:
    for project in sorted_projects:
        f.write(f"{project['name']} - Forks: {project['forks']}, Stars: {project['stars']}\n")
