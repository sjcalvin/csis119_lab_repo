#Input variables...
param ($venv_name, $empty, $req_file)

# Define a function to create the project virtual environment and install all required packages.
Function generate_venv ($venv_name, $empty = $false, $req_file = 'requirements.txt') {
# Function creates the virtual environment for the project and installs all required packages.
#
# Arguments:
#               $venv_name: name of virtual environment.
#               $req_file: name of requirements text file.
#
# Author: Skylar Calvin
# Date 01/23/2023

    # Check if virtualenv is installed.
    $virtualenv_installed = py.exe -m pip show virtualenv

    # if empty isn't empty...
    if ($null -eq $virtualenv_installed) {

        # Then isntall it.
        py.exe -m pip install virtualenv

    }

    # If a venv directory exists in the current folder...
    if (Test-Path -Path venvs) {

        # Say that it already exists...
        Write-Output 'the ./venvs/ folder already exists.'
    
    # Otherwise...
    } else {

         # Create one...
         Write-Output "the ~/venvs/ folder doesn't already exist. Creating it."
         New-Item -Name "venvs" -ItemType "Directory"

    }

    # Now, create the virtual environment using the name you passed to the function.
    Write-Output "Creating the $venv_name virtual environment..."
    py.exe -m virtualenv venvs/$venv_name

    # And, Activate it...
    Set-Location venvs/$venv_name/Scripts/
    ./activate
    Set-Location ../../..

    # If you didn't secify to use the requirements folder.
    if ($empty -eq $true) {

        # Leave the environment empty and say so.
        Write-Output "Environment left Empty."

    } else {

        # Install all of the packages in the requirements file.
        Write-Output "Installing specified required packages into the $venv_name environment."
        py.exe -m pip install -r $req_file

    }

    # Deactivate the environment.
    deactivate
    Write-Output "Environment deactivated."

}

generate_venv -venv_name $venv_name -req_file $req_file -empty $empty 