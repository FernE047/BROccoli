# BROccoli

A Python-based mod loader for Dadish 1 for PC. Easily load and manage mods for your game, offering a streamlined experience without having to manually replace files.

## Features

- **Automatic Detection**: Automatically detects game installation from Steam.
- **Backup System**: Safely keeps a backup of your base game to revert any time.
- **Supports Multiple Mod Types**: Whether it's a full-fledged mod or just a few files, the mod loader handles it.
- **Graphical User Interface**: A simple and intuitive GUI for managing your mods.

## Installation

1. **Clone or Download**: Clone this repository or download the ZIP file. Extract it to a suitable location on your system.
   
   ```bash
   git clone [repository URL]
   ```

2. **Run the Mod Loader**: Navigate to the directory and run `BROccoli.exe`

## Usage

1. **Adding mods**: Add your mods to the folder mods, in the same directory as Broccoli.exe
2. **Open the Mod Loader**: Run the executable or the Python script.
3. **Locate Game Directory**: If the mod loader can't automatically detect your game directory, specify it.
4. **Manage Mods**: Use the interface to load mods into your game
5. **Apply & Play**: Select your desired mod and apply. Start your game (or reset the level) to see the changes!

## Phonetics:

BROccoli
BRO-kuh-lee = /ˈbroʊ.kə.li/

Where:

BRO is pronounced like the slang term for "brother", rhyming with "throw" or "show".
"kuh-lee" represents the standard pronunciation of "-ccoli" in "broccoli".

## Standard Mods

### Definition:
Standard mods adhere to a specific directory and file structure. They are organized in a way that mirrors the base game's assets and can be easily recognized and processed by the mod loader.

### Structure:
Standard mods come with a folder structure that matches the game's base assets, as shown below:

```
assets/
│
├── data/
│   └── [levels...]
│
├── graphics/
│   └── 1x/
│       └── [graphics...]
│
├── music/
│   └── [musics...]
│
└── sfx/
    └── [sfx...]
```

### Implementation:
When a standard mod is applied, the mod loader simply has to move files from the mod's folders to the corresponding folders in the game. The clear and organized structure ensures a smooth and error-free mod installation process.

## Non-Standard Mods

### Definition:
Non-standard mods do not adhere to the predefined folder and file structure of standard mods. These mods may contain a mixture of files without the nested folder organization, and it's up to the mod loader to correctly identify and place each file.

### Structure:
Non-standard mods might have a loose collection of files, such as `.ogg`, `.mbs`, `.scn`, and image formats like `.png` or `.jpg`.

### Implementation:
The mod loader needs to be more dynamic in its approach when dealing with non-standard mods:

- Files like `.ogg` are directed to the `sfx` folder.
- `.mbs` and `.scn` files are identified to belong to the `data` folder.
- Image files like `.png` or `.jpg` are placed in the `graphics/1x/` directory.

## Contributing

Contributions are welcome! Please fork this repository and open a pull request with your changes.

## License

you can use this code, you can alter this code, go wild

## Credits

- **Developer**: Felipereis11011
- **Special Thanks**: To the game's community and everyone who tested the mod loader.
