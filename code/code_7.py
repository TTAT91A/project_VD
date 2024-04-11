<<<<<<< HEAD
from ruamel.yaml import YAML

#ok:avoid-unsafe-ruamel
y1 = YAML()  # default is 'rt'

#ok:avoid-unsafe-ruamel
y2 = YAML(typ='rt')

#ok:avoid-unsafe-ruamel
y3 = YAML(typ='safe')

#ruleid:avoid-unsafe-ruamel
y3 = YAML(typ='unsafe')

#ruleid:avoid-unsafe-ruamel
=======
from ruamel.yaml import YAML

#ok:avoid-unsafe-ruamel
y1 = YAML()  # default is 'rt'

#ok:avoid-unsafe-ruamel
y2 = YAML(typ='rt')

#ok:avoid-unsafe-ruamel
y3 = YAML(typ='safe')

#ruleid:avoid-unsafe-ruamel
y3 = YAML(typ='unsafe')

#ruleid:avoid-unsafe-ruamel
>>>>>>> 4568c2435b8367fca9bbe02afc2078287c266144
y4 = YAML(typ='base')