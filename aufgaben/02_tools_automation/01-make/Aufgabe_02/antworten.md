# Aufgabe 2
Ein Makefile enthält einen Vorgang, welcher ausschliesslich die installierte Version der Software make ausgibt. Das Target wird version genannt.

1. Was würde passieren, wenn ein File mit dem Namen version erstellt würde?

2. Wie kann sichergestellt werden, dass der Vorgang version zuverlässig ausgeführt wird? Erstelle das entsprechende Makefile.

# Antworten
1. Wenn im Verzeichnis eine Datei namens version existiert, würde der Befehl``make version``
nichts ausführen, weil make davon ausgeht, dass das Ziel "version" bereits aktuell ist.

2. Man markiert das Target als phony (also „kein echtes File-Ziel“).
Dadurch wird es immer ausgeführt, egal ob eine Datei version existiert oder nicht.
