# 2 Include, Variablen, Rules

### Beschreibe den Unterschied zwischen einer lokalen und einer globalen Variable
lokale variable: 
- wird innerhalb eines jobs oder einer pipeline definiert
- Nur dieser Job / Pipeline kann sie nutzen

globale variable: 
- wird für das gesamte projekt oder gitLab-account definiert
- alle pipelines und jobs im projekt können darauf zugreifen

---
### Beschreibe eine beliebige, vorgegebene Variable von GitLab.
Variable: CI_COMMIT_SHA

- enthält die aktuelle commit-d, die die pipeline ausgelöst hat
- automatisch in jedem job verfügbar

