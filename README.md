# rulegolfer
A Python script based on [qfind](https://github.com/Matthias-Merzenich/qfind) for finding spaceship-friendly rules.

## Usage

There are a few "config variables" near the beginning of `search.py`.

Replace `speeds` with your favorite list of speeds (a Python list where each element is of format `(period, displacement, width)`)

Replace `forbidden_trans`with your list of least favorite transitions -- the script will be forbidden for toggling those transitions.

**Most importantly**, replace `qfind_path` with the path of the qfind executable on your computer.

After started, `search.py` will wait for one line of input; if you give it a rule, it will start golfing from that rule. Else it will choose a random one. 
