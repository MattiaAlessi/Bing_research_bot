import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import threading
import pyautogui
import time
import random
import nltk
from nltk.corpus import words
import os
import sys
import json

# Variabile globale per controllare l'esecuzione
execution_active = False

# Funzione per gestire i percorsi delle risorse (per lo sviluppo e l'eseguibile)
def resource_path(relative_path):
    """ Ottiene il percorso assoluto delle risorse, funziona sia per lo sviluppo che per l'eseguibile """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Percorso predefinito dell'immagine (usando resource_path)
IMAGE_PATH = resource_path("program folder\\pointer.jpg")

# Funzione per generare pause casuali
def sleep_random(min_time=1, max_time=3):
    time.sleep(random.uniform(min_time, max_time))

# Funzione per leggere i dati degli account da un file JSON
def read_accounts():
    try:
        with open(resource_path("program folder\\accounts.json"), "r") as file:
            return json.load(file)
    except Exception as e:
        log_text.insert(tk.END, f"Error reading account data: {e}\n")
        return []

# Funzione per eseguire il login su Bing Rewards
def perform_login(email, password):
    try:
        log_text.insert(tk.END, f"Logging in for account: {email}\n")

        pyautogui.hotkey('win', 'r')
        sleep_random(1, 2)
        pyautogui.write('msedge')
        pyautogui.press('enter')
        sleep_random(3, 5)

        pyautogui.hotkey('ctrl', 'l')
        sleep_random(1, 2)
        pyautogui.write("https://login.live.com/")
        pyautogui.press('enter')
        sleep_random(5, 7)

        pyautogui.write(email, interval=random.uniform(0.1, 0.2))
        pyautogui.press('enter')
        sleep_random(3, 5)

        pyautogui.write(password, interval=random.uniform(0.1, 0.2))
        pyautogui.press('enter')
        sleep_random(5, 7)

        # Verifica il login
        if not pyautogui.locateOnScreen(resource_path("program folder\\logged_in.jpg"), confidence=0.8):
            log_text.insert(tk.END, f"Login failed for account: {email}\n")
            return False

        log_text.insert(tk.END, f"Login successful for account: {email}\n")
        return True
    except Exception as e:
        log_text.insert(tk.END, f"Error during login for account {email}: {e}\n")
        return False

# Funzione per eseguire le ricerche casuali per l'account principale
def perform_random_searches_main_account():
    global execution_active
    execution_active = True
    interrupt_button.configure(state=tk.NORMAL)
    log_text.insert(tk.END, "Starting random searches for the main account...\n")

    def operations():
        try:
            nltk.download('words')

            def generate_random_words(num_words):
                dictionary = words.words()
                random_words = random.sample(dictionary, num_words * 3)  # Genera tre volte le parole necessarie
                return [" ".join(pairs[:3]) for pairs in zip(random_words[::3], random_words[1::3], random_words[2::3])]  # Combina a gruppi di 3

            try:
                num_searches = int(searches_entry.get())
                if num_searches <= 0:
                    log_text.insert(tk.END, "Enter a valid number of searches.\n")
                    return
            except ValueError:
                log_text.insert(tk.END, "Enter a valid number of searches.\n")
                return

            random_queries = generate_random_words(num_searches)

            pyautogui.hotkey('win', 'r')
            sleep_random(1, 2)
            pyautogui.write('msedge')
            pyautogui.press('enter')
            sleep_random(3, 5)

            for i in range(num_searches):
                if not execution_active:
                    break
                log_text.insert(tk.END, f"Search number: {i+1} for the main account\n")

                pyautogui.hotkey('ctrl', 't')
                sleep_random(1, 2)

                search_query = random_queries[i]
                pyautogui.write(search_query, interval=random.uniform(0.1, 0.2))  # Simula digitazione umana
                pyautogui.press('enter')
                sleep_random(3, 5)

                pyautogui.hotkey("ctrl", "w")
                sleep_random(1, 2)

            log_text.insert(tk.END, "Random searches completed for the main account.\n")

        except Exception as e:
            log_text.insert(tk.END, f"Error during random searches: {e}\n")

        finally:
            interrupt_button.configure(state=tk.DISABLED)

    threading.Thread(target=operations).start()

