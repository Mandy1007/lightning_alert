#Introduction 

The purpose for this project is to write a program that reads lightning data from stdin and matches that data against a source of assets to produce an alert. Each line of the lightning data should be arranged as a JSON object representing a lightning strike.  The assets data should also be arranged as a list of JSON objects.

# Install

The package was expected to work in linux environment. Firstly clone the repo.

```
$ git clone 
```

The project was preferably installed and implemented in a virtual environment. So create a new environment by

```
$ virtualenv lightening_venv
$ . lightening_venv/bin/activate
```

 The next step is to install the program by
 
```
$ pip install -e .[test]
```

We can run the following code for testing

```
$ lightning_alert < lightning.json assets.json
```

Where lightning.json and assets.json is in the installed folder.

If the project was expected to installed in actual environment, we can run the following code to install and test

```
$ sudo pip install -e .[test]
$ lightning_alert < lightning.json assets.json
```

# Characteristics

##Time complexity

Suppose we have N assets and M lightning strikes, the time complexity is O(N+M). What we did is firstly scanning the assets.json file and save the assets information in a dict (i.e. the quadkey as key and (assetsOwner, assetsName) as value. Notable that if several owners have same quadkey, the value will be a list). This step takes O(N). Then for each strike information, it takes O(1) to process (since searching a key in dict takes O(1) time). Therefore totally it takes O(N+M) for this program.

##Bad data handling
If the asset .json object of a specific owner was invalid (e.g. missing quadkey or assetsOwner information), the program will just ignore this asset information and printed out "invalid assest input: " with red color. If one lightning strike .json object was invalid, smilarly the program will ignore this strike information and printed out "invalid strike input: " with red color.

##Potential improvement

For further improvement we may consider the following:
 - If the lightning data is very large and the asset data is relatively small, we may want to do an early stop. As soon as we detect the asset dictionary is empty we stop the whole process. By doing this, we could speed up the total running time.
 - If the asset data is very large, building a dictionary may spend a lot of memory. Thus, we could use a Trie data structure instead of a dictionary here. The advantages of using Trie for large asset data are: higher memory efficiency, faster on average at insertion, and also generally faster than hash table for small keys by avoiding hash function.

So above are two strategies to do the possible further improvement.
