<pre align="center"><b>AI that learns your <i>rock, paper, scissors</i> play style</b></pre>

![Python](https://img.shields.io/badge/made_with-Python-blue)

<br>

<img src="./img/img1.png" alt="img1" width="49%"> <img src="./img/img2.png" alt="img2" width="49%">

---

<br>

This app uses simple **pattern recognition**.

Due to the algorithm's complexity being approximately $O(n^3)$, the app doesn't search the entire game history for patterns.

The exact numbers are located in the [data.json](data.json) file.

_Example file:_

```json
{
    "memory": 250,
    "pattern": 50,
    "exponent": 2.0
}
```

- `memory` is the number of last moves the app searches through.
- `pattern` is the length of the longest pattern that will be searched for.
- `exponent` determines how much longer patterns are preferred over shorter ones.

The formula for the weight of a pattern is $w = len^{exp}$. If the value is set to $1.0$, the weight will scale linearly, meaning a pattern of length $2$ will be equivalent to two patterns of length $1$.
