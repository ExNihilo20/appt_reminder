# Backend Developer Setup

The initial project setup is geared toward a `Ubuntu` OS, but the steps are similar for `Windows` and `Apple` OS clients. 

## Git and GitHub Configuration

1. **Install Git**

    Follow installation link instructions: https://git-scm.com/downloads

2. **Initial git config**:
    - Enter project root directory 
        ```bash
        cd /home/user/projects/backend
        git init
        ```

    -  Set up your git username, email address, text editor (for merge conflicts)
        ```bash
        git config --global user.name "Yourfirstname Yourlastname"
        git config --global user.email "first.last@example.com"
        git config --global core.editor nano
        ```
    - Check your settings
        ```bash
        git config --list
        ```

3. **Set up SSH keys** (if not already done)
    1. In the terminal
        ```bash
        ssh-kegen -t ed25519 -C "your.email@address.here"
        ```
        This creates two files: 
        1. `~/.ssh/id_ed25519` (private)
        2. `~/.ssh/id_ed25510.pub` (public)
        3. Ensure SSH Agent is running and keys are added (add this to the end of your `.bashrc` for persistence)
            ```bash
            eval "$(ssh-agent -s)"
            ssh-add ~/.ssh/id_ed25519
    2. Add public key to GitHub
        1. cat the public key
        ```bash
        cat ~/.ssh/id_ed25519.pub
        ```
        2. Copy the `entire` public key
        3. Go to `Github > Settings > SSH and GPG Keys > New SSH key`
        4. Paste in your public key
        7. Request invite as collaborator


4. **Clone the Repository**
    1. using SSH
        ```bash
        git clone git@github.com:username/repo.git
        ```
        GitHub will authenticate you based on the SSH key in your SSH agent. 

## MariaDB Setup (`Ubuntu/Debian`)

1. Update package index before installation:
    ```bash
    sudo apt update
    ```
2. Install MariaDB Server:
    ```bash
    sudo apt install mariadb-server mariadb-client
    ```
3. Secure the installation:
    After installation, run the security script to set a root password, remove anonymous users, and disable root login
    ```bash
    sudo mariadb-secure-installation:
    ```
    Follow the prompts to configure your security settings.

4. Start and verify the service:
    MariaDB typically starts automatically after installation. You can check its status and manually start it if needed.
    - Check Status:
        ```bash
        sudo systemctl status mariadb
        ```
    - Start the service (`if not running`):
        ```bash
        sudo systemctl start mariadb
        ```
    - Verify installation as connecting to root
        ```bash
        mariadb -u root -p
        ```
5. Download Heidi SQL (`GUI Editor`)
    Direct .deb file download:
        - https://www.heidisql.com/download.php#
    - Follow the prompts for installation.

6. Create a user for this application

    ```sql
    CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
    ```

Replace `username` with the desired username, `hostname` with the hostname or IP address from which the user will connect, and `password` with the desired password for the user 

After creating the user, you can check his or her status by running:

    ```sql
    SELECT User FROM mysql.user;
    ```

This will list all the users in the MariaDB system, including the newly created user 

Once the user is created, you can grant them specific privileges using the `GRANT` statement. For example, to grant all privileges on all databases to the user, you would use:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'hostname';
```

After granting privileges, it is important to reload the privileges to ensure the changes take effect. You can do this by running:

```sql
FLUSH PRIVILEGES;
```

This ensures that the new user has the correct permissions and can access the database as intended.

If you need to grant specific privileges, such as SELECT, INSERT, UPDATE, and DELETE on a particular database, you can use:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON database_name.* TO 'username'@'hostname';
```

Replace `database_name` with the name of the database you want to grant access to 

Additionally, if you want to create a user with remote access, you can use `%` as the hostname, which allows the user to connect from any host:

```sql
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
```

This is useful if the user needs to connect from different machines or networks 

For more detailed information on creating users and managing privileges, you can `refer to the MariaDB documentation.` 

## Generate Your Config Gile

### From the home directory:

1. Generate a `conf/` directory.

2. Create a `appt_reminder.config` file

3. Copy/paste the contents below to your config file and update the information to suite your local needs. This project is set up for using Protonmail secure email client, but feel free to modify the config file for Gmail, Outlook, or your preferred email client.

```properties
[protonmail]
pm_email_address = first.last@email.com
pm_username = email_username
pm_password = email_password

[proton_bridge]
pb_hostname = 127.0.0.1
pb_IMAP_port = 1143
pb_SMTP_port = 11025
pb_username = email.address@pdomain.com
pb_password = randomprotonbridgecharstring
pb_security = STARTTLS

[carrier]
verizon = vtext.com
att = txt.att.net
tmobile = tmomail.net

[mysql]
mysql_user = root
mysql_pass = yourpassword
mysql_host = localhost
mysql_port = 3306
mysql_dbname = appt_reminder
```
The python config parser will pick up the contents of this file as properties for the project.