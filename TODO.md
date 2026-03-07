# Task Tracker CLI — TODO

Obiettivo: costruire un Task Tracker da terminale che salva i task in `tasks.json` e supporta add/update/delete/mark/list.

---

## Fase 0 — Setup progetto

- [x] Crea repo Git (opzionale ma consigliato) e cartella progetto.
- [x] Crea `todo.md` (questo file), `README.md` (vuoto per ora) e `tasks.json` (se vuoi crearlo a mano).
- [x] Definisci convenzioni: nomi comandi, stati validi (`todo`, `in-progress`, `done`), formato date.

---

## Fase 1 — Storage JSON (il “database”)

- [x] All’avvio, verifica se `tasks.json` esiste.
- [x] Se non esiste, crealo con contenuto iniziale: lista vuota.
- [x] Implementa lettura da JSON → lista Python.
- [x] Implementa scrittura lista Python → JSON (sovrascrive).
- [x] Gestisci errori: file vuoto/corrotto, permessi, JSON non valido.

Criterio “done”:

- Lanciando il programma, `tasks.json` viene sempre gestito senza crash.

---

## Fase 2 — CLI (parsing comandi)

- [x] Scegli approccio: `argparse` (consigliato) oppure `sys.argv`.
- [x] Definisci i comandi supportati:
  - `add "descrizione"`
  - `list [todo|in-progress|done]`
  - `update <id> "nuova descrizione"`
  - `delete <id>`
  - `mark-in-progress <id>`
  - `mark-done <id>`
- [x] Gestisci input non valido (messaggi chiari).
- [x] Crea lo “smistamento” comandi → funzioni (anche vuote per ora).

Criterio “done”:

- Ogni comando stampa almeno un messaggio (anche placeholder) e non va in errore.

---

## Fase 3 — Modello dati task

Definisci struttura minima di un task (consigliata):

- `id` (int, univoco)
- `description` (string)
- `status` (`todo`/`in-progress`/`done`)
- `createdAt` (timestamp/string)
- `updatedAt` (timestamp/string)

- [x] Decide formato data/ora (ISO 8601 consigliato).
- [x] Definisci come generi ID: `max(id)+1` oppure contatore persistente.

Criterio “done”:

- Hai una struttura chiara e coerente che userai ovunque.

---

## Fase 4 — Add + List (funzionalità base)

- [x] `add`: crea task con status `todo`, setta `createdAt`/`updatedAt`, salva.
- [ ] `list`: stampa tutti i task in modo leggibile.
- [ ] `list <status>`: filtra per stato.

Edge cases:

- [ ] `add` con descrizione vuota → rifiuta.
- [ ] `list` con file vuoto → stampa “nessun task”.

Criterio “done”:

- Puoi aggiungere 3 task e listarli, anche filtrando.

---

## Fase 5 — Update + Mark (modifica stato/testo)

- [ ] `update <id> "testo"`: aggiorna description + `updatedAt`.
- [ ] `mark-in-progress <id>`: aggiorna status + `updatedAt`.
- [ ] `mark-done <id>`: aggiorna status + `updatedAt`.
- [ ] Se ID non esiste → messaggio chiaro, nessuna modifica al file.

Criterio “done”:

- I task cambiano stato/testo correttamente e restano persistenti.

---

## Fase 6 — Delete

- [ ] `delete <id>`: rimuovi task dalla lista e salva.
- [ ] ID non esiste → messaggio chiaro.

Criterio “done”:

- Eliminazione corretta e `tasks.json` resta valido.

---

## Fase 7 — Qualità (refactor + robustezza)

- [ ] Separa: parsing CLI / logica / storage.
- [ ] Centralizza validazione stati e parsing ID.
- [ ] Output consistente (stesso formato per tutte le azioni).
- [ ] Aggiungi exit code (opzionale) per errori vs successo.

---

## Fase 8 — README (portfolio-ready)

- [ ] Descrivi requisiti, comandi, esempi d’uso.
- [ ] Documenta formato `tasks.json`.
- [ ] Aggiungi “Roadmap / Next steps” (feature future).

---

## Extra (facoltativi)

- [ ] `--help` completo e chiaro.
- [ ] Ordinamento `list` (per id o per data).
- [ ] Ricerca testo: `search "parola"`.
- [ ] Export CSV.
- [ ] Test automatici (unit test) per storage e comandi.
