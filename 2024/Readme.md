# Installation initiale

"Oui bon je vais pas m'embêter avec un pyproject.toml"

=> Oui bah en fait si.

[Source sur Stackoverflow](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143)

En résumé pour commencer une nouvelle année, procéder ainsi :

- récupérer le dossier `00`, `utils.py` et `pyproject.toml` et mettre tout ça dans un dossier "année" ;
- ajouter les `__init__.py` partout où ils manquent ;
- `pip install -e .` dans le dossier "année".

Pour travailler dans le dossier "année", activer le `venv` au préalable : 

```
source venv/bin/activate
```

A priori `import utils` fonctionne bien comme ça, ainsi que l'autocomplétion.