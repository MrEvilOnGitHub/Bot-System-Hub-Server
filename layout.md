# User-DB
- Type: SQLite3 (b/c easier to just import to python, no extra server needed)

## Tables
### Users
- id (primary, int, not null)
- name (text)
- mail (text)
- pw (text)

### IDs
- user (foreign key -> users.id, int not null)
- twitch (int)
- youtube (text)
- discord (text)

### subscriptions
- user (foreign key -> users.id, int not null)
- date (text, not null) (0 if inactive)
- streak (int, not null) (0 if inactive)
- level (int, nut null) (0 if inactive, 1-3 for twitch, 4 yt (this might update in the future))

# API
## Operations
### Read
- TBD
### Write
- TBD

## DB
- Auth key (string, primary key, not null)
- permissions(int, not null) (saved in "binary", aka each permision is represented by a single number in the big integer)

# Public Website
- TBD