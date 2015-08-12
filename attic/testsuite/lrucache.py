from attic.lrucache import LRUCache
from attic.testsuite import AtticTestCase


class LRUCacheTestCase(AtticTestCase):

    def test(self):
        c = LRUCache(2, dispose=lambda _: None)
        self.assert_equal(len(c), 0)
        for i, x in enumerate('abc'):
            c[x] = i
        self.assert_equal(len(c), 2)
        self.assert_equal(c.items(), set([('b', 1), ('c', 2)]))
        self.assert_equal(False, 'a' in c)
        self.assert_equal(True, 'b' in c)
        self.assert_raises(KeyError, lambda: c['a'])
        self.assert_equal(c['b'], 1)
        self.assert_equal(c['c'], 2)
        c['d'] = 3
        self.assert_equal(len(c), 2)
        self.assert_equal(c['c'], 2)
        self.assert_equal(c['d'], 3)
        del c['c']
        self.assert_equal(len(c), 1)
        self.assert_raises(KeyError, lambda: c['c'])
        self.assert_equal(c['d'], 3)
