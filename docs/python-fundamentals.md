# Notes de base — Python

Ces notes actualisent les explications qui figuraient historiquement après le code de `main.py`.
L'ancienne version reste consultable dans l'historique Git.

## Parenthèses `(...)`

- Appeler une fonction : `print("Bonjour")`, `sum([1, 2])`.
- Regrouper une expression : `(2 + 3) * 4`.
- Créer un tuple : `(1, 2, 3)` ou, sans parenthèses, `1, 2, 3`.
- Une liste utilise `[1, 2]`, un dictionnaire `{"a": 1}`, un ensemble `{1, 2}` et l'ensemble vide `set()`.

## Dictionnaires et boucles

```python
prices = {"apple": 0.75, "egg": 0.50}
quantities = {"apple": 1, "egg": 6}
total = sum(prices[item] * quantity for item, quantity in quantities.items())
print(f"{total:.2f}")
```

## Prochaines étapes

Typage, traitement d'erreurs, tests unitaires et maîtrise de Git. Les scripts de ce dépôt sont des exercices de débutant.
