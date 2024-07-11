import subprocess

# Lista pakietów do zainstalowania
packages = ["xmltodict", "pyyaml"]

# Plik z komendami instalacji
install_script = 'installResources.ps1'

def update_install_script(package):
    # Komenda instalacji
    pip_command = f"pip install {package}\n"
    
    # Sprawdzenie, czy komenda już istnieje w pliku
    try:
        with open(install_script, 'r') as file:
            lines = file.readlines()
            if pip_command in lines:
                print(f"Package {package} is already in the install script.")
                return
    except FileNotFoundError:
        # Plik nie istnieje, utworzymy nowy
        pass
    
    # Dodanie komendy do pliku
    with open(install_script, 'a') as file:
        file.write(pip_command)
    print(f"Added {pip_command.strip()} to {install_script}.")

def install_package(package):
    try:
        # Instalacja pakietu
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}.")
        # Aktualizacja skryptu instalacyjnego
        update_install_script(package)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}.")

def main():
    for package in packages:
        install_package(package)

if __name__ == "__main__":
    main()
