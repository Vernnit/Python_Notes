import Dummyfile as df    #hello shello  line doesn't execute in this file but blabla executes form the dummy file.


# if you print __name__ it gives __main__ if it is being run from the same file , but if it is being accessed within other file from the root file .. it will display name of that file.

# if __name__ == "__main__" it means if name is main i.e. it is being run within same file then execute it otherwise not if being imported from some other module.

# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.
print(df.__name__)

print(__name__)