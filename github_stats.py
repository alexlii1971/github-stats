import requests

# 项目列表
projects = [
    "drupal/drupal",
    "joomla/joomla-cms",
    "octobercms/october",
    "getgrav/grav",
    "pyrocms/pyrocms",
    "bolt/bolt",
    "pagekit/pagekit",
    "microweber/microweber",
    "GetSimpleCMS/GetSimpleCMS",
    "textpattern/textpattern",
    "concrete5/concrete5",
    "agentejo/cockpit",
    "silverstripe/silverstripe-cms",
    "e107inc/e107",
    "modxcms/revolution",
    "sulu/sulu",
    "TYPO3/TYPO3.CMS",
    "contao/contao",
    "pimcore/pimcore",
    "cmsimple-org/cmsimple",
    "picocms/Pico",
    "pluck-cms/pluck",
    "daylerees/FUEL-CMS",
    "anchorcms/anchor-cms",
    "Chyrp/chyrp-lite",
    "symphonycms/symphony-2",
    "PhileCMS/Phile",
    "meso-cms/cmsmadesimple",
    "TypiCMS/TypiCMS",
    "tikiorg/tiki",
    "bludit/bludit",
    "robiso/wondercms",
    "TryGhost/Ghost",
    "strapi/strapi",
    "keystonejs/keystone",
    "apostrophecms/apostrophe",
    "payloadcms/payload",
    "netlify/netlify-cms",
    "directus/directus",
    "tinacms/tinacms",
    "hexojs/hexo",
    "docpad/docpad",
    "digitalcraftsman/calipso",
    "reactioncommerce/reaction",
    "meanjs/mean",
    "VulcanJS/Vulcan",
    "wagtail/wagtail",
    "django-cms/django-cms",
    "stephenmcd/mezzanine",
    "plone/Products.CMFPlone",
    "matthiask/feincms",
    "rochacbruno/quokka",
    "Kotti/Kotti",
    "lektor/lektor",
    "stephenmcd/cartridge",
    "Fantomas42/django-blog-zinnia",
    "refinery/refinerycms",
    "owen2345/camaleon-cms",
    "locomotivecms/engine",
    "radiant/radiant",
    "comfy/comfortable-mexican-sofa",
    "rails/spina",
    "AlchemyCMS/alchemy_cms",
    "jekyll/jekyll",
    "publify/publify",
    "typus/typus",
    "mwunsch/mephisto",
    "gohugoio/hugo",
    "GoCMS/GoCMS",
    "qor/qor",
    "beego/beego",
    "go-admin-team/go-admin",
    "getzola/zola",
    "cobalt-org/cobalt.rs",
    "overhangio/still",
    "bitwalker/ex_cms",
    "smpallen99/ex_admin",
    "alchemist-cms/alchemist",
    "gatsbyjs/gatsby",
    "vercel/next.js",
    "nuxt/nuxt.js",
    "11ty/eleventy",
    "vuejs/vuepress",
    "gridsome/gridsome",
    "sveltejs/kit",
    "redwoodjs/redwood",
    "blitz-js/blitz",
    "middleman/middleman",
    "getpelican/pelican",
    "getnikola/nikola",
    "assemble/assemble",
    "scullyio/scully",
    "jnordberg/wintersmith",
    "MoOx/phenomic",
    "google/docsy"
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
