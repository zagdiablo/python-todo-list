from modules.InputOutputOperation import IOOperation as io
from modules.DisplayOperation import Display as d


#TODO create delete all list item function
#TODO maintain and clean the code 

# main function
def main():
    while True:
        io.readDataFile()       #read data from Datafile.txt
        d.displayList()         #display the data from DataFile.txt
        d.displayOptions()      #show user options
        io.readUsrInput()       #read user input


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:   #exit if ctrl+c is pressed on keyboard
        print("exiting...")