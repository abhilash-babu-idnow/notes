% YAML

```python
import yaml
from io import StringIO
import pprint
pp = pprint.PrettyPrinter(indent=4)
```

Basically are key value pairs


```python
f = StringIO("""
name: Abhilash
""")
pp.pprint(yaml.load(f, yaml.Loader))
```

    {'name': 'Abhilash'}
    

- YAML with list of values

Indentation and alignment is important, otherwise it is not a valid yaml file


```python
f = StringIO("""
team: India
players:
    - Sachin
    - Sourav
    - Rahul
    - Lakshman
""")
pp.pprint(yaml.load(f, yaml.Loader))
```

    {'players': ['Sachin', 'Sourav', 'Rahul', 'Lakshman'], 'team': 'India'}
    

- YAML also supports nested data


```python
f = StringIO("""
team: India
players:
    - Sachin
    - Sourav
    - Rahul
    - Lakshman
roles:
    batsman:
        - Sachin
        - Sourav
        - Rahul
        - Lakshman
    bowler:
        - Sachin
        - Sourav
    wicket keeper:
        - Rahul
""")
pp.pprint(yaml.load(f, yaml.Loader))
```

    {   'players': ['Sachin', 'Sourav', 'Rahul', 'Lakshman'],
        'roles': {   'batsman': ['Sachin', 'Sourav', 'Rahul', 'Lakshman'],
                     'bowler': ['Sachin', 'Sourav'],
                     'wicket keeper': ['Rahul']},
        'team': 'India'}
    

* YAML with multiline string

Use the ```|``` symbol for that


```python
f = StringIO("""
team: India
desc: | 
    Indian cricket team with legends.
    And Sachin is my all time favourite.
    Sachin's cover drive, Sourav dancing 
    down the pitch, Rahul's cover drive and 
    Lakshman's flick.
players:
    - Sachin
    - Sourav
    - Rahul
    - Lakshman
""")
pp.pprint(yaml.load(f, yaml.Loader))
```

    {   'desc': 'Indian cricket team with legends.\n'
                'And Sachin is my all time favourite.\n'
                "Sachin's cover drive, Sourav dancing \n"
                "down the pitch, Rahul's cover drive and \n"
                "Lakshman's flick.\n",
        'players': ['Sachin', 'Sourav', 'Rahul', 'Lakshman'],
        'team': 'India'}
    

- YAML with a long single line string written on multiple lines

Use the ```>``` symbol for that


```python
f = StringIO("""
team: India
desc: >
    Indian cricket team with legends.
    And Sachin is my all time favourite.
    Sachin's cover drive, Sourav dancing 
    down the pitch, Rahul's cover drive and 
    Lakshman's flick.
players:
    - Sachin
    - Sourav
    - Rahul
    - Lakshman
""")
pp.pprint(yaml.load(f, yaml.Loader))
```

    {   'desc': 'Indian cricket team with legends. And Sachin is my all time '
                "favourite. Sachin's cover drive, Sourav dancing  down the pitch, "
                "Rahul's cover drive and  Lakshman's flick.\n",
        'players': ['Sachin', 'Sourav', 'Rahul', 'Lakshman'],
        'team': 'India'}
    

- YAML also has anchors and aliases


```python
f = StringIO("""
definitions: 
  steps:
    - step: &build-test
        name: Build and test
        script:
          - mvn package
        artifacts:
          - target/**

pipelines:
  branches:
    develop:
      - node: *build-test
    master:
      - node: *build-test
""")
pp.pprint(yaml.load(f, yaml.Loader))
```

    {   'definitions': {   'steps': [   {   'step': {   'artifacts': ['target/**'],
                                                        'name': 'Build and test',
                                                        'script': [   'mvn '
                                                                      'package']}}]},
        'pipelines': {   'branches': {   'develop': [   {   'node': {   'artifacts': [   'target/**'],
                                                                        'name': 'Build '
                                                                                'and '
                                                                                'test',
                                                                        'script': [   'mvn '
                                                                                      'package']}}],
                                         'master': [   {   'node': {   'artifacts': [   'target/**'],
                                                                       'name': 'Build '
                                                                               'and '
                                                                               'test',
                                                                       'script': [   'mvn '
                                                                                     'package']}}]}}}
    


```python

```
