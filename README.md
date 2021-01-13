# email
Send emails on a schedule  
  
Please Note:  
Environment variables set in google cloud sdk's aka GAE's datastore  
To test locally, you will need to register, login, and create a local instance of your credentials  
https://cloud.google.com/docs/authentication/getting-started  

If you would prefer to set environment variables with os.environ[var], switch out the function env(var) in config.py for the commented out one.

Deploy the app with 'gcloud app deploy' 