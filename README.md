### oc-chessmanager

## Install ChessManager

# Clone this repository
```
git clone https://github.com/jogubo/oc-chessmanager.git
cd oc-chessmanager
```

# Create and activate python virtualenv
```
python -m venv .venv
source .venv/bin/activate
```

#Install dependencies
```
pip install -r requirements.txt
```

##  Run ChessManager
Launch this command:
```
python chessmanager/main.py
```
Then follow the instructions of the program

## Flake8
# View report
The report  is available via  an html file:
flake-report/index.html

# Generate new flake8 report
```
flake8 --format=html --htmldir=flake-report
```
