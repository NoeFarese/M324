# Erkläre die Begriffe Pipeline, Stage und Job.

### Pipeline
repräsentiert den gesamten CI/CD Prozess.

### Stage
ist eine gruppe von jobs und die werden nacheinander ausgeführt.

Beispiel: build, test, deploy

nächste stage beginnt erst, wenn alle jobs von der vorherigen stage erfolgreich waren.

### Job
ein job ist eine einzelne aufgabe innerhalb einer stage.

z.b: kompilieren des codes oder tests ausführen

---

# Eine Pipeline enthält 3 Stages à je 2 Jobs.
### Unter welcher Bedingung wird die Pipeline als passed gekennzeichnet?
wenn alle 6 jobs erfolgreich waren.

### Unter welcher Bedingung wird die Pipeline als failed gekennzeichnet?
wenn irgendein job failed