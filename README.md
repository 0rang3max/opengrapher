## Opengrapher

##### utility for parsing the Open Graph tags from url

_(read more about the specification at http://ogp.me/)_

#### Installation

```bash
   $ pip install opengrapher
```

#### Usage

```python

   >>> import opengrapher
   >>> opengrapher.parse('https://www.imdb.com/title/tt0110912')
   {
      "url": "https://www.imdb.com/title/tt0110912",
      "title": "Pulp Fiction (1994) - IMDb",
      "type": "video.movie",
      "image": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
      "description": """
         Directed by Quentin Tarantino.  With John Travolta, Uma Thurman, 
         Samuel L. Jackson, Bruce Willis. The lives of two mob hitmen, 
         a boxer, a gangster and his wife, and a pair of diner bandits 
         intertwine in four tales of violence and redemption.
      """,
   }
```

---

List of parsing tags is stored in PARSE_TAGS constant
```python

   >>> from opengrapher import PARSE_TAGS
   >>> PARSE_TAGS
   ["url", "title", "type", "image", "description"]
```

You can pass a specific list of tags to `parse` function if you want:
```python

   >>> import opengrapher
   >>> custom_tags = ['url', 'title']
   >>> opengrapher.parse('https://www.imdb.com/title/tt0110912', parse_tags=custom_tags)
   {
      "url": "https://www.imdb.com/title/tt0110912",
      "title": "Pulp Fiction (1994) - IMDb",
   }
```

> Note that all tags will be transformed to "og:{tag}" format, as it stated in opengraph notation
