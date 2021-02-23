# DB
- Type: SQLite3 (b/c easier to just import to python, no extra server needed)

## Tables
### Subs
- Internal UID
- Twitch-ID (Empty if from YT)
- Youtube-ID (Empty if from Twitch)
- Start of Subscription
- Streak in Months
- Level (1/2/3 if from Twitch, always 1 if from Youtube)
### General Users
- UID
- Registered Name
- Registered E-Mail
- PW-Hash or some other safe way of storing a password
- Twitch-ID (if linked)
- Youtube-ID (if linked)
- Discord-ID (if linked)

# API
### Read
- TBD
### Write
- TBD

# Public Website
- TBD