# Funzione per eseguire le ricerche casuali su più account
def perform_random_searches_multiple_accounts():
    global execution_active
    execution_active = True
    interrupt_button.configure(state=tk.NORMAL)
    log_text.insert(tk.END, "Starting random searches for all accounts...\n")

    accounts = read_accounts()
    if not accounts:
        log_text.insert(tk.END, "No accounts available. Ensure the accounts.json file is correct.\n")
        return

    def operations():
        try:
            for account in accounts:
                if not execution_active:
                    break

                email = account["email"]
                password = account["password"]

                # Effettua il login per l'account corrente
                if not perform_login(email, password):
                    log_text.insert(tk.END, f"Login failed for account: {email}. Skipping searches.\n")
                    continue

                # Esegui le ricerche casuali per l'account
                execute_random_searches_for_account(account)

        except Exception as e:
            log_text.insert(tk.END, f"Error during execution for all accounts: {e}\n")

        finally:
            interrupt_button.configure(state=tk.DISABLED)
            log_text.insert(tk.END, "Random searches completed for all accounts.\n")

    threading.Thread(target=operations).start()

# Funzione per eseguire le ricerche casuali per un account specifico
def execute_random_searches_for_account(account):
    global execution_active
    email = account["email"]
    log_text.insert(tk.END, f"Starting searches for account: {email}\n")

    def operations():
        try:
            nltk.download('words')

            def generate_random_words(num_words):
                dictionary = words.words()
                random_words = random.sample(dictionary, num_words * 3)
                return [" ".join(pairs[:3]) for pairs in zip(random_words[::3], random_words[1::3], random_words[2::3])]

            try:
                num_searches = int(searches_entry.get())
                if num_searches <= 0:
                    log_text.insert(tk.END, "Enter a valid number of searches.\n")
                    return
            except ValueError:
                log_text.insert(tk.END, "Enter a valid number of searches.\n")
                return

            random_queries = generate_random_words(num_searches)

            for i in range(num_searches):
                if not execution_active:
                    break
                log_text.insert(tk.END, f"Search number: {i+1} for account {email}\n")

                pyautogui.hotkey('ctrl', 't')
                sleep_random(1, 2)

                search_query = random_queries[i]
                pyautogui.write(search_query, interval=random.uniform(0.1, 0.2))
                pyautogui.press('enter')
                sleep_random(3, 5)

                pyautogui.hotkey("ctrl", "w")
                sleep_random(1, 2)

            log_text.insert(tk.END, f"Searches completed for account: {email}\n")

        except Exception as e:
            log_text.insert(tk.END, f"Error during searches for account {email}: {e}\n")

    threading.Thread(target=operations).start()

# Funzione per interrompere l'esecuzione
def stop_execution():
    global execution_active
    execution_active = False
    log_text.insert(tk.END, "Execution interrupted by the user.\n")
    interrupt_button.configure(state=tk.DISABLED)

# Configurazione di CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# Creazione della finestra principale
root = ctk.CTk()
root.title("Bing Rewards Automation")
root.geometry("900x700")

# Frame principale
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Titolo dell'applicazione
title_label = ctk.CTkLabel(main_frame, text="Bing Searches", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Campo di input per il numero di ricerche
searches_label = ctk.CTkLabel(main_frame, text="Number of searches:", font=("Arial", 14))
searches_label.pack(pady=5)
searches_entry = ctk.CTkEntry(main_frame, width=300, font=("Arial", 14))
searches_entry.pack(pady=10)

# Pulsante per avviare le ricerche casuali sull'account principale
random_searches_main_button = ctk.CTkButton(
    main_frame,
    text="Start Random Searches (Main Account)",
    command=perform_random_searches_main_account,
    font=("Arial", 16),
    width=200,
    height=40
)
random_searches_main_button.pack(pady=10)

# Pulsante per avviare le ricerche casuali su più account
random_searches_multiple_button = ctk.CTkButton(
    main_frame,
    text="Start Random Searches (All Accounts)",
    command=perform_random_searches_multiple_accounts,
    font=("Arial", 16),
    width=200,
    height=40
)
random_searches_multiple_button.pack(pady=10)

# Pulsante per interrompere il programma
interrupt_button = ctk.CTkButton(
    main_frame,
    text="Interrupt",
    command=stop_execution,
    font=("Arial", 16),
    width=200,
    height=40,
    state=tk.DISABLED
)
interrupt_button.pack(pady=10)

# Area di testo per i log
log_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
log_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Avvio della GUI
root.mainloop()