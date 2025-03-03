# Overview

The Bing Rewards Automation Bot is a powerful and user-friendly tool designed to automate Bing search activities and maximize your Microsoft Rewards points. This bot leverages keyboard input simulation to mimic human-like typing behavior, ensuring natural interactions that reduce the risk of detection or account restrictions.

Key Features:
Human-Like Typing Simulation :
The bot uses randomized typing speeds and intervals to replicate the way humans type, making it nearly indistinguishable from manual searches.
Each keystroke is carefully timed with slight variations to avoid triggering automated system flags.
Customizable Search Volume :
Users can specify the number of random searches they want to perform via an intuitive graphical interface.
The bot generates realistic search queries by combining words from the NLTK English corpus, ensuring high-quality and relevant searches.
Multi-Account Support :
Supports multiple accounts through a JSON configuration file (accounts.json), allowing you to manage and automate rewards collection for several profiles effortlessly.
Automatically logs in to each account using secure credentials stored in the JSON file.
Pause and Random Delays :
Implements strategic pauses between actions (e.g., opening tabs, typing, clicking) to simulate human behavior and avoid suspicion.
Delays are randomized within specified ranges to further enhance realism.
Interrupt Functionality :
Includes a dedicated "Interrupt" button, enabling users to stop the bot's execution at any time without affecting their system stability.
Logging and Feedback :
Provides real-time logs of all actions performed, including successful logins, completed searches, and potential errors.
Logs help users monitor progress and troubleshoot issues effectively.
Cross-Platform Compatibility :
Developed using Python libraries like pyautogui, nltk, and customtkinter, ensuring compatibility across Windows systems.
Can be packaged into a standalone executable for easy distribution and use.

# How It Works

Main Account Mode :
Perform random searches directly on your primary account without needing to store its credentials in the JSON file.
Ideal for users who prefer to keep their main account separate while automating secondary accounts.
Multi-Account Mode :
Reads account details (email and password) from the accounts.json file.
Logs in to each account sequentially, performs the specified number of searches, and ensures proper logout before switching to the next account.
Random Query Generation :
Generates meaningful and varied search terms by combining words from the NLTK corpus, avoiding repetitive patterns that could raise suspicion.
Why Choose This Bot?
Security : Credentials are securely stored in a local JSON file, which can be encrypted or protected as needed.
Efficiency : Automates tedious tasks, saving you time and effort while maximizing your reward points.
Reliability : Designed to handle edge cases, such as CAPTCHA challenges or unexpected UI changes, with robust error-handling mechanisms.
Discretion : Mimics human behavior through randomized typing, delays, and mouse movements, minimizing the likelihood of being flagged as automated activity.
System Requirements :
Operating System: Windows
Dependencies: Python libraries (pyautogui, nltk, customtkinter)
Browser: Microsoft Edge (required for optimal performance)

#The bot is for educational purposes only, its use could lead to the banning of the account, the creator assumes no responsibility for its use.
