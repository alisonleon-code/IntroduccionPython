# Tema 3: Operadores y Variables 🏷️

En esta sesión aprendimos que en Python las variables no son contenedores físicos, sino etiquetas que referencian objetos en la memoria.

## 🔑 Conceptos Clave
* **Variable en Python:** Es un nombre (etiqueta) asociado a un objeto.
* **Objeto:** Cada dato en Python tiene un **ID único**, un **Tipo** y un **Valor**.
* **Tipado Dinámico:** Una variable puede cambiar el tipo de objeto al que apunta en cualquier momento.

## 🛠️ Herramientas de Inspección
* `type(variable)`: Devuelve el tipo de dato (int, float, str, etc.).
* `id(variable)`: Devuelve el identificador único del objeto en memoria.

## 📏 Reglas de Nomenclatura (PEP 8)
1. **Permitido:** Letras, números y guiones bajos `_`.
2. **Inicio:** Siempre debe empezar con una letra o `_`.
3. **Prohibido:** Empezar con números, usar espacios o palabras reservadas (Keywords).
4. **Estilo:** Se recomienda usar `snake_case` (ej. `nombre_usuario`).

## ⚡ Asignaciones Aumentadas
Para simplificar el código:
* `a += 1` es igual a `a = a + 1`
* `a *= 2` es igual a `a = a * 2`
