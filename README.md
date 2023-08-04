
# Configure Files For Pvs Studio

## Roadmap

- About
- Tech
- Demo
- Run locally
- Documentation
## About

"Configure Files For Pvs Studio" is a script that can add and remove special text on the very beginning file with a certain extension (*.h, *.hpp, *.cpp or custom extension). This special text is required for the static analyzer code in c++.
## Tech Stack

- python(v3.11.3)
- operating systems(Windows, Linux)

## Demo

- Using the -add option:

https://github.com/cppVolodya/ConfigureFilesForPvsStudio/assets/103601559/0a0119d8-e558-404b-b47c-41c918ed9049

- Using the -delete option:

https://github.com/cppVolodya/ConfigureFilesForPvsStudio/assets/103601559/b22018fb-1e03-4ba8-a1c8-d7c9b931ff98

- Using the -extension option:

https://github.com/cppVolodya/ConfigureFilesForPvsStudio/assets/103601559/7f3469a2-f2aa-436d-bdac-4e50f575ac4b

## Run Locally

#### To test the script, follow these steps:

1. Clone or download (rar or zip file) the project:

  ```bash
  git clone https://github.com/cppVolodya/ConfigureFilesForPvsStudio.git
  ```

2. Go to the directory with the script:

  ```bash
  configure_files_for_pvs_studio/program/
  ```
  
3. Choose Linux or Windows, depending on your operating system:
- Windows

  ```bash
  configure_files_for_pvs_studio/program/windows/
  ```

- Linux

    ```bash
  configure_files_for_pvs_studio/program/linux/
  ```

4. Run the executable file with parameters (refer to the documentation below):
- Windows

  ```bash
  ./configure_files_for_pvs_studio [-add directory1, ...] or [-remove directory1, ...] [-extensions extensions1, ...]
  ```

- Linux
  ```bash
  .\configure_files_for_pvs_studio [-add directory1, ...] or [-remove directory1, ...] [-extensions extensions1, ...]
  ```

## Documentation

- You need to choose one of the options: [-add directory1, ...] or [-remove directory1, ...].

- If the directory contains subdirectories with files, the option [-add directory1, ...] or [-remove directory1, ...] will also be applied to them.

- [-add directory1, ...](mandatory option) - adds a special text to the beginning of the files found in the directory you specified, provided that the special text was not added.

- [-remove directory1, ...](mandatory option) - removes the special text at the beginning of the files found in the directory you specified, provided that the special text is present.

- [-extensions extensions1, ...](optional option) - applies the [-add directory1, ...] or [-remove directory1, ...] option to files with the final extension you entered, if if this option is not specified, the default file extensions ".hpp" , ".h", ".cpp" will be selected.

- Special text that will be added or deleted as follows:
  ```bash
  "// This is a personal academic project. Dear PVS-Studio, please check it.\n"
  "// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: https://pvs-studio.com\n\n"
  ```
