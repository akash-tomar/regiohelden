# Bank Management

Django application to manage (CRUD) users and their bank account data (IBAN). 

## Details: 

It supports addition, deletion, editing and viewing of bank users. 

It has been implemented using Django web framework. 

## Features:

- Data validation from user
- Administrators of the app can authenticate using a Google account
- Administrators can create, read, update and delete users
- Manipulation operations on the user can only by done by the administrator who created them
- PostgreSQL as the database backend
- Python 3.4.3
- Documented with how to setup and how to use

## Setup

Install:

- `VirtualBox <https://www.virtualbox.org/>`_

- `Vagrant <https://www.vagrantup.com/>`_

- `Ansible <http://www.ansible.com/>`_ 


Step 1: **git clone https://github.com/akash-tomar/regiohelden.git**

Step 2: **cd regiohelden**

Step 3: **vagrant up --provision**

Step 4: **vagrant ssh**

Step 5: **cd /home/bank_regiohelden/regiohelden**

step 6: **sh start.sh**

Finally, go to your local browser and point to **localhost:8000** or **127.0.0.1:8000** 


## Documentation:

It supports seven end points:

### Home [/]

All the operations allowed on the bank users are listed on the home.

### Add [/add/]

#### Add a bank user 

You can add a bank user using this action. 

Input:

- first name
- last_name
- IBAN details:
  - Country code
  - IBAN checksum
  - Swift/BIC code
  - Account number

### Delete [/delete/]

#### Delete a bank user 

You may delete a bank user using this action. 
It takes first name and last name as identifier. Any user is uniquely identified by a combination of first name and last name.

Input:

- first name
- last_name


### Update [/update/]

#### Update bank user details 

You may update bank user details using this action. 
The system will only update those fields which have been updated by the user.

Input:

- first name
- last_name
- IBAN details:
  - Country code
  - IBAN checksum
  - Swift/BIC code
  - Account number

### View [/view/]

#### View the bank user details

You may view the bank user details using this action. 

Input:

- First name
- Last name

Output:

- first name
- last_name
- IBAN details:
  - Country code
  - IBAN checksum
  - Swift/BIC code
  - Account number

### Login [/login/]

#### Login to the bank portal

You may login to the bank portal using this action.
You can login using your google account.
If you have multiple google accounts, they will be listed to choose from.
We only access basic information like name and email ID from your google account.


### Logout [/logout/]

#### Logout from the current session.

You may logout the bank portal using this action. 