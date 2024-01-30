#!/bin/bash

# Define a function to create the project virtual environment and install all required packages.
function generate_venv() {
    # Function creates the virtual environment for the project and installs all required packages.
    #
    # Arguments:
    #               1: name of virtual environment.
    #               2: name of requirements text file.
    #
    # Author: Skylar Calvin
    # Date 01/23/2023

    # Check if virtualenv is installed.
    virtualenv_installed=$(python3 -c "import sys; print('virtualenv' in sys.modules)")

    #echo $virtualenv_installed

    # if it is...
    if [[ $virtualenv_installed == 'False' ]] ; 
    
    then

        # Install it.
        sudo apt install python3-virtualenv -y

    fi

    # If the ~/venvs/ directory exists...
    if test -d ~/venvs;
     
    then
        
        # Say that it already exists...
        echo 'the ~/venvs/ folder already exists.'

    # If not...
    else

        # Create one...
        echo "the ~/venvs/ folder doesn't already exist. Creating it."
        mkdir ~/venvs

    fi

    # Now, create the virtual environment using the name you passed to the function.
    echo "Creating the $1 virtual environment..."
    virtualenv ~/venvs/$1

    # Activate the Environment.
    echo "Activating the $1 virtual environment."
    source ~/venvs/$1/bin/activate

    # Install all of the packages in the requirements file.
    echo "Installing required packages into the $1 environment."
    python3 -m pip install -r $2

    # Deactivate the environment.
    echo "Deactivating Environment."
    deactivate

}

# Call the function to create an environment using the requirements in the text file.
generate_venv 'csis_119_venv' 'requirements.txt'