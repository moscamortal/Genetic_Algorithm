import csv

class Csv_Manager():

    def write_list_to_file(guest_list, filename):
        """Write the list to csv file."""

        with open(filename, "w") as outfile:
            for entries in guest_list:
                outfile.write(str(entries))
                outfile.write("\n")
        print("Resultado salvo em result.csv")