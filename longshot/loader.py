
def sanitize_header(site):
    return site.replace('- ', '').strip()


def parse_row(row):
    bits = row.split()
    path = bits.pop(0)
    exp = bits.pop(0)
    rest = ' '.join(bits)
    for bad in ["'", '"']:
        if bad in rest:
            rest = rest.replace(bad, '')
    return (path, exp, ' '.join(rest.split()))


def load(src):
    raw = None
    with open(src, 'r') as data:
        raw = data.readlines()
    return raw


def process(data):
    first_row = data.pop(0)
    assert first_row.startswith('- '), "First row in file must be the site (- www.sitename.com)"  # noqa

    out = {}
    out['site'] = sanitize_header(first_row)  # should be the site
    out['tests'] = {}
    rows = [parse_row(r) for r in data]
    for row in rows:
        path = row[0]
        expression = row[1]
        value = row[2]
        if path not in out['tests']:
            out['tests'][path] = []
        out['tests'][path].append({
            'expression': expression,
            'value': value
            })

    return out


def parse(src):
    return process(load(src))
