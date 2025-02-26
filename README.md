# Piedra, Papel o Tijeras

Este es un juego de **Piedra, Papel o Tijeras** desarrollado en Python utilizando la biblioteca **Pygame**. El juego incluye una interfaz gráfica interactiva y varias funcionalidades para mejorar la experiencia del usuario.

## Funcionalidades principales

1. **Menú principal**:
   - **Start Game**: Permite al jugador comenzar una nueva partida.
   - **History**: Muestra el historial de partidas anteriores, incluyendo los puntajes y el ganador.
   - **Exit**: Cierra el juego.

2. **Ingreso del nombre del jugador**:
   - Antes de comenzar el juego, el jugador puede ingresar su nombre, que será utilizado para mostrar los puntajes y resultados.

3. **Juego principal**:
   - El jugador puede elegir entre **Piedra**, **Papel** o **Tijeras** haciendo clic en los íconos correspondientes o presionando las teclas `1`, `2` o `3`.
   - El juego se juega al mejor de 5 rondas. El ganador es quien obtenga más puntos al final de las rondas.

4. **Resultados de cada ronda**:
   - Después de cada ronda, aparece un mensaje emergente indicando si el jugador ganó, perdió o empató contra la computadora.

5. **Pantalla de fin de juego**:
   - Al finalizar las 5 rondas, se muestra el ganador del juego (Jugador o Computadora) junto con los puntajes finales.
   - Un botón permite regresar al menú principal para iniciar una nueva partida.

6. **Historial de puntajes**:
   - El juego guarda automáticamente los resultados de las partidas en un archivo `scores.json`.
   - En la sección de historial, se pueden ver los últimos 10 resultados, incluyendo el nombre del jugador, los puntajes y el ganador.

## Requisitos

- Python 3.8 o superior
- Biblioteca Pygame (instalable con `pip install pygame`)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu_usuario/piedra-papel-tijeras.git
   cd piedra-papel-tijeras](https://github.com/BarbaraP97/Logica-de-Programacion)
   ```

2. Instala las dependencias:
   ```bash
   pip install pygame
   ```

3. Asegúrate de tener las imágenes necesarias (`rock.png`, `paper.png`, `scissors.png`) en el mismo directorio que el archivo principal del juego.

## Cómo jugar

1. Ejecuta el juego:
   ```bash
   Juego de Piedra, papel o tijera final.py
   ```

2. En el menú principal, selecciona "Start Game" para comenzar.
3. Ingresa tu nombre y presiona Enter.
4. Selecciona tu jugada haciendo clic en los íconos o presionando las teclas `1`, `2` o `3`.
5. Juega hasta completar las 5 rondas y observa quién es el ganador.
6. Revisa el historial para ver los resultados de partidas anteriores.

## Personalización

- Puedes cambiar las imágenes de los íconos (`rock.png`, `paper.png`, `scissors.png`) para personalizar el diseño del juego.
- Modifica el archivo `scores.json` si deseas reiniciar el historial de puntajes.

¡Diviértete jugando a Piedra, Papel o Tijeras! 🎮✂️📄🪨
