
def sanitize_header(site):
    return site.replace('- ', '').strip()


def _strip_bad_chars(val):
    for bad in ["'", '"']:
        if bad in val:
            val = val.replace(bad, '')
    return val


def parse_row(row):
    parts = row.split('::')
    path, selector = parts[0].split(' ', 1)
    action, expected = parts[1].split(' ', 1)
    expected = _strip_bad_chars(expected)
    # strip out extra spaces
    expected = ' '.join([f for f in expected.split(' ') if f])
    return (path.strip(), selector.strip(), action.strip(), expected.strip())


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
    out['tests'] = []
    rows = [parse_row(r) for r in data if r.startswith('/')]
    for row in rows:
        path = row[0]
        expression = row[1]
        action = row[2]
        value = row[3]
        out['tests'].append((path, expression, action, value))

    return out


def parse(src):
    return process(load(src))
