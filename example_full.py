from demo.Classify import Classify

# process all inputs from 'demo/inputs/..' directories 
# a full run through of file processing, classification and outputs
# tidies input files away into an 'archive'directory

# drop files into `/demo/input/barclays_myaccountef` or similar
# run this script and you'll get output in seconds in `/demo/output/barclays_myaccountef/..`
full_demo = Classify()
full_demo.process_inputs()