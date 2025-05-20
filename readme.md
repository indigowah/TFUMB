# Federated Moderation Bot

A moderation bot with support for local and federated moderation actions across a network of servers.

---

## Features

- **Local Moderation Commands**:
  - `/ban [user] [time] [reason]`: Ban a user.
  - `/unban [user]`: Unban a user.
  - `/mute [user] [time] [reason]`: Mute a user.
  - `/unmute [user]`: Unmute a user.
  - `/timeout [user] [time] [reason]`: Timeout a user.
  - `/untimeout [user]`: Remove user timeout.
  - `/warn [user] [reason]`: Warn a user.
  - `/unwarn [user] [warn_id]`: Remove a specific warning from a user.

- **Federated Moderation Commands**:
  - `/fban [user]`: Propose a federated ban.
  - `/bans [user]`: List out federated ban proposals across the network.
  - `/fmute [user] [time] [reason]`: Propose a federated mute.
  - `/mutes [user]`: List federated mute proposals.
  - `/ftimeout [user] [time] [reason]`: Propose a federated timeout.
  - `/timeouts [user]`: List federated timeout proposals.
  - `/fwarn [user] [reason]`: Propose a federated warn.
  - `/warns [user]`: List federated warn proposals.
  - `/excuse [user]`: Excuse a particular user from federation moderation.

---

## Configuration

- `/config`
  - `/config mode [auto|review|manual]`
    - `auto`: Automatically applies federated moderation once the limit is reached.
    - `review [channel id]`: Sends an embed to a particular channel when limit is reached.
    - `manual`: Allows moderators to manually apply bans without warnings for network-wide moderation list (NWML) updates.
  
  - `/config update [ASAP|hourly|daily|weekly|monthly]`
    - Controls the frequency of database synchronization.
  
  - `/config check_on_join [true|false]`
    - Checks the database when a user joins the server and bans them instantly if they are on the blacklist.
  
  - `/config limit [int]`
    - Number of federation proposals before local moderation action is triggered.
  
  - `/config pings [true|false]`
    - Pings moderators when members are detected on the list.
  
  - `/config DMs [true|false]`
    - Directly messages moderators when members are detected on the list.

---

## Database

- Uses PostgresDB for storing moderation and federation data.

---

## Real World Use Cases

- Enhanced prevention and coordination of moderation actions across multiple servers.
- Streamlined federated approach for community moderation.

---

For further help, use the command `/help` or refer to the command descriptions above.