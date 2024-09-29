Installation
1. To run this web scraper, you need to have Python, mysql, and scrapy library installed on your machine.

2. Install Scrapy: pip install scrapy
3. Install mysql using Homebrew:
   1. Install "homebrew" if you don't have it via Terminal: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   2. After the installation, type "brew --version" to check if it's successfully installed
   3. Install mysql via homebrew: brew install mysql
   4. Start the mySQL Server: brew services start mysql
   5. Run mySQL: mysql -u root -p
   6. If you need to set a root password and remove anonymous users, then type: mysql_secure_installation and follow the instructions. After that,
      initiate the step 5 again using the password that has been set by you.
4. Create the database by typing this on the Terminal: CREATE DATABASE your_database;
   *change "your_database" to be your own database's name. In this case it will be "countryscraper"
5. Create a new user with a password by typing this on the Terminal: CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   *change "your_username" and "your_password" with your desired ones.
6. Grant the access to the user on the new database: GRANT ALL PRIVILEGES ON your_database.* TO 'your_username'@'localhost';
7. After all these steps done, you can go to Terminal on VSCODE and run "scrapy crawl countries". 


