# UberEgg

Uber-egg (egg with dependencies) builder.

Uber-egg contains both the package and all its dependencies in one single egg
file. It is python equivalent of java uber-jar aka fat-jar.

## install
```
pip install git+https://github.com/liquanchen9/uberegg.git
```

## Usage

```
python setup.py bdist_uberegg -r requirements.txt
```

See command help for other options.
