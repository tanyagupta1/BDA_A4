import sys
import data_proc

n=int(sys.argv[1])

venues_authors, selected_venues = data_proc.return_input_data()


with open('consumer_script_DGIM.sh', 'a') as the_file:
    the_file.write("#!/bin/bash\n")
    for venue in selected_venues[0:n]:
      s="python3 DGIM_consumer.py "+venue+ " > DGIM_"+venue+".txt\n"
      the_file.write(s)


with open('consumer_script_FM.sh', 'a') as the_file:
    the_file.write("#!/bin/bash\n")
    for venue in selected_venues[0:n]:
      s="python3 FM_consumer.py "+venue+ " > FM_"+venue+".txt\n"
      the_file.write(s)