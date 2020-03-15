import os,sys,inspect, shutil
from BankClassify import BankClassify


input_directory = 'demo/input'
store_directory = 'demo/cache'
output_directory = 'demo/output'
archive_directory = 'demo/archive'


availableBanks = ['barclays', 'lloyds']

# Options: 
# For the purposes of the below text `input_directory` is configurable, i.e `input`

# a. create sub directories inside `input_directory` named after each account as below:
    # `barclays_TakesTheBiscuit` or
    # `lloyds_CarSavings`
    # This is helpful to split your analysis by account

# This script will ingest each csv file - from in `input_directory` from each sub directory
# Sub directory naming convention is: `bank_accountName`

# Each file will then be run through the classifier in turn.
# The correct training file will be applied to each account - so after first run do not rename folders.

# Once all have been classified we run `bc._prep_for_analysis()` and store some outputs.
# The classified spend/income will be stored in appropriate `output_directory` - one per account.
# Those outputs will help you analyse month by month and `latest` which contains everything to-date. 

# Once outputs are saved we move the input files to archive directory
# Leaving the solution clean to run again next time

class Classify():

    def __init__(self):
        print("Classify full demo running..")
        self.bClassify = BankClassify

    def process_inputs(self):
        for root, dirs, files in os.walk(input_directory):
            # grab files from sub dirs (intended use: many bank accounts)
            for dir in dirs:
                print("Sub account found: " + dir)
                for subRoot, subDirs, subFiles in os.walk(input_directory + "/" + dir):
                    # scoop up sub (account) level csv files inside 'input'
                    
                    if (len(subFiles) < 1):
                        print("No bank statements found")

                    for file in subFiles:
                        if file.endswith('.csv'):
                            # Found file! use sub dir name to identify account type
                            print (dir + " > " + file)
                            
                            # bankType string, false, or throws exception
                            bankType = self.getBank(dir)
                           
                            bc = self.bClassify(store_directory + '/' + dir + '.csv')
                            bc.add_data(input_directory + "/" + dir + "/" + file, bankType)

                            bc._prep_for_analysis()

                            # i think it is useful to have the original input processed
                            # and stored back into categorised buckets
                            output_dir_concat = output_directory + '/' + dir 
                            archive_dir_concat = archive_directory + '/' + dir 

                            if not os.path.exists(output_dir_concat):
                                print("Created dir: " + output_dir_concat)
                                os.mkdir(output_dir_concat)

                            bc.inc.to_csv (output_dir_concat + '/income_' + file , index = False, header=True)
                            print(dir + " > Income Saved")

                            bc.out.to_csv (output_dir_concat + '/outgoing_' + file , index = False, header=True)
                            print(dir + " > Outgoing Saved")

                            # now Archive the input file
                            if not os.path.exists(archive_dir_concat):
                                print("Created dir: " + archive_dir_concat)
                                os.mkdir(archive_dir_concat)

                            # move it
                            shutil.move(os.path.join(input_directory + '/' + dir , file), os.path.join(archive_dir_concat, file))
                            print(dir + " > Archived input files")


    def getBank(self, fileOrDirName):
        if ('_' in fileOrDirName):
            bankType = fileOrDirName.split('_')[0] # e.g `barclays_MONTH001.csv` will be `barclays`
            return bankType
        else:
            raise ValueError('Bank type will not be readable, filenames should be formatted {bankName_}yourRef.csv.')

        if (bankType not in availableBanks):
            raise ValueError('Bank type csv not supported, filenames should be formatted {bankName_}yourRef.csv. Could not read banktype: ' + bankType)

        #fallthrough
        return false