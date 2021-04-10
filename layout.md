# User-DB
- Type: SQLite3 (b/c easier to just import to python, no extra server needed)

## Tables
### users
- id (primary, int, not null)
- name (text)
- mail (text)
- pw (text)

### ids
- user (foreign key -> users.id, int not null)
- twitch (int)
- youtube (text)
- discord (text)

### subscriptions
- user (foreign key -> users.id, int not null)
- date (text, not null) (0 if inactive)
- streak (int, not null) (0 if inactive)
- level (int, not null) (0 if inactive, 1-3 for twitch, 4 Twitch-Prime, 5 YT (this might update in the future))

# API
## Operations
### Read
- Banned words list
### Write
- new subscriptions (not yet implemented)

## DB
- Auth key (string, primary key, not null)
- permissions(int, not null) (saved in "binary", aka each permision is represented by a single number in the big integer)

## Permissions
- All read
- All write

# Public Website
- TBD
