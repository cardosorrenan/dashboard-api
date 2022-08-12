

## Prerequisites

Have the following features with their respective versions installed on the machine:

- Node `12.x+` - You can use [NVM](https://github.com/nvm-sh/nvm)
- Ruby `2.6.6` - You can use [RVM](http://rvm.io)
- PostgreSQL 12
  - OSX - `$ brew install postgresql` or install [Postgress.app](http://postgresapp.com/)
  - Linux - `$ sudo apt-get install postgresql`
  - Windows - [PostgreSQL for Windows](http://www.postgresql.org/download/windows/)
- Bundler `2.2.16`

## Setup the project

After you get all the [prerequisites](#prerequisites), simply execute the following commands in sequence:

```bash
1. Install the dependencies above
2. $ git clone  # Clone the project
3. $ cd bycoders_model # Go into the project folder
4. $ gem install bundler # Bundler install
5. $ bundle install # Install ruby dependencies
7. $ yarn install # Install JS dependencies
8. $ rake db:create # Creates db
9. $ rake db:migrate # Migrates db
10. $ rake db:seed # Seed db
11. $ rspec spec # Run the specs to see if everything is working fine
```
