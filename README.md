# Password Generator

## Description
This Password Generator is a Python application with a graphical user interface (GUI) that allows users to generate secure passwords based on specified criteria. It also provides functionality to save generated passwords locally with timestamps.

## Features
- Adjustable password length (6-30 characters)
- Options to include uppercase letters, lowercase letters, numbers, and symbols
- Generate passwords based on selected criteria
- Save generated passwords with timestamps
- View history of saved passwords

## Requirements
- Python 3.x
- tkinter (usually comes pre-installed with Python)

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the `password_generator.py` file.

```
git clone https://github.com/yourusername/password-generator.git
```

3. Navigate to the project directory:

```
cd password-generator
```

## Usage
Run the script using Python:

```
python password_generator.py
```

The GUI will appear, allowing you to:
1. Adjust the password length using the slider.
2. Select which character types to include using checkboxes.
3. Click "Generate Password" to create a new password.
4. Click "Save Password" to store the generated password.
5. View saved passwords in the text area at the bottom of the window.

## File Structure
- `password_generator.py`: The main Python script containing the application code.
- `saved_passwords.json`: JSON file where saved passwords are stored (created upon first save).

## Security Considerations
- This application is for educational purposes and may not meet all security standards for password management.
- Saved passwords are stored in plain text. For real-world applications, consider using encryption.
- It's recommended to use a dedicated password manager for storing actual passwords.

## Contributing
Contributions to improve the project are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
Your Name - Aryan Adhikari

Email - aadhikari678@outlook.com

Project Link: https://github.com/Aryan01101/password_generator