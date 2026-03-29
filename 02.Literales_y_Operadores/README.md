# Tema 2: Literales y Operadores 🧪

En esta sesión profundizamos en cómo Python representa la información y las reglas matemáticas para manipularla.

## 💡 Conceptos Fundamentales
* **Literal:** Es un dato que se codifica directamente en el código (ej. `123`, `"Hola"`). A diferencia de una variable, su valor es evidente por sí mismo.
* **Tipado Dinámico:** En Python, las "variables" son nombres o referencias a objetos, y pueden cambiar de tipo de dato durante la ejecución.

## 🔢 Operadores Aritméticos Especiales
| Operador | Nombre | Descripción |
| :---: | :--- | :--- |
| `//` | División Entera | Devuelve el cociente sin decimales. |
| `%` | Módulo | Devuelve el residuo de la división. |
| `**` | Potencia | Eleva un número a una potencia (ej. `x ** 0.5` para raíz). |

## 📐 Jerarquía de Prioridades (Orden de ejecución)
1. **Paréntesis `()`**: Tienen la mayor prioridad.
2. **Potencia `**`**.
3. **Multiplicación, División, Módulo y División Entera** (`*`, `/`, `%`, `//`).
4. **Suma y Resta** (`+`, `-`).

> **Nota importante:** La división real (`/`) siempre devuelve un tipo `float` (decimal), incluso si el resultado es exacto (ej. `4 / 2` es `2.0`).

## ✍️ Manejo de Cadenas (Strings)
Aprendí a usar **caracteres de escape** para evitar errores:
* `\n`: Salto de línea.
* `\"`: Incluir comillas dobles dentro de un texto.
* `\'`: Incluir comillas simples.
