# GitZen

This is a web application built using Django that links Zendesk and Github for
easier developer management.


### Setting up the environment for Heroku deployment (on Ubuntu)

1. Make a Heroku account on their [website](http://www.heroku.com/).

2. Install the Heroku toolbet using the command
	>`wget -qO- https://toolbelt.heroku.com/install.sh | sh`

3. Login to Heroku by running the command
	>`heroku login`

	and filling out the requested credentials.

4. Install python and virtualenv. (A guide for this can be found
[here](http://docs.python-guide.org/en/latest/starting/install/linux/))

5. Install a version of Postgres from
[here](http://www.postgresql.org/download/) so testing can be done locally.

6. Clone the GitZen repo with the command
	>`git clone git://github.com/PolicyStat/GitZen.git`

7. Change directories to the newly cloned GitZen directory and setup a virualenv
using the command
	>`virtualenv venv --distribute`

8. Activate the virtualenv with the command
	>`source venv/bin/activate`
		
	You must source the virtualenv environment for each terminal session where
you wish to run your app.

9. Run the command
	>`sudo apt-get install libpq-dev python-dev`

	to install the necessary packages that allow for the installation of
psycopg2 (Postgresql support for python) in the following step.

10. Install the required packages for GitZen and Heroku with pip by using the
command
	>`pip install -r requirements.txt` 


### Deploying the application to Heroku (on Ubuntu)

1. Create the app on the Heroku Cedar stack by running the command
	>`heroku create --stack cedar`

2. Deploy the app with the command
	>`git push heroku master`

3. The command
	>`heroku logs`

	can be used to view the logs of the app if desired, and the command
	>`heroku open`

	can be used to visit the app on the web.

4. In order to conduct one-off admin processes for the app in django, preface
the commands with
	>`heroku run`

	An example of this would be syncing the databases in django by using the
command
	>`heroku run python manage.py syncdb`


### Configuration Instructions

1. Go to the [GitZen website](http://gitzen.herokuapp.com) on Heroku.

2. Click on the "Create New User" button on the login screen.

3. Begin filling out the information to create a new user by first assigning
them a username and password and filling the "Username", "Password", and
"Confirm Password" fields with this information.

4. In order to use GitHub issue information in GitZen, each user must provide
information on the GitHub repository from which issue information should be
monitored. This access information consists of a GitHub organization name and
repository name associated with the desired issue information, and those
parameters should be filled into the "GitHub Organization" and "GitHub
Repository" fields respectively. If the repository is under a user account
rather than an organization, provide the username of that account in the
organization field instead.

5. In order to use Zendesk ticket information in GitZen, each user must provide
a set of access information from a Zendesk account linked to the tickets that
should be monitored. The first information required to access this data is a
Zendesk user email which should be filled into the "Zendesk User Email" field of
the form. The other three bits of Zendesk access information needed are more
specific and are covered in the following steps.

6. In order to allow API token access to the Zendesk account, "Token Access"
must be enabled. This option can be found by logging into Zendesk with an
account that has administrator level credentials and looking under
"Settings"->"Channels"->"API". After clicking "edit" and checking the "Token
Access" box, copy the displayed API token and paste it into the "Zendesk API
Token" field in the form.

7. For the "Zendesk URL Subdomain" field in the form, enter in the full
URL that comes up after logging into the Zendesk account associated with the
desired ticket information (The URL should be in the format
"https://\{yourcompanyname\}.zendesk.com").

8. For the "Zendesk Ticket Association Field ID" field in the form, the ID
number of the field that holds the external ticket association data for each
Zendesk ticket must be found. In order to find this ID number, first look up the
ID number of a Zendesk ticket from the desired account that has this ticket
association field on it. Then open up a command terminal and enter in the
following command, substituting the parameters surrounded by braces with the
information from the desired Zendesk account and substituting the `id` parameter
with the ticket ID number that was just looked up:
	>`curl {zendesk_url_subdomain}/api/v2/tickets/{id}.json -u
	>{email_address}/token:{api_token}`

	From the output of this command, look for the dictionary key "fields", and
within the dictionaries listed for the value of this key, look for the one with
the value of the "value" key matching the value of the ticket association field
of the Zendesk ticket that was looked up for this process. In the same
dictionary as this "value" pair, the number value for the "id" key is the ID
number that must be entered into the "Zendesk Ticket Association Field ID" field
in form.

9. For the "Time Zone (UTC Offset)" field in the form, enter in the UTC offset
of your local time zone in order to adjust the dates and times of the
application to the proper times for your location. The number value of the
offset should be prefaced with a "+" or "-" to indicated whether the offset is
ahead or behind UTC time (i.e. "-4" or "+9").

11. For the "View Type" field in the form, select whether the home page should
be presented from a GitHub-centered or Zendesk-centered user perspective. By
selecting one of these options, the home page will be set up to provide
information in a more useful way depending on whether the GitZen user is using
the application from a GitHub perspective or a Zendesk perspective. 

12. Check to see that all fields in the form are filled out accurately, and then
click the "Submit" button to create a user with the given information.

13. Once the account has been created, the next page will instruct you to
authorize GitZen on GitHub for the newly created user by clicking the "GitHub
Authorization" button. Click this button to start the authorization process, and
after it is completed (either automatically or by following the GitHub
instructions), a confirmation page will come up with a button that links back to
the login page where one can login to the newly created GitZen account. 
