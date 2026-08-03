# Prompt alat

Mali CLI bez dodatnih ovisnosti služi za pregled, pretragu i popunjavanje promptova.
Potreban je Python 3.10 ili noviji.

```powershell
python prompt_tool.py list
python prompt_tool.py search automatizacija
python prompt_tool.py show automation-scripts-automatizacija-organizacije-datoteka
python prompt_tool.py fill automation-scripts-automatizacija-organizacije-datoteka
```

Naredba `fill` pita za svaku oznaku u uglatim zagradama. Prazan odgovor ostavlja
oznaku netaknutom. Rezultat se može spremiti s `--output gotov-prompt.txt`.

Testovi se pokreću naredbom:

```powershell
python -m unittest discover -s tests
```
