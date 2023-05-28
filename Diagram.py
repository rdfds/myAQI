#Device State Diagram

#New Out Of Box
    # Start AP Mode
    # create http server
    # Wait for user to request setup page
    # server out setup page
    # Wait for user to submit form (HTTP POST)
    # save credentials to file system
    # restart device

#Failed to connect to wifi
    # Start AP Mode
    # create http server
    # Wait for user to request setup page
    # server out setup page
        # Include the error message and potentially faulty credentials
    # Wait for user to submit form (HTTP POST)
    # save credentials to file system
    # clear error flag from file system
    # restart device

#Wifi creds exist
    # Use cached creds to connect to wifi
    # Wifi connection success -> Normal device working state
    # Wifi connection failed -> Go to failed to connect state


#Wifi failed to connect
    # store an error message in the file system
    # set an error flag

#Device factory Reset Process
    # Clear credentials from file system
    # Clear any error flags / error messages from FS
    # restart device

#Device Startup operation workflow

#Startup
#check the file system for cached/saved wifi credentials
    # Check for the error flag
        # Error flag exists => Failed to connect to wifi
    #Creds do not exist -> New Out of box
    #Creds exist -> Connect to wifi

