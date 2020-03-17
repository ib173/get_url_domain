def parse_url(url):
    url_domain = get_url_domain(url)
    p_dex = url.rindex('.')
    post_fix = url[p_dex:]
    image_type = post_fix
    return url_domain, image_type

def get_url_domain(url):
    DOMAIN_POSTFIXES = [
        '.com',
        '.org',
        '.edu',
        '.net',
        '.ae'
        '.ru'
        '.at',
        '.sq',
        '.es'
        '.menu'
        '.site'
    ]
    domain = url.split('://')[1]

    if 'www.' in domain:
        domain = domain.split('www.')[1]
    else:
        domain = domain

    for postfix in DOMAIN_POSTFIXES:
        if postfix in domain:
            domain = (domain.split(postfix)[0])
    return domain
