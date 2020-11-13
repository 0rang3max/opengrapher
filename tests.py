# encoding: utf-8

import mock
import unittest
from collections import namedtuple
from opengrapher import parse


TEST_DATA = {
    'url': 'https://www.imdb.com/title/tt0110912',
    'title': 'Pulp Fiction (1994) - IMDb',
    'type': 'video.movie',
    'image': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY1200_CR97,0,630,1200_AL_.jpg',
    'description': '''
        Directed by Quentin Tarantino.  With John Travolta, Uma Thurman,
        Samuel L. Jackson, Bruce Willis. The lives of two mob hitmen,
        a boxer, a gangster and his wife, and a pair of diner bandits
        intertwine in four tales of violence and redemption.
    ''',
}

HTML = '''
    <html xmlns:og="http://ogp.me/ns#">
    <head>
    <title>{title}</title>
    <meta property="og:title" content="{title}" />
    <meta property="og:type" content="{type}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:image" content="{image}" />
    <meta property="og:description" content="{description}" />
    </head>
    </html>
'''.format(
    **TEST_DATA
)


def mock_requests_side_effect(*args, **kwargs):
    Response = namedtuple('Response', ['ok', 'content'])
    return Response(ok=True, content=HTML)


class test(unittest.TestCase):
    @mock.patch('requests.get', mock_requests_side_effect)
    def test_url(self):
        self.maxDiff = None
        self.assertEqual(parse(TEST_DATA['url']), TEST_DATA)


unittest.main()
