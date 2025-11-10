# Aufgabe 3
Erstelle ein C++ Programm main.cpp, welches “Hi from C++” ausgibt.

1. Erstelle ein Makefile, welches das Programm kompilliert.

2. Was muss getan werden, damit die Kompillierung nur durchläuft, wenn das File main.cpp auch existiert?

3. Mit welchem Befehl kann das Programm via Makefile kompilliert werden?

4. Was passiert, wenn dieser Befehl nochmals ausgeführt wird?

5. Ändere die Ausgabe im C++ Programm auf “Compiled by Makefile”.
Was passiert, wenn der Befehl aus den vorhergehenden Aufgaben nochmals ausgeführt wird?

# Antworten

2.
```
TARGET = main 
$(TARGET): main.cpp
```
Target ist dann abhängig vom File main.cpp


3. ```make main```


4. Wenn sich nichts im main.cpp geändert hat, dann kommt: "make: 'main' is up to date."

5. Das Programm wird neu kompiliert