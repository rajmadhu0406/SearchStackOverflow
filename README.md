# SearchStackOverflow
#### Auto search for solutions to errors in your code on StackOverflow

Installation
-

```sh
mkdir SearchStackOverflow 

cd SearchStackOverflow

git clone https://github.com/rajmadhu0406/SearchStackOverflow.git 
```

Run .py File
-

```sh
touch fileName.py

cat fileName.py
```

> ___Write your program in this file___

```sh
cat run.py
```

> ___Change SearchSO.run('fileName.py')___

```sh
python3 run.py
```

Run Personalize Query
-

```sh
  import SearchSO
  SearchSo.findSolution(question,language) 
```
> ___Here pass strings for both question and language___ 

Features
-

- Automatically opens browsers and search for solution for python
- Added a function to search for questions for different languages(*manually*)
- You can pass any *error/question* as string to function to search for solutions
