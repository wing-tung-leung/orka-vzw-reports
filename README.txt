Werkwijze
=========

1 - Dexia online
2 - opvragen afschriften in PDF vorm, stockeren in "exports" folder
3 - export naar CSV formaat, ook bewaren in "exports" folder
4 - kopier naar "automatic" folder met naam "export.csv"
5 - start "prepare.sh" om enkel velden te selecteren die van belang zijn

./prepare.sh > prepare.out

Uitgaves
--------
Filter met "filter_expense.py".

cat prepare.out | ./filter_expense.py > expenses.csv

OpenOffice import:
 - Language: English (USA)
 - semicolon separator
 - first column: Date (DMY)

Inkomsten
---------
Filter met "filter_income.py".

cat prepare.out | ./filter_income.py > income.csv

Om velden in dezelfde volgorde als Excel te brengen:

cat income.csv | awk -F\; '{print $1";"$2";"$3";"$4}' > income2.csv

Openenen in Office met ; als separator, en eerste kolom als datum (DMY).

Opmerkingen
-----------
Transactienummers zijn pas ingevuld na het opvragen van afschriften,
dus het is belangrijk voor volledige data in de CSV exports.
