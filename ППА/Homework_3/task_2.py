class CustomConfigParser:
    def __init__(self):
        self._config = {}

    def read(self, filepath):
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filepath} not found")

        section = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1].strip()
                if not section.isascii() or any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz " for c in section):
                    raise ValueError(f"Invalid line in config file: {line}")
                self._config[section] = {}
            elif "=" in line and section is not None:
                key, value = map(str.strip, line.split("=", 1))
                if not key.isascii() or any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" for c in key):
                    raise ValueError(f"Invalid line in config file: {line}")
                self._config[section][key] = value
            else:
                raise ValueError(f"Invalid line in config file: {line}")

    def get(self, section, key):
        if section not in self._config:
            raise KeyError(f"Section '{section}' not found")
        if key not in self._config[section]:
            raise KeyError(f"Key '{key}' not found in section '{section}'")
        return self._config[section][key]

    def set(self, section, key, value):
        if section not in self._config:
            self._config[section] = {}
        self._config[section][key] = value

    def add_section(self, section):
        if section in self._config:
            raise KeyError(f"Section '{section}' already exists")
        self._config[section] = {}

    def remove_section(self, section):
        if section not in self._config:
            raise KeyError(f"Section '{section}' not found")
        del self._config[section]

    def remove_option(self, section, key):
        if section not in self._config:
            raise KeyError(f"Section '{section}' not found")
        if key not in self._config[section]:
            raise KeyError(f"Key '{key}' not found in section '{section}'")
        del self._config[section][key]

    def write(self, filepath):
        with open(filepath, 'w') as file:
            for section, options in self._config.items():
                file.write(f"[{section}]\n")
                for key, value in options.items():
                    file.write(f"{key} = {value}\n")
                file.write("\n")
