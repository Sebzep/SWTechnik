# Abgabe: Software Engineering – TST

**Student:** Sebastian Zepke

**Repository-Link:** *[Hier deinen GitHub/GitLab-Link einfügen]*

---

## 1. TDD-Durchlauf (Warenkorb)

Die Git-History zeigt den disziplinierten TDD-Ansatz nach dem Prinzip **Red $\rightarrow$ Green $\rightarrow$ Refactor** für folgende Features:

* **Feature 1:** Initialisierung eines leeren Warenkorbs (Anzahl = 0).
* **Feature 2:** Hinzufügen von Produkten und korrekte Aktualisierung der Gesamtanzahl.

Jeder Schritt wurde als einzelner Commit mit entsprechendem Zeitstempel festgehalten, um den methodischen Weg der Entwicklung zu dokumentieren.

---

## 2. Mock-Durchlauf (Datenbank-Isolierung)

### Testergebnis (Konsolen-Ausgabe)

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK

```

### Begründung für die Mock-Wahl

> "Die Methode `Database.get_price_from_db` musste im dritten Testfall herausgemockt werden, da sie in einer realen Produktionsumgebung eine aktive Netzwerk- oder Datenbankverbindung erfordert. Im Rahmen des Unit-Tests soll ausschließlich die Berechnungslogik der Methode `get_total_price` im Warenkorb geprüft werden, ohne von externen Faktoren wie Datenbank-Verfügbarkeit, Latenzen oder echten Datenbeständen abhängig zu sein. Durch den Einsatz von `unittest.mock.patch` bleibt der Test vollständig isoliert, deterministisch und unabhängig von der Infrastruktur."

