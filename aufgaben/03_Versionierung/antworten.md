# 3 Commits, Branches, Merges
### 3.1 Was ist der Unterschied zwischen einem lokalen Repository und einem remote Repository?
- Ein lokales Repository liegt auf dem eigenen Rechner und enthält den vollständigen Projektverlauf inkl. Commits, Branches und Tags.
- Ein remote Repository liegt auf einem Server (z. B. GitLab) und dient als zentrale Austausch- und Sicherungsstelle für mehrere Entwickler.

### 3.2 Mit welchem Befehl kann ein Repository, welches auf GitLab abgespeichert ist, auf einen lokalen Speicherpfad kopiert werden?
``git clone <repository-url>``

### 3.3 Du hast ein lokales Repository. Zwischenzeitig wurde auf dem remote Repository eine Änderung vorgenommen. Mit welchem Befehl kann die Änderung im lokalen Repository übernommen werden?
``git pull``

### 3.4 Mit welcher Befehlsabfolge können Änderungen an einem lokalen Repository auf ein remote Repository übertragen werden?
``git add .``

``git commit -m "message"``

``git push``

### 3.5 Wozu werden Branches genutzt?
Branches werden genutzt, um parallel und isoliert an Features, Bugfixes oder Experimenten zu arbeiten, ohne den stabilen Hauptzweig zu gefährden.
Sie ermöglichen saubere Entwicklung, Code-Reviews und kontrollierte Merges.

### 3.6.1 Was stellst du auf dem Branch main fest?
Auf dem Branch ``main`` ist keine der neuen Änderungen sichtbar:
- README.md ist unverändert (Originalzustand beim Clone)
- Die Datei main.cpp existiert nicht
- Der Branch enthält nur den Stand, der beim Klonen des Repositories vorhanden war

### 3.6.2 Was stellst du auf dem Branch develop fest?
Auf dem Branch ``develop`` gilt:
- Die Datei main.cpp existiert
- README.md ist unverändert
- Änderungen aus doc/readme-instructions sind nicht sichtbar

### 3.6.3 Was stellst du auf dem Branch doc/readme-instructions fest?
Auf dem Branch ``doc/readme-instructions`` gilt:
- Die Datei README.md ist geändert
- Die Datei main.cpp existiert nicht
- Änderungen aus develop sind nicht vorhanden

### 3.7 Welche Vorbereitungen müssen beim Mergen getroffen werden und weshalb?
Vor dem Mergen muss sichergestellt werden, dass der Ziel-Branch aktuell ist (z. B. durch git pull) und dass der zu mergende Branch fehlerfrei ist.
Dazu gehören kompilierbarer Code, erfolgreiche Tests und ein sauberer Working Tree ohne uncommittete Änderungen.

Zusätzlich sollten Merge-Konflikte vorab geprüft und wenn möglich bereits im Feature-Branch gelöst werden.

Diese Vorbereitungen sind notwendig, um Konflikte, Build-Fehler und instabile Zustände im Ziel-Branch zu vermeiden und die Integrität des Repositories sicherzustellen.

### 3.8 Beschreibe die Befehle für diesen Vorgang:
![img.png](aufgabe8.png)

``git checkout main``

``git pull``

``git add <changed files>``

``git commit -m "commit 0"``

``git add <changed files>``

``git commit -m "commit 1``

``git push``

---

``git checkout -b develop/gui``

---

``git add .``

``git commit -m "commit 2"``

``git add .``

``git commit -m "change 3"``

``git push``

---

``git checkout main``

---

``git merge develop/gui``

---

``git branch -d develop/gui``

---

``git add <changes files>``

``git commit -m "commit 5"``

``git push``

### 3.9 Beschreibe die Befehle für diesen Vorgang:
![img_1.png](aufgabe9.png)

## Merge Conflict Aufgabe
### 3.10.1 Mit welchem Befehl werden die Branches gemergt?
``git checkout ux/friendly-text``

``git merge ux/session-end``

### 3.10.2 Dokumentiere, wie der Merge Konflikt behoben wird, sodass der Merge letztendlich erfolgreich durchgeführt wurde.
Von beiden Seiten die Änderungen reinnehmen.

Dann ``git add greet.py`` machen und ``git commit`` (automatische merge-commit message ovn git)

# 4 Releases
### 4.1 Beschreibe welche zusätzlichen Funktionen ein Release gegenüber einem Commit hat.
Ein Commit ist lediglich ein technischer Schnappschuss des Codes zu einem bestimmten Zeitpunkt.

Ein Release geht darüber hinaus und bietet zusätzliche Funktionen:

- **Versionierung:** Ein Release kennzeichnet einen definierten, stabilen Stand (z. B. für Produktion).
- **Nachvollziehbarkeit:** Releases bündeln mehrere Commits zu einer fachlich sinnvollen Einheit.
- **Dokumentation:** Releases enthalten üblicherweise Release Notes (Änderungen, Fixes, bekannte Probleme).
- **Verteilbarkeit:** Ein Release kann gebaut, ausgeliefert oder deployed werden (Artefakte, ZIPs, Docker Images).
- **Referenzpunkt:** Ein Release dient als fixer Anker für Rollbacks, Hotfixes und Support.

Kurz: Jeder Release ist ein Commit, aber nicht jeder Commit ist ein Release.

### 4.2 Wie werden Release Tags sinnvollerweise dargestellt? Schreibe drei beispielhafte Release Tags.
Release Tags werden sinnvollerweise als **annotated Tags** mit einer Versionsnummer erstellt.  
Standard ist **Semantic Versioning (SemVer)**.

### Beispielhafte Release Tags
- `v1.0.0`
- `v1.2.3`
- `v2.0.0`

### Optional (praxisnah)
- `v1.1.0-beta`
- `v2.0.1-hotfix`

---

- Commit = technisch
- Release = fachlich + versioniert + dokumentiert
- Tags = eindeutig, versioniert, stabil