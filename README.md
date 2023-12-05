# NewsFrames

A single-label classifier for universal framing dimensions in news articles on political
topics.

## Setup

Create python environment, for example with conda. Python 3.8 or later is supported.

```bash
conda create --yes -n NewsFrames python=3.8
conda activate NewsFrames
```

Install:

```bash
pip install NewsFrames
```

## Usage

```python
from NewsFrames import Classifier
classifier = Classifier()
results = classifier.predict(["Executives at the British software company Autonomy mischaracterised revenues from clients including Tottenham Hotspur, the Serious Fraud Office and the BBC to inflate software sales figures before a disastrous £8bn acquisition by the US firm Hewlett-Packard, London’s high court has heard."])
print(results)
```

You can use the `attribute_mode` parameter to get predictions for the individual
attributes (`attribute_mode="withattributes"`) or only whether the respective dimension
is present or not (`attribute_mode="withoutattributes"`). The default is 
`withattributes`.

```python
classifier = Classifier(attribute_mode="withoutattributes")
```

# Dev

## Upload new version

```bash
python -m pip install build twine
python -m build
python -m twine upload dist/*
rm -rf dist/*
```
