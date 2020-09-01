# Documentation separation
| File    | Information                          |
|---------|--------------------------------------|
| doc1.md | General information                  |
| doc2.md | Folder/File structure of the project |
| doc3.md | Accounts' and Tasks' commands & info |
| doc4.md | Other commands                       |

# How to run?
First you need to run the file db_creator.py in the root folder of the project directory. It creates a project's database.
Then you can launch the app itself (app.py).
root user rights are required since the database is located in the /opt directory (in the future database will be located in the $HOME dir)

```shell
$ sudo python3 db_creator.py
$ sudo python3 app.py
```
