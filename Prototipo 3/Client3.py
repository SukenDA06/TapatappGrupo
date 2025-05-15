import requests
import hashlib
import os

BASE_URL = "http://127.0.0.1:5000"
TOKEN_FILE = "session_token.txt"

def generate_token(user_name, password):
    """Genera un token hash de 256 caracteres basado en el nombre de usuario y la contraseña."""
    combined = f"{user_name}:{password}"
    return hashlib.sha256(combined.encode()).hexdigest()

def save_token(token):
    """Guarda el token en un archivo."""
    with open(TOKEN_FILE, "w") as file:
        file.write(token)

def load_token():
    """Carga el token desde el archivo si existe."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as file:
            return file.read().strip()
    return None

def delete_token():
    """Elimina el archivo del token."""
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)

def get_all_accounts():
    response = requests.get(f"{BASE_URL}/accounts")
    if response.status_code == 200:
        return response.json()
    return None

def get_account_by_username(user_name):
    response = requests.get(f"{BASE_URL}/account/{user_name}")
    if response.status_code == 200:
        return response.json()
    return None

def get_all_infants():
    response = requests.get(f"{BASE_URL}/children")
    if response.status_code == 200:
        return response.json()
    return None

def get_infants_by_acc_id(acc_id):
    response = requests.get(f"{BASE_URL}/children/{acc_id}")
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    token = load_token()
    if token:
        print("Sesión activa detectada. No es necesario iniciar sesión.")
        logged_in = True
    else:
        print("No hay sesión activa. Por favor, inicia sesión.")
        user_name = input("Introduce el nombre de usuario para iniciar sesión: ")
        password = input("Introduce la contraseña: ")
        account = get_account_by_username(user_name)
        if account and account["passwd"] == password:
            print("Inicio de sesión exitoso.")
            token = generate_token(user_name, password)
            save_token(token)
            logged_in = True
        else:
            print("Usuario o contraseña incorrectos. No se pudo iniciar sesión.")
            logged_in = False

    if logged_in:
        print("Obteniendo todas las cuentas:")
        accounts = get_all_accounts()
        print(accounts)

        print("Obteniendo todos los infantes:")
        infants = get_all_infants()
        print(infants)

        acc_id = input("Introduce el ID de usuario para buscar infantes asociados: ")
        if acc_id.isdigit():
            user_infants = get_infants_by_acc_id(int(acc_id))
            print(user_infants if user_infants else "No se encontraron infantes para este usuario")
        else:
            print("ID de usuario no válido")

        # Preguntar si desea cerrar sesión
        logout = input("¿Deseas cerrar sesión? (si/no): ").strip().lower()
        if logout == "si":
            delete_token()
            print("Sesión cerrada. El token ha sido eliminado.")
        else:
            print("Sesión activa. Puedes continuar.")