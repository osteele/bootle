# Bootle: Half-Index Lists for Python

“Should array indices start at 0 or 1? My compromise of 0.5 was rejected
without, I thought, proper consideration.” -- Stan Kelly-Bootle

## Installation

```bash
pip3 install bootle
```

## Usage

```python
from bootle import List

xs = List([1, 2, 3])
assert xs[0.5] == 1
assert xs[:1.5] == [1]
xs[1.5] == 2
assert xs.index(2) == 1.5
```

## References

* ["Why numbering should start at zero"](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html), Edsger W. Dijkstra, 1982
* [Why Numbering Should Start At Zero](http://wiki.c2.com/?WhyNumberingShouldStartAtZero), WikiWikiWeb
* [Why Numbering Should Start At One](http://wiki.c2.com/?WhyNumberingShouldStartAtOne),  WikiWikiWeb
* [Zero-based numbering](https://en.wikipedia.org/wiki/Zero-based_numbering), Wikipedia

## License

WTFPL
