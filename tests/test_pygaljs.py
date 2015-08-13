import pygaljs


def test_it_works():
    p = pygaljs.path('2.0.x', 'pygal-tooltips.js')
    print(p)
    assert 'function()' in open(p).read()
    print(pygaljs.uri('2.0.x', 'pygal-tooltips.js'))