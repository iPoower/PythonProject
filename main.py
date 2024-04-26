# Lean Python Go Work ! #

# Price + Apple + #

prices = {'apple': 0.75, 'egg': 0.50}
cart = {
    'apple': 1,
    'egg': 6
}

bill = sum(prices[item] * cart[item]
           for item in cart)

print(f'I have to pay {bill:.2f}')
-------------------------------------------------------------

Les parenthèses (()) sont utilisées dans Python pour définir des structures de données comme les listes, les tuples, les ensembles et les dictionnaires, ainsi que pour appeler des fonctions et des méthodes. Voici quelques utilisations courantes des parenthèses en Python :

- **Définition de Structures de Données :**
  - **Listes :** Les parenthèses sont utilisées pour définir une liste d'éléments. Par exemple :
    ```python
    my_list = [1, 2, 3]  # Définit une liste avec des crochets
    ```

  - **Tuples :** Les parenthèses sont utilisées pour définir un tuple (une séquence immuable d'éléments). Par exemple :
    ```python
    my_tuple = (1, 2, 3)  # Définit un tuple avec des parenthèses
    ```

  - **Ensembles :** Les parenthèses peuvent également être utilisées pour définir un ensemble en utilisant des accolades avec ou sans valeurs. Par exemple :
    ```python
    my_set = {1, 2, 3}  # Définit un ensemble avec des accolades
    ```

- **Appel de Fonctions et de Méthodes :**
  Lorsque vous appelez une fonction ou une méthode en Python, vous utilisez des parenthèses pour entourer les arguments de la fonction. Par exemple :
  ```python
  result = my_function(arg1, arg2)  # Appel d'une fonction avec des arguments entre parenthèses
  obj.method(arg1, arg2)  # Appel d'une méthode sur un objet avec des arguments entre parenthèses
result = (x + y) * z  # Les parenthèses autour de (x + y) spécifient que l'addition est effectuée en premier